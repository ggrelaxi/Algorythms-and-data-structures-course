import ctypes
from typing import ItemsView

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i > self.capacity:
            raise IndexError('Index is out of bounds')
        elif i == self.capacity and i == self.count:
            self.resize(2 * self.capacity)
            self.append(itm)
        elif i == 0 and i == self.count:
            self.array[i] = itm
            self.count += 1
        elif i <= self.count:
            if self.count == self.capacity:
                self.resize(2*self.capacity)
            for x in range(self.count, i, -1):
                self.array[x] = self.array[x-1]
            self.array[i] = itm
            self.count += 1
        else:
            raise IndexError('Index is out of bounds')

    def delete(self, i):
        if i < 0 and i >= self.count:
            raise IndexError('Index is out of bounds')
        if i == 0 and self.count == 1:
            newArray = self.make_array(self.capacity)
            self.array = newArray
            self.count = 0
        else:
            newArray = self.make_array(self.capacity)

            for x in range(0, self.count - 1, 1):
                if x < i:
                    newArray[x] = self.array[x]
                else:
                    newArray[x] = self.array[x+1]

            self.array = newArray
            self.count -= 1
            
            if (self.count < (int(self.capacity // 2))) and self.capacity >= 24:
                self.resize(int(self.capacity // 1.5))