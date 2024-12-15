# this files containing functions to create the sankey string

# create a function to create the sankey string
def generate_sankey_string(category_sums, subcategory_sums):

    #divide all category_sums and subcategory_sums by 12 to get monthly values
    for sums in category_sums.values():
        sums['income'] /= 12
        sums['outcome'] /= 12
    for sums in subcategory_sums.values():
        sums['income'] /= 12
        sums['outcome'] /= 12


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

    # calculate uebrtrag from or to next year
    if sumincome > sumoutcome:
        sankeystring.append(f"Budget [{round(sumincome-sumoutcome,2)}] Übertrag")
    else:
        sankeystring.append(f"Übertrag [{round(sumoutcome-sumincome,2)}] Budget")

    # Calculate and compare sums for each category, because if an outcome was wihtout subcategory, it is not in the sankeystring
    # so we check if somethin is missing and adding it afterwards
    for category, category_sum in category_sums.items():
        subcategory_income_total = sum(
            sums['income'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')
        subcategory_outcome_total = sum(
            sums['outcome'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')

        outcome_diff = category_sum['outcome'] - subcategory_outcome_total

        if outcome_diff >= 0.01:
            # first check if the category is defined as category in the subcategory_sums
            if any(cat == category for (_, cat) in subcategory_sums):
                print(f"Category '{category}' outcome differs by {outcome_diff:.2f} euros")
                sankeystring.append(f"{category} [{outcome_diff:.2f}] Weiteres:{category}")

    return "\n".join(sankeystring)

# Example usage
# sankey_string = generate_sankey_string(category_sums, subcategory_sums)
# print(sankey_string)

def appendSettingsToString(sankeystring):
    return sankeystring + '\r\n' +  """
// === Settings ===
        
size w 900
h 1400
margin l 12
r 12
t 18
b 20
bg color #ffffff
transparent N
node w 12
h 19.5
spacing 75
border 0
theme a
color #888888
opacity 1
flow curvature 0.5
inheritfrom outside-in
color #999999
opacity 0.45
layout order automatic
justifyorigins N
justifyends Y
reversegraph N
attachincompletesto nearest
labels color #000000
hide N
highlight 0
fontface sans-serif
linespacing 0.25
relativesize 100
magnify 100
labelname appears Y
size 9.5
weight 400
labelvalue appears Y
fullprecision Y
position after
weight 400
labelposition autoalign -1
scheme auto
first before
breakpoint 5
value format ',.'
prefix ''
suffix ''
themeoffset a 9
b 0
c 0
d 0
meta mentionsankeymatic Y
listimbalances Y
"""