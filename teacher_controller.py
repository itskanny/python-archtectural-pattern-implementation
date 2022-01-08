from json import JSONDecodeError

from database import Database
from notifications import NotificationAPIBridge
from teacher import Teacher
from student import Student
import json


# Teacher controller class that implements indirection

class TeacherController:

    def __init__(self, email):
        unclean_data = Database().get_by_email("teacher", email)
        if unclean_data is not None:
            self.teacher = Teacher(*list(unclean_data.values()))
        else:
            self.teacher = None

        if self.teacher is not None:
            self.students = self.get_students()
        else:
            raise Exception("Teacher not found in the database")

        self.notification_api_bridge = NotificationAPIBridge()

    def get_students(self):
        return Student.from_list(Database().get_generic_data("student", "semester", self.teacher.semester))

    def notify(self, message):
        if self.teacher is not None:
            if len(self.students) != 0:
                self.notification_api_bridge.send_notification(self.teacher, self.students, message)
            else:
                raise Exception("This teacher does not have any students to send the notification to")
        else:
            raise Exception("Teacher not found in the database")



