
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from queue import Queue, Empty
from threading import Lock


class MailManager:
    def __init__(
        self,
        smtp_server: str,
        port: int,
        username: str,
        password: str,
        sender: str,
        pool_size: int = 5,
        use_ssl: bool = False,
        timeout: int = 60,
    ):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password
        self.sender = sender
        self.pool_size = pool_size
        self.use_ssl = use_ssl
        self.timeout = timeout 

        self._pool = Queue(maxsize=pool_size)
        self._lock = Lock()

        self._initialize_pool()

    def _initialize_pool(self):
        """Initialize the connection pool with SMTP connections."""
        for _ in range(self.pool_size):
            try:
                conn = self._create_connection()
                self._pool.put(conn)
            except Exception as e:
                print(f"Failed to create initial connection: {e}")

    def _create_connection(self):
        """Create a new SMTP connection."""
        try:
            if self.use_ssl:
                server = smtplib.SMTP_SSL(
                    self.smtp_server, self.port, timeout=self.timeout
                )
            else:
                server = smtplib.SMTP(self.smtp_server, self.port, timeout=self.timeout)
                server.starttls()

            server.login(self.username, self.password)
            print(f"Connected to SMTP server: {self.smtp_server}")
            return server
        except Exception as e:
            raise RuntimeError(f"Failed to connect to SMTP server: {e}")

    def _get_connection(self):
        """Retrieve a valid connection from the pool."""
        with self._lock:
            try:
                conn = self._pool.get_nowait()
                # Validate connection (optional, e.g., with `noop` command)
                if not self._is_connection_alive(conn):
                    print("Connection is not alive, creating a new one.")
                    conn = self._create_connection()
                return conn
            except Empty:
                print("Connection pool exhausted, creating a new connection.")
                return self._create_connection()

    def _release_connection(self, conn):
        """Return a connection to the pool or close it if pool is full."""
        with self._lock:
            try:
                if self._pool.full():
                    conn.quit()
                    print("Connection closed because the pool is full.")
                else:
                    self._pool.put(conn)
            except Exception as e:
                print(f"Error releasing connection: {e}")

    def _is_connection_alive(self, conn):
        """Check if the connection is alive using a NOOP command."""
        try:
            status = conn.noop()[0]
            return status == 250  # SMTP 'OK' response
        except Exception as e:
            print(f"Connection failed NOOP check: {e}")
            return False

    def send(
        self, receiver_email: str, subject: str, body: str, service_name: str = ""
    ) -> bool:
        """Send a single email."""
        conn = self._get_connection()
        try:
            msg = MIMEMultipart()
            msg["From"] = f"{service_name or 'email'} <{self.sender}>"
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "html"))

            conn.sendmail(self.sender, receiver_email, msg.as_string())
            print(f"Email sent to {receiver_email}")
            return True
        except Exception as e:
            print(f"Error sending email to {receiver_email}: {e}")
            return False
        finally:
            self._release_connection(conn)

    def send_bulk(
        self, recipients: list, subject: str, body: str, service_name: str = ""
    ) -> dict:
        """Send emails to multiple recipients with status tracking."""
        results = {}
        for email in recipients:
            success = self.send(email, subject, body, service_name)
            results[email] = success
        return results

    def close_all_connections(self):
        """Close all active connections in the pool."""
        with self._lock:
            while not self._pool.empty():
                conn = self._pool.get_nowait()
                try:
                    conn.quit()
                    print("SMTP connection closed.")
                except Exception as e:
                    print(f"Failed to close SMTP connection: {e}")

    def __str__(self):
        return f"<MailManager {self.smtp_server}:{self.port} (Pool size: {self.pool_size})>"

    def __repr__(self):
        return self.__str__()


def create_mail_manager(
    password: str,
    username: str,
    smtp_server: str,
    port: int,
    sender: str,
    use_ssl: bool,
) -> MailManager:
    """factory mail manager creator.

    :param username: username of the smtp server
    :type username: str
    :param password: password of the smtp server
    :type password: str
    :param smtp_server: smtp server address
    :type smtp_server: str
    :param port: port of the smtp server
    :type port: int
    """
    mail = MailManager(
        username=username,
        password=password,
        smtp_server=smtp_server,
        port=port,
        sender=sender,
        use_ssl=use_ssl,
    )
    return mail