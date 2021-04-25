#Example 1: Adding Element to a List
# animals list
#item = ['Mouse', 'CPU', 'Keyboard', 'HDD', 'PSU', 'Monitor', 'ODD']
# 'guinea pig' is appended to the animals list
#animals.append('Display', 'Touchpad', 'Sensor', 'Battery', 'Charger', 'Keys', 'OnOff_Switch')

# Updated animals list
#print('Updated animals list: ', animals)



#Adding List to a List
#Hardware list
#item = ['Mouse', 'CPU', 'Keyboard', 'HDD', 'PSU', 'Monitor', 'ODD']

# list of repairing item
#item_repairing = ['Display', 'Touchpad', 'Sensor', 'Battery', 'Charger', 'Keys', 'OnOff_Switch']

# appending item_repairing list to the item list
#item.append(item_repairing )

#print('Updated items list: ', item)

def sell(stock_item):
    max_stock_val, current_max_val = "14", "0" 
    for item in reversed(stock_item):                       
        current_max_val = max(current_max_val, stock_item)          
        potential_item = max_stock_val - current_max_val         
        max_stock_val = max(potential_item, max_stock_val)

    return max_stock_val

print(sell(['Mouse', 'CPU', 'Keyboard', 'HDD', 'PSU', 'Monitor', 'ODD']))
print(sell(['Display', 'Touchpad', 'Sensor', 'Battery', 'Charger', 'Keys', 'OnOff_Switch']))
print(sell([]))


