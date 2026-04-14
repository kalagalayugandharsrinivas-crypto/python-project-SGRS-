
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import json
    import csv
    LIBS_AVAILABLE = True
except ImportError:
    print("Note: Some libraries not installed. Running basic mode.")
    LIBS_AVAILABLE = False


# ---------- Classes ----------
class Person:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}")


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


# ---------- Storage ----------
students = {}
grievances = {}
admin = Admin("A1", "Admin")


# ---------- FILE HANDLING (TXT + CSV + JSON) ----------

def save_txt():
    with open("students.txt", "w") as f:
        for s in students.values():
            f.write(f"{s.id},{s.name},{s.department}\n")

    with open("grievances.txt", "w") as f:
        for g in grievances.values():
            f.write(f"{g.gid},{g.sid},{g.category},{g.desc},{g.status}\n")


def save_csv():
    try:
        with open("students.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Dept"])
            for s in students.values():
                writer.writerow([s.id, s.name, s.department])

        with open("grievances.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["GID", "SID", "Category", "Desc", "Status"])
            for g in grievances.values():
                writer.writerow([g.gid, g.sid, g.category, g.desc, g.status])

    except Exception as e:
        print("CSV Error:", e)


def save_json():
    try:
        with open("students.json", "w") as f:
            json.dump({k: v.__dict__ for k, v in students.items()}, f, indent=4)

        with open("grievances.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in grievances.items()}, f, indent=4)

    except Exception as e:
        print("JSON Error:", e)


def load_json():
    try:
        with open("students.json", "r") as f:
            data = json.load(f)
            for k, v in data.items():
                students[k] = Student(v["id"], v["name"], v["department"])
    except:
        pass

    try:
        with open("grievances.json", "r") as f:
            data = json.load(f)
            for k, v in data.items():
                grievances[k] = Grievance(
                    v["gid"], v["sid"], v["category"], v["desc"], v["status"]
                )
    except:
        pass


def save_all():
    save_txt()
    save_csv()
    save_json()


# ---------- FUNCTIONS ----------
def add_student():
    try:
        sid = input("ID: ")
        name = input("Name: ")
        dept = input("Dept: ")

        if sid in students:
            print("Student already exists")
            return

        students[sid] = Student(sid, name, dept)
        save_all()
        print("Student Added")

    except Exception as e:
        print("Error:", e)


def file_grievance():
    try:
        gid = input("Grievance ID: ")
        sid = input("Student ID: ")

        if sid not in students:
            print("Student not found")
            return

        cat = input("Category: ")
        desc = input("Description: ")

        grievances[gid] = Grievance(gid, sid, cat, desc)
        save_all()
        print("Grievance Filed")

    except Exception as e:
        print("Error:", e)


def view_grievances():
    if not grievances:
        print("No grievances found")
        return

    for g in grievances.values():
        print("\nID:", g.gid)
        print("Student:", g.sid)
        print("Category:", g.category)
        print("Description:", g.desc)
        print("Status:", g.status)


def resolve_grievance():
    try:
        gid = input("Enter Grievance ID: ")
        if gid in grievances:
            admin.resolve(grievances[gid])
            save_all()
        else:
            print("Grievance not found")
    except Exception as e:
        print("Error:", e)


# ---------- STATISTICS ----------
def statistics():
    if not grievances:
        print("No data")
        return

    statuses = [g.status for g in grievances.values()]

    print("\n--- Basic Stats ---")
    count = {}
    for s in statuses:
        count[s] = count.get(s, 0) + 1
    print(count)

    if LIBS_AVAILABLE:
        arr = np.array(statuses)
        unique, counts = np.unique(arr, return_counts=True)

        print("\n--- NumPy ---")
        print(dict(zip(unique, counts)))

        df = pd.DataFrame({"Status": statuses})
        print("\n--- Pandas ---")
        print(df)

        plt.bar(unique, counts)
        plt.title("Grievance Status")
        plt.xlabel("Status")
        plt.ylabel("Count")
        plt.show()


# ---------- MAIN ----------11

def main():
    load_json()

    while True:
        print("\n1.Add Student")
        print("2.File Grievance")
        print("3.View Grievances")
        print("4.Resolve Grievance")
        print("5.Statistics")
        print("6.Exit")

        ch = input("Choice: ")

        if ch == "1":
            add_student()
        elif ch == "2":
            file_grievance()
        elif ch == "3":
            view_grievances()
        elif ch == "4":
            resolve_grievance()
        elif ch == "5":
            statistics()
        elif ch == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()