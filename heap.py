class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.Size = 0
        self.MaxSize = 0

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        length = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * length
        self.MaxSize = length

        for i in range(len(a)):
            self.HeapArray[i] = a[i]
            self.Size += 1

        i = self.Size - 1
        while (i >= 0):
            self.goUp(i)
            i -= 1

    def GetMax(self):
        if len(self.HeapArray) == 0:
            return -1
        max = self.HeapArray[0]
        last = self.HeapArray[self.Size - 1]
        self.HeapArray[self.Size - 1] = None
        self.HeapArray[0] = last
        self.Size -= 1

        self.goDown(0)

        return max

    def Add(self, key):
        if self.Size == self.MaxSize:
            return False

        self.HeapArray[self.Size] = key
        self.goUp(self.Size)
        self.Size += 1

        return True

    def goUp(self, i):
        while (i > 0):
            parentIdx = (i - 1) // 2

            if self.HeapArray[parentIdx] is not None and self.HeapArray[parentIdx] < self.HeapArray[i]:
                temp = self.HeapArray[parentIdx]
                self.HeapArray[parentIdx] = self.HeapArray[i]
                self.HeapArray[i] = temp
                i = parentIdx
            else:
                break

    def goDown(self, i):
        while (i < self.Size // 2):
            leftChildIdx = 2 * i + 1
            rightChildIdx = 2 * i + 2
            largestChildIdx = i

            if (leftChildIdx < self.Size and self.HeapArray[leftChildIdx] > self.HeapArray[largestChildIdx]):
                largestChildIdx = leftChildIdx
            if (rightChildIdx < self.Size and self.HeapArray[rightChildIdx] > self.HeapArray[largestChildIdx]):
                largestChildIdx = rightChildIdx
            if (largestChildIdx == i):
                break

            temp = self.HeapArray[i]
            self.HeapArray[i] = self.HeapArray[largestChildIdx]
            self.HeapArray[largestChildIdx] = temp
            i = largestChildIdx
