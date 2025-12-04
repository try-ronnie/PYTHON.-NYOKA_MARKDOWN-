#implementingg......]

#try.....except .... else .... finally block
#this is a method used to catch a form of an exception(error that happens during runtime) and lets you handle it instead of python.

def tryExcept ():
    try:
        x = int(input('enter a number: ')) # this acts as the risky code that might raise an exception 
        result = 10 / x 
        print(result)
    except ValueError:#this value error is an exception raised that then runs another command 
        print("Bruh gimme a number")
    except ZeroDivisionError:
        print("Brutha its division")
