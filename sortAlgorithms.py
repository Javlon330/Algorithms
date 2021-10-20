def quickSort(array):
    """Quick Sort O (nlog2N) vaqtda ishlaydi"""




# def bubbleSort(numbers):
#     """Bubble Sort"""
#     k = None
#     for i in range(len(numbers) - 1):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] > numbers[j]:
#                 k = numbers[i]
#                 numbers[i] = numbers[j]
#                 numbers[j] = k
#     print(numbers)
array_numbers = [1, 4, 5, 7, 3, 4, 6, 8,  0, 6, 4, 3, 4,11,12,3]
# del array_numbers[0]
# print(array_numbers)
# print("Sorted in :")
# bubbleSort(array_numbers)

# def maxxim(r):
#     maxx = r[0]
#     for i in range(1,len(r)):
#         if maxx<r[i]:
#             maxx = r[i]
#     return maxx
# def selectionSort(array):
#     """Selection Sort"""
#     sort_array = []
#     for i in range(len(array)-1):
#         sort_array.append(maxxim(array))
#         array.remove(maxxim(array))
#
#     return sort_array
# print(selectionSort(array_numbers))