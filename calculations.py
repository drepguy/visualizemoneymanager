from config import TRANSFER_TYPE_INCOME, TRANSFER_TYPE_OUTCOME

def calculate_sums(entries):
    category_sums = {}
    subcategory_sums = {}

    # iterate through all entries
    for entry in entries:

        # check if the category is already in the category_sums dictionary
        if entry.category not in category_sums:
            # if not, add it to the dictionary with initial values of 0
            category_sums[entry.category] = {'income': 0, 'outcome': 0}
        # add the entry's amount to the appropriate category
        if entry.transfer_type == f'{TRANSFER_TYPE_INCOME}':
            # if the entry is an income, add the amount to the income value
            category_sums[entry.category]['income'] += entry.eur
        if entry.transfer_type == f'{TRANSFER_TYPE_OUTCOME}':
            # if the entry is an outcome, add the amount to the outcome value
            category_sums[entry.category]['outcome'] += entry.eur

        # check if there is a subcategory defined
        if entry.subcategory:
            # check if the subcategory is already in the subcategory_sums dictionary
            if (entry.subcategory, entry.category) not in subcategory_sums:
                # if not, add it to the dictionary with initial values of 0, also add the parent category, because of same name issues
                subcategory_sums[(entry.subcategory, entry.category)] = {'income': 0, 'outcome': 0, 'category': entry.category}
            # add the entry's amount to the appropriate subcategory
            if entry.transfer_type == f'{TRANSFER_TYPE_INCOME}':
                # if the entry is an income, add the amount to the income value
                subcategory_sums[(entry.subcategory, entry.category)]['income'] += entry.eur
            if entry.transfer_type == f'{TRANSFER_TYPE_OUTCOME}':
                # if the entry is an outcome, add the amount to the outcome value
                subcategory_sums[(entry.subcategory, entry.category)]['outcome'] += entry.eur

    # iterate through all main categories
    for category in list(category_sums.keys()):
        # iterate through all subcategories
        for (subcategory, _) in subcategory_sums.keys():
            # check for name conflicts, if an income category is same name as a subcategory outcome, rename the income category
            # otherwise sankeymatic will have looping errors
            if subcategory in category and category_sums[category]['income'] > 0:
                new_category_name = f"Income {category}"
                category_sums[new_category_name] = category_sums.pop(category)
                break

    return category_sums, subcategory_sums