r = input("what range would you like to test? ")
r = int(r)

for i in range(0, r):
    x = 0
    h = i
    n = -i
    while n != -1:
        x += 1
        if n % 2 == 0:
            n = n/2
        elif n % 2 != 0:
            n = (3 * n) + 1
        if n == -h:
            f = open("negative_data", "a")
            f.write(str(i) + "\n")
            f.write(str(x) + ": " + str(n) + "\n")
            break
        elif n == -5:
            f = open("negative_data", "a")
            f.write(str(i) + "\n")
            f.write(str(x) + ": " + str(n) + "\n")
            break
        elif n == -17:
            f = open("negative_data", "a")
            f.write(str(i) + "\n")
            f.write(str(x) + ": " + str(n) + "\n")
            break
        f = open("negative_data", "a")
        f.write(str(i) + "\n")
        f.write(str(x) + ": " + str(n) + "\n")
print("done")
