# ---------- Inheritance ----------
class Student(Person):
    def __init__(self, sid, name, dept):
        super().__init__(sid, name)
        self.department = dept

    # Method Overriding
    def display(self):
        print(f"Student ID: {self.id}, Name: {self.name}, Dept: {self.department}")


class Admin(Person):
    def resolve(self, grievance):
        grievance.status = "Resolved"
        print("Grievance Resolved Successfully")


class Grievance:
    def __init__(self, gid, sid, category, desc, status="Pending"):
        self.gid = gid
        self.sid = sid
        self.category = category
        self.desc = desc
        self.status = status

    def to_dict(self):
        return self.__dict__
