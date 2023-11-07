
def GenerateBBSTArray(a):
    a.sort()
    bbst = [None] * len(a)

    def iter(part, acc, index=0):
        if len(part) == 0:
            return

        leftIndex = (2 * index) + 1
        rightIndex = (2 * index) + 2

        middleIndex = len(part) // 2
        currentItem = part[middleIndex]
        acc[index] = currentItem

        iter(part[:middleIndex], acc, leftIndex)
        iter(part[middleIndex + 1:], acc, rightIndex)

    iter(a, bbst)

    return bbst
