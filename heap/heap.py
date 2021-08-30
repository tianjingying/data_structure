import heapq

def swap(arr, src_index, dst_index):
    """ 交换数组中两个元素"""
    if src_index > len(arr) - 1 or dst_index > len(arr) - 1:
        return
    temp = arr[src_index]
    arr[src_index] = arr[dst_index]
    arr[dst_index] = temp
#
#
# def max_heap_insert(arr, index):
#     if index > len(arr) - 1:
#         return
#
#     while (arr[index] > arr[(index - 1) / 2]):
#         swap(arr, index, (index - 1) / 2)
#         index = (index - 1) / 2

def heap_insert(arr, index):
    while arr[index] < arr[(index - 1) // 2] and index > 0:
        swap(arr, index, (index - 1) // 2)
        index = (index - 1) // 2

if __name__ == '__main__':
    arr_list = [1, 3, 6, 2, 5, 4]

    heap = []
    heapq.heappush(heap, 6)
    print(f" heap: {heap}")
    heapq.heappush(heap, 3)
    print(f" heap: {heap}")
    # print(f"list: {arr_list}")
    # print(f" heapify {heapq.heapify(arr_list)}")
    # print(f"after heapify arr_list: {arr_list}")
    arr = [6, 3]
    heap_insert(arr, 1)
    print(arr)
