# Impact Analytics Assignment

## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

 

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773


## Approach - 
Let’s Assume a day when a student is present I represent the attendance as 1 (one) . If absent then I represent it as 0 (zero) so a particular way of attending all the classes will look like a binary number.

When days n = 2, ways to attend classes would look like
11 (present on both days)
01 (absent on first day, present on second day)
10 (present on first day, absent on second day)
00 (absent on both days)

Let a(n) be the number of ways when 4 or more consecutive absences not allowed

Now let’s focus on the last digit of number as 

Case 1: when last digit is 1 
In this case the last n - 1 digits must satisfy the condition that no 4 or more consecutive zeros then number of ways would be a(n-1)
Case 2: when last digit is 0
In this case when last digit is already 0 we have to place other digits in such a way that remaining digits will form valid way so 
10 (1 before last zero, and renaming is valid) = a(n-2)
100 (1 before last two zeros, and renaming is valid) = a(n-3)
1000 (1 before last tree zeros, and renaming is valid) = a(n-4)

Number of ways to attend n days can be represented by below recurrence relation 
a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4)

above recurrance relation looks like fibonacci series so just like fibonacci series we use base values to calculate the next value.

Base cases would be   
n = 0, a(0) = 1
n = 1, a(1) = 2
n = 2, a(2) = 4
n = 3, a(3) = 8
n = 4, a(4) = 15

### Answer 1 - calculate the number of ways to attend the classes 
To calculated value of n = 5
Just put n = 5 in recurrence relation
a(5) = a(4)+a(3)+a(2)+a(1)
a(5) = 15 + 8 + 4 + 2 = 29
So the number of ways to attend classes is 29 when 4 or more consecutive absences are not allowed.
### Answer 2 - calculate the probability of missing the graduation ceremony  
To calculate the probability of missing the graduation ceremony we have to find out the number of ways of missing the graduation ceremony. 
Now a student will miss the ceremony if he/she is absent on the last day.
Now number of ways to miss ceremony = ways to attend n classes - ways to attend (n-1) classes
Why n-1 ? because the student is absent on the last day.

Now probability of missing ceremony = (ways to miss ceremony) / (ways to attend classes)
When n = 5
Probability = (a(5)-a(4))/a(5) = (29-15)/29 = 14/29

Similarly we can calculate the value for any n.

# Steps to run code
1. clone repo
2. change to impact-analytics-assignment directory
3. python main.py <days>

python main.py 5     
Output - For 5 days: 14/29  
python main.py 10     
Output - For 10 days: 372/773