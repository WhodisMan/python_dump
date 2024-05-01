s = "GEEKS"

n = len(s)

for i in range(n):
	for j in range(n):
		if (i == j) or (i+j == n-1):
			print(s[j],end="")
		else:
			print(" ",end="")
	print("")
