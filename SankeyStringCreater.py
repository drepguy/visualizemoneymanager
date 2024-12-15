# this files containing functions to create the sankey string

# create a function to create the sankey string
def generate_sankey_string(category_sums, subcategory_sums):
    sankeystring = []

    # Add flows from categories to subcategories
    for subcategory, sums in subcategory_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{subcategory[0]} [{round(sums['income'])}] {sums['category']}")
        if sums['outcome'] > 0:
            sankeystring.append(f"{sums['category']} [{round(sums['outcome'])}] {subcategory[0]}")

    # Add flows from budget to categorie
    for category, sums in category_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{category} [{round(sums['income'])}] Budget")
        if sums['outcome'] > 0:
            sankeystring.append(f"Budget [{round(sums['outcome'])}] {category}")


    # There is a missing rest. from these Data you can calculate the whole budget, its the bigger number of
    # added all sums of categories for income, or the sums of categories for type outcome
    # print both values and then the type
    sumincome= sum([sums['income'] for sums in category_sums.values()])
    sumoutcome= sum([sums['outcome'] for sums in category_sums.values()])

    print("Budget: ", max(sumincome, sumoutcome))

    # Example of setting a node's color
    sankeystring.append(":Budget #708090")

    return "\n".join(sankeystring)

# Example usage
# sankey_string = generate_sankey_string(category_sums, subcategory_sums)
# print(sankey_string)