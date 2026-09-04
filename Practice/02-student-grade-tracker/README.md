"""
====================================================================
Python Exercise: Student Grade Tracker (Lists)
====================================================================

Exercise Description:
---------------------
In this exercise, you will create a Python program that manages a
collection of student grades using a list.

The program should allow the user to enter multiple grades, store
them inside a list, display useful information about the grades,
search for specific values, and remove grades when requested.

This exercise is designed to help you practice working with Python
lists while reinforcing loops, variables, user input, conditional
logic, and basic built-in functions.


Learning Objectives:
--------------------
By completing this exercise, you should gain experience with:

- Creating and using lists
- Adding items to a list with append()
- Accessing values stored inside a list
- Using loops to collect user input
- Searching for values using the in operator
- Removing values from a list with remove()
- Using built-in functions such as:
    - len()
    - max()
    - min()
    - sum()
- Calculating an average
- Using if / else statements to control program flow


Program Guidelines:
-------------------

Your program should complete the following tasks:


1. Collect User Information:
   - Ask the user for their name.
   - Display a personalized greeting.
   - Explain what the program will do.


2. Create the Grade List:
   - Create an empty list called grades.
   - Ask the user how many grades they would like to enter.
   - Use a loop to collect each grade.
   - Store every grade inside the list.


3. Display Grade Information:
   - Display the complete list of grades.
   - Display:
        - Highest grade
        - Lowest grade
        - Average grade
        - Total number of grades entered


4. Search the List:
   - Ask the user for a grade to search for.
   - Determine whether the grade exists in the list.
   - Display an appropriate message.


5. Remove a Grade:
   - Ask the user if they would like to remove a grade.
   - If the grade exists:
        - Remove only the first occurrence.
        - Display the updated list.
   - If the grade does not exist:
        - Display an error message.


6. End the Program:
   - Thank the user for using the program.
   - Display the final list of grades.


Requirements:
-------------
Your program must include:

- At least one list
- append() to add items
- remove() to remove an item
- A loop for collecting grades
- A loop or conditional statement when appropriate
- Variables for storing user information
- if / else statements
- User input using input()
- Numeric conversion using int() or float()


Challenge Extensions (Optional):
--------------------------------
After completing the basic version, consider improving your program
by adding additional features:

- Sort the grades from lowest to highest.
- Sort the grades from highest to lowest.
- Count how many grades are passing (70 or higher).
- Count how many times a specific grade appears.
- Allow the user to edit a grade by entering its index.
- Prevent invalid grades (less than 0 or greater than 100).
- Continue asking for grades until the user types "done".
- Allow the user to repeat the program without restarting it.


End Product:
------------
The finished program should be a complete interactive grade tracker.

When the program runs, the user should:

1. Enter their name.
2. Enter multiple grades.
3. View all stored grades.
4. View statistics about the grades.
5. Search for a specific grade.
6. Remove a grade if desired.
7. View the updated list.
8. Exit the program successfully.


Goal:
-----
Create a simple but functional Python program that demonstrates your
understanding of lists, loops, variables, user input, and conditional
logic while practicing common list operations.

====================================================================
"""

"""
====================================================================
Sample Test Data
====================================================================

Use the following information to test your program. You can also
change the values to test different scenarios.

Student Name:
-------------
Jordan

Number of Grades:
-----------------
12

Grades:
-------
87
94
76
88
91
100
69
82
95
73
84
90

Grade to Search:
----------------
95

Grade to Remove:
----------------
69


Expected Results:
-----------------
Original Grades:
[87, 94, 76, 88, 91, 100, 69, 82, 95, 73, 84, 90]

Highest Grade:
100

Lowest Grade:
69

Average Grade:
85.75

Total Grades:
12

Search Result:
95 was found in the list.

Updated Grades:
[87, 94, 76, 88, 91, 100, 82, 95, 73, 84, 90]

--------------------------------------------------------------------

Additional Test Cases
---------------------

Case 1:
Search Grade:
50

Expected:
50 was not found in the list.

--------------------------------------------------------------------

Case 2:
Grade to Remove:
150

Expected:
Grade not found. Nothing was removed.

--------------------------------------------------------------------

Case 3:
Grades:
100
100
95
95
88
88
70
70
60
60

Search Grade:
88

Remove Grade:
88

Expected Updated Grades:
[100, 100, 95, 95, 88, 70, 70, 60, 60]

(Note: Only the first occurrence of 88 should be removed.)

====================================================================
"""