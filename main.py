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
        if entry.inOrOutcome == "Ausgabe":
            expenses.append(entry.amount)
        else:
            incomes.append(entry.amount)

    plt.bar(["Expenses", "Incomes"], [sum(expenses), sum(incomes)])

    # now we want to show the bar diagram
    plt.show()

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
        if entry.subcategory not in subcategory_sums:
            subcategory_sums[entry.subcategory] = {'income': 0, 'outcome': 0, 'category': entry.category}
        if entry.inOrOutcome == 'Einkommen':
            subcategory_sums[entry.subcategory]['income'] += entry.eur
        else:
            subcategory_sums[entry.subcategory]['outcome'] += entry.eur

    # Print the results
    print("Category Sums:")
    for category, sums in category_sums.items():
        print(f"{category}: Income = {sums['income']}, Outcome = {sums['outcome']}")

    print("\nSubcategory Sums:")
    for subcategory, sums in subcategory_sums.items():
        print(f"\t{subcategory} (Category: {sums['category']}): Income = {sums['income']}, Outcome = {sums['outcome']}")

    # Prepare data for the bar diagram
    categories = []
    incomes = []
    outcomes = []

    for category, sums in category_sums.items():
        categories.append(category)
        incomes.append(sums['income'])
        outcomes.append(sums['outcome'])

    # Plot the bar diagram for categories
    x = range(len(categories))
    bar_width = 0.4
    plt.bar(x, incomes, width=bar_width, label='Income', align='center')
    plt.bar(x, outcomes, width=bar_width, label='Outcome', align='edge')

    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Amount in EUR')
    plt.title('Income and Outcome by Category')
    plt.xticks(x, categories, rotation='vertical')
    plt.legend()

    # Show the bar diagram
    plt.tight_layout()
    plt.show()

    # Prepare data for the bar diagram for subcategories
    subcategories = []
    sub_incomes = []
    sub_outcomes = []

    for subcategory, sums in subcategory_sums.items():
        subcategories.append(f"{sums['category']} - {subcategory}")
        sub_incomes.append(sums['income'])
        sub_outcomes.append(sums['outcome'])

    # Sort the subcategories by main category
    sorted_subcategories = sorted(zip(subcategories, sub_incomes, sub_outcomes), key=lambda x: x[0].split(' - ')[0])
    subcategories, sub_incomes, sub_outcomes = zip(*sorted_subcategories)

    # Plot the bar diagram for subcategories
    x = range(len(subcategories))
    bar_width = 0.4

    plt.figure(figsize=(12, 8))  # Increase the figure size
    income_bars = plt.bar(x, sub_incomes, width=bar_width, label='Income', align='center')
    outcome_bars = plt.bar(x, sub_outcomes, width=bar_width, label='Outcome', align='edge')

    # Add labels and title
    plt.xlabel('Subcategories')
    plt.ylabel('Amount in EUR')
    plt.title('Income and Outcome by Subcategory')
    plt.xticks(x, subcategories, rotation='vertical', fontsize=8)
    plt.legend()

    # Scale the y-axis logarithmically
    plt.yscale('log')

    # Add exact values on top of the bars
    for bar in income_bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom',
                 rotation='vertical')

    for bar in outcome_bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom',
                 rotation='vertical')

    # Adjust the bottom margin to fit long descriptions
    plt.gcf().subplots_adjust(bottom=0.5)

    # Show the bar diagram
    # plt.tight_layout()
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
