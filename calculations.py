def calculate_sums(entries):
    category_sums = {}
    subcategory_sums = {}

    for entry in entries:
        if entry.category not in category_sums:
            category_sums[entry.category] = {'income': 0, 'outcome': 0}
        if entry.in_or_outcome == 'Einkommen':
            category_sums[entry.category]['income'] += entry.eur
        else:
            category_sums[entry.category]['outcome'] += entry.eur

        if entry.subcategory:
            if (entry.subcategory, entry.category) not in subcategory_sums:
                subcategory_sums[(entry.subcategory, entry.category)] = {'income': 0, 'outcome': 0, 'category': entry.category}
            if entry.in_or_outcome == 'Einkommen':
                subcategory_sums[(entry.subcategory, entry.category)]['income'] += entry.eur
            else:
                subcategory_sums[(entry.subcategory, entry.category)]['outcome'] += entry.eur

    for category in list(category_sums.keys()):
        for (subcategory, _) in subcategory_sums.keys():
            if subcategory in category and category_sums[category]['income'] > 0:
                new_category_name = f"Income {category}"
                category_sums[new_category_name] = category_sums.pop(category)
                break

    return category_sums, subcategory_sums