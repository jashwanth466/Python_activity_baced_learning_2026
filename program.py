def main():
    n = int(input("Number of subjects: "))
    records = []
    latest_scores = []

    for i in range(n):
        name = input(f"Subject {i + 1} name: ")
        previous = float(input("Previous exam score (0-100): "))
        latest = float(input("Latest exam score (0-100): "))
        if not (0 <= previous <= 100 and 0 <= latest <= 100):
            print("Scores must be between 0 and 100.")
            return
        records.append((name, previous, latest))
        latest_scores.append(latest)

    print("\nPERFORMANCE TREND")
    for name, previous, latest in records:
        change = latest - previous
        label = "Improved" if change > 0 else "Declined" if change < 0 else "Unchanged"
        print(f"{name}: {previous:.1f} -> {latest:.1f} ({change:+.1f}, {label})")

    average = sum(latest_scores) / n if n else 0
    weakest = records[latest_scores.index(min(latest_scores))][0] if n else "N/A"
    category = "High" if average >= 75 else "Moderate" if average >= 50 else "Needs Improvement"
    print(f"Latest average: {average:.2f}")
    print(f"Weakest subject: {weakest}")
    print(f"Classification: {category}")

if __name__ == "__main__":
    main()
