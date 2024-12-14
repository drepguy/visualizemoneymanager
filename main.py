# This is a sample Python script.
import os
import sys
import matplotlib.pyplot as plt

from MoneyMangerExportParser import parse_moneymanager_export, print_entries


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_bye(message):
    print(f'Bye, {message}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_bye('PyCharm')
    print('This is a sample Python script.')

    # define a filepath to the MoneyManager export file
    file_path = "C:/tmp/test/01-01-23_31-12-23.xls"

    # Check if the file exists
    if not os.path.exists(file_path):
        print("The file does not exist.")
        sys.exit(1)

    # parse the MoneyManager export file
    entries = parse_moneymanager_export(file_path)

    # define another filepath to the MoneyManager export file
    print_entries(entries)

    # now we want to print a bar diagram of the expenses and incomes
    expenses = []
    incomes = []
    for entry in entries:
        if entry.type == "Ausgabe":
            expenses.append(entry.amount)
        else:
            incomes.append(entry.amount)

    plt.bar(["Expenses", "Incomes"], [sum(expenses), sum(incomes)])

    # now we want to show the bar diagram
    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
