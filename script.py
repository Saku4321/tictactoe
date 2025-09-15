# This is a sample Python script.
import math
from turtledemo.sorting_animate import qsort


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#ZADANIE 1.1
r = 2.5
print(math.pi*r**2)

#ZADANIE 1.2
s="42"
con = int(s)+8
print(con)

#ZADANIE 2.
s = "Python"
print(s.lower(), s.upper(), len(s))
print(s[0], s[-1], s[1:4])      # indeksy i slicing

title = " hello world "
title_new = title.strip()
title_new = title_new.strip()
print(title_new)
title_new = title_new[0].upper() + title_new[1:6].lower() + title_new[6].upper() + title_new[7:].lower()
print(title_new)

#ZADANIE 3.1
nums = [5,2,8,1,5,2]
nums.append(10)
nums.remove(5)
print(len(nums))
nums.sort()
print(nums)
#ZADANIE 3.2
letters = ['a','b','c','d','e']
print(letters[1]+letters[3])
letters.pop()
letters.insert(0,'z')
print(letters)

def square(num):
    return num*num
def is_even(num):
    if num % 2 == 0: return True
    else: return False
print(is_even(5))
print(square(5))

def reverse_list(lst):
    return list(reversed(lst))
print(reverse_list(nums))
letters.reverse()
print(letters)

#TUPLE
t= (5,"string",3.14)
print(t)
x,y,z = t
print(x,y,z)
pt= (7,4)
def zmiana_pt(ptt):
    x,y=ptt
    pttt=(y,x)
    return pttt
print(zmiana_pt(pt))


points = [(1,2), (3,4), (5,6)]
p1,p2,p3=points
x1,y1=p1
x2,y2=p2
x3,y3=p3
print("Punkt: x=",x1,",y=",y1)
print("Punkt: x=",x2,",y=",y2)
print("Punkt: x=",x3,",y=",y3)

