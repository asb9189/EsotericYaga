# Getting Started with Yaga

## A Gentle Introduction
Yaga was designed with the user experience being first and foremost. Even though
Yaga was developed in under three hours. I poured my heart and soul
into the documentation and not a scanner that provides you with helpful
error messages. (If my interperter won't accept your .yaga file your guess is as good as mine)

Unlike most programming languages, you won't need a Udemy degree to
become proficient with Yaga. Grab your favorite beverage, clean the keyboard
of gamer gunk, and buckle up because everything you learned in school is
going to be just as useless as this programming language is.

### Learning the Ropes

As mentioned previously, Yaga has several keywords accessible to you at no cost.
But before we can dive in, it's important to understand how Yaga work's under the hood.

Yaga is quite nice and loans you a chunk of memory (184 bytes to be exact) at the start of each process.
With the help of Yaga, you can manipulate this chunk of memory by shifting a single
pointer to the **right** or to the **left**. Let's go ahead and try it!

```markdown
# Remember when I said 184 bytes? Yaga loans us an array of size 16!
# Try spinning up a Python3 REPL and type: print(sys.getsizeof([0] * 16))
# Yaga also set's the pointer to point to the first element in memory (always)
Memory: [0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]
Pointer: ^

The Keywords Yaga and yAga increment and decrement the value the pointer is pointing too respectfully.

Let's make a file called test.yaga

# Did I forget to mention Yaga only cares that you put white space between
# each keyword. You can have your code all on one line or one keyword
# for every new line. Anything in the file Yaga doesn't recognize is treated
# as a comment. Theoretically, you could copy and paste something from wiki
# and Yaga will always attempt to interpret it and potentially output some interesting results.
test.yaga
    
    This program will increment the value the pointer is pointing too by two then decrement it by one
    Yaga Yaga yAga
    
After running Python3 yaga.py test.yaga our memory will look like the following:
Memory: [1][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]

But what if we wanted to print out the memory as we execute our code? No problem Yaga has you covered!
Try using the YAGAYAGA keyword in your own .yaga file ;)

At this point you have learned roughly a third of the language. The next portion is moving the pointer.

Let's rewrite our test.yaga

test.yaga

    Yaga yagA
    yAga yAga yAga yaGa
    
After running python3 yaga.py test.yaga our memory and pointer will look like the following:
Memory: [1][-3][0][0][0][0][0][0][0][0][0][0][0][0][0][0]
Pointer:    ^

Hopefully you can guess what yagA and yaGa do but if you can't heres a little help.
yagA shifts the pointer to the right and yaGa shifts the pointer to the left.

That's it!

Rather than dragging on this documentation page I thought it would be better to give
two in-depth examples and then leave a cheat sheet at the end containing all the Yaga keywords.
```

```markdown
         
Yaga
yAga
yaGa
yagA
yagayaga
YAGAYAG
yagaYAGA
YAGAyaga
agay
AGAY

```
