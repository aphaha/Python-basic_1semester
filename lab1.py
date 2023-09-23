
print("task 1")

print()

def task1(arg):
    print(len(arg))
    return arg

arg = input("Введіть текст:")

task1(arg)

print()

print("task 2")

print()

def task2(a1, oper, a2):
    if type(a1) == int and type(a2) == int and type(oper) == str:
        if oper == "+":
            print(a1 + a2)
        elif oper == "-":
            print(a1 - a2)     
        elif oper == "*":
            print(a1 * a2)
        elif oper == "/":
            print(a1 / a2)    
        elif oper == "**":
            print(a1 ** a2)
        elif oper == "//":
            print(a1 // a2)   
        else:
            print("Введіть правильний символ !")
    
        return a1, oper, a2
        
    else:    
        print("Введіть правильнi значення !")
        return None
    

a1 = int(input("Введіть перше число: "))
oper = input("Введіть операнд(+,-,*,/,//,**): ")
a2 = int(input("Введіть друге число: "))

task2(a1, oper, a2)

print()


print("task 3")

print()

def task3(list1):
    if not list1:
        return None  
    else:
        max_value = max(list1)
        return max_value


list2 = [1, 2, 3, 9, 7]
result = task3(list2)
print(f"Максимальне значення в списку: {result}")

print()


