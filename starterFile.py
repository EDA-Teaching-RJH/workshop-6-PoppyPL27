#Your code goes here. 

import math

def main():
    print(safe_divide(20,5))
    print(safe_divide(7,0))
    print(str(process_list([5,'r', 0, 34])))
    print(nested_operations("7","5"))
    print(nested_operations("b","5"))
    print(nested_operations("7","0"))
    process_input()

def safe_divide(a, b):
    """
    This function takes two numbers as parameters and divides the first by the second.
    Parameters:
        a (int): the number you want to divide by b
        b (int): the number you want to divide a by
    Returns:
        str: the result of the calculation
    """
    try:
        result = a/b
        return "your result is "+ str(result)
    except ZeroDivisionError:
        return "you cannot divide by 0"

def process_list(input_list):
    """
    This function takes a list as a parameter and returns the sum of the squares of all the integers in the list
    Parameters:
        input-List: the list of values
    Returns:
        squared sum (int): the sum of the squares of all the integer values
    """
    squaredSum = 0
    for item in input_list:
        try:
            itemSquared = item * item
            squaredSum = squaredSum + itemSquared
        except(TypeError, ValueError):
            pointless = "this is a pointless line of code"
    return squaredSum

def nested_operations(a, b):
    """
    This function should try to convert both parameters to integers, divide the first by the second, and then calculate the square root of the result. 
    Parameters
        a (str): the first number we are working with
        b (str): the second number we are working with
    Returns:
        str: the result of the calculation or an appropriate error message
    """
    try:
        numberOne = int(a)
        numberTwo = int(b)
        try:
            division = numberOne/numberTwo
            root = math.sqrt(division)
            return "the square root of the division of "+a+ " and "+b+" is "+ str(root)
        except ZeroDivisionError:
            return "you cant divide by 0"
    except ValueError:
        return "one of these inputs are not numbers. you cannot perform calculations on non numerical values"

def process_input():
    """
    This function takes a number from the user and squares it
    Parameters:
        N/A
    Returns:
        N/A
    """
    Input = input("please enter a number: ")
    try:
        Input = float(Input)
        Input = Input*Input
    except ValueError:
        print("this isnt a valid number")
    else:
        print("your result is "+str(Input))
    finally:
        print("processing complete")



main()
