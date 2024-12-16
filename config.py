# Configuration settings
FILE_PATH = "C:/tmp/test/01-01-24_31-12-24.xls"
DIVIDE_AMOUNTS_BY = 12
MIDDLE_NODE_NAME = "Budget"
REMAINING_AMOUNT_NAME = "Übertrag"
TRANSFER_TYPE_INCOME = "Einkommen"
TRANSFER_TYPE_OUTCOME = "Ausgabe"
TRANSFER_TYPE_TRANSFER_IN = "Eingehender Transfer"
TRANSFER_TYPE_TRANSFER_OUT = "Ausgehender Transfer"

# noinspection SpellCheckingInspection
SANKEY_CHART_SETTINGS = """
// Use the controls below to customize
// your diagram's appearance...
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