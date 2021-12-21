from json import JSONDecodeError

from database import Database
from notifications import NotificationMediator
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

        self.notification_mediator = NotificationMediator()

    def get_students(self):
        return Student.from_list(Database().get_generic_data("student", "semester", self.teacher.semester))

    def notify(self, message):
        if self.teacher is not None:
            if len(self.students) != 0:
                self.notification_mediator.notify(self.teacher, self.students, message)
            else:
                raise Exception("This teacher does not have any students to send the notification to")
        else:
            raise Exception("Teacher not found in the database")


# if __name__ == "__main__":
#
#     try:
#         with open("config.json", mode="r") as file:
#             raw_data = file.read()
#             try:
#                 config_data: dict = json.loads(raw_data)
#             except JSONDecodeError as e:
#                 raise Exception("The added configuration file has some errors. Consult from sample config file")
#     except FileNotFoundError:
#         raise Exception("The provided config file does not exist. Please create a config file using the sample config "
#                         "file")
#
#     if len(config_data) == 2 and config_data.keys().__contains__("email") and config_data.keys().__contains__("message"):
#         TeacherController(config_data['email']).notify(config_data['message'])
#     else:
#         raise Exception("Provided config file either does not contains required data and has extra or wrong data. "
#                         "Please consult from sample config file and provide correct data")
