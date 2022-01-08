from person import Person


class Teacher(Person):

    # Data class for Teacher

    def __init__(self, id=None, name=None, email=None, semester=None, preferred_notification=None):
        super().__init__(id=id, email=email, name=name)
        self.semester = semester
        self.preferred_notification = preferred_notification

    def update(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def view(self):
        pass
