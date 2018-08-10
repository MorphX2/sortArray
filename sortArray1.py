arr = [ 1, 5, 4, 2, 5, 6 ]
reversed_arr = []

index = len(arr) - 1
size = len(arr) - 1
counter = 0

print("Original order of elements: " +  str(arr))

while counter <= size:
    print(arr[index])
    reversed_arr.insert(counter, arr[index])
    index = index - 1
    counter += 1

print("New array: " + str(reversed_arr))
