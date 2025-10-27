class Example:
    def __init__(self):
        self.public = "Public Data"
        self._protected = "Protected Data"
        self.__private = "Private Data"

obj = Example()
print(obj.public)
print(obj.protected)
print(obj.private)