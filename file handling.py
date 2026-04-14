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

