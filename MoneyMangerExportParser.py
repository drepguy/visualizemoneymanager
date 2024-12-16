# This python file contains code to parse the MoneyManager export file.
# It reads the file and creates a list of MoneyManagerEntry objects and returns them as a list
# the MoneyManager export file is a xls file with the following columns:
# - Date
# - Account
# - Category
# - Subcategory
# - Note
# - EUR
# - Type (income or expense)
# - Description
# - Amount
# - Currency
# - Konto

# Since the MoneyManager export file is a xls file, we need to use the xlrd library to read the file
import xlrd
from MoneyManagerEntry import MoneyManagerEntry

# next we need to define a function to parse the MoneyManager export file
def parse_moneymanager_export(file_path):
    # open the xls file using the xlrd library
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)

    # create an empty list to store the MoneyManagerEntry objects
    entries = []

    # iterate over the rows in the xls file
    for i in range(1, sheet.nrows):
        # extract the data from each row
        date = sheet.cell_value(i, 0)
        account = sheet.cell_value(i, 1)
        category = sheet.cell_value(i, 2)
        subcategory = sheet.cell_value(i, 3)
        note = sheet.cell_value(i, 4)
        eur = sheet.cell_value(i, 5)
        type = sheet.cell_value(i, 6)
        description = sheet.cell_value(i, 7)
        amount = sheet.cell_value(i, 8)
        currency = sheet.cell_value(i, 9)
        konto = sheet.cell_value(i, 10)

        # create a MoneyManagerEntry object and add it to the list
        entry = MoneyManagerEntry(date, account, category, subcategory, note, eur, type, description, amount, currency,
                                  konto)
        entries.append(entry)

    # return the list of MoneyManagerEntry objects
    return entries


# create a print function to print the entries
def print_entries(entries):
    for entry in entries:
        print(entry)
