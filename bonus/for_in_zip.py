groceries = [('orange', 'apple', 'grapefruit'),
             ('tomato', 'cucumber', 'potato', 'radish'),
             ('white bread', 'donut')]
filenames = ['fruits.txt', 'vegetables.txt', 'bread.txt']

for grocery, filename in zip(groceries, filenames):
    grocery = str(grocery)
    grocery = grocery.strip("()")
    grocery = grocery.replace(", ", "\n")
    grocery = grocery.replace("'", "")
    file = open(f"../files/{filename}", "w")
    file.write(grocery)
