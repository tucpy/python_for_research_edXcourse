# python_for_research_edXcourse
Exercises for homework (Week 1). In this homework, we will use objects, functions, and randomness to find the length of documents, approximate pi, and smooth out random noise.


+++Exercise 1: count the frequency of each letter in a given string.
Import the string library.
1. Create a variable alphabet that consists of the lowercase and uppercase letters in the English alphabet using the ascii_letters data attribute of the string library.

2. Consider the sentence 'Jim quickly realized that the beautiful gowns are expensive'. Create a dictionary count_letters with keys consisting of each unique letter in the sentence and values consisting of the number of times each letter is used in this sentence. Count upper case and lower case letters separately in the dictionary.

3. Rewrite your code from 1b to make a function called counter that takes a string input_string and returns a dictionary of letter counts count_letters. Use your function to call counter(sentence).

4. Abraham Lincoln was a president during the American Civil War. His famous 1863 Gettysburg Address has been stored as address, and the counter function as defined in part 1c has been loaded. Use these to return a dictionary consisting of the count of each letter in this address, and save this as address_count.
Print address_count.

5. The frequency of each letter in the Gettysburg Address is already stored as address_count. Use this dictionary to find the most common letter in the Gettysburg address.
Store this letter as most_frequent_letter, and print your answer.

+++Exercise 2: Consider a circle enclosed by a square. The ratio of their areas is pi / 4. In this six-part exercise, we will find a way to approximate this value.

1. Using the math library, calculate and print the value of pi / 4

2. Using random.uniform(), create a function rand() that generates a single float between -1 and 1.

Call rand() once. So we can check your solution, we will use random.seed() to fix the value called by your function.

3. The distance between two points x and y is the square root of the sum of squared differences along each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the distance between them. Use your function to find the distance between x=(0,0) and y=(1,1).

4. Write a function in_circle(x, origin) that determines whether a two-dimensional point falls within a unit circle surrounding a given origin.
Your function should return a boolean that is True if the distance between x and origin is less than 1, and False otherwise.
distance(x, y) as defined in 2c is pre-loaded.
Use your function to determine whether the point (1,1) lies within the unit circle centered at (0,0).
Print your answer.

5. Create a list of R=10000 booleans called inside that determines whether each point in x falls within the unit circle centered at (0,0). Make sure to use in_circle.
Find the proportion of points within the circle by summing the count of True in inside, and dividing by R.
Print your answer. This proportion is an estimate of the ratio of the two areas!
6. Find the difference between your estimate from part 2e and math.pi / 4. Note: inside and R are defined as in Exercise 2e.
Print your answer.

+++Exercise 3:

A list of numbers can be very unsmooth, meaning very high numbers can be right next to very low numbers. This list may represent a smooth path in reality that is masked with random noise (for example, satellite trajectories with inaccurate transmission). One way to smooth the values in the list is to replace each value with the average of each value's neighbors, including the value itself.

1. Write a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors n_neighbors on either side of a given member of the list to consider.
For each value in x, moving_window_average(x, n_neighbors) computes the average of that value's neighbors, where neighbors includes the value itself.
moving_window_average should return a list of averaged values that is the same length as the original list.
If there are not enough neighbors (for cases near the edge), substitute the original value as many times as there are missing neighbors.
Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1.

2. Compute and store R=1000 random values from 0-1 as x.
moving_window_average(x, n_neighbors) is pre-loaded into memory from 3a. Compute the moving window average for x for values of n_neighbors ranging from 1 to 9 inclusive.
Store x as well as each of these averages as consecutive lists in a list called Y.

3. moving_window_average(x, n_neighbors=2) and Y are already loaded into memory. For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
Print your answer. As the window width increases, does the range of each list increase or decrease? Why do you think that is?

The range decreases, because the average smooths a larger number of neighbors. Because the numbers in the original list are just random, we expect the average of many of them to be roughly 1 / 2, and more averaging means more smoothness in this value. 