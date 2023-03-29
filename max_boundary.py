def maxb(word):
    n = len(word)
    f = [0]*n
    k = 0
    for i in range(1,n):
        while word[k] != word[i] and k > 0:
            k = f[k -1]
        if word[k] == word[i]:
            k = k + 1
        f[i]= k
    return f

def pat_match(s,pattern):
    seperator = '\x00'
    assert seperator not in s and seperator not in pattern
    n = maxb(pattern+seperator+s)
    lpat=len(pattern)
    i=0
    for i,ni in enumerate(n):
        if ni==lpat:
            matched_index = i - (2 * lpat)
            return matched_index
        i+=1
    return -1
    