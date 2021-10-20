# def BinSearch(search_array,son):
#     """ Binary Search log2(n) ikkilik qidiruv tizimi """
#       L = 0
#     H = len(search_array)-1
#     m = int((L + H) / 2)
#     while search_array[m] != son:
#         if  son > search_array[m]:
#             L = m + 1
#         else:
#             H = m-1
#         m = int((L + H) / 2)
#     return m
#
# def binarysearch(list,item):
#     low = 0
#     high = len(list)-1
#     while low <= high:
#         middle = (low + high)//2
#         if list[middle] == item:
#             return middle
#         if list[middle] > item:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return None
#
#
#
# def LinearSearch(r,s):
    """Linear Search chiziqli qidiruiv algoritimi"""
    # index = 0
    # while r[index] != s:
    #     index += 1
    # return index
#     for i in range(len(r)-1):
#         if r[i] == s:
#             return i
#     return None
#
# numbers = [2,5,7,8,12,11,54,65,66,67,13,9,88,77,83,14,81,24]
#
# print(binarysearch(numbers,14))
# print(LinearSearch(numbers,14))
# print(BinSearch(numbers,14))




