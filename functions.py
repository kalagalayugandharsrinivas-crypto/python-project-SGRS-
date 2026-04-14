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

