# this files containing functions to create the sankey string

# create a function to create the sankey string
def generate_sankey_string(category_sums, subcategory_sums):
    sankeystring = []

    # Add flows from categories to subcategories
    for subcategory, sums in subcategory_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{subcategory} [{round(sums['income'])}] {sums['category']}")
        if sums['outcome'] > 0:
            sankeystring.append(f"{sums['category']} [{round(sums['outcome'])}] {subcategory}")

    # Add flows from budget to categorie
    for category, sums in category_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{category} [{round(sums['income'])}] Budget")
        if sums['outcome'] > 0:
            sankeystring.append(f"Budget [{round(sums['outcome'])}] {category} ")

    # Add flows from Budget to categories
    #for category, sums in category_sums.items():
    #    if sums['outcome'] > 0:
    #        sankeystring.append(f"Budget [{round(sums['outcome'])}] {category}")


    # Example of setting a node's color
    sankeystring.append(":Budget #708090")

    return "\n".join(sankeystring)

# Example usage
# sankey_string = generate_sankey_string(category_sums, subcategory_sums)
# print(sankey_string)