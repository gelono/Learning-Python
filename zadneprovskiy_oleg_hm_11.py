"""написать функцию которая принимает от пользователя 2 аргумента и делит оlин на другой.
при попытке деления на ноль вывести пользователю "ай яй яй делить на ноль можно не многим"
Все остальные исключения с поймать и вывести их значение в текстовом формате.
И в любом случае вывести. " I 'am happy that you learn python"""


def division():
    try:
        x = int(input())
        y = int(input())
    except Exception as er:
        return er
    else:
        try:
            return x / y
        except ZeroDivisionError:
            return "Division by 0 is not available to everyone"
    finally:
        print("I'am happy that you learn python")


print(division())

#-------------------------------------------------------------------
def example1():
    for i in range( 3 ):
        try:
            x = int( input( "enter a number: " ) )
            y = int( input( "enter another number: " ) )
        except Exception as er:
            return er
        else:
            try:
                print( x, '/', y, '=', x/y )
            except ZeroDivisionError:
                return "Division by 0 is not available to everyone"

#------------------------------------------------------------------
def example2(L):
    print("\n\nExample 2")
    #sum = 0
    sumOfPairs = []
    for i in range(len(L) - 1):
        try:
            sumOfPairs.append(L[i] + L[i+1])
        except TypeError as er:
            #print(er)
            sumOfPairs.append(None)
    print("sumOfPairs = ", sumOfPairs)

print(example2(([ 10, 3, 5, 6, "NA", 3 ] )))
#-------------------------------------------------------------------
def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError as er:
        return 'File not found'
    for line in file:
        try:
            print(line.upper())
        except Exception as er:
            return er
    file.close()