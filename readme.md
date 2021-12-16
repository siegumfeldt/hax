# Python microtutorial

The following is a very short introduction to Python fundamentals. You can paste the snippets into
a text editor (like VS Code) and run them or you can fire up a Python console and paste or type them
into an interactive python terminal :rocket:

## Printing a value to the console

We'll start with [Hello World](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program).

```python
print("Hello World")
```

This prints the words "Hello World" to the console by calling the *function* `print()` here, passing
in the string `"hello"` - we'll get back to functions later. The need the quotes (`"..."`) to tell
Python that we want to print the actual string of letters H-e-l-l-o-(space)-W-o-r-l-d and not get
the content of a variable named Hello - we'll get to variables in a while, too.

Try printing a few words and numbers to the console - see which of the following will work:

```python
print(Hello World)
print("1234")
print(1234)
print(1234.5678)
print(1234.5678.90)
print("Hello" "World")
```

## Comments

Comments start with `#` in Python. You can put them after code:

```python
print("Hello World")  # This prints Hello World
```

or on a line of their own:


```python
# This entire line is just one really long comment that seems to go on forever...
```

## Doing simple calculations

Python can do calculations on "simple" values like strings and numbers:

```python
print(2 + 2) # 4
print(1.2 + 3.4) # 4.6
print("two" + "two") # twotwo
print("2" + "2") # 22 - why?
```

Things like `2 + 2` are called *expressions* and then Python sees one, it immediately calculated the value of the expression
(or *evaluates* the expression) and replaces the expression with the value (in this case, 4). This means that anything that we can do with
a simple value (like `2` or `"hello"`), we can do with an expression (like `1 + 1` or `"hel" + "lo"`).

We can put expressions inside other expressions to make more complex expressions:

```python
print(1 + 2 + 4) # prints 7
```

When this expression is evaluated, Python first evaluated 1 + 2 and gets 3, then evaluated 3 + 4 to get 7.

There are many kinds of expressions:

```python
print(10 - 6)      # subtraction
print(10 * 6)      # multiplication
print("a" * 10)    # multiplication
print(2 + 2 == 4)  # addition and comparison (more about that later)
```

We call things like `+` and `-` *operators*, because they do things to (or "operate on") values to make other values.
Later we'll get to functions, which are like user-defined operators.

## Storing a value in a variable

Sometimes, we need to store a value somewhere - maybe because we'll need to use it several times and don't want to
calculate it every time we need it.

Variables are like boxes for storing values. The boxes have names printed on them, and this is the name of the variable:

```python
n = 42 # n is now 42
print(n) # 42
```

Here we're storing the simple value (42) on the right of the equals sign (`=`) in the variable on the left (n). This
is also called *variable assignment*. When we *use* a variable like `n`, we're really telling Python to find the box
labeled `n`, open it up and replace the variable with whatever is in the box.

The right hand side could be the result of evaluating an expression (since anything we can do with a simple value,
we can do with an expression):

```python
n = 2 + 2  # n is now 4
```

We can also store the value of one variable in another:

```python
n = 42  # n is now 42
m = n   # m is now also 42
```

Expressions can (and most often do) use variables, letting us write things like:

```python
n = 2      # n is 2
m = n + 2  # m is 4
```

Using a variable that has not been defined doesn't work:

```python
print(x) # raises a NameError (if we never stored anything in x)
```

An undefined variable is different from one that merely has no value. `None` is a special value that
represents the absence of a value:

```python
n = None # n is now None, meaning that it has no "real" value
```

If variables are like boxes, `n` is an empty box here.

## Comparisons

We'll briefly talk about a special kind of expression that looks a bit like variable assignment: Comparison.

A double equals sign (`==`) does *not* store a value in a variable, it compares the right-hand side to the left-hand side.
The result is a *truth value* (True if the values are equal, False if they're not):

```python
print(2 + 2 == 4) # Prints the value True
```

There's a "not equal" operator, too:

```python
print(2 + 2 != 5) # Prints the value True
```

Truth values (also known as boolean values) can be used if if/then statements, which is the subject of the next section.

## Conditionals (if/then)

TODO

Your programs will usually have more than one line of code, 

## Lists

TODO

## Dictionaries

TODO




## Defining a function

A function is like a machine or factory that takes an input value and returns a output value:

```python
def add_two(n):
    return n + 2
```

The input is the value in parentheses (here it's `n`, presumably a number) and the output is the expression after `return` (`n` plus 2).

Here, we're just defining a function - `n` does not have any specific value (yet) and no numbers are being added and returned (yet).

The function doesn't do anything until we *call* (or *invoke*) it. We do this by wrtiting the name af the function and adding a pair of parentheses with an input value:

```python
print(add_two(2)) # prints 4
```

Calling a function lets us put an input value (in this case 2) into the "function-machine" and receive an output (in this case the number 4).

Like with variables, we can use function calls anywhere we could use a "simple" value.

We can assign it to a variable:

```python
n = add_two(2) # n is now 4
```

We can assign it to a variable:

```python
n = add_two(2) + add_two(2) # n is now (2+2) + (2+2) = 8
```

The *call* to the function (`add_two(2)`) looks a lot like the first line of the *definition* of the function
(`def add_two(n):`). This is even more the case if the input value to the call is itself a variable called `n`,
which is often is: 

```python
def add_two(n):  # Function definition
    return n + 2

n = 3
three_plus_two = add_two(n)  # Function call
```

There are two differences, though:

1) We use the `def` keyword to begin the definition of a function. Not for calling it (or for anything else besides defining a function).
1) We use a colon when defining a function, not when calling it. (A colon in Python usually means that an indented block of code is coming.)


### Mindbending stuff about functions (that you should probably skip)

Defining a function creates a new "thing" in your program - the function. That function gets stored, and just like the other
values that we've stored until now, a function is stored in a variable. This means that we can do other things than just
calling it. We can print it:

```python
print(add_two)
```

This gets us something like `<function add_two at 0x0000027EFD3BCEE0>`.

Since `print` is *itself* a function, we can do:

```python
print(print)
```

to get `<built-in function print>`. (What does `print(print(print))` do? Why?)

We can also store the function in a different variable to create a sort of alias:

```python
write = print
write(2)       # prints 2
```

We can even pass it to another function:

```python
def use_function_twice(f, n):
    return f(f(n))

n = use_function_twice(add_two, 5) # n is now 5 + 2 + 2 = 9
```

We can even return a function from another function:

```python
def create_function(number_to_add):
    def add_some_number(n):
        return n + number_to_add
    return add_some_number
```

This last one is like a machine that makes machines.

The `lambda` keywords lets us define *anonymous functions*:

```python
n = use_function_twice(lambda n: n+2, 2) # 
```

:exploding_head:



# Table of Contents

##  Warmup

  - 001_truth: Return True - always!
  - 002_plus: return the sum of two numbers
  - 003_greatest: Return the greatest of two numbers
 
## Sequences
  - 100_length: Return twice the length of a string
  - 100_sum: calculate the sum of a list of numbers
  - 101_search: return true if a list contains a certain number
  - 102_count: count the number of even numbers in a list (for / comprehension+if)
  - 103_pairs: calculate the pair-wise sum of two lists of numbers
  - 104_range: return a range (build a list in a loop)
  - 105_duplicate: return a list of identical numbers (comprehensions/yield)
  - 106_double: double every other number in a list (comprehensions/yield)
  - 107_every_other: return every other item from a list (loop/comprehension+range)
  - 108_dupes: Remove duplicates from a list
  - 109_split: split a list of numbers in odd and even
  - 110_merge: merge two sorted lists
  

- 200_strings:
  - slice: 
  - replace: a -> i
  - remove all e's from a string (filter / comprehension+join)
  - interpolation: name => "Hello name!"
  - reverse a string (reversed+str.join() / reversed + loop / reversed + list.insert + join)
  - b => bob, z=> zoz ...



- functions:
  - 300_call: Call a function and return the return value
  - 301_pass: Call a function with an argument and return the return value
  - 
  - _decode: decode a message using a decoder function
  - 
  - given a check() function, guess a number in (0,1,2) in two guesses
  - given a check() function, guess a number in (0,1,2,3,4,5,6) in three guesses
  - 

- dicts:
  - 400_lookup: Look up a word in a dictionary
  - 401_compose: compose a word from an {int: char} dict ( loop + dict[] / range + dict[] + join)
  - _compose2: compose a word from an {int: char} dict ( loop + dict[] / range + dict[] + join)
  - 2_decode: decode a message using a dict decoder ()
  - follow a trail of letters {">f -> o -> x"}

- objects:
  - 500_push_button: Push a button
  - 501_push_button_more: Push a button until the light turns green
  - 502_flip_switch: Flip a switch if it is not flipped
  - 503_flip_switches: Flip all the switches that aren't flipped 
  - 504_counter: Click the counter until it reaches a hundred

- complex objects:
  - login to a server
  - hack a server by adding yourself as a user (calling a method)
  - hack a server by bypassing the login process (setting an attribute)

