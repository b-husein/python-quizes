
# Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. 

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't