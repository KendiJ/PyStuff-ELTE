#1
my_list = [1,2]
for v in range (2):
    my_list[-1] = my_list[v]
print(my_list)

#2
nums = [1, 2, 3]
vals = nums
print(vals)

#3
def function_1(a):
    return a
def function_2(a):
    return function_1(a) * function_1(a)
print(function_2(2))

#4
for i in range(5):
    if i // 2 == 0:
        print(i)

#5
a = 10
b = True
print(isinstance(a, float) or isinstance(b, bool))

#6
class Foo:
    value = 10
    def __init__(self):
        self.value = 5
f = Foo()
print(Foo.value, f.value)

#7
count = 3
while count > -1:
    print("*")
    count -= 1

#8
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))

#9
str1 = "Hi"
print(str1 * 3)

#10
my_tuple = (2, 3)
# my_tuple[1] = my_tuple[1] + my_tuple[0]
print(my_tuple)

#11
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']
print(dict[v])

#12
class A:
    def __init__(self):
        pass
    def show(self):
        print("A")
        
class B(A):
    def show(self):
        print("B")
        super().show()
b = B()
b.show()

#13
print(chr(ord('b') + 3))

#14
# class A:
#     l = 0
#     def __init__(self, v = 2):
#         self.v = v
#         A.l += 1
# a = A()
# b = A()
# print(a.l == b.1)
# print(A.l)

#15
class T:
    def __init__(self, v = 2):
        self.v = v
    def set(self, v = 1):
        self.v += v
        return self.v
a = T()
b = a
b.set()
print(a.v)

#16
def mystery(n):
    if n == 0:
        return 0
    else:
        return mystery(n - 1) + 1
print(mystery(2))

#17
# for line in open('text.txt', 'r'):
#     print(line)

#18
print(float("1.3"))

#19
try:
    value = 0
    print(int(value)/ len(value))
except ValueError:
    print("Bad input")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Boo!")

#20
x = 10
def func():
    x = x + 1
    print(x)
# func()