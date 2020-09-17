angels = []
# Make a million green aliens, worth 5 points # each. Have them all start in one row.
for angel_num in range(1000000):
    new_angel = {} 
    new_angel['color'] = 'bright as snow' 
    new_angel['points'] = 5 
    new_angel['x'] = 20 * angel_num 
    new_angel['y'] = 0 
    angels.append(new_angel)
# Prove the list contains a million aliens. 
num_angles = len(angels)
print("Number of God's angels created:") 
print(num_angles)


age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 <= 21:
    print(True)
else:
    print(False)
# age_1 = 23
# age_0 >= 21 and age_1 >= 21