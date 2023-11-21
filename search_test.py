import search 

def run_single_search(values, toFind, expected_result, expected_num_comparisons):
    num_comparisons, actual_result = search.binary_search2(values, toFind, 0, len(values) - 1)
    assert actual_result == expected_result
    assert num_comparisons == expected_num_comparisons

def test_binary_search():
    run_single_search([2,4,6,8,10,12,14,16,18,20], 14, True, 11)
    run_single_search([2,4,6,8,10,12,14,16,18,20], 7, False, 13)
    run_single_search([2,4,6,8,10,12,14,16,18,20], 21, False, 13)
