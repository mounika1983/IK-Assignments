class MyHashMap:

    def __init__(self):
        self.my_list = []

    def put(self, key: int, value: int) -> None:

        for pair in self.my_list:
            if key == pair[0]:
                pair[1] = value
                return

        pair = [key, value]
        self.my_list.append(pair)

    def get(self, key: int) -> int:

        for pair in self.my_list:
            if key == pair[0]:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:

        for pair in self.my_list:
            if key == pair[0]:
                self.my_list.remove(pair)
                return