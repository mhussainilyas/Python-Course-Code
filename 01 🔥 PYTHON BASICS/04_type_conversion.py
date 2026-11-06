# =======================
#   Implicit Conversion
# =======================

a = 100
b = 120.3
c = a + b
print(c, type(c))

# =======================
#   Explicit Conversion
# =======================

num = "100"
intNum = int(num)
print(intNum, type(intNum))

num = 100.2
intNum = int(num)
print(intNum, type(intNum))

num = 100
strNum = str(num)
print(strNum, type(strNum))

num = 100.6
strNum = str(num)
print(strNum, type(strNum))

num = 100
floatNum = float(num)
print(floatNum, type(floatNum))

num = "100"
floatNum = float(num)
print(floatNum, type(floatNum))

num = "100abc"
intNum = int(num) # ValueError

num = "100.1"
intNum = int(num) # ValueError

x = "100"
y = "200"
z = int(x) + int(y)
print(z, type(z))