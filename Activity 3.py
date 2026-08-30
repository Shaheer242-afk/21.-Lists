L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list:", L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("Sum =", count)
print("Average =", avg)
L.sort()
print("Smallest Element is:", L[0])
print("Largest Element is:", L[-1])