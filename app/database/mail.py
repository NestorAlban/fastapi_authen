from typing import List

import os

from fastapi_mail import FastMail, MessageSchema,ConnectionConfig

# conf = ConnectionConfig(
#     MAIL_USERNAME = "YourUsername",
#     MAIL_PASSWORD = "strong_password",
#     MAIL_FROM = "your@email.com",
#     MAIL_PORT = 587,
#     MAIL_SERVER = "your mail server",
#     MAIL_TLS = True,
#     MAIL_SSL = False,
#     USE_CREDENTIALS = True,
#     VALIDATE_CERTS = True
# )

class Mail():
    def __init__(self) -> None:
        pass
        
    def create_config():
        mail_username = os.getenv("MAIL_USERNAME")
        main_password = os.getenv("MAIL_PASSWORD")
        mail_from = os.getenv("MAIL_FROM")
        mail_port = os.getenv("MAIL_PORT")
        mail_server = os.getenv("MAIL_SERVER")
        mail_tls = os.getenv("MAIL_TLS")
        mail_ssl = os.getenv("MAIL_SSL")
        #use_credentials = os.getenv("USE_CREDENTIALS")
        #validate_certs = os.getenv("VALIDATE_CERTS")
        conf = ConnectionConfig(
            MAIL_USERNAME = mail_username,
            MAIL_PASSWORD = main_password,
            MAIL_FROM = mail_from,
            MAIL_PORT = mail_port,
            MAIL_SERVER = mail_server,
            MAIL_TLS = mail_tls,
            MAIL_SSL = mail_ssl,
            # USE_CREDENTIALS = self.use_credentials,
            # VALIDATE_CERTS = self.validate_certs
        )
        return conf

      
    def send_email(
        subject: str, 
        recipients: List, 
        body: str
    ):
        message = MessageSchema(
            subject = subject,
            recipients = recipients,
            body = body,
            subtype = "html"
        )
        mail_config = Mail.create_config()
        fm = FastMail(mail_config)
        fm.send_message(message)



