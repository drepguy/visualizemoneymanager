import random
from config import FILE_PATH

import plotly.graph_objects as go
import logging

from config import MIDDLE_NODE_NAME, REMAINING_AMOUNT_NAME

def generate_sankey_data(category_sums, subcategory_sums):

    # divide by DIVIDE_AMOUNTS_BY to get monthly/yearly values

    # create empty arrays to store the nodes and links
    labels = []
    source = []
    target = []
    value = []

    # iterate through all categories_sums
    for category, sums in category_sums.items():
        if sums['income'] > 0:
            # sankeystring.append(f"{category} [{round(sums['income'], 2)}] {MIDDLE_NODE_NAME}")
            if category not in labels:
                labels.append(category)
            if MIDDLE_NODE_NAME not in labels:
                labels.append(MIDDLE_NODE_NAME)
            #find index of category in labels
            source.append(labels.index(category))
            target.append(labels.index(MIDDLE_NODE_NAME))
            value.append(round(sums['income'], 2))
        if sums['outcome'] > 0:
            # sankeystring.append(f"{MIDDLE_NODE_NAME} [{round(sums['outcome'], 2)}] {category}")
            if category not in labels:
                labels.append(category)
            if MIDDLE_NODE_NAME not in labels:
                labels.append(MIDDLE_NODE_NAME)
            # find index of category in labels
            source.append(labels.index(MIDDLE_NODE_NAME))
            target.append(labels.index(category))
            value.append(round(sums['outcome'], 2))

    # iterate through all subcategories_sums
    for subcategory, sums in subcategory_sums.items():
        if sums['income'] > 0:
            # sankeystring.append(f"{subcategory[0]}:{subcategory[1]} [{round(sums['income'], 2)}] {sums['category']}")
            if f"{subcategory[1]}:{subcategory[0]}" not in labels:
                labels.append(f"{subcategory[1]}:{subcategory[0]}")
            if subcategory[1] not in labels:
                labels.append(subcategory[1])
            source.append(labels.index(f"{subcategory[1]}:{subcategory[0]}"))
            target.append(labels.index(sums['category']))
            value.append(round(sums['income'], 2))

        if sums['outcome'] > 0:
            # sankeystring.append(f"{sums['category']} [{round(sums['outcome'], 2)}] {subcategory[0]}:{subcategory[1]}")
            if subcategory[0] not in labels:
                labels.append(f"{subcategory[1]}:{subcategory[0]}")
            if subcategory[1] not in labels:
                labels.append(subcategory[1])
            source.append(labels.index(sums['category']))
            target.append(labels.index(f"{subcategory[1]}:{subcategory[0]}"))
            value.append(round(sums['outcome'], 2))

    # add all main categories sums together to get the total income and outcome
    sum_income = sum([sums['income'] for sums in category_sums.values()])
    sum_outcome = sum([sums['outcome'] for sums in category_sums.values()])

    # we need to add a REMAINING_AMOUNT_NAME to keep sankey diagram balanced (inflow should be equal to outflow)
    if sum_income > sum_outcome:
        # sankeystring.append(f"{MIDDLE_NODE_NAME} [{round(sum_income - sum_outcome, 2)}] {REMAINING_AMOUNT_NAME}")
        if REMAINING_AMOUNT_NAME not in labels:
            labels.append(REMAINING_AMOUNT_NAME)
        if MIDDLE_NODE_NAME not in labels:
            labels.append(MIDDLE_NODE_NAME)
        source.append(labels.index(MIDDLE_NODE_NAME))
        target.append(labels.index(REMAINING_AMOUNT_NAME))
        value.append(round(sum_income - sum_outcome, 2))
    else:
        # sankeystring.append(f"{REMAINING_AMOUNT_NAME} [{round(sum_outcome - sum_income, 2)}] {MIDDLE_NODE_NAME}")
        if REMAINING_AMOUNT_NAME not in labels:
            labels.append(REMAINING_AMOUNT_NAME)
        if MIDDLE_NODE_NAME not in labels:
            labels.append(MIDDLE_NODE_NAME)
        source.append(labels.index(REMAINING_AMOUNT_NAME))
        target.append(labels.index(MIDDLE_NODE_NAME))
        value.append(round(sum_outcome - sum_income, 2))

    # handling for empty subcategories
    # if subcategory is empty, we need to add a Weiteres subcategory to keep sankey diagram balanced, and put the difference there
    # without it in case of outcome, we would have more inflow than outflow
    for category, category_sum in category_sums.items():
        subcategory_income_total = sum(
            sums['income'] for (subcategory, cat), sums in subcategory_sums.items() if
            cat == category and subcategory[0] != '')
        subcategory_outcome_total = sum(
            sums['outcome'] for (subcategory, cat), sums in subcategory_sums.items() if
            cat == category and subcategory[0] != '')

        outcome_diff = category_sum['outcome'] - subcategory_outcome_total
        income_diff = category_sum['income'] - subcategory_income_total

        if outcome_diff >= 0.01:
            if any(cat == category for (_, cat) in subcategory_sums):
                # log the difference
                logging.info(f"Category '{category}' outcome differs by {outcome_diff:.2f} euros")
                # add a * to the sankey string (basically create a new subcategory for it called Weiteres) which lets the remaining amount flow out of it
                # sankeystring.append(f"{category} [*] Weiteres:{category}")
                if category not in labels:
                    labels.append(category)
                if f"{category}:Weiteres" not in labels:
                    labels.append(f"{category}:Weiteres")
                source.append(labels.index(category))
                target.append(labels.index(f"{category}:Weiteres"))
                value.append(outcome_diff)

        if income_diff >= 0.01:
            if any(cat == category for (_, cat) in subcategory_sums):
                # log the difference
                logging.info(f"Category '{category}' income differs by {income_diff:.2f} euros")
                # add a ? to the sankey string (basically create a new subcategory for it called Weiteres) which lets the remaining amount flow into it
                # sankeystring.append(f"Weiteres:{category} [?] {category}")
                if category not in labels:
                    labels.append(category)
                if f"{category}:Weiteres" not in labels:
                    labels.append(f"{category}:Weiteres")
                source.append(labels.index(f"{category}:Weiteres"))
                target.append(labels.index(category))
                value.append(income_diff)

    return labels, source, target, value




def draw_sankey(labels, source, target, value):
    glossy_colors2 = [
        "#6BAED6",  # Muted blue
        "#9ECAE1",  # Light blue
        "#FDD0A2",  # Soft orange
        "#74C476",  # Fresh green
        "#A1D99B",  # Soft green
        "#BCBDDC",  # Lavender
        "#9E9AC8",  # Muted purple
        "#FCAE91",  # Pastel coral
        "#FB6A4A",  # Warm coral
        "#C6DBEF",  # Pale sky blue
        "#FFDDC1",  # Peach
        "#FFD7E9",  # Blush pink
        "#FFABAB",  # Light rose
        "#A7E8BD",  # Mint green
        "#EAD7F7",  # Soft lilac
        "#B3E5FC",  # Baby blue
        "#FFFACD",  # Lemon chiffon
        "#FDE2E4",  # Pale rose
        "#F6D55C",  # Sunflower pastel
    ]

    # an array with colors for as many labels as we have in labels
    colors = []
    colors_flows = []

    # loop over labels to make random source colors
    for _ in labels:
        colors.append(random.choice(glossy_colors2))

    # now get each color from the source and apply it to flows
    for s in source:
        colors_flows.append(colors[s])

    # now we want to append the sum of source or target to the label
    for l in labels:
        # get the index of the label
        i = labels.index(l)
        # in the source array, find all indices, which equals i
        indices = [index for index, value in enumerate(source) if value == i]
        # now check the value array for each index in indices and sum them up
        sum_of_source = sum([value[index] for index in indices])

        # in the target array, find all indices, which equals i
        indices = [index for index, value in enumerate(target) if value == i]
        # now check the value array for each index in indices and sum them up
        sum_of_target = sum([value[index] for index in indices])

        # append the sum of the source to the label
        if sum_of_source > 0:
            labels[i] += f" ({round(sum_of_source,2)})"
        else:
            labels[i] += f" ({round(sum_of_target,2)})"

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color=colors,
        ),
        link=dict(
            source=source,  # indices correspond to labels, e.g. A1, A2, A1, B1, ...
            target=target,
            value=value,
            color=colors_flows,
        ))])

    #fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    fig.update_layout(title_text=f"{FILE_PATH}", font_size=10)
    fig.show()

