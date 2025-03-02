import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json


class FinanceTrackerGUI:
    def __init__(self, root):

        self.root = root
        self.root.geometry("825x320")
        self.root.title("Personal Finance Tracker")

        # Frame for the search bar and search button
        self.topFrame = tk.Frame(root, width=825, height=40, background='#2595AB')
        self.entry = tk.Entry(self.topFrame, width=80)
        self.btnsearch = tk.Button(self.topFrame, text='Search', background='#18CB20',
                                   command=self.search_transactions)

        self.tableFrame = tk.Frame(root, width=825, background='#2595AB')  # Frame for table and scrollbar
        # Treeview for displaying transactions
        self.table = ttk.Treeview(self.tableFrame, columns=('first', 'second', 'third', 'fourth'),
                                  show='headings')
        self.clicked_header = ['fourth', '1']  # a list for store the last clicked column header

        self.transactions = {}
        self.load_transactions()
        self.create_widgets()

    def create_widgets(self):

        self.topFrame.place(x=0, y=0)
        self.tableFrame.place(x=0, y=60)

        self.table.heading('first', text='Index')
        self.table.heading('second', text='Description', command=lambda: self.sort_by_column('second'))
        self.table.heading('third', text='Amount', command=lambda: self.sort_by_column('third'))
        self.table.heading('fourth', text='Date', command=lambda: self.sort_by_column('fourth'))

        scrollbar = ttk.Scrollbar(self.tableFrame, command=self.table.yview)  # Scrollbar for the Treeview
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y', padx=2)
        self.table.pack(fill='both', expand=True)

        labelsearch = tk.Label(self.topFrame, text='Search:', font=('Arial', 14, 'bold'), background='#2595AB')
        labelsearch.place(x=70, y=5)

        # Search bar and button
        self.entry.place(x=150, y=10)
        self.btnsearch.place(x=650, y=5)

    def load_transactions(self):
        try:
            with open("transactions1.json", 'r') as file:
                self.transactions = json.load(file)

        except FileNotFoundError:
            messagebox.showerror("File Not Found")

    def display_transactions(self, transactions):

        # Remove existing entries
        for id in self.table.get_children():
            self.table.delete(id)

        # Add transactions to the treeview
        count = 1
        for key, value in transactions.items():
            second = key

            for items in value:
                first = count
                third = items['amount']
                fourth = items['date']
                data = (first, second, third, fourth)
                self.table.insert(parent='', index=tk.END, values=data)
                count += 1

    def search_transactions(self):
        # Placeholder for search functionality
        search = self.entry.get().lower()

        if search:
            for id in self.table.get_children():
                x = self.table.item(id)['values']
                list = [str(x[0]), x[1].lower(), str(x[2]), x[3]]
                if not search in list:
                    self.table.delete(id)
        else:
            self.display_transactions(self.transactions)

    def sort_by_column(self, col):
        # Placeholder for sorting functionality

        if col == "second":
            data = [(self.table.set(id, col), id) for id in self.table.get_children('')]
            self.check_ascending_or_descending(col, data)

        if col == "third":
            data = [(int(self.table.set(id, col)), id) for id in self.table.get_children('')]
            self.check_ascending_or_descending(col, data)

        if col == "fourth":
            data = [(self.table.set(id, col), id) for id in self.table.get_children('')]
            self.check_ascending_or_descending(col, data)

    def check_ascending_or_descending(self, column_header, data):

        if column_header == self.clicked_header[0]:  # check the clicked header is previous-clicked header or not

            if self.clicked_header[1] == '1':
                self.clicked_header[1] = '0'
                self.sort_data_descending(column_header, data)
            else:
                self.clicked_header[1] = '1'
                self.sort_data_ascending(column_header, data)

        else:

            self.clicked_header[0] = column_header
            self.clicked_header[1] = '1'
            self.sort_data_ascending(column_header, data)

    def sort_data_ascending(self, col, data):
        data.sort()
        for index, (item, id) in enumerate(data):
            self.table.move(id, '', index)
            self.table.heading(col, command=lambda: self.sort_by_column(col))  # Update heading for next sorting

    def sort_data_descending(self, col, data):
        data.sort(reverse=True)
        for index, (item, id) in enumerate(data):
            self.table.move(id, '', index)
            self.table.heading(col, command=lambda: self.sort_by_column(col))  # Update heading for next sorting


def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()


if __name__ == "__main__":
    main()

