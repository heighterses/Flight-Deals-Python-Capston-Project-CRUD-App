from data_manager import DataManager
from notification_manager import NotificationManager

# ====== Object of Updating Sheet ======

update_sheet = DataManager()
update_sheet.post_method()


# ====== Object of Email Notifications ======

notif_mail = NotificationManager()
notif_mail.sending_mail()

