

def select(arr, i):
    arr = [1, 3, 4, 5, 5, 6]


def selectionSort(arr, n):
  for i in range(n):
        index = i
        for j in range(i + 1, n):
            if arr[j] < arr[index]:
                index = j
        (arr[i], arr[index]) = (arr[index], arr[i])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)