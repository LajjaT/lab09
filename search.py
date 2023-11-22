# INSERT YOUR IMPLEMENTATION OF binary_search HERE
def binary_search(values, to_find, start_index, end_index, num_comparisons):

    if start_index > end_index:
      num_comparisons+=1
      return False, num_comparisons
    
    middle = (start_index + end_index) // 2

    if to_find == values[middle]:
      num_comparisons+=1
      return True, num_comparisons
    
    elif to_find < values[middle]:
      num_comparisons+=1
      return binary_search(values, to_find, start_index, middle - 1, num_comparisons)
    
    else:
      num_comparisons+=1
      return binary_search(values, to_find, middle + 1, end_index, num_comparisons)
    

num_comparisons = 0
values = [2,4,6,8,10,12,14,16,18,20]
print(binary_search(values, 14, 0, len(values) - 1, num_comparisons))
print(binary_search(values, 7, 0, len(values) - 1, num_comparisons))


max_elements = 10000000
for length in range(1, max_elements, 500000):
    values = list(range(1, (2 * length) + 1, 2))
    num_comparisons, found = binary_search(values, length + 1, 0, len(values) - 1, num_comparisons)
    print(f'{length:08d}', '*' * (num_comparisons // 10))
