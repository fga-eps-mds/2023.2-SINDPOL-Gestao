import email.message
import os
import secrets
import smtplib
import string


def generate_password(length: int = 8) -> str:
    characters = string.ascii_letters + string.digits
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def send_email(
    user_name: str, user_email: str, new_password: str, logo_path: str
) -> None:
    email_data = {
        "email_address": os.getenv("EMAIL_ADDRESS"),
        "email_password": os.getenv("EMAIL_APP_PASSWORD"),
        "email_subject": "recover-password SG-SINDPOL",
        "email_body": f"""
                        <img src="{logo_path}" width=200 style="height: auto;">
                        <p>recover-password system from SG-SINDPOL<p>
                        <p>name: {user_name}<p>
                        <p>new-password: {new_password}<p>
                    """,
    }

    msg = email.message.Message()
    msg["Subject"] = email_data["email_subject"]
    msg["From"] = email_data["email_address"]
    msg["To"] = user_email
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(email_data["email_body"])

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], email_data["email_password"])
    s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
