import json
from GUI import main
# Global dictionary to store transactions
transactions = {}


# Function to load transactions from JSON file
def load_transactions():
    global transactions
    try:
        with open("transactions1.json", "r") as file:
            transactions = json.load(file)
            file.close()

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass


# Function to save transactions to JSON file
def save_transactions():
    with open("transactions1.json", "w") as file:
        json.dump(transactions, file)
        file.close()


# Function to read bulk transactions from a file
def read_bulk_transactions_from_file(filename):
    try:
        filename = filename + ".txt"
        with open(filename, "r") as file:
            #  To read file line by line, convert strings in a line to elements of a list and remove spaces in elements
            line = [x.strip() for x in file.readline().split()]
            while line:
                category = line[0]      # To get first element as the category
                transaction = {"amount": line[1], "date": line[2]}
                line = [x.strip() for x in file.readline().split()]

                if category in transactions:   # To check is category already in the dictionary or not
                    transactions[category].append(transaction)
                else:
                    transactions[category] = [transaction]
            save_transactions()
            print("\nSaved your transactions from", filename)

    except FileNotFoundError:
        print("\n* File Not Found *")


# Function to add new transactions
def add_transactions():

    category = input("\nEnter transaction category: ")

    while True:
        try:
            amount = int(input("Enter transaction amount: "))
            break
        except ValueError:
            print("\nInvalid input. Please try again")

    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if len(date) == 10:
            break
        else:
            print("\nInvalid date format. Please try again")

    transaction = {"amount": amount, "date": date}

    if category in transactions:     # To check is user entered category already in the dictionary or not
        transactions[category].append(transaction)
    else:
        transactions[category] = [transaction]
    save_transactions()
    print("\nTransaction Added Successfully!")


# Function to see all the transactions user have done
def view_transactions():
    if transactions:

        for key, value in transactions.items():
            print("\n_____", key, "_____")

            count = 1  # To give transactions to an index number
            for items in value:
                print(f"\n{count}. Amount = {items["amount"]}, Date = {items["date"]}")
                count += 1
    else:
        print("\nNo Transactions Found")


# Function to update a transaction in the dictionary
def update_transactions():
    view_transactions()

    if transactions:
        category = input("\nWhat category of transaction do you want to update? ")
        if category in transactions:
            index = int(input("Enter index of transaction to update: "))
            if 0 < index <= len(transactions[category]):
                update_trans = transactions[category][index - 1]
                print("\nSelected transaction: ", update_trans)  # To display user selected transaction

                while True:
                    print("\nWhat do you want to change?\n1.Amount\n2.Date")
                    update_item = input("> ")

                    if update_item == "1":
                        print("Current amount is: ", transactions[category][index - 1]["amount"])
                        while True:
                            try:
                                amount = int(input("Enter new amount: "))
                                break
                            except ValueError:
                                print("\nInvalid input. Please try again")

                        transactions[category][index - 1]["amount"] = amount
                        print("\nChanges Saved Successfully!")
                        break

                    elif update_item == "2":
                        print("Current date is: ", transactions[category][index - 1]["date"])
                        while True:
                            date = input("\nEnter the date (YYYY-MM-DD): ")
                            if len(date) == 10:
                                break
                            else:
                                print("\nInvalid date format. Please try again")

                        transactions[category][index - 1]["date"] = date
                        print("\nChanges Saved Successfully!")
                        break
                    else:
                        print("Invalid input.Try again.")

                    save_transactions()

            else:
                print("Transaction not found")
        else:
            print("There is no category named ", category)


# Function to delete a key if there are no values in it
def delete_key_if_empty(key):
    if key in transactions and not transactions[key]:
        del transactions[key]
        save_transactions()


# Function to delete a transaction
def delete_transactions():
    view_transactions()

    if transactions:
        category = input("\nWhat category of transaction do you want to delete? ")
        if category in transactions:
            index = int(input("Enter index of transaction to delete: "))
            if 0 < index <= len(transactions[category]):
                del transactions[category][index - 1]
                save_transactions()
                print("\nTransaction Deleted Successfully!")
                delete_key_if_empty(category)
            else:
                print("\nThere is no transaction for index", index, "in ", category, "category")

        else:
            print("\nThere is no category named ", category)


# Function to get a summary of transactions
def summary_of_transactions():
    # To calculate how many transactions user have done
    no_of_values = sum(len(value_list) for value_list in transactions.values())

    print("\nYou have done", no_of_values, "transactions")
    categories = list(transactions.keys())  # To get a list of all the keys in dictionary
    print(f"Your transaction categories: {categories}")


def main_menu():
    load_transactions()
    while True:
        print("\n_____PERSONAL FINANCE TRACKER_____")
        print("\n1. Add Transaction")
        print("2. View Transactions via CLI")
        print("3. View Transactions via GUI")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Summary of transactions")
        print("7. Read Bulk Transactions from File")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_transactions()
        elif choice == 2:
            view_transactions()
        elif choice == 3:
            main()
        elif choice == 4:
            update_transactions()
        elif choice == 5:
            delete_transactions()
        elif choice == 6:
            summary_of_transactions()
        elif choice == 7:
            # To get the file name user want to read transactions from
            filename = input("Enter filename to read bulk transactions from: ")
            read_bulk_transactions_from_file(filename)
        elif choice == 8:
            print("Exit")
            break
        else:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    main_menu()
