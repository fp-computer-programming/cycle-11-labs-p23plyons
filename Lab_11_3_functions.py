# Author: PCL 2/1/23

#1
#creating a function which finds the lowest number of any given array
def minimum(arr):
    arr.sort()
    return arr[0]

#2
#creating a function which finds the highest number of any given array
def maximum(arr):
    arr.sort()
    return arr[len(arr)-1]

#3
#Creating a function which finds the greatest possible difference
#from the highest and lowest numbers found in the array by the previous two functions
def largest_possible_dif(arr):
    highest = maximum(arr)
    lowest = minimum(arr)
    return(highest-lowest)

#4
#creating a function that will find the sum of two numbers - adds the two variables, sets them equal to a new variable, and returns them
def find_sum():
    num1 = input("Please input the first number you would like to add: ")
    num2 = input("Please input the second number you would like to add: ")
    num_sum = int(num1) + int(num2)
    return(num_sum)

#5
#creating a function to count how many letter "a"'s are in a string
def count_a():
    word = input("Please input the string that you would like to find out the number of letter 'a's: ")
    #lowercasing whatever string is input
    lowered_word = word.lower()
    #turning the inputted string into a list of individual characters
    lowered_word[::-1]
    #defining a count for the while loop and the number of a's detected
    count = 0
    num_a = 0
    while (count < len(lowered_word)):
        if (lowered_word[count] == "a"):
            num_a += 1
        count += 1
    return (num_a)

#6
#creating a function which finds the factorial of any number inputted by the user
def factorial(num):
    #defining a count for the while loop so that it goes over each number and multiplies them
    count = 0
    #setting a product where all the numbers will be multiplied and saved to
    product = 1
    while (count < num):
        count += 1
        product *= count
    return(product)

#7
def better_is_palindrome(word):
    palindrome = "".join(word[::-1])
    return (palindrome.lower() == word.lower())

#8
#creating a function which prints the sum of all numbers from zero to, and including the input
def sum_to(n):
    #where the sum will be counted
    total = 0
    #counter for the while loop
    count = 0
    while (count < int(n)):
        count += 1
        total += count
    return (total)

#9
def indexed_names (names):
    for index, vars in enumerate(names):
        #breaking each name into a list so that charcters can be added to the beginning of the strings
        namex = [*vars] 
        #recombining the lists into a string
        namex.insert(0, str(index)+": ")
        names[index] = "".join(namex)
    return (names)

#10
def double_stuff (stuff):
    for index, var in enumerate(stuff):
            stuff[index] = var*2
    return(stuff)
