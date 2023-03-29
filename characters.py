def isUnique(word):
    vals = [False] * 128
    for i in word:
        if (vals[n:=ord(i)]):
            return False
        else:
            vals[n] = True
    return True




if __name__ == "__main__":
    test = input()
    print(isUnique(test))
    
