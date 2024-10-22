"""
 * py-smtper OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2024 - ali sharifi
 * https://github.com/alisharify7/py-smtper
"""

from .klass import MailManager


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