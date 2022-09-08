# Задача 1:

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.cursor = -1
        self.nested_list_len = len(self.nested_list)

    def __iter__(self):
        self.cursor += 1
        self.nested_cursor = 0
        return self

    def __next__(self):
        if self.nested_cursor == len(self.nested_list[self.cursor]):
          iter(self)
        if self.cursor == self.nested_list_len:
          raise StopIteration
        self.nested_cursor += 1
        return self.nested_list[self.cursor][self.nested_cursor - 1]

if __name__ == '__main__':

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

# Задача 2:

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(nested_list):
    for items in nested_list:
        for item in items:
            yield item


if __name__ == '__main__':

    for items in flat_generator(nested_list):
        print(items)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)




