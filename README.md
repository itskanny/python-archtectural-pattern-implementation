### Architectural Patterns implementation by using notification handler module prototype

##### Patterns Covered in this code

- Adapter
- Indirection
- Singleton
- Factory
- Mediator

##### About the code

This project implements the required patterns in required scenario by fetching the dummy data from the database.

The required patterns are implemented based on the scenario of sending notification alerts to the different users based on the preference of the method of receiving the notification tols by the users.

Student and teacher classes are controlled by the by respective controller classes and then notification mediator and other classes handles other things.

##### Restrictions about the code

Currently, only the teacher can send notification to the students and this process uses only semester number which is shared by both the students and the teachers. Meaning that a will currently teach only a specific semester. You can add data dummy data in the sqlite database file directly by using any editor that supports the functionality.

##### About Error Handling of the Code

As this code will be later plugged into other code so the error handling is done by raising Exception() class exception. Later these exceptions can be replaced by the respective classes.

##### How to run this code

- The driver class for this code is
    `teacher_controller.py`
- This code requires some configurations to run, so they need to be added correctly in
    `config.json` our code provides a sample file with the sample required values named as `config_sample.json` 
- You need to do the above step according to the values in the database but sample config file currently contains correct data according to current database file and for now the db file name can only be changed by changing code file
- This code can be run in two ways. First by [`python >= 3`](https://www.python.org/downloads/) (needs to be installed) by using following command in the same directory as the code

    `python ./teacher_controller.py`

- The other way this code can be run is by using the [`docker`](https://www.docker.com/) install by clicking on it if not
- First build the image by using following command in the same directory as code

    `docker build . [IMAGE_NAME]`
    
    Replace image name with any name you like but convention is using `[DOCKER_ID]/[IMAGE_NAME]`
- The docker image will use docker volume to mount all the to the docker container, so you do not have to rebuild the image every time.
- While staying in the same folder as the code run

    ###### Windows
    
    `docker run -v ${PWD}:/patterns [IMAGE_NAME]`

    replace the `[IMAGE_NAME]` with your built image name

    ###### Linux/Mac

    `docker run -v "$(pwd)":/patterns [IMAGE_NAME]`
- If you need to change id or message then just run `docker run` app again as told in above point