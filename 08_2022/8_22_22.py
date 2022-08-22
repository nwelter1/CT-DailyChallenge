# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
# O(n) Time | O(1) Space
def find_short(s):
    # your code here
    i = 0
    j = 0
    shortest = len(s)
    while j <= len(s):
        if j == len(s) or s[j] == ' ':
            shortest = min(j-i, shortest)
            i = j+1
            j = i+1
        else:
            j += 1
    return shortest