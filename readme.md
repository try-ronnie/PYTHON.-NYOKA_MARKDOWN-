#  NYOKA MARkDOWN
##  *AUTHOR* : **RONNIE GIKANDI**
### this is a well layed out markdown of python according that helps grasp key basics in a giffy .... and also questions i asked myself as i learnt this superpower
<br>

## python basics
Python code is broken into blocks to be interpreted as a continuation of one idea- these are like the recipes for each course of your meal. Maybe you need to prepare a dressing and sun-dry some tomatoes for your salad; these can be written as smaller code blocks inside of the block for a recipe as a whole.
A code block begins with a colon : followed by a newline and an indentation.
Every indentation in Python code should consist of four spaces. This is long enough to distinguish between indentation levels but short enough to provide space for indentation levels in several nested code blocks.
PEP 8 guidelines state that indentations in Python should consist of spaces rather than tabs. Tabs are visually interpreted differently in different environments, so they are not advisable in production code.
## 2.Conditional operators
Just from the name ... this are methods of controlling flow of execution in our program
 Python has many built-in classes have the following functions that can be used to compare two values:

> : greater than
>= : greater than or equal to
<: less than
<=: less than or equal to
==: equal to
!=: not equal to

but in python == checks if the objects on both sides are considered equivalent values 

``` 1 == 1  # this is true 
    '1' == 1 # this is false
```
another difference is that the js operator (===) checks if both objects have the same identity , refer to the same space in memory .... so that means that 2 arrays are different to it since it takes them as 2 different identities
but in python it would return true since it considers them to have the same values and doesnt give af if they are separate arrays in memory
```[1,2,3] == [1,2,3]
```
this would be false in js with the (===) operator
python will also chrck if an interger has the equivalent calue to a float even though theyre technically different data types :
``` 1.0 == 1 ```

### LOGICAL OPERATORS
Python has the same logical operators that youll find in many other languages 
eg **and:** returns true if both statements are true
   **or:** returns true if one of the 2 statements is true 
   **not:** Coerces the data to its boolean equivalent then reverses it 


### Vocabularies
**Interpreter:** a program that executes other programs. Python programs require the Python interpreter to be installed on your computer so that they can be run.
**Python Shell:** an interactive interpreter that can be accessed from the command line.
***Data Type:** a specific kind of data. The Python interpreter uses these types to determine which actions can be performed on different data items.
**Exception:** a type of error that can be predicted and handled without causing a program to crash.
**Code Block:** a collection of code that is interpreted together. Python groups code blocks by indentation level.
**Function:** a named code block that performs a sequence of actions when it is called.
Scope: the area in your program where a specific variable can be called.

## Common data types (canvas)
### strings -
inorder for you to "interpolate" values in python you need a special formatted string called an f-string 

```
dog_name = 'lucy'
print(f'say hello to {dog-name}' )
```

without the f-string it will just print out the variable name without passing its stored data 

for advanced formatting in python you can use the the semicolon(:)as a format specifier symbol used inside f strings
it tells python how to format the value 
```
x = 12345
print(f"{x:,}")    # adds commas → 12,345
print(f"{x:>10}")  # right-aligns it in 10 spaces
print(f"{3.14159:.2f}")  # 2 decimal places → 3.14
```

***2. What’s an “instance of the string class”?***
So in python **everything is an object** even strings , numbers and list
so when you write :
```
"hello".upper()
```
youre actually calling a method (like a function attached to an object) on an instance of the str class.
Think of a class as a blueprint — like a recipe for making cakes.
An instance is the actual cake you bake from that recipe.
so 
```
"hello"
```
is an instance (actual object) made from the str class (the blueprint for all strings).
Think of a class as a blueprint + behavior container.
It defines:

What data each instance has (its attributes or state)

What actions it can perform (its methods)

***Under the hood, each class itself is also an object (yes, even classes are objects).
It lives in memory and contains:

A dictionary of methods and attributes (like .upper(), .lower(), etc for strings)

Metadata about the type (its name, parent classes, etc)

***picture it like this .... when you type a string Here’s what really happens behind the scenes:***

1.Python sees "Ronnie" — that’s a literal string.

2.It looks up the str class, which is the blueprint for how strings work.

3.It creates an instance of that class (your actual "Ronnie" object) and puts it in memory.

4.It binds the name name to that memory location.

So yes — every typed instance is “connected” to its class through a kind of internal pointer.

You can even check that connection yourself:
Memory
│
├── class str (the blueprint)
│     ├── methods: upper(), lower(), replace(), ...
│     └── shared behavior for all strings
│
└── instance "Ronnie"
      ├── data: ['R','o','n','n','i','e']
      └── knows it belongs to class str

So "Ronnie" doesn’t contain all the methods itself — it just references its class, and when you call name.upper(), Python looks up that method in the class.
so when you run a function like :
```name.upper()```
***Python goes through a process like this internally:***

1.Look at the instance name

2.Check its class (str)

3.Look in that class’s dictionary for a function called upper

4.Call that function with your instance (name) as the argument

```str.upper(name)```
Concept	Meaning
Class---	Blueprint defining attributes + methods
Instance--- 	Actual object in memory built from a class
type()---	Tells you which class made that object
Everything---	Even classes are objects themselves
Methods---	Functions defined inside the class, shared by all instances

using the dir function () will list a method that objects responds to.... example
```
dir("hello")
# => ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]
```
***note methods that are preceded and followed by double underscores are called magic methods or dunder methods(double underscores) these methods run automatically in some certain conditions ...... that ad more will be covered under object-oriented programming

### 2.Numbers
in python ...... there are 2 types of numbers : intergers and floats
intergers --- 7
float --- 7.1
you can convert some other data types to intergers or floats with the int() and float()
class constructor functions:
```
int("1")
# => 1
int(1.1)
# => 1
float("1.1")
# => 1.1

```
python will convert an interger to a float when performing math operations
```
4/3
#1.3333333333
```
<br>

### SEQUENCE TYPES
Python has a number of different data types that are useful for storing data. Each of these types can store any type of data inside; what differs between them are the rules for organizing and accessing the data.

### 1.LISTS
There are a number of ways to create a list. Just like with creating strings, you can use the literal constructor or the class constructor.

[1,2,4,5] this is the syntax of list
you can also create a list with the list() syntax
```
list()
#  => [ ]   just gives an empty list
```
in order to access a specif element in a list you need to know its index , or the place it occupies in the list 
Indices start at 0 and move up by 1 with each subsequent element. Once the index is known, the element can be accessed using square brackets and the index.
```
list_abc = ['a','b','c']
list_abc[0]
# => 'a'
list_abc[1]
# => 'b'
list_abc[2]
# => 'c'

len([1, 3, 400, 7])
# 4
sorted([5, 100, 234, 7, 2])
# [2, 5, 7, 100, 234]
list_123 = [1, 2, 3]
list_123.pop()
# 3
list_123.remove(1)
print(list_123)
# [2]

```

### 2.TUPLES 
Nearly identical to lists with 2 key diff:
--->First, tuples are ***created with open and close parentheses*** (in place of square brackets). The tuple() class constructor function can also be used to cast lists and other iterable data types to tuples.(syntax difference)
```
(1, 2, 3)
# => (1, 2, 3)
tuple([1, 2, 3])
# => (1, 2, 3)
```
---> second , tupleas are immutable. This means that once a tuple has been ceated the typle itself cannot be changed. Pyhton functions that work on lists to create new data will still work on tuples but tuples do not contain methods like .pop and insert that would change thier contents
mostly where you will see tuples being used is in data retrieved from a database. This is because tuple protects the data as it cant be changed as your application works with the data
  
>**NOTE: Parentheses can also be used for order of operations and grouping statements. To let Python know that it's looking at a tuple, there has to be at least one comma- even in tuples with only one element: (1,).**

### 3. Sets and Dicts
Sets and dicts in Python also store sequences of data, but the individual elements in sets and dicts are unique.

#### A) SETS
A set is unindexed, unordered, and unchangeable

->**Unindexed** means that we cannot access elements of the set using square brackets as we do in lists and tuples.

->**Unordered** means that the contents of the set are in a random order.

->**Unchangeable** means that the individual elements of a set cannot be changed.

It can be **initiated with curly brackets or the set() class constructor**. **The set() class constructor takes a list or tuple as its only argument** (remember those brackets and parentheses!)

*The elements of a set are unique:*
```
set()
#->{} it gives an empty set as you can see initialized by the curly bracket{}

set(3,2,2 ,'a','b','a')
# => TypeError: set expected at most 1 argument, got 6

set([3,2,2,'a','b','a'])
#-> {3,2,'a','b'}
```

---->***NOTE: Immutable and unchangeable mean different things when we're talking about data types in Python. A set is not immutable because its overall structure can be changed; it can be made shorter or longer. It is unchangeable because an element cannot be changed into something else since you can't even get one element since its unindexed(no index give to the values) and unorder(literally no arrangement)!!!! .this is well proved by the examples im about to show you :***
```
s = {1, 2, 3}
#this is out set under variable name s .... and we know that sets are mutable but unchangeable meaning we cant do s[0] = 5 .... we cant since it doesnt know where zero is cause of no index provided by set .... but you can add any element to the set (mutable)... you can add or remove numbers from the set
s.add(4) #{1,2,3,4}
s.remove(2) #{1,3,4} its mutable as it can store more sets but unchangeable since you cant work on the elements inside 
```
uses of set
1.**Sets automatically remove duplicates.**
this is super useful when you only want distinct values instead of having to write a whole ass looping statement just to get the work done
```
numbers = [1, 2, 2, 3, 3, 3] #so it was a list of numbers .... but set only works with distinct so ofc it will clear out duplicates
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3}
```
this will help if you want maybe unique users or a set of unique items

2.**Fast membership testing**
checking whether something exists in a set is much faster than a list .... especially for big collections
>lists often do this by going through one by one checking each element which in turn becomes slow when dealing with large data **but for sets each element is converted into a hash**... that is a unique number representing that element  PYTHON uses this hash to **directly jump to a memory slot instead of scanning each element** like a list does
*Example analogy:*

List: You have a row of boxes, and to check if “3” is there, you open each box one by one → O(n) time.

Set: You have a magical locker where each number has a unique “address.” To check if “3” is there, you jump directly to its slot → O(1) time.
So the unordered structure doesn’t make it slow — because Python isn’t scanning; it’s using the hash to go directly where the element should be.
>In short: order isn’t needed for speed, because sets use hashes to locate elements instantly.\

💡 Memory trick:
Think of a set as a magical, unordered locker of unique items.
You can’t grab by index (no order), but you can check membership, add, remove, and do math operations extremely fast.


### B) DICTIONARIES
Dictionaries are Python's equivalent of a plain old JavaScript object. They are composed of key/value pairs. Each key points to a specific value, just like a word and a definition in a regular dictionary.
You can create a dictionary by simply writing key/value pairs enclosed in curly brackets. Note that keys must be in string format:
To access data from this dictionary, you can use the square bracket notation and pass in the symbol for the key you are trying to access:

```
my_dict = { "key1": 1, "key2": 2 }
my_dict["key2"]
# => 2
```
You can also use the built-in .get() method to retrieve the value for a key. This is a useful method for times when you're unsure if a key exists, as it returns None instead of an error if no matching key exists:
```
my_dict = { "key1": "value1", "key2": "value2" }
print(my_dict["key3"])
# => KeyError: 'key3'

print(my_dict.get("key3"))
# => None
```
Unlike JavaScript, you cannot use the dot notation to access keys on dictionaries — only the bracket notation will work:
You can also create dictionaries using the dict() method..
```
dict(x = 1, y = 2)
# => {'x': 1, 'y': 2}
```

### NONE
this a special value that represents the absence of a value
in js theres usually null or undefined ....
Python won't let you create a variable without assigning a value. You must explicitly assign a value of None if you want an "empty" variable:
```
no_value
# => NameError: name 'no_value' is not defined

no_value = None
print(no_value)
# => None

```

### BOOLEANS
There are two values of the boolean and that true or false
then theres the concept of truthy and falsy
So:
Anything “empty” or “zero” = falsy
Anything “non-empty” or “non-zero” = truthy

```
if 0: str
    print('hello world")
else
    print {'so its falsy'}
    #-> so its falsy is printed out since zero in ython is considered falsy
if 1:
    print("Runs!")
else:
    peint('doesnt')
# Output: Runs!

```


## ERROR HANDLING
**Syntax errors** are pretty self-explanatory
**Logic errors** Logic errors are often difficult to find because they are not perceived as errors by the Python interpreter itself.. To find a logic error, a programmer will often need to comb through their code line by line. Debugging tools such as pdb (which we will cover later on in Phase 3) are very helpful for locating and fixing logic errors.
**EXCEPTIONS**Exceptions pop up when the interpreter knows what to do with a piece of code but is unable to complete the action. A key difference between the other types of errors and exceptions is that the Python interpreter can continue reading your application after an exception- you just need to tell it what to expect. 
such errors include
    1.*AssertionError* -> n assert() statement tells the interpreter that the code inside of it must proceed without error or exception. If an assertion fails, an AssertionError is raised.
    2.*IndexError & KeyError* -> IndexErrors arise when you try to access an element at an index past the end of a list.  Key errors relate to dict objects in Python (similar to JSON objects). If a key is referenced but does not exist, this exception is thrown
    3.*NameError* -> A NameError arises when a name is referenced before it has been defined.
    4.*TypeError* -> TypeErrors arise when an operation or function is applied to an object of the wrong type.




## FUNCTIONS 
WORKS THE SAME WAY AS JS
but there are some key differences : 
Use the def keyword to identify this code as a function.
Write the name of the method in snake case (by convention).
Parameters are still defined in parentheses, after the method name.
Instead of curly brackets, begin with a colon after the parentheses.
In Python, we must indent all code that is meant to be executed in my_function. The PEP-8 standardsLinks to an external site. for writing Python code state that each indentation should be composed of four spaces (though the interpreter is less picky).
return statements in Python work very similarly to those in JavaScript, but no semicolon is needed after the return value.
Rather than closing with a curly bracket, any new code can be written at the original indentation level.
arguements work the same as js 
We can fix the behavior of our JavaScript function above by providing a default argument: a value that will be used if we don't explicitly provide one.

```
function sayHi(name = "friend") {
  console.log(`Hi there, ${name}!`);
}

sayHi();
// => "Hi there, friend!"
sayHi("Sunny");
// => "Hi there, Sunny!"
```
for **return values** when using return just like in js it returns the specific in-line value and breaks of the running of the code 
*pass* There will be times when you're writing out your code and know that you will need a function later, but you don't quite know what to put in there yet. A good practice in Python development is to make use of the pass keyword in empty functions until they are ready to be fleshed out.
Because Python uses indentation to determine when a code block starts and ends, it is necessary to put something inside of an empty function- comments, sadly, do not count.
Python developers typically opt for pass over return None because it is a statement rather than an expression. It does not terminate the function like a return statement would do. You can even put code after your pass and it will be executed! A pass statement reminds you that there is work to be done without interfering with your development.




## DEBUGGING USING IPDB
IPBD is just a more improved version of the python REPL
THE Best part of it is that you can inject it to your code rather than having to start up your whole REPL and copy paste your code just to see if its working

once you install it via the dependencies or by yourself .... you can use its function anywhere which is 
```
ipdb.set_trace()
```
ipdb.set_trace() gives you similar functionality to using debugger in a JavaScript application, in that it lets you set a breakpoint in your code that will pause the execution of your program at a certain point so you can inspect the variables, functions, and other context available at a specific place in your code.





















































