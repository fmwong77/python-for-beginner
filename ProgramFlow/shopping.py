shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
for item in shopping_list:
    if item != 'spam':
        print(item)
print("================")
for item in shopping_list:
    if item == 'spam':
        continue
    else:
        print(item)
print("================")
for item in shopping_list:
    if item == 'spam':
        break
    else:
        print(item)

item_to_find = 'spam'
found_at = None
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is None:
    print("No such item found")
else:
    print("Item found at position {}".format(found_at))


if item_to_find in shopping_list:
    print("Item found at position {}".format(shopping_list.index(item_to_find)))
else:
    print("No such item found")