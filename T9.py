#predict word based on T9 key sequence
#http://poj.org/problem?id=1451

t9="22233344455566677778889999"



def char_to_digit(x):
    assert 'a' <= x <= 'z'
    return t9[ord(x)-ord('a')]


def file_():
    dic= {}
    t9_seq={}
    
    i=int(input())
    while i > 0:
        w=int(input())
        while w > 0:
            word,weight= input().split()
            add(dic,word,weight)
            w-=1
        m=int(input())
        p=0
        print(dic)
        propose = realweights(dic)
        print(propose)
        while m > 0:
            part=''
            #t9 input sequence that contains the num 1 at the end for newline
            t9_seq[p]=str(input())
            for x in t9_seq[p]:
               if x !="1": 
                part+=x
                print(f"{predict(part,propose)} \n")
            p+=1
            m-=1

        #print(t9_seq)
        t9_seq={}
        dic={}
        i-=1


        

def  predict(seq,prop):
    if seq in prop:
        return prop[seq]
    return "MANUALLY"
    

# parameters: word and probability
def add(dic,w,prob):
    dic[w]=int(prob)

def convertTot9(w):
    return ''.join(map(char_to_digit,w))


def realweights(dic):
    
    total_weight={}
    for word, weight in dic.items():
        prefix = ''
        for part in word:
            prefix+=part
            
            if prefix in total_weight:
                total_weight[prefix]+=weight
            else:
                total_weight[prefix]=weight
     #prefix to be proposed        
    prop = {}
    print(total_weight)       
    for prefix in total_weight:
        sequence = convertTot9(prefix)
        if (sequence not in prop or total_weight[prop[sequence]] < total_weight[prefix]):
                    prop[sequence]=prefix
                    
    return prop
    
    
if __name__=="__main__":
        file_()