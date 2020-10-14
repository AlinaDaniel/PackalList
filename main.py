class PackalList:
    """Class of Packal List"""
    def __init__(self, *elem):
        self.elem = list(elem)
    def __str__(self):
        return str(self.elem)
    def __getitem__(self, item):
        return self.elem[item-1]
    def __setitem__(self, key, value):
        self.elem[key-1] = value