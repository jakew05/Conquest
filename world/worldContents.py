import item_files.items as items

# sub world-contents-dictionaries
wh = {
    'main' : items.white_hall_main
}
fog = {
    'main' : [],
    'grave' : items.field_of_graves_grave,
    'crate' : items.field_of_graves_crate,
    'monument' : items.field_of_graves_monument
}
df = {
    'main' : [],
    'trunk' : items.dead_forest_trunk,
    'pit' : []
}
tr = {}
br = {}
s = {}
at = {}
hh = {}
h = {}
dw = {}
gg= {}
cs = {}

# main world-contents-dictionary
world = {
    'white_hall' : wh,
    'field_of_graves' : fog,
    'dead_forest' : df,
    'tall_rocks' : tr,
    'burned_ruins' : br,
    'sorroweive' : s,
    'abandoned_tower' : at,
    'helmet_high' : hh,
    'helmwind' : h,
    'distant_windlands' : dw,
    'great_gate' : gg,
    'corrupted_spire' : cs,
}