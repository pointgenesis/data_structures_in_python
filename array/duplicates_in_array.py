class Duplicates:

    def __init__(self):
        pass

    def examine(self, values):
        print(f'values: {values}')

        map_of_values = {}
        duplicates = []
        for value in values:
            str_value = str(value)
            if str_value in map_of_values:
                duplicates.append(value)
            else:
                map_of_values[str_value] = value
            # end if
        # end for
        print(f'map_of_values: {map_of_values}')
        print(f'duplicates: {duplicates}')
    # end def


if __name__ == '__main__':
    values = [1, 2, 4, 1, 7, 2]
    duplicates = Duplicates()
    duplicates.examine(values)