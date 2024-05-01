a = [7, 8, 12, 1, 9, 0]
t = []
for i in range(1,len(a)):
    t.append(a[i] - a[i-1])
print((max(t)))
