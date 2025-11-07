worldGraph = {
    'field_of_graves' : ['dead_forest', 'tall_rocks', 'burned_ruins', 'helmwind'],
    'tall_rocks' : ['field_of_graves', 'sorroweive'],
    'dead_forest' : ['field_of_graves', 'sorroweive', 'helmet_high'],
    'burned_ruins' : ['field_of_graves', 'abandoned_tower'],
    'helmwind' : ['field_of_graves', 'distant_windlands', 'great_gate'],
    'helmet_high' : ['dead_forest'],
    'sorroweive' : ['dead_forest', 'tall_rocks'],
    'abandoned_tower' : ['burned_ruins'],
    'distant_windlands' : ['helmwind'],
    'great_gate' : ['helmwind', 'corrupted_spire'],
    'corrupted_spire' : ['great_gate']
}