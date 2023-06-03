dict = {}

# print(dict)

fruits = {'name': ['apple', 'banana']}

# print(fruits)
#
# print(fruits['name'])

diclist = [
    {
        'name': 'Hari',
        'age': 20,
        'college': 'Rajalakshmi Engg. college',
        'address': '123, nanganallur',
        'contact_no': '9841095555',
        'hobby': 'watching tv, eating paneer butter masala'
    },
    {
        'name': 'Mrithu',
        'age': 15,
        'college': 'Prince mooka school',
        'address': '1234, nanganallur',
        'contact_no': '9841095555',
        'hobby': 'watching tv, eating everything'
    },
    {
        'name': 'Chandini',
        'age': 20,
        'college': 'Rajalakshmi Engg. college',
        'address': '123, nanganallur',
        'contact_no': '9841095555',
        'hobby': 'watching tv, eating paneer butter masala'
    },
]

items = [1, 2, 3, 4]

# print(diclist[0])
# print(diclist[1])
# print(len(diclist))

for items in diclist:
    print('executing for loop')
    print(items)
    print(items['college'])
    if(items['name'] == 'Chandini'):
        print(f"I study at: {items['college']}")
        print('I study at: {}'.format(items['college']))
        print("I study at: " + items['college'])

        print('I study at: {} and my hobby: {}'.format(items['college'], items['hobby']))
        print(f"I study at: {items['college']} and my hobby: {items['hobby']}")

states = {
    'tamilnadu': {
        'capital': 'Chennai',
        'beach': 'Marina',
        'cricket_team': 'CSK',
        'dishes': 'idly, dosa, puri'
    },
    'kerala': {
        'capital': 'Trivandram',
        'beach': 'alle river',
        'cricket_team': 'KTS',
        'dishes': 'puttu, kaalai, pallampuri'
    },
    'karnataka': {
        'capital': 'Bangalore',
        'beach': 'Cauvery river',
        'cricket_team': 'RCB',
        'dishes': 'mysore bonda'
    },
    'andra': {
        'capital': 'Hyderabad',
        'beach': 'Krishna river',
        'cricket_team': 'HSR',
        'dishes': 'kara chutney, briyani'
    }
}

# print(states['tamilnadu'])
# print(states.keys())
# for item in states.keys():
#     print(item)
#     print(states[item])

items = [1, 2, 3, 4, 5, 6, 7]

# for i in range(0, len(items)):
#     print(str(i))
#
# for i in range(len(items)):
#     print(str(i))

# for i in range(2, len(items)):
#     print(str(i))

# for(int i=0;i < items.length(); i++) {
#     System.out.println(i)
# }


# for i, value in enumerate(items):
#     print(str(i) + ': ' + str(value))

# for x in range(2, 6):
#   print(x)

# for x in range(5, 30,4):
#   print(x)

cars = ['benz', 'bmw', 'audi', 'toyota', 'honda', 'ferrari', 'lambhorghini', 'tesla']
# for i in range(len(cars)):
#     print(str(i))
#     print(cars[i])

# for i, car in enumerate(cars):
#     # print(str(i) + ":" + car)
#     print(str(i))
#     print(car)

for car in cars:
    print(car)

cars.append('ford')
print(cars)

cars[2] = 'volvo'
cars.insert(2, 'volvo')
print(cars)


my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
print(my_tuple[0])

my_tuple = ('apple', 'banana', 'kiwi')
print(my_tuple)
print(my_tuple[0])


