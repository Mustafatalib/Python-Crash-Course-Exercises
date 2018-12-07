pizza = ['cheese pizza', 'olive pizza', 'pepperoni pizza']
for i in pizza:
    print(i.title() + " is my favourite pizza.")
print("I really lieke to eat pizzas when im hungry and these are my favourite pizzas. ")
print("I really love pizzas.")
frnd_pizza = ['cheese pizza', 'olive pizza', 'pepperoni pizza']
frnd_pizza.append('go pizza')
print("Here are the two list of my and my frnds pizzas:")
print(pizza)
print(frnd_pizza)
print("My fav pizzas are: ")
for myp in pizza:
    print("- " + myp)
print('\t')
print("My frnds fav pizzas are:  ")
for myfp in frnd_pizza:
    print("- " + myfp)

