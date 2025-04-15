# 5. Exercises

Write a function for each of the following questions.

## Practice Questions

1. Calculate and display the absolute value of a number entered by the user.

2. Determine if an integer entered by the user is even or odd.

3. Read three numbers and print the smallest of these three numbers.

4. Calculate the total salary of an employee. Read the hourly wage and the number of hours worked as input. If the employee worked more than 40 hours, overtime hours are paid at 1.5 times the hourly wage.

5. Read three positive numbers representing the lengths of the sides of a triangle. Print:
   - "Scalene" if all three sides are unequal
   - "Isosceles" if two sides are equal
   - "Equilateral" if all three sides are equal

6. A professor provides you with three grades calculated out of 100. Calculate the average and print "fail" if the final grade is less than 60/100. Otherwise, print the student's grade.

7. Read a final course grade as input. If the grade is less than 0, or if the grade is greater than 100, then display "This grade is invalid" and terminate the function. If the grade is valid, then display a letter corresponding to the grade according to the following conditions:
   - **E**: less than 60
   - **D**: from 60 to less than 70
   - **C**: from 70 to less than 80
   - **B**: from 80 to less than 90
   - **A**: 90 or more

8. Read a number between 1 and 10 inclusive.
   - If the number is not in this range, display *"invalid"*.
   - If the number is valid, display *"valid"*.

9. Read a number between 1 and 10 inclusive.
   - If the number is not in this range, display *"invalid"* and ask for the number again. You must ensure that the number is valid before continuing to the next step. There is no limit on the number of incorrect attempts.
   - If the number is valid, display *"valid"*.

10. Read a number between 1 and 10 inclusive.
    - If the number is not in this range, display *"invalid"* and ask for the number again. You must ensure that the number is valid before continuing to the next step. There is a limit of 3 incorrect attempts.
    - If the maximum number of incorrect attempts has been reached, display *"Maximum number of attempts reached."* and the method must terminate.
    - If the number is valid, display *"valid"*.

11. Read an integer and display it in reverse. For example, if the user enters `123456`, the program displays `654321`. For this exercise, you cannot reverse a string representing the number; you must use an `int` and use division and modulo operations on this `int`.

12. Read an integer and display a countdown from this number to 0. When the countdown is complete, display "Finished!" instead of the number 0. For example, if the entered number is 5, you should display:
    ```
    5
    4
    3
    2
    1
    Finished!
    ```

13. For each of the following questions, define a list of integers containing approximately 10 values of your choice. The exact length of the list and the numbers it contains are up to you, but they should allow for good testing of the questions. Answer the questions in different functions. Using a `for` loop on the indices of the list:
    1. Find the sum and average of all numbers in the list.
    2. Display all even numbers contained in the list.
    3. Determine if all numbers in the list are positive or not. If all numbers are positive, display *True*, otherwise display *False*.

14. Repeat the previous question, but using a `while` loop on the list.
