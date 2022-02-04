class DataObject(object):
    def __init__(self, *args) -> None:
        for arg in args:
            print(f'{arg}')


def main():
    my_list = {"travis", 50, "archery"}
    data_object = DataObject(*my_list)


if __name__ == '__main__':
    main()
