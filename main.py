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

    if not os.path.exists(FILE_PATH):
        logging.error("The file does not exist.")
        sys.exit(1)

    entries = parse_moneymanager_export(FILE_PATH)
    print_entries(entries)

    category_sums, subcategory_sums = calculate_sums(entries)

    sankey_string = generate_sankey_string(category_sums, subcategory_sums)
    sankey_string = append_settings_to_string(sankey_string)
    logging.info(sankey_string)

    pyperclip.copy(sankey_string)
    logging.info("Sankey string copied to clipboard")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
