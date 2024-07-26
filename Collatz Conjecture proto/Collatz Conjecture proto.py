r = input("What range would you like to test? ")
r = int(r)

for i in range(1, r):
    x = 0
    m = i
    while m != 1:
        x += 1
        if m % 2 == 0:
            m = m/2
        elif m % 2 != 0:
            m = (3*m)+1

        f = open("data", "a")
        f.write(str(i) + '\n')
        f = open("data", "a")
        f.write(str(x) + ": " + str(m) + '\n')
print("Done")
