class Example:
    def __init__(self):
        self.public = "Public Data"
        self._protected = "Protected Data"
        self.__private = "Private Data"

        print(self._protected)
        print(self.__private)


obj = Example()
# print(obj.public)
print(obj.protected)
# print(obj.private)