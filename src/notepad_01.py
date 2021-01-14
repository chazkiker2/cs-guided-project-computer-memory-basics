"""
a = [1,2,3,4,5,6,7,8,9, ..., 10100101, 10100012]

x = a[3]
y = a[8]
z = a[32422]

complexity of array access: O(1)

memory

location    value   access
--------    -----   ----
3566        1       a, a[0]
3567        2       a[1]
3568        3       a[2]
3569        4       a[3]
3570        5       a[4]

what is address of a[4]
take address of a[0]: 3566
add on the index of a[4]: 4: 3566 + 4 = 3570

something similar applies to dictionaries and sets — there's an intermediary step that resolves where's the index

I think the point of today is to siphon off some of the abstractness of programming with Python (or programming in general, more so).
So we're going down a level by mocking out some of the functionality built into Python (i.e., making our own islower() function).

But if we couldn't use ord(), we'd spend the rest of the afternoon building out what ord() does in addition to what islower() does
"""


def my_islower(c):
    return 97 <= ord(c) <= 122


def my_upper(s):
    return_str = ""
    # send every character to my_islower
    for c in s:
        # if char is lowercase
        if my_islower(c):
            # get the ord val
            # subtract 32
            val = ord(c) - 32
            # convert val back to character
            # add to result
            c = chr(val)

        return_str += c

    if return_str == "":
        return "EMPTY"

    return return_str


a = "hi there!"

# print(my_islower('a'))
# print(my_islower('A'))
# print(my_islower('z'))
# print(my_islower('Z'))
# print(my_islower('!'))
# print(my_islower('~'))
# print(my_islower(' '))
# test_lst = ['a', 'b', 'c']
# print(my_upper(test_lst))
# print(my_upper("lowers"))
# print(my_upper("UPPERS"))
