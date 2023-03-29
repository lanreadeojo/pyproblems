from string import ascii_letters

def test():
        words= {char:None for char in ascii_letters}
        print(words)
        word = 'nothing'
        print(words[word[1]])


if __name__=="__main__":
    test()