# this files containing functions to create the sankey string

# create a function to create the sankey string
def generate_sankey_string(category_sums, subcategory_sums):

    # divide by 12 to get monthly values
    for sums in category_sums.values():
        sums['income'] /= 12
        sums['outcome'] /= 12
    for sums in subcategory_sums.values():
        sums['income'] /= 12
        sums['outcome'] /= 12

    # create a list to store the sankey string
    sankeystring = []

    #
    for category, sums in category_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{category} [{round(sums['income'], 2)}] Budget")
        if sums['outcome'] > 0:
            sankeystring.append(f"Budget [{round(sums['outcome'], 2)}] {category}")

    for subcategory, sums in subcategory_sums.items():
        if sums['income'] > 0:
            sankeystring.append(f"{subcategory[0]}:{subcategory[1]} [{round(sums['income'], 2)}] {sums['category']}")
        if sums['outcome'] > 0:
            sankeystring.append(f"{sums['category']} [{round(sums['outcome'], 2)}] {subcategory[0]}:{subcategory[1]}")

    sum_income = sum([sums['income'] for sums in category_sums.values()])
    sum_outcome = sum([sums['outcome'] for sums in category_sums.values()])

    print("Budget: ", max(sum_income, sum_outcome))

    if sum_income > sum_outcome:
        sankeystring.append(f"Budget [{round(sum_income-sum_outcome,2)}] Übertrag")
    else:
        sankeystring.append(f"Übertrag [{round(sum_outcome-sum_income,2)}] Budget")

    # handling for empty subcategories
    for category, category_sum in category_sums.items():
        subcategory_income_total = sum(
            sums['income'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')
        subcategory_outcome_total = sum(
            sums['outcome'] for (subcategory, cat), sums in subcategory_sums.items() if cat == category and subcategory[0] != '')

        outcome_diff = category_sum['outcome'] - subcategory_outcome_total
        income_diff = category_sum['income'] - subcategory_income_total

        if outcome_diff >= 0.01:
            if any(cat == category for (_, cat) in subcategory_sums):
                print(f"Category '{category}' outcome differs by {outcome_diff:.2f} euros")
                sankeystring.append(f"{category} [{outcome_diff:.2f}] Weiteres:{category}")

        if income_diff >= 0.01:
            if any(cat == category for (_, cat) in subcategory_sums):
                print(f"Category '{category}' outcome differs by {income_diff:.2f} euros")
                sankeystring.append(f"Weiteres:{category} [{income_diff:.2f}] {category}")

    return "\n".join(sankeystring)

# noinspection SpellCheckingInspection
def append_settings_to_string(sankeystring):
    return sankeystring + '\r\n' +  """
// === Settings ===
size w 900
  h 1400
margin l 12
  r 14
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