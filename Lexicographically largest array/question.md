# Lexicographically Largest Array


## Problem Description

Given an integer array A consisting of distinct elements. 
You are asked to create a lexographically largest array `S = X + reverse(Y)`.
'+' denotes concatenation.
It should satisfy the following conditions:
- len(S) <= len(A)
- X is the prefix array of A and Y is the suffix array of array A

Note: Array X or Y can be empty.

## Problem Constraints

- 1 <= len(A) <= 10^5
- 1 <= A[i] <= 10^9

## Input Format

First and only argument is an integer array A

## Output Format

Return an integer array denoting the lexicographically largest array S

## Example Input 1

`A = [4, 1, 3, 2]`

## Example Output 1

`[4, 2, 3, 1]`

## Explanation 1

`X = [4]`

`Y = [1, 3, 2]`

`Reverse(Y) = [2, 3, 1]`

`S = X + Reverse(Y) = [4, 2, 3, 1]`

## Example Input 2

`A = [10, 20, 30, 40]`

## Example Output 2

`[40, 30, 20, 10]`

## Explanation 2

`X = []`

`Y = [10, 20, 30, 40]`

`Reverse(Y) = [40, 30, 20, 10]`

`S = X + Reverse(Y) = [40, 30, 20, 10]`

Source: [CodeDrift: 2 Pointers by InterviewBit](https://www.interviewbit.com/contest/code-drift-2-pointers/)
