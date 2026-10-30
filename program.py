def main():
    balance = float(input("Opening balance: "))
    limit = float(input("Maximum withdrawal per transaction: "))
    n = int(input("Number of transactions: "))
    accepted = rejected = 0
    history = []

    for i in range(n):
        kind, amount_text = input(f"Transaction {i + 1} (D/W amount): ").split()
        amount = float(amount_text)
        kind = kind.upper()
        if amount <= 0:
            result = "REJECTED: amount must be positive"
            rejected += 1
        elif kind == "D":
            balance += amount
            result = "ACCEPTED: deposit"
            accepted += 1
        elif kind == "W" and amount <= limit and amount <= balance:
            balance -= amount
            result = "ACCEPTED: withdrawal"
            accepted += 1
        else:
            result = "REJECTED: invalid type, limit, or insufficient balance"
            rejected += 1
        history.append((kind, amount, result, balance))

    print("\nTRANSACTION SUMMARY")
    for i, (kind, amount, result, current) in enumerate(history, 1):
        print(f"{i}. {kind} {amount:.2f} - {result}; balance={current:.2f}")
    print(f"Final balance: {balance:.2f}")
    print(f"Accepted: {accepted} | Rejected: {rejected}")

if __name__ == "__main__":
    main()
