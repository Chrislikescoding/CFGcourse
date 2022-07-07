





    with open('trees.csv', 'r') as csv_file:
        csv_file
        spreadsheet = csv.DictReader(csv_file)
        # Add code to open the csv file
        heights = []
        for row in spreadsheet:
            tree_height = row['height']
        heights.append(tree_height)
        shortest_height = min(heights)
        print(shortest_height)