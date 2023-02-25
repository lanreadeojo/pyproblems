def boolAnagram(phrases):
        dict_ = {}
        for word in phrases:
                s = ''.join(sorted(word))
                
                if s in dict_ :
                    dict_[s].append(word)
                else:
                        dict_[s] = [word]
        return ("true" if (len(dict_[s]) > 1) else "false" )

def findAnag():
     T = int(input())
     for i in range(1,T+1):
            line = [ x for x in str(input()).split()]
            print(boolAnagram(line))
            line = []

if __name__ == "__main__":
    findAnag()
    

