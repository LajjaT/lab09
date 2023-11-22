# ADD YOUR IMPLEMENTATION OF insertion_sort HERE
def insertion_sort(values, num_comparisons):
    for j in range(1, len(values)):
        key = values[j]
        i = j - 1
        
        while i >= 0 and values[i] > key:
            values[i+1] = values[i]
            i = i-1
            values[i+1] = key
            num_comparisons+=2

    return values, num_comparisons

num_comparisons = 0
unsorted = [4,3,7,1,8,2]
sorted = insertion_sort(unsorted, num_comparisons)
print(sorted)

max_elements = 30

for length in range(1, max_elements):
    unsorted = list(range(length, 0, -1))
    sorted, num_comparisons = insertion_sort(unsorted, num_comparisons)

    print(f'{num_comparisons:03d}', '*' * (num_comparisons // 10))