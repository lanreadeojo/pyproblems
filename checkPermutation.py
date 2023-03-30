def checkPermutation(word1, word2):
    if len(word1) != len(word2):
        return False
    characters = [0]*128
    for c in word1:
        characters[ord(c)] += 1

    for c in word2:
        characters[index:=ord(c)] -=1
        if(characters[index] < 0):
            return False
    return True
               


if __name__ == "__main__":
    first = input()
    second = input()
    print(checkPermutation(first,second))
