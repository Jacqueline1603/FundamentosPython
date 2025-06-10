### Listas

my_list = [1, 2, 3,  'x', 'xd', True, 2.3, [0,1]]

print (my_list)
print (my_list[6])
my_list[7]=10

my_list.append('Inserta valores')
print (my_list.pop())

## Diccionarios

my_dict = {
    "name": "Peter",
    "last_name": "Parker",
    "age": 22,
    "hero": "Spiderman",
    "power": "Super Strong",
    "is single": True,
    "height": 1.63,
}

print (my_dict ["name"])
print(f"{ my_dict["name"] } { my_dict["last_name"] } es { my_dict["hero"]}")

my_dict["power"] = ["super strong", "Spiderweb"]

print(my_dict)

print (my_dict.keys)
print (my_dict.values)
