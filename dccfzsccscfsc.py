 M = [int(x) for x in open('17_13088.txt')]
A = [x for x in M if abs(x) % 100 == 17]
count = 0
maxi = -9999999999
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if len([i for i in [x, y, z] if len(str(abs(i))) == 4]) == 2:
        if any(i % 5 == 0 for i in [x, y, z]):
            if (x + y + z) > max(A):
                count += 1
                maxi = max(maxi, x + y + z)
print(count, maxi)