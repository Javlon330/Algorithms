# from random import randrange
# def quickSort(array):
#     """Quick Sort O (nlog2N) vaqtda ishlaydi"""
#     if len(array)<2:
#         return array
#     else:
#         pivot = array.pop(randrange(len(array)))
#         kichik = [i for i in array if i<=pivot]
#         katta = [i for i in array if i> pivot]
#         return quickSort(kichik) + [pivot] + quickSort(katta)
#
#
# array_numbers = [1, 4, 5, 7, 3, 4, 6, 8,  0, 6, 4, 3, 4,11,12,3]
# print(array_numbers)
# print(quickSort(array_numbers))





# from random import randrange
# def qsort(arr):
#     if len(arr)<2:
#         return arr
#     else:
#         markaz = arr.pop(randrange(len(arr)))
#         katta = [i for i in arr if i > markaz]
#         kichik = [i for i in arr if i<= markaz]
#         return qsort(katta) + [markaz] + qsort(kichik)

# print(qsort(array_numbers))





# def bubbleSort(numbers):
#     """Bubble Sort"""
#     for i in range(len(numbers)):
#         for j in range(len(numbers)-i-1):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
#     return numbers
# array_numbers = [1, 4, 5, 7, 3, 4, 6, 8, 0, 6, 4, 3, 4, 11, 12, 3]
# print(bubbleSort(array_numbers))


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

# def mergeSort(arr):
#     """Merge Sort tartiblash algoritmmi"""
#     if len(arr)>1:
#         #  royxat o'rtasini belgilaymiz
#         mid = len(arr)//2
#         L = arr[:mid]
#         print(L)
#         R = arr[mid:]
#         print(R)
#         mergeSort(L)
#         mergeSort(R)
#
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R [j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr
# def printlist(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=' ')
#
# array_numbers = [1, 4, 5, 7, 3, 4, 6, 8, 0, 6, 4, 3, 4, 11, 12]
# print(mergeSort(array_numbers))
# print(printlist(array_numbers))


























