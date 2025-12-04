# sometimes we need to create oneline functions
# mostly we use def .... that is mostly filled with blocks of code
# but if we wanted to create a function that runs under one line
# we use the built-in method lambda

add_double = lambda n: n + 2

print(add_double(3))  # this will output 5

# this is used for one line operations
# it mimicks comprehensions
# the real power in lambdas comes from our ability to pass them as arguments to and return them from other functions.

def my_func(x):
    return lambda o : o + x

new_century = my_func(100)
print(new_century(2000))

# when we call my functio x = 100
#python creates a lambda that remembers x = 100
#that lambda is then returned with x as constant 100
# so new_century  is a function equivalent to: lambda n: n + 100
# new_century is the lambda: lambda n: n + 100
#n = 2000 → computes 2000 + 100 = 2100
# when you call the first function .... it return another function to be runned now with the passed value>>>>> now to run the returned lambda we have to invoke again with the other value that will take the place of o
# inshort the 1st function just returns the lambda function to be run with the value x