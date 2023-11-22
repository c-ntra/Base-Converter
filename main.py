a = input("Number to convert: ")
b = int(input("Base of input number: "))
c = int(input("Base of output number: "))


def deci_dual(n):
    n = int(n)
    output = []
    while n != 0:
        result = int(n / 2)
        remainder = n - result * 2
        output.append(remainder)
        n = result
    output.reverse()
    print("Your converted number is: ", *output, sep="")


def deci_hexa(n):
    n = int(n)
    output = []
    while n != 0:
        result = int(n / 16)
        remainder = n - result * 16
        if remainder == 10:
            remainder = "A"
        if remainder == 11:
            remainder = "B"
        if remainder == 12:
            remainder = "C"
        if remainder == 13:
            remainder = "D"
        if remainder == 14:
            remainder = "E"
        if remainder == 15:
            remainder = "F"
        output.append(remainder)
        n = result
    output.reverse()
    print("Your converted number is: ", *output, sep="")


def dual_deci():
    newlist = []
    output = []
    m = 0
    for ia in a:
        newlist.append(ia)
    newlist.reverse()
    for il in newlist:
        il = int(il)
        hoch = 2 ** m
        result = il * hoch
        m += 1
        output.append(result)
    add = 0
    for io in output:
        io = int(io)
        add += io
    print("Your converted number is:", add)


def dual_hexa():
    newlist = []
    output = []
    m = 0
    for ia in a:
        newlist.append(ia)
    newlist.reverse()
    for il in newlist:
        il = int(il)
        hoch = 2 ** m
        result = il * hoch
        m += 1
        output.append(result)
    add = 0
    for io in output:
        io = int(io)
        add += io
    n = add
    output = []
    while n != 0:
        result = int(n / 16)
        remainder = n - result * 16
        if remainder == 10:
            remainder = "A"
        if remainder == 11:
            remainder = "B"
        if remainder == 12:
            remainder = "C"
        if remainder == 13:
            remainder = "D"
        if remainder == 14:
            remainder = "E"
        if remainder == 15:
            remainder = "F"
        output.append(remainder)
        n = result
    output.reverse()
    print("Your converted number is: ", *output, sep="")


def hexa_deci():
    newlist = []
    output = []
    m = 0
    for ia in a:
        if ia == "A":
            ia = "10"
        elif ia == "B":
            ia = "11"
        elif ia == "C":
            ia = "12"
        elif ia == "D":
            ia = "13"
        elif ia == "E":
            ia = "14"
        elif ia == "F":
            ia = "15"
        newlist.append(ia)
    newlist.reverse()
    for il in newlist:
        il = int(il)
        hoch = 16 ** m
        result = il * hoch
        m += 1
        output.append(result)
    add = 0
    for io in output:
        io = int(io)
        add += io
    print("Your converted number is:", add)


def hexa_dual():
    newlist = []
    output = []
    m = 0
    for ia in a:
        if ia == "A":
            ia = "10"
        elif ia == "B":
            ia = "11"
        elif ia == "C":
            ia = "12"
        elif ia == "D":
            ia = "13"
        elif ia == "E":
            ia = "14"
        elif ia == "F":
            ia = "15"
        newlist.append(ia)
    newlist.reverse()
    for il in newlist:
        il = int(il)
        hoch = 16 ** m
        result = il * hoch
        m += 1
        output.append(result)
    add = 0
    for io in output:
        io = int(io)
        add += io
    n = add
    output = []
    while n != 0:
        result = int(n / 2)
        remainder = n - result * 2
        output.append(remainder)
        n = result
    output.reverse()
    print("Your converted number is: ", *output, sep="")


if b == 10:
    if c == 2:
        deci_dual(a)
    elif c == 16:
        deci_hexa(a)
if b == 2:
    if c == 10:
        dual_deci()
    elif c == 16:
        dual_hexa()
if b == 16:
    if c == 10:
        hexa_deci()
    elif c == 2:
        hexa_dual()
