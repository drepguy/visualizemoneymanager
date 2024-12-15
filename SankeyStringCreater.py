# this files containing functions to create the sankey string

# create a function to create the sankey string
def generate_sankey_string(category_sums, subcategory_sums):
    sankeystring = []

    # Add flows from budget to categorie
    for category, sums in category_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{category} [{round(sums['income'], 2)}] Budget")

    # Add flows from categories to subcategories
    for subcategory, sums in subcategory_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{subcategory[0]} [{round(sums['income'], 2)}] {sums['category']}")
        if sums['outcome'] > 0:
            sankeystring.append(f"{sums['category']} [{round(sums['outcome'], 2)}] {subcategory[0]}:{subcategory[1]}")

    # Add flows from budget to categorie
    for category, sums in category_sums.items():
        if sums['outcome'] > 0:
            sankeystring.append(f"Budget [{round(sums['outcome'], 2)}] {category}")

    # There is a missing rest. from these Data you can calculate the whole budget, its the bigger number of
    # added all sums of categories for income, or the sums of categories for type outcome
    # print both values and then the type
    sumincome= sum([sums['income'] for sums in category_sums.values()])
    sumoutcome= sum([sums['outcome'] for sums in category_sums.values()])

    print("Budget: ", max(sumincome, sumoutcome))

    if sumincome > sumoutcome:
        sankeystring.append(f"Budget [{round(sumincome-sumoutcome,2)}] Übertrag")
    else:
        sankeystring.append(f"Übertrag [{round(sumoutcome-sumincome,2)}] Budget")

    # Calculate and compare sums for each category
    for category, category_sum in category_sums.items():
        subcategory_income_total = sum(
            sums['income'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')
        subcategory_outcome_total = sum(
            sums['outcome'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')

        income_diff = category_sum['income'] - subcategory_income_total
        outcome_diff = category_sum['outcome'] - subcategory_outcome_total

        #if income_diff >= 0.01:
        #    print(f"Category '{category}' income differs by {income_diff:.2f} euros")
        if outcome_diff >= 0.01:
            # first check if the category is defined as category in the subcategory_sums
            if any(cat == category for (_, cat) in subcategory_sums):
                print(f"Category '{category}' outcome differs by {outcome_diff:.2f} euros")
                sankeystring.append(f"{category} [{outcome_diff:.2f}] Weiteres:{category}")






    return "\n".join(sankeystring)

# Example usage
# sankey_string = generate_sankey_string(category_sums, subcategory_sums)
# print(sankey_string)