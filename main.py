# This is a sample Python script.
import os
import sys
import pyperclip
from config import FILE_PATH

from sankey_chart import draw_sankey, generate_sankey_data
from MoneyMangerExportParser import parse_moneymanager_export
from SankeyStringCreater import generate_sankey_string, append_settings_to_string
from calculations import calculate_sums
from logger_setup import logger


def main():

    # log python version
    logger.info(f"Python version: {sys.version}")

    # check if the file exists
    if not os.path.exists(FILE_PATH):
        # if the file does not exist, log an error and exit the program
        logger.error("The file does not exist.")
        # exit the program with an error code
        sys.exit(1)

    # parse the MoneyManager export file
    entries = parse_moneymanager_export(FILE_PATH)

    # log all entries with new line in between them
    logger.info("\n".join([str(entry) for entry in entries]))

    # calculate the sums for the categories and subcategories
    category_sums, subcategory_sums = calculate_sums(entries)

    # generate the sankey raw string
    sankey_string = generate_sankey_string(category_sums, subcategory_sums)

    # append the settings to the sankey string
    sankey_string = append_settings_to_string(sankey_string)

    # print the sankey string
    logger.info(f'Sankey string: \n{sankey_string}')

    # copy the sankey string to the clipboard
    pyperclip.copy(sankey_string)

    logger.info("Sankey string copied to clipboard.")

    # generate the sankey data
    labels, source, target, value = generate_sankey_data(category_sums, subcategory_sums)

    draw_sankey(labels, source, target, value)

    # draw the sankey chart
    # x and y given as array_like objects
    # fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    # fig.show(renderer="browser")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
