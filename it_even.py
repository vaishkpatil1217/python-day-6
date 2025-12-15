class Eveno:
    def __iter__(self):
        self.no = 2
        return self

    def __next__(self):
        if self.no <= 20:
         x = self.no
         self.no += 2  
         return x
        else:
            print("Iteration is finished")
            raise StopIteration

even = Eveno()
it = iter(even)

for i in it:
    print(i)