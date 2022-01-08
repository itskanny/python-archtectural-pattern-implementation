import json
from json import JSONDecodeError

from teacher_controller import TeacherController

if __name__ == "__main__":

    try:
        with open("config.json", mode="r") as file:
            raw_data = file.read()
            try:
                config_data: dict = json.loads(raw_data)
            except JSONDecodeError as e:
                raise Exception("The added configuration file has some errors. Consult from sample config file")
    except FileNotFoundError:
        raise Exception("The provided config file does not exist. Please create a config file using the sample config "
                        "file")

    if len(config_data) == 2 and config_data.keys().__contains__("email") and config_data.keys().__contains__("message"):
        TeacherController(config_data['email']).notify(config_data['message'])
    else:
        raise Exception("Provided config file either does not contains required data and has extra or wrong data. "
                        "Please consult from sample config file and provide correct data")