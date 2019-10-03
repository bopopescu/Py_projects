class MaxSizeList:

    def __init__(self, max):
        self.max_size = max
        self.innerlist = []

    def push(self, obj):
        self.innerlist.append(obj)
        if len(self.innerlist) > self.max_size:
            self.innerlist.pop(0)

    def get_list(self):
        return self.innerlist

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

print(a.get_list())
