from notifications import Notification


class Student:

    def __init__(self, id = None, email = None, name = None, roll_number = None, batch = None, section = None, cgpa = None, semester = None, prefered_notification = None):
        self.id = id
        self.name = name
        self.email = email
        self.preferred_notification = prefered_notification
        self.batch = batch
        self.semester = semester
        self.section = section
        self.cgpa = cgpa
        self.roll_number = roll_number
        self.notification = Notification(prefered_notification)

    def update(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def view(self):
        pass

    def get_notified(self, message, sender):
        self.notification.notify(sender, self, message)

    @classmethod
    def from_list(cls, data_list):
        student_list = []

        for data in data_list:
            student_list.append(cls.from_dict(data))

        return student_list

    @classmethod
    def from_dict(cls, data_dict):
        student = Student(**data_dict)
        return student



