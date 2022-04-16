# Exercise 04: Creating Records
At this point in the development of your NEA project it falls on you to decide the best way to store **records** in your program. What most experienced programmer would do at this point is make use of a database, either local or remote, and store and retrieve the information from there (*Hey, repl.it even has it's own wonderful data storage function, it's on the left hand toolbar when you're developing - give it a go when you've got time*). The problem with that is twofold, first we can only use the built in libraries and the basic database libraries in Python can leave a lot to be desired, and secondly this adds *so much unnecessary complexity* to something that you're meant to be able to do with no internet access, no reference resources or code examples!

## Creating a 2D List of Records

In order to take best advantage of the built in capabilities of Python, and make it as straight forward as possible to implement, let's take a look at a question and how we might tackle it in the most efficient way.

```
Store the information required to create a leaderboard for a gaming event, you will need to take in:
* Contestant Name
* Contestant Email Addres
* Best Score for the match
```

It's basically asking us to make a **high score** table for an eSports event - nice. Now, as ever, the first step in implementation will be to start to collect the data from the user - but this time, even before we start, we're going to set up a blank `list` that will eventually store the records. So you'll need something like this:

```python
leaderboard = []
```

Which is just a good variable name being set equal to `[]` which is a blank `list`. Simple so far? Let's add to that with a loop that asks the user for the data required over and over again.

```python
leaderboard = []

while(True):
  name = input("Name: ")
  email = input("Email: ")
  bestScore = int(input("Best Score: "))
```

We're making good use of our Frankenstein-friend `while(True):` to loop the indented code below it for as long as the program runs. The data collection isn't anything exciting, we're not putting validation in at this point to try and make the code more understandable but in the real NEA make sure that's your next step. The only real thing of note is that the score has been set to an `int` as we're expecting whole numbers.

With the data collected we need to start thinking about what makes a **record**? Well a record is a collection of **fields** that are all about a single entity: in our case a record would be all of that data collected together. At this point it's worth thinking a bit further ahead, because this is all going to be stored in a 2D List and that looks a bit like a table. Grab a pen and paper and quickly sketch out what this table would look like with data in it - including some example data.

![Table Design](https://static.curriculum.repl.co/GCSEPy/design.png)

So this is what we're going to aim to build. First things first, let's put that data that's been entered into its own row.

```python
leaderboard = []

while(True):
  name = input("Name: ")
  email = input("Email: ")
  bestScore = int(input("Best Score: "))

  row = [name, email, bestScore]
```

This is nice and simple really, we're just creating another `list` that contains all of the variables we've just accessed but in the order from our plan. We then need to take that row and add it to the `leaderboard` itself.

```python
leaderboard = []

while(True):
  name = input("Name: ")
  email = input("Email: ")
  bestScore = int(input("Best Score: "))

  row = [name, email, bestScore]
  leaderboard.append(row)
```

The `append` function adds a variable to a `list`, in this case it's adding another row to our table and as long as we remember the order which is `list.append(variable)` you'll be able to construct a consistent 2D data structure with absolute ease. That's it, we're done. Each iteration of the while loop would add a new row to the records for us - the only problem is that we haven't printed out the `list` yet so that we can see it changing.

## Pretty Printing
We know that we can make pretty much anything print out from python with the `print()` command, the problem is that if we do that to a 2D `list` then we get the literal code appearing on screen and that's just not nice. It'll look a little something like this `[["Jack", "jack@test.com", 429],  ["Penny", "penny@test.com", 12941]]` It's something than regular users should never really have to see. What we need then is a way of printing a 2D array out nicely and that's called *pretty printing*.

The main strategy we're going to start with is that we're going to use a `for` loop to pull out each row, one at a time, and just print those.

```python
leaderboard = []

while(True):
  name = input("Name: ")
  email = input("Email: ")
  bestScore = int(input("Best Score: "))

  row = [name, email, bestScore]
  leaderboard.append(row)

  print("== LEADERBOARD ==")
  for row in leaderboard:
    print(row)
```

The key part of this is the line `for row in leaderboard:` which goes through each element in the `leaderboard` and extracts it, one at a time, to the variable `row`. When we then `print(row)` we're printing out the row that's just been extracted, this gives us this slightly nicer version.

```python
== LEADERBOARD ==
["Jack", "jack@test.com", 429]
["Penny", "penny@test.com", 12941]
```

But it's still not idea, there's a lot of code still remaining. My Nan can play Fortnite with the best of them, but she gets a bit freaked out if she sees source code being dumped onto the screen! Let's help people like my Nan out a bit and give the code a bit more of a tweak to tidy that up, this time we're using a nested `for` loop.

```python
leaderboard = []

while(True):
  name = input("Name: ")
  email = input("Email: ")
  bestScore = int(input("Best Score: "))

  row = [name, email, bestScore]
  leaderboard.append(row)

  print("== LEADERBOARD ==")
  for row in leaderboard:
    for item in row:
		print(item, end="\t")
	  print()
```

That nested `for item in row:` is doing the heavy lifting here, if an example of the row is `["Jack", "jack@test.com", 429]` then the `item` is going to be each of those elements extracted one at a time. There's some more brain-power on display here though, because the `print` command is being customised, the line `print(item, end="\t")` has a second argument that customised what `print` does at the end. By default `print` will create a newline, but here we've used `end="\t"`to tell the interpreter that instead of starting a new line each time it should just press the `tab` key instead! This means we get this nice output:

```python
== LEADERBOARD ==
Jack	jack@test.com	429
Penny	penny@test.com	12941
```

It's by no means perfect, but it's certainly much nicer than we've seen before. You could customise it more with some headings, maybe the odd `|` to separate the items, but that's just a matter of taste!

## Your Task
MockéBeasts is a video game where a lone child stalks the wilderness to capture tiny monsters in small plastic orbs, it sounds very familiar. The developer of MockéBeasts wants to build a MockéDex to store the information about them in an easily accessible manner. 

1. Build a command line tool to take in the following information in a loop:
	* Beast Name
	* Beast Type (*Must be Earth, Fire, Air, Water or Spirit*)
	* Special Move
	* Starting HP (*A value between 1 and 999*)
	* Starting MP (*A value between 1 and 999*)

2. Add functionality to be able to add each beast to a 2D data structure

3. Add a pretty print function that prints out the list of beasts nicely after each one has been added

### Extension

4. Update your pretty print function so that the output includes the **index value** of the record in the 2D `list`, this should be amended so that the first beast is number 1, the second is number 2, etc.

  