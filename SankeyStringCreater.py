# this files containing functions to create the sankey string

import logging
from config import DIVIDE_AMOUNTS_BY, MIDDLE_NODE_NAME, REMAINING_AMOUNT_NAME, SANKEY_CHART_SETTINGS

# create a function to create the sankey string
def generate_sankey_string(category_sums, subcategory_sums):

    # divide by DIVIDE_AMOUNTS_BY to get monthly/yearly values
    for sums in category_sums.values():
        sums['income'] /= DIVIDE_AMOUNTS_BY
        sums['outcome'] /= DIVIDE_AMOUNTS_BY
    for sums in subcategory_sums.values():
        sums['income'] /= DIVIDE_AMOUNTS_BY
        sums['outcome'] /= DIVIDE_AMOUNTS_BY

    # create a list to store the sankey string
    sankeystring = []


    # iterate through all categories_sums
    for category, sums in category_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{category} [{round(sums['income'], 2)}] {MIDDLE_NODE_NAME}")
        if sums['outcome'] > 0:
            sankeystring.append(f"{MIDDLE_NODE_NAME} [{round(sums['outcome'], 2)}] {category}")

    # iterate through all subcategories_sums
    for subcategory, sums in subcategory_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{subcategory[0]}:{subcategory[1]} [{round(sums['income'], 2)}] {sums['category']}")
        if sums['outcome'] > 0:
            sankeystring.append(f"{sums['category']} [{round(sums['outcome'], 2)}] {subcategory[0]}:{subcategory[1]}")

    # add all main categories sums together to get the total income and outcome
    sum_income = sum([sums['income'] for sums in category_sums.values()])
    sum_outcome = sum([sums['outcome'] for sums in category_sums.values()])

    # we need to add a REMAINING_AMOUNT_NAME to keep sankey diagram balanced (inflow should be equal to outflow)
    if sum_income > sum_outcome:
        sankeystring.append(f"{MIDDLE_NODE_NAME} [{round(sum_income-sum_outcome,2)}] {REMAINING_AMOUNT_NAME}")
    else:
        sankeystring.append(f"{REMAINING_AMOUNT_NAME} [{round(sum_outcome-sum_income,2)}] {MIDDLE_NODE_NAME}")

    # handling for empty subcategories
    # if subcategory is empty, we need to add a Weiteres subcategory to keep sankey diagram balanced, and put the difference there
    # without it in case of outcome, we would have more inflow than outflow
    for category, category_sum in category_sums.items():
        subcategory_income_total = sum(
            sums['income'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')
        subcategory_outcome_total = sum(
            sums['outcome'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')

        outcome_diff = category_sum['outcome'] - subcategory_outcome_total
        income_diff = category_sum['income'] - subcategory_income_total

        if outcome_diff >= 0.01:
            if any(cat == category for (_, cat) in subcategory_sums):
                # log the difference
                logging.info(f"Category '{category}' outcome differs by {outcome_diff:.2f} euros")
                # add a * to the sankey string (basically create a new subcategory for it called Weiteres) which lets the remaining amount flow out of it
                sankeystring.append(f"{category} [*] Weiteres:{category}")

        if income_diff >= 0.01:
            if any(cat == category for (_, cat) in subcategory_sums):
                # log the difference
                logging.info(f"Category '{category}' income differs by {income_diff:.2f} euros")
                # add a ? to the sankey string (basically create a new subcategory for it called Weiteres) which lets the remaining amount flow into it
                sankeystring.append(f"Weiteres:{category} [?] {category}")

    return '\n'.join(sankeystring)

# noinspection SpellCheckingInspection
def append_settings_to_string(sankeystring):
    return sankeystring + '\r\n' +  f'''{SANKEY_CHART_SETTINGS}'''