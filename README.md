py-smtper
===============

<a href="https://www.coffeete.ir/alisharify7">Donate/Support [Optional]</a>

<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/alisharify7/py-smtper"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/alisharify7/py-smtper"> <img alt="GitHub repo Licence" src="https://img.shields.io/pypi/l/py-smtper">

![PyPI Downloads](https://static.pepy.tech/badge/py-smtper)
![PyPI Downloads](https://static.pepy.tech/badge/py-smtper/month)
[![Latest version](https://img.shields.io/pypi/v/py-smtper)](https://pypi.python.org/pypi/py-smtper)
[![Supported python versions](https://img.shields.io/pypi/pyversions/py-smtper)](https://pypi.python.org/pypi/flask_captcha2)


🚀  py-smtper is a Python SMTP client for sending SMTP requests, with connection pooling and fallback option.
---


<img src="https://raw.githubusercontent.com/alisharify7/py-smtper/main/doc/smtper.png">

Py-Smtper is a python client package that help you send smtp request (emails) easily.
----


🔨 How to install
---
    pip install py-smtper


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

