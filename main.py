1
#

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
horses = ['Charlie','Blue','Lynx']
print(len(horses))

new_item = input('Enter a to-do item: ')
with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()
    todo = todo + new_item + '\n'
with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)

    import csv

    with open('trees.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        # Add code to open the csv file
        heights = []
        for row in spreadsheet:
            tree_height = row['height']
            heights.append(tree_height)
            shortest_height = min(heights)
    print(shortest_height)