from enum import Enum


class NotificationType(Enum):
    EMAIL_NOTIFICATION = "EMAIL_NOTIFICATION"
    DATABASE_NOTIFICATION = "DATABASE_NOTIFICATION"
    REALTIME_NOTIFICATION = "REALTIME_NOTIFICATION"
    SMS_NOTIFICATION = "SMS_NOTIFICATION"


class Notification:

    def __init__(self, notification_type: NotificationType):
        self.adapter = NotificationFactory.get_notification(notification_type)

    def notify(self, sender, receiver, message):
        self.adapter.send_notification(sender, receiver, message)


# These classes help in implementing adapter pattern

class BaseAdapter:
    def send_notification(self, sender, receiver, message):
        pass


class DatabaseNotificationAdapter(BaseAdapter):

    def send_notification(self, sender, receiver, message):
        print(f"Database Notification for email: {receiver.email}, username: {receiver.name} from {sender.email} with "
              f"the message: '{message}'")


class EmailNotificationAdapter(BaseAdapter):

    def send_notification(self, sender, receiver, message):
        print(f"Email Notification for email: {receiver.email}, username: {receiver.name} from {sender.email} with "
              f"the message: '{message}'")


class SmsNotificationAdapter(BaseAdapter):

    def send_notification(self, sender, receiver, message):
        print(f"SMS Notification for email: {receiver.email}, username: {receiver.name} from {sender.email} with the "
              f"message: '{message}'")


class RealtimeNotificationAdapter(BaseAdapter):

    def send_notification(self, sender, receiver, message):
        print(
            f"Realtime =Notification for email: {receiver.email}, username: {receiver.name} from {sender.email} with "
            f"the message: '{message}'")


# This class implements factory pattern

class NotificationFactory:

    @classmethod
    def get_notification(cls, notification_type: NotificationType):
        if notification_type == NotificationType.SMS_NOTIFICATION.name:
            return SmsNotificationAdapter()
        elif notification_type == NotificationType.EMAIL_NOTIFICATION.name:
            return EmailNotificationAdapter()
        elif notification_type == NotificationType.DATABASE_NOTIFICATION.name:
            return DatabaseNotificationAdapter()
        elif notification_type == NotificationType.REALTIME_NOTIFICATION.name:
            return RealtimeNotificationAdapter()
        else:
            raise Exception("Adapter Type Undefined")

# Mediator Pattern implementation

class NotificationMediator:

    def notify(self, sender, receivers, message):
        for receiver in receivers:
            receiver.get_notified(message, sender)
