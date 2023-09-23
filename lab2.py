
# task1

def task1(number1,znak,number2):
    if isinstance(number1, int) and isinstance(number2, int) and isinstance(znak, str):
        if znak == ">":
            some_result = number1 > number2
        elif znak == "<":
            some_result = number1 < number2
        elif znak == ">=":
            some_result = number1 >= number2
        elif znak == "<=":
            some_result = number1 <= number2   
        elif znak == "==":
            some_result = number1 == number2   
        elif znak == "!=":
            some_result = number1 != number2   
        else:
            print("Wrong operator!")
            return None    
    else:
        print("Wrong value!")
        return None    

    return some_result

number1 = int(input("Write first number: "))
znak = input("Wrire logical operator: ")
number2 = int(input("Write second number: "))

result = task1(number1,znak,number2)

if result is not None:
    print(f"Result: {result}")
    
# task2

def task2(text,number):
    if isinstance(text,str) and isinstance(number,int):
        if len(text) > number:
            some_result = len(text)
        else:
            some_result = number
    else:
        print("Wrong values!")
        return None
            
    return some_result

text = input("Write some text: ")
number = int(input("Write some number: "))

result = task2(text,number)

if result is not None:
    print(f"Result: {result}")
    
#task3

def task3(number1,number2,number3):
    if all(isinstance(x, int) for x in [number1, number2, number3]) and number1 == number2 == number3:
        some_result = True
    else:
        some_result = False
        
    return some_result
    
number1 = int(input("Write some number: "))
number2 = int(input("Write some number: "))
number3 = int(input("Write some number: "))

result = task3(number1,number2,number3)

if result is not None:
    print(f"Result: {result}")    
    
    