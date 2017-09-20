import sys

firstnumber=float(input("enter a number "))
secondnumber=float(input("enter a number "))

try:
    result=firstnumber/secondnumber
    print(result)
    #sys.exc_info will tell you the error 
except ZeroDivisionError:
    print("the answer is infinity")
    #sys.exit will stop execution
    #sys.exit()
    # or set a flag ...
    errorflag=True
except:
    error=sys.exc_info()[0]
    print('something went wrong')
    print(error)
finally:
    if not errorflag:
        print('i will always run')
