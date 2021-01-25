# Replace with Factors

## Problem Description

Rishabh has given you a linked list in the form of its head node A.He has also given you an integer B. You need to change the current value of each node to its nearest multiple of B that is <= current value.

## Problem Constraints

1 <= size of list <= 10^5
1 <= value of each node <= 10^5
1 <= B <= 10^5

## Input Format

First argument is the head pointer of linked list A.
Second argument is the integer B.

## Output Format

Return the head of the changed linked list.

## Example

A = 1 -> 2 -> 3

B = 2

OUTPUT:0 -> 2 -> 2

A = 3 -> 4 -> 5

B = 3

OUTPUT: 3 -> 3 -> 3