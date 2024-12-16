# This is a sample Python script.
import os
import sys
import logging
import pyperclip
from config import FILE_PATH

from MoneyMangerExportParser import parse_moneymanager_export, print_entries
from SankeyStringCreater import generate_sankey_string, append_settings_to_string
from calculations import calculate_sums


logging.basicConfig(level=logging.INFO)

def main():

    # log python version
    logging.info(f"Python version: {sys.version}")

    # check if the file exists
    if not os.path.exists(FILE_PATH):
        # if the file does not exist, log an error and exit the program
        logging.error("The file does not exist.")
        # exit the program with an error code
        sys.exit(1)

    # parse the MoneyManager export file
    entries = parse_moneymanager_export(FILE_PATH)

    # log all entries with new line in between them
    logging.info("\n".join([str(entry) for entry in entries]))

    # calculate the sums for the categories and subcategories
    category_sums, subcategory_sums = calculate_sums(entries)

    # generate the sankey raw string
    sankey_string = generate_sankey_string(category_sums, subcategory_sums)

    # append the settings to the sankey string
    sankey_string = append_settings_to_string(sankey_string)

    # print the sankey string
    logging.info(sankey_string)

    # copy the sankey string to the clipboard
    pyperclip.copy(sankey_string)

    logging.info("Sankey string copied to clipboard")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
