import sort

def run_single_sort(unsorted, correct_sorted, correct_num_comparisons):
    sorted, num_comparisons = sort.insertion_sort(unsorted)
    assert len(sorted) == len(unsorted)
    assert sorted == correct_sorted
    assert num_comparisons == correct_num_comparisons

def test_insertion_sort():
    run_single_sort([3,11,-4,8,1,9,6], [-4,1,3,6,8,9,11], 32)
    run_single_sort([4,3,7,1,8,2], [1,2,3,4,7,8], 26)
    run_single_sort([8,19,-4,21,-13,0,6,-4], [-13,-4,-4,0,6,8,19,21], 48)
