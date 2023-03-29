def checkPermutation(word1, word2):
    new_word1 = ''.join(sorted(word1))
    new_word2 = ''.join(sorted(word2))
   
    if (new_word1 == new_word2):
        return True
    else:
        return False
    

if __name__ == "__main__":
    first = input()
    second = input()
    print(checkPermutation(first,second))
