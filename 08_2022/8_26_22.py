# O(n) Time | O(n) Space
def runLengthEncoding(string):
    i = 0
    j = 0
    count = 0
    res = []
    while j < len(string):
        if string[i] == string[j]:
            if count == 9:
                res.append(f'{count}{string[i]}')
                count = 1
            else:
                count += 1
            j += 1
        else:
            res.append(f'{count}{string[i]}')
            count = 1
            i = j
            j += 1
    res.append(f'{count}{string[i]}')
    return ''.join(res)