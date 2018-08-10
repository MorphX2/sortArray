class SortArray(object):
    def __init__(self, array):
        self.array_to_sort = array
        self.unique = []
        self.duplicates = []
    def findDuplicates(self):
        for x in self.array_to_sort:
            if x not in self.unique:
                self.unique.append(x)
            else:
                self.duplicates.append(x)
        return self.duplicates
    def printUnique(self):
        for x in self.array_to_sort:
            if x not in self.unique:
                self.unique.append(x)
            else:
                self.duplicates.append(x)
        return self.unique
    def descendingOrder(self):
        return sorted(self.array_to_sort, reverse=True)
    def ascendingOrder(self):
        return sorted(self.array_to_sort)


arr = [ 1, 2, 2, 5, 5, 2, 3, 5, 6 ]

print("Original array: " + str(arr))

getArrProperties = SortArray(arr)

print("Duplicate elements in original array: " 
        + str(getArrProperties.findDuplicates()))
print("Unique elements in original array: " 
        + str(getArrProperties.printUnique()))
print("Sorting original array in descending order: "
        + str(getArrProperties.descendingOrder()))
print("Sotring original array in ascending order: "
        + str(getArrProperties.ascendingOrder()))
