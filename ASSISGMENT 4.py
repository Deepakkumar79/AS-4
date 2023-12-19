#!/usr/bin/env python
# coding: utf-8

# # ASSIGMENT 4
1.What exactly is []?

ANSWER:- '[]'represents an empty list.2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

ANSWER:-spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
3. What is the value of spam[int(int('3' * 2) / 11)]?

ANSWER:-spam[int(int('3' * 2) / 11)] is equivalent to spam[3]. In Python, list indices start from 0, so the fourth element of the list ['a', 'b', 'c', 'd'] is accessed. Therefore, the correct value of spam[int(int('3' * 2) / 11)] is 'd'. 4. What is the value of spam[-1]?

ANSWER:-'d' (Negative indexes count from the end.)
5.What is the value of spam[:2]?
Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True]  .

ANSWER:-

FOR EXAMPLE:-
spam = [3.14, 'cat', 11, 'cat', True]
result = spam[:2]
print(result)

OUTPUT:-

[3.14, 'cat']


6. What is the value of bacon.index('cat')?

Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True]

ANSWER- The value of bacon.index('cat') is 1.7.How does bacon.append(99) change the look of the list value in bacon?
ANSWER:-[3.14, 'cat', 11, 'cat', True, 99]
8.How does bacon.remove('cat') change the look of the list in bacon?

ANSWER:-[3.14, 11, 'cat', True]9.What are the list concatenation and list replication operators?

ANSWER:-The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)10.What is difference between the list methods append() and insert()?

ANSWER:-While append() will add values only to the end of a list, insert() can add them anywhere in the list11.What are the two methods for removing items from a list?

ANSWER:-The del statement and the remove() list method are two ways to remove values from a list.
12. Describe how list values and string values are identical.

ANSWER:-Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.13.What's the difference between tuples and lists?

ANSWER:-Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists use the square brackets, [ and ].14.How do you type the tuple value that has just the integer value 42?

ANSWER:- (42,) (The trailing comma is mandatory.)15.  How do you get a tuple value's list form?

ANSWER:-The tuple() and list() functions, respectively16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

ANSWER:-They contain references to list values.17. How do you distinguish between copy.copy() and copy.deepcopy()?

ANSWER:-The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.