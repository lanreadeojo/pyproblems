# Given an all lower-case string, like "python", return the first non-repeating letter from the left to right

## bbaac -> c
## bbaa --> None
## "" -> None
## bab -> a
## bacab -> c

def lowerc(s):
	dic = {}
	if len(s) == 0:
		return None
	for i in range(len(s)):
		dic[s[i]] = dic.get(s[i], 0) + 1
	for j in range(len(s)):
		if dic[s[j]]==1:
			return dic[s[j]]
