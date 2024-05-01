inp = "50 2012 37 31 2573"
[n, h0, a, c, q] = list(map(int, (inp).split()))
print(n, h0, a, c, q)
l1 = [h0]

for i in range(n - 1):
    temp = (a * l1[-1] + c) % q
    l1.append(temp)

l2 = []

count = n-1
for i in range(len(l1)):
    if l1.index(max(l1))+1 < i:
        count+=1

print(count)

print(l1)
print(l2)
