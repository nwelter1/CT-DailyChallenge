# O(n) Time and Space where n == total len of input array
def backSpace(arr):
    def typeWord(words):
        out = []
        for char in words:
            if char != '-B' and char != '':
                out.append(char)
            else:
                if len(out):
                    out.pop()
        return ''.join(out)
    word_1 = arr[0].split(',')
    word_2 = arr[1].split(',')
    return typeWord(word_1) == typeWord(word_2)