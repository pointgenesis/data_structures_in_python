class DataObject(object):
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            print(f'{key}: {value}')


def main():
    my_dict = {"name": "travis", "age": 50, "hobby": "archery"}
    data_object = DataObject(**my_dict)


if __name__ == '__main__':
    main()
