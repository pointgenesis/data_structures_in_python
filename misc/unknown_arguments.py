

def print_values(*args):
    for value in args:
        print(value)


print_values("a", "b", "c", "d")


def print_key_value(**kwargs):
    for arg in kwargs:
        print(f'{arg}:{arg[0]}')
    print(f'{kwargs["first_name"]}')


print_key_value(first_name='fred', last_name='flintstone', address='bedrock')

my_dict = {
    "first_name": "barney",
    "last_name": "rubble",
    "age": "prehistoric"
}

print_values(my_dict)
