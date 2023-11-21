# Lab 09 - Algorithms and Algorithm Strategies

In this lab, we'll learn how to implement a few popular algorithms.

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab09-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will write the `search.py` and `sort.py` files so that it meets the requirements described in the following sections.  This file has no basic code to start, and it will be up to you to write all of the code for this lab.

#### Part 1

In the file `sort.py`, write a Python function (`insertion_sort`) that implements the insertion sort algorithm, discussed in the lectures.  You can use the pseudocode provided in the lecture notes as a template, and simply write the function in Python with the same logic.

This function will take exactly one list argument, and will return a list.  The argument (`values`) is a list of integers to be sorted.  You will return a new list which has been sorted in ascending order.

Below, you will find some code to test your insertion sort:

```python
unsorted = [4,3,7,1,8,2]
sorted = insertion_sort(unsorted)
print(sorted)
```

Here is the sample output from this test code:

```
[1,2,3,4,7,8]
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

#### Part 2

In `sort.py`, modify your `insertion_sort` function to count the number of comparisons (==, <, <=, >, or >=).  The function will now return both the number of comparisons made and the sorted list (in that order).

_**Note:** For simplicity, since counting these comparisons won't improve the accuracy of your count very much, we'll ignore the comparisons made in the final iteration of the loop.  One or both of these comparisons may actually be made, so determining the exact number of comparisons would be more challenging.  Thus, you can just count the comparisons made within the body of the loop._

The code below calls your function, and creates a simple ASCII bar chart of the number of comparisons (divided by 10, to account for small differences):

```python
max_elements = 30
for length in range(1, max_elements):
    unsorted = list(range(length, 0, -1))
    sorted, num_comparisons = insertion_sort(unsorted)

    print(f'{num_comparisons:03d}', '*' * (num_comparisons // 10))
```

The output of the test code has been provided, below:

```
000
002
006
012 *
020 **
030 ***
042 ****
056 *****
072 *******
090 *********
110 ***********
132 *************
156 ***************
182 ******************
210 *********************
240 ************************
272 ***************************
306 ******************************
342 **********************************
380 **************************************
420 ******************************************
462 **********************************************
506 **************************************************
552 *******************************************************
600 ************************************************************
650 *****************************************************************
702 **********************************************************************
756 ***************************************************************************
812 *********************************************************************************
```

#### Part 3

In `search.py`, write a Python function (`binary_search`) that implements the binary search algorithm, discussed in the lectures.  You can use the pseudocode provided in the lecture notes as a template, and simply write the function in Python with the same logic.

This function will take a list argument (`values`), a value to search for (`to_find`), a start index (`start_index`), and an end index (`end_index`).  The function will return `True` if `to_find` is present in `values`, and `False` otherwise.

Below, you will find some code to test your binary search:

```python
values = [2,4,6,8,10,12,14,16,18,20]
print(binary_search(values, 14, 0, len(values) - 1))
print(binary_search(values, 7, 0, len(values) - 1))
```

The output of the test code is below:

```
True
False
```

#### Part 4

In `search.py`, modify your `binary_search` function to count the number of comparisons (==, <, <=, >, or >=).  The function will now return both the number of comparisons made and the `True` or `False` result.  

The code below calls your function, and creates a simple ASCII bar chart of the number of comparisons (divided by 10, to account for small differences).

Some code to test your function has been provided, below:

```python
max_elements = 10000000
for length in range(1, max_elements, 500000):
    values = list(range(1, (2 * length) + 1, 2))
    num_comparisons, found = binary_search(values, length + 1, 0, len(values) - 1)
    print(f'{length:08d}', '*' * (num_comparisons // 10))
```

The output of this test code has also been provided, below:

```
004
055 *****
058 *****
061 ******
061 ******
064 ******
064 ******
064 ******
064 ******
067 ******
067 ******
067 ******
067 ******
067 ******
067 ******
067 ******
067 ******
070 *******
070 *******
070 *******
```

## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._



## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 09 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
