# Personal Finance Tracker

A Python-based application to manage financial transactions effectively. 

## 📌 Features

1. **Add transactions** : Enter transaction category, amount, and date (`YYYY-MM-DD`).
2. **View transactions (GUI)** : Displays data in a searchable/sortable table.
3. **View transactions (CLI)** : Displays data in the command line.
4. **Update transactions** : Modify amount or date by row number.
5. **Delete transactions** : Remove a transaction by row number.
6. **Display transactions Summary** : Shows total transactions and transaction categories.
7. **Add Bulk transactions** : Import from a text file (`format: transaction,Amount,Date`).

### 💻 GUI Features

- __Table View__: Displays all transactions from `transactions.json`.
- __Search__: Enter keywords in the search bar.
- __Sort__: Click column headers (Category/Amount/Date).
- 
### 📄 Bulk Transaction Text File Format

```
salary    140000   2024-04-10
petrol    3000     2024-04-13 
```
_Ensure spaces separate fields and each transaction is on a new line._

### 🛠️ Design Choices

- __Tkinter__: Standard Python GUI toolkit.
- __JSON Storage__: Lightweight and easy to manipulate.



