# import smtplib
# from email.mime.text import MIMEText
# from datetime import datetime
# import geocoder

# EMAIL = "rohinigibu@gmail.com"
# APP_PASSWORD = "mckm sgbh cezh pidm"


# def send_emergency_email(to_email, task="Emergency detected"):

#     # 📍 Get location (optional)
#     try:
#         g = geocoder.ip('me')
#         location = f"{g.city}, {g.country}"
#     except:
#         location = "Location not available"

#     # 🕒 Time
#     time_now = datetime.now().strftime("%Y-%m-%d %I:%M %p")

#     # 📧 Message
#     subject = "🚨 EMERGENCY ALERT"

#     body = f"""
# Emergency Alert!

# The user needs immediate help.

# 📝 Issue: {task}
# 📍 Location: {location}
# 🕒 Time: {time_now}

# Please respond immediately.
# """

#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = EMAIL
#     msg["To"] = to_email

#     try:
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(EMAIL, APP_PASSWORD)
#             server.send_message(msg)

#         print(f"📧 Email sent to {to_email}")

#     except Exception as e:
#         print("❌ Email error:", e)


import smtplib
from email.mime.text import MIMEText
from datetime import datetime

EMAIL = "rohinigibu@gmail.com"
APP_PASSWORD = "mckm sgbh cezh pidm"


def send_email(to_email, subject, message):

    time_now = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    body = f"""
{message}

🕒 Time: {time_now}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, APP_PASSWORD)
            server.send_message(msg)

        print(f"📧 Email sent to {to_email}")

    except Exception as e:
        print("❌ Email error:", e)