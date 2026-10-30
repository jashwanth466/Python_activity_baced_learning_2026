# Case Study 13: ATM Transaction Sequence Simulation

## 1. Problem Statement
Process a sequence of deposits and withdrawals, maintain a simulated balance, enforce a per-withdrawal limit, reject invalid transactions, and produce a transaction summary.

## 2. Objectives
- Maintain a running account balance.
- Validate transaction amounts and withdrawal limits.
- Summarize accepted and rejected transactions.

## 3. Assumptions
- Opening balance is non-negative.
- Transactions are entered as D amount or W amount.
- A withdrawal cannot exceed the current balance or the per-transaction limit.

## 4. Algorithm
1. Read opening balance and withdrawal limit.
2. Process each transaction in order.
3. Accept a deposit if its amount is positive.
4. Accept a withdrawal only if its amount is positive, within the limit, and no greater than the balance.
5. Record each result and print the final summary.

## 5. Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[Read and validate input]
    B --> C[Process data using loops and conditions]
    C --> D[Calculate results and check rules]
    D --> E[Display report]
    E --> F([End])
```

## 6. Pseudocode
```text
INPUT balance, limit, n
accepted = 0; rejected = 0
REPEAT n times:
    INPUT type, amount
    IF amount <= 0: reject
    ELSE IF type is D: balance = balance + amount; accept
    ELSE IF type is W AND amount <= limit AND amount <= balance: balance = balance - amount; accept
    ELSE: reject
PRINT balance, accepted, rejected
```

## 7. Python Source Code
See [`program.py`](program.py).

## 8. Test Cases
| Test input / condition | Expected result |
|---|---|
| 1000; limit 500; D 200, W 300 | Final balance 900; 2 accepted, 0 rejected |
| 100; limit 80; W 120 | Final balance 100; 0 accepted, 1 rejected |
| 500; limit 200; W 100, W 450 | Final balance 400; 1 accepted, 1 rejected |

## 9. Sample Output
The `output_screenshot.png` file in this folder is a sample terminal-style output illustration. Run `program.py` with the test input to verify the actual output on your system.

## 10. Conclusion
The program simulates ATM transactions using a running balance and validates each transaction before updating the account.
