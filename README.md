# py-smtper
## 🚀 py-smtper is a Python SMTP client for sending SMTP requests, with connection pooling and fallback option.



<img src="./doc/smtper.png">



# 🚧 How to install

    not implemented yet


# 📍 how to use

```python
    from py_smtper import MailManager
    mail_manager = MailManager(host, port, user, pass, use_ssl, etc)
    mail_manager.send() # single send
    mail_manager.send_bulk() # bulk send
```

TODO: add logger and test
