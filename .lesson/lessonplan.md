# Exercise 04: Creating Records

## Learning Objectives
1. Students will understand that a record is composed of related fields and stored in a 2D Data structure
2. Students will be able to create 2D Lists to store the results of their data collection to allow easy access and manipulation
3. Students will be familiar with the concept of *pretty printing* and be able to develop simple algorithms to make the output process better
 
## Overview
This unit takes roughly an hour to complete and whilst it might seem like a straightforward addition to their skillset, students often fall at this hurdle when trying to work with dynamic 2D data structures in their NEA controlled time. This unit has been built to allow consolidation of the previously acquired skills in context and supports the spaced practice methodology of concept retention.

It is really important that this topic is understood to support the next two aspects, that of quick saving and loading as well as data manipulation: without the use of this data structure students have to invent their own data storage methods which adds to cognitive load in an otherwise stressful situation.

## Delivering the content in class

1. ***Creating a 2D List*** (20 minutes) Model the builds and, in particular, take the time to plan out the 2D array as a table on a whiteboard or similar analogue medium to model data design to the students. Talk about global variables and why this 2D list needs to be global in nature for this system to work. Remind students of the concepts behind indexing (and zero indexing is key), and how a 2D list is a list-of-lists and so doesn't behave quite the way you'd expect a table to. Ask the students to build the leaderboard.

2. ***Pretty Printing*** (10 minutes) Talk to the students about the major issue with the previous task, i.e. that they have no idea if the data actually went in. Demonstrate simple printing with `print()` of the 2D list and how awful that is for readability, then model the build of the simple first level iteration and then tidying it up with the nested `for` loops. Students will need to have the `end` argument to print explained as well as the literal character `\t` for `tab`.

3. ***Task*** (30 minutes)  Students should understand what this is a comedy version of, but if not remind them that they need to 'be the very best, the best there ever was' and prepare yourselves for a sing along of a theme tune you've not thought about since the early 2000s. Students should be prompted to add validation to tis data entry to ensure consistency in the 2D list. Encourage further development of the data and expansion to store additional information. If students are not engaging with the task please just ask them to create a 'dex' for whatever they are interested in - some students, for example, may want to think along Fifa lines and store football players, some may want to replicate the core mechanics of top trumps - anything that allows data storage and slightly links to their interests.


  