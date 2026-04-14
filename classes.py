class Person:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name


class Student(Person):
    def __init__(self, sid, name, dept):
        super().__init__(sid, name)
        self.department = dept


class Admin(Person):
    def resolve(self, grievance):
        grievance.status = "Resolved"
        print("Resolved Successfully")


class Grievance:
    def __init__(self, gid, sid, category, desc, status="Pending"):
        self.gid = gid
        self.sid = sid
        self.category = category
        self.desc = desc
        self.status = status