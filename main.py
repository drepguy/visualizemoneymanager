# This is a sample Python script.
import os
import sys
import matplotlib.pyplot as plt
import pyperclip

from MoneyMangerExportParser import parse_moneymanager_export, print_entries
from SankeyStringCreater import generate_sankey_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

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

    # Initialize dictionaries to store sums
    category_sums = {}
    subcategory_sums = {}

    # Iterate through the entries
    for entry in entries:
        # Sum for main category
        if entry.category not in category_sums:
            category_sums[entry.category] = {'income': 0, 'outcome': 0}
        if entry.inOrOutcome == 'Einkommen':
            category_sums[entry.category]['income'] += entry.eur
        else:
            category_sums[entry.category]['outcome'] += entry.eur

        # Sum for subcategory
        if entry.subcategory:
            if (entry.subcategory, entry.category) not in subcategory_sums:
                subcategory_sums[(entry.subcategory, entry.category)] = {'income': 0, 'outcome': 0, 'category': entry.category}
            if entry.inOrOutcome == 'Einkommen':
                subcategory_sums[(entry.subcategory, entry.category)]['income'] += entry.eur
            else:
                subcategory_sums[(entry.subcategory, entry.category)]['outcome'] += entry.eur

    # Check and rename categories if needed
    for category in list(category_sums.keys()):
        # Rename income main category if it contains any subcategory string
        for (subcategory, _) in subcategory_sums.keys():
            if subcategory in category and category_sums[category]['income'] > 0:
                new_category_name = f"Income {category}"
                category_sums[new_category_name] = category_sums.pop(category)
                break

    # divide all category_sums and subcategory_sums by 12
    #for sums in category_sums.values():
    #    sums['income'] /= 12
    #    sums['outcome'] /= 12
    #for sums in subcategory_sums.values():
    #    sums['income'] /= 12
    #    sums['outcome'] /= 12

    sankey_string = generate_sankey_string(category_sums, subcategory_sums)
    print(sankey_string)

    # put sankey_string into clipboard
    pyperclip.copy(sankey_string)
    print("Sankey string copied to clipboard")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
