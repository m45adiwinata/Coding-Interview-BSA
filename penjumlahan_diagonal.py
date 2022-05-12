arr = [
        [11,2,4,15],
        [4,5,6,8],
        [10,8,12,13],
        [8,5,9,7]
    ]

A = 0
B = 0

for i in range(len(arr)):
    A += arr[i][i]
    B += arr[i][-1-i]

print(A+B)
