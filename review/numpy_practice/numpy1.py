ml = [4, 23, 45, 11, 5413, 242, 2, 54, 6]
ml.sort()

class Mylist(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))

y=Mylist(ml)
