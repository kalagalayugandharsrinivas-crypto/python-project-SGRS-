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