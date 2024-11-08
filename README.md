py-smtper
===============

🚀  py-smtper is a Python SMTP client for sending SMTP requests, with connection pooling and fallback option.
---


<img src="https://raw.githubusercontent.com/alisharify7/py-smtper/main/doc/smtper.png">

Py-Smtper is a python client package that help you send smtp request (emails) easily.
----


🔨 How to install
---
    pip install p-smtper


📍 how to use
---

1.0 create an instance of MailManager class
---

```python
    from py_smtper import MailManager
    mail_manager = MailManager(host, port, user, pass, use_ssl, etc)
```

## 2.0 send emails

```python
    mail_manager.send(service_name=, body=, subject=, receiver_email=)
    mail_manager.send_bulk(subject=, body=, recipients=, service_name=)
```

