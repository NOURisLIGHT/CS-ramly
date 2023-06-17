print("enter the first time by h/m/s")
h1 = int(input())
m1 = int(input())
s1 = int(input())
print("enter the second time by h/m/s")
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2
t = t1 - t2
h = int(t / 3600)
m = int((t - h * 3600) / 60)
s = int(t - h * 3600 - m * 60)
print("the diff. between the two times is ", end='', flush=True)
print(str(h) + "/" + str(m) + "/" + str(s))
