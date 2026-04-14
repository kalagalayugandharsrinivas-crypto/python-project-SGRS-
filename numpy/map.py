if LIBS_AVAILABLE:
    arr = np.array(statuses)
    unique, counts = np.unique(arr, return_counts=True)

    print("\n--- NumPy Statistics ---")
    for u, c in zip(unique, counts):
        print(u, ":", c)

    # ---------- Pandas ----------
    df = pd.DataFrame({"Status": statuses})
    print("\n--- Pandas DataFrame ---")
    print(df)

    # ---------- Matplotlib ----------
    plt.bar(unique, counts)
    plt.title("Grievance Status")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()
else:
    print("\n(Advanced libraries not available - showing basic stats only)")
