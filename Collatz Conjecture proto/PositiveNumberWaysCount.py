r = input("What range would you like me to test? ")
r = int(r)

ones = 0
twos = 0
for i in range(1, r):
    n = i
    x = 0
    var = (n - 1)/3
    var2 = 2 * n
    if var.is_integer():
        var = int(var)
        x += 1
    if var2.is_integer():
        x += 1
    if x == 2:
        twos += 1
    elif x == 1:
        ones += 1
    f = open("PositiveNumberWaysCount_Data", "a")
    f.write(str(i) + ": " + str(x) + " " + str(var) + " " + str(var2) + "\n")
f = open("PositiveNumberWaysCount_Data", "a")
f.write("Ones: " + str(ones) + "\n")
f.write("Twos: " + str(twos) + "\n")
