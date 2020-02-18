"""
    https://www.freecodecamp.org/learn/coding-interview-prep/rosetta-code/100-doors
    Date - 18/02/2020
    Description -

    There are 100 doors in a row that are all initially closed. You make 100
    passes by the doors. The first time through, visit every door and 'toggle'
    the door (if the door is closed, open it; if it is open, close it). The
    second time, only visit every 2nd door (i.e., door #2, #4, #6, ...) and
    toggle it. The third time, visit every 3rd door (i.e., door #3, #6, #9,
    ...), etc., until you only visit the 100th door.

    Implement a function to determine the state of the doors after the last
    pass. Return the final result in an array, with only the door number
    included in the array if it is open.
"""


def hundred_doors_naive():
    # False -> Door is closed
    # True -> Door is open

    num_doors = 100
    num_passes = 100

    doors = {i: False for i in range(1, num_doors + 1)}

    for pass_num in range(1, num_passes+1):
        for key in doors.keys():
            if key % pass_num == 0:
                doors[key] = not doors[key]

    return [key for key in doors.keys() if doors[key]]


def hundred_doors_optimized():
    # Optimized version after observing the naive version's output

    num_doors = 100
    return [i*i for i in range(1, int(num_doors ** 0.5) + 1)]


if __name__ == '__main__':
    open_doors_naive = hundred_doors_naive()
    open_doors_optimized = hundred_doors_optimized()
    print("Output from naive version =", open_doors_naive)
    print("Output from optimized version =", open_doors_optimized)
