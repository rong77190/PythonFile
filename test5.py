from __future__ import division
def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def sheng(x,y):
    return x*y
def chu(x,y):
    return x/y

# def operator(x,o,y):
#     if o == "+":
#         print(jia(x,y))
# operator(2,"+",9)

operactor= {"+":jia,"-":jian,"*":sheng,"/":chu}
def f(x,o,y):
    print(operactor.get(o)(x,y))





f(3,"-",1)
x = 1
y = 2
operactor="/"
result = {
    "+":x+y,
    "-":x-y,
    "*":x*y,
    "/":x/y
}
print (result.get(operactor))
