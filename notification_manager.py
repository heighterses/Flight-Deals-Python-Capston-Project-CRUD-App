import smtplib
from data_manager import fare


class NotificationManager:
    def __init__(self):
        self.email = "heighter79@gmail.com"
        self.password = "prwdfkzpwvivnykc"
        self.receiver = "binaftaba@gmail.com"

    def sending_mail(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=self.receiver,
                                msg=f"Subject:Flight Fare (ISB to Jeddah)\n\n"
                                    f"The Flight Fare of Today is {fare}\n"
                                    f"FROM ISLAMABAD AIRPORT to JEDDAH AIRPORT\n"
                                    f"For checking the previous Fares you can check the Google Sheets"
                                )


send_email = NotificationManager()
send_email.sending_mail()
