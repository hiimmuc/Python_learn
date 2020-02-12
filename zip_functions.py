list_1 = [0, 1, 2, 3]
list_2 = ['one', 'two', 'three', 'four']
zipped = list(zip(list_1, list_2))

fruits = ['apple', 'banana', 'grape']
costs = [10, 20, 15]
numbers = [1, 2, 4]
sentences = list()
for (number, cost, fruit) in zip(numbers, costs, fruits):
    number = str(number)
    cost = str(cost)
    fruit = str(fruit)
    sentence = f"I have bought {number} kg of {fruit} with the price {cost}.000 VND each."
    sentences.append(sentence)
print(sentences)
