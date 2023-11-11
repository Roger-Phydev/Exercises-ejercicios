# Information list

## 01. Fizzbuzz:
### Write a program that show in console (via print): numbers from 1 to 100 (including both of them and with a line break every print), and replacing:
* Multiples of 3 for "fizz".
* Multiples of 5 for "buzz".
* Multiples of 3 AND of 5 at the same time for "fizzbuzz".

## 02. Anagrams:
### Write a function that receives two strings and returns a Boolean (true or false) depending whether they are anagrams or aren't.
* An Anagram consist of forming a word re-ordering ALL of the letters in another original word.
* It is NOT necesary to check if both words have sense.
* Two words that are the same are NOT Anagrams.

## 03. Fibonacci
### Write a program that prints the first 50 numbers of the Fibonacci sequence starting from 0. The Fibonacci sequence is composed of a number sequence in which the next term is the sum of the two previous terms: 0, 1, 1, 2, 3, 5, 8, 13...

## 04. Primes
### Write a program that checks whether a number is a prime or not. Then, print the primes numbers between 1 and 100.

## 05. Poligon's area
### Make a function (and just one function) that is able to calculate and return the area of a poligon:
* The function will receive a parameter that represent a kind of poligon.
* The poligons availables will be Triangle, Square and Rectangule.
* Print an example for every kind of poligon.

## 06. Reversing strings
### Make a program that can reverse the order in a string. Don't use Python functions that can solve the problem immediately. Example: if we introduce "Hello world" it will return "dlrow olleH"

## 07. Counting words
### Make a program that counts how many times is repeated every word in a phrase, and show the count.
* Punctuation marks does not contribute to the count.
* A word is the same even if it is written in lower or upper case.
* You cannot use Python's functions that can solve the problem automaticately
#### Note: I have two ways to solve this problem, in 7_1 I use regex, take a look :)

## 08. Decimal to binary
### Make a program which is able to transform a decimal number into a binary number, don't use Python's functions that can solve the problem in a direct way.

## 09. Morse Code
### Make a program that can transform natural text into Morse code, and viceversa.
* It must detect automatically what kind of text is receiving and perform the conversion
* Morse code uses a line "—" and point "." to form letters and symbols, uses space " " to split letters and symbols, and two spaces to split words "  ".
* The alphabet you must use is shown in https://en.wikipedia.org/wiki/Morse_code.

## 10. Balanced expressions
### Make a program that checks if parenthesis, braces and brakets in an expression are balanced
* Balanced means that these delimiters are opened and closed in the right way (order).
* Parenthesis, braces and brakets have the same priority, so there isn't any most important delimeter
* Balanced expression: { [ a * ( c + d ) ] - 5 }
* Unbalanced expression: { a * ( c + d ) ] - 5 }

## 11. Deleting characters
### Make a function that receives two strings as parameters (str1,str2) and prints other two strings as outputs (out1,out2)
* out1 will contain all characters that are present in str1 but not in str2.
* out2 will contain all characters that are present in str2 but not in str1.

## 12. Palindromes
### Write a function which receives a text and returns a boolean (True or False) depending whether the text is or not a palindrome.
* A palindrome is a word that reads exactly the same if it reads from right to left or left to right.
* Spaces and punctuation symbols mustn't take into count.
* Example: race car

## 13. Recursive factorial
### Write a function that calculates and returns the factorial of a number but in a recursive way (the function must apply itself in some part of its code).

## 14. Armstrong's numbers
### Write a function which calculate if a given number is an Armstrong's number. If you don't know what an Armstrong's number is, you must find some information about it.

## 15. How many days?
### Make a function which calculates and returns how many days are there between two strings that represent dates.
* An string that represents a date has the follow format: "dd/mm/yyyy".
* The function will receive two strings and return an int.
* The difference must be absolute (it doesn't matter the order of the two strings).
* If one of the strings doesn't represent a date, the program will run an except.

## 16. Upper cases
### Make a function that receives an string and replace the first letter of every word in the string with its upper case equivalent. You mustn't use Python's functions that can solve the problem directely.

## 17. Obstacle race
### Make a function that evaluates whether an athelet has done correctely an obstacle race. The function will receive two parameters:
* A list which can only contain one of the strings "run", "jump" and represents the athelet.
* An string that represents the racetrack and it only can cointain "_" (ground) o "|" (fence)
### The function will print what's the result of the race:
* If the athelet does "run" with "_" (ground) or does "jump" with "|" (fence) it'll be correct and nothing will happen to the symbol in the racetrack
* If the athelet does "jump" with "_" (ground), the actual symbol of the racetrack will be replaced with  "x".
* If the athelet does "jump" with "|" (fence), the actual symbol of the racetrack will be replaced with "/".
* The function will return a boolean that represents if the race has been completed or not. To perform this, the athelet must have done the right action at every segment of the racetrack.

## 18. Tic,tac,toe
### Make a function that analyses a 3x3 matrix made with "X" y "O" and returns:
* "X" if the "X" has won
* "O" if the "O" has won
* "Tie" if a tie has happened
* "Null" if the proportion of "X" and "O" is not correct, or the dimensions of the matrix are not correct or the two players has won.
#### Note: The matrix might not be completely composed of "X" and "O". It might include "" to represent a void segment.

## 19. Time conversor
### Make a function that receives days, hours, minutes and seconds (as integers) and returns the equivalent in milliseconds.

## 20. Stopping time
### Make a function that sums two numbers and returns its result after a few seconds.
* It'll receive two numbers as parameters (which will be sumed) and a third number that will be the quantity of seconds that the result will be delayed.

## 21. TXT calculator
### The program will be able to read a txt file that cointains calculator inputs, and returns the result as real calculator would do.
* Each line of the file will have a number or an operation represented by a symbol(it will toggle between these two options).
* The numbers can be integers or decimals.
* It supports sum "+", substraction "-", multiplication "*" and división "/".
* The result is show when the program ends of reading the file (just if the format of the file is correct)
* If the file doesn't have the right format, the program will inform that the operations could not have solve.

## 22. Sets
### Make a function that receives two lists and boolean and returns a list.
* If the boolean is True, it'll find and return the common elements between the two lists.
* If the boolean is False, it'll find and return the not common elements between the two lists.
* You mustn't use Python's operations that can solve directely the problem.

## 23. Maximum common divisor and minimum common multiple
### Make two functions, one of these calculates the maximum common divisor (MCD) and the other calculates the minimum common multiple of two integer numbers.
* Again, you can't use Python's functions that can solve the problem directely.

## 24. Iteration master
### How many ways to print the numbers from 1 to 100 do you know? Make a code for every way

## 25. Rock,paper,scissors
### Make a program that calculates who wins the most games of rock,paper,scissors.
* The result can be: "Player 1", "Player 2" and "Tie"
* The function receives a list which contains pairs that represent games.
* Every pair has combinations of "R"(rock), "P" (paper) or "S" (scissors).
* Example. Input: [("R","S"), ("S","R"), ("P","S")]. Result: "Player 2".

## 26. Triangle and square
### Make a program that draws an square or a triangle using "*".
* The size of a side and the name of the figure (square or triangle) will be the function's parameters
* EXTRA: ¿Are you able to draw another kind of figure?

## 27. Orthogonal vectors
### Make a program that determines whether two vectors are orthogonal or not.
* The two list (vectors) must have the same length 
* Example: [1, -2] , [-2, 1]

## 28. Vending machine
### Simulate a vending machine creating a function that receives money(list of coins) and a number that represents the product selection.
* The program will return the product's name and a list that represents the change(using the minimum quantity of coins)
* If the money is not enough or the product's number doesn't exist, the program will show a message that explains the error, and will return all the coins.
* If there's no change, the list of change will be void (corresponding to []).
* It only supports coins of 5, 10, 50, 100 and 200.
* Be careful, the value of every coin received must be valid.

## 29. Ordering a list
### Make a function that orders and returns a number matrix. The function will receive a list (for example: [2, 4, 6, 8, 9]) and an additional parameter "Asc" or "Desc" to indicate whether the list must order in ascent or descent order. You can't use functions that can solve the problem easily.

## 30. Words frame
### Make a function that receives a text and shows Crea una función que reciba un texto y muestre cada palabra en una línea, formando un marco rectangular de asteriscos. ¿Qué te parece el reto? Se vería así:
##   **********
##   * ¿Qué   *
##   * te     *
##   * parece *
##   * el     *
##   * reto?  *
##   **********

## 31. Leap years
### Make a function that prints the 30 leap years after a given year. Use as less lines as possible to solve the problem.

## 32. The second most
### Given a list of numbers, find the second greatest.

## 33. Sexagenary chinese cycle
### Make a function that receives a year and returns the element and animal for the year according to the sexagenary chinese cycle:
* Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
* The cycle is composed by element (wood, fire, ground, metal and water) and animal (rat, ox, tiger, rabbit, dragon, snake, horse, sheep, monkey, rooster, dog and pig)
* Each element is repeated for two consecutive years, then it changes to the next one.
* Each animal changes to the next one every year.
* The las cycle began in 1984 (Wooden Rat).

## 34. Lost numbers
### Given a list of integers sorted and without repeated elements, make a function that calculates and returns all the numbers that are not in the list between the maximum and minumum. The function shows a notice if the list's format is not correct.

## 35. Pokemon battle
### Make a program that calculates the damage of an attack during a Pokemon battle.
* The formula will be given by the expression: daño = 50 * (attack / defense) * efectivity
* Efectivity: x2 (super effective), x1 (neutral), x0.5 (not very effective)
* There are just 4 types of pokemon: water, fire, plant and electric (find their effectivity up).
### The program receives the next parameters:
* Type of the attacker pokemon.
* Type of the defenser pokemon.
* Attack: between 1 and 100.
* Defense: between 1 and 100.

## 36. Rings of power
### ¡The middle earth is at war! Loyal to Sauron races will fight against benevolent ones whom don't want the evil take over their lands. Each race has a value between 1 and 5:
* Benevolent races: Harfoots (1), good variags (2), Dwarves (3), Númenor (4), Elves (5)
* Evil races: bad variags (2), Orcs (2), Goblins (2), wargs (3), Trolls (5)
### Make a program that calculates the result of a battle between two kind of armies:
* The result can be "Good wins", "Evil wins" or "Tie" depending on the sum of the values for every army.
* Each army can be composed by a different number for each race.
* You can change the values for every race in this problem.
* Ex: 1 Harfoot loses against 1 Orc; 2 Harfoots tie agains 1 Orc; 3 Harfoots win agains 1 Orc.

## 37. Zelda's launch dates
### Make a program that calculates how many years and days are there between two zelda games of your choice. You must find every zelda title and its launch date (if you don't find a date for some title, just use the month or even come up with a date).

## 38. Binary to decimal
### Make a program that turns a binary number into a decimal number without help of functions that can solve the problem immediately.

## 39. Quick sort: A brief study
### Implement one of the most famous algorithms: "Quick Sort", created by C.A.R. Hoare. You must study deeply this algorithm not just copy-paste, make sure you understand the inner working of it.

## 40. Pascal's triangle
### Make a function that can draw the pascal's triangle just given to it the side size.

## 41. Ohm's Law
### Make a function that calculates the value of the lost parameter in the Ohm's law.
* It receives just two of three parameters (V, R, I), and returns the value of the third parameter (rounded to 2 decimals).
* If the parameters are incorrect or insuficient, the functions will return the string "Invalid values".

## 42. Temperature conversor
### Make a function that transforms Celsius degrees into Fahrenheit degrees and vice versa. The parameter must include a symbol "°" and a unity of measurement ("C" or "F"). Else it'll return an error.

## 43. Trick or treat
### Make a program in which we can indicate whether we want to do a "trick" or a "treat", and a list of people with the next features:
* Child's name
* Age
* Heigh (in centimeters)
### If people indicate trick, the program will return aleatory scaries according to the next criteries:
* A scary per two letters in the name per child.
* Two scares per every even age.
* Three scares per 100cm in the total height (sum of all heights).
* Scares: 🎃 👻 💀 🕷 🕸 🦇
### If people indicate treat, the program will return aleatory candies according to the next criteries:
* A candy per every name's letter
* A candy per every three years until a max of ten years per person
* Two candies per every 50cm in the height until a max of 150cm.
* Candies: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩

## 44. Boomerangs
### Make a function that returns the total number of boomerangs in a list of integer numbers and prints each of them. A boomerang is a sequence composed of three consecutive numbers, the first and third numbers are the same, and the second one is different to the others. Example: [2, 1, 2].
* In the list [2, 1, 2, 3, 3, 4, 2, 4] there are 2 boomerangs ([2, 1, 2] and [4, 2, 4]).

## 45. Water deposit
### Given a list of integer positive numbers, where each represents unities of blocks apiled, we must calculate how many unities of water will be stacked between them.
### Example: For the list [4, 0, 3, 6, 1, 3].
        ⏹
        ⏹
⏹💧💧⏹
⏹💧⏹⏹💧⏹
⏹💧⏹⏹💧⏹
⏹💧⏹⏹⏹⏹

### ⏹︎ represents a block and 💧 represents water, so 7 unities of water will be stocked. 

## 46. Where's the robot
### Calculate where the robot will be (its final coordinates). The robot is on a grid represented by the axes "x" and "y".
* The robot begins at (0, 0).
* To indicate it to move, we send it a list of integer numbers which indicate the sequence of steps to do, and it counts as an instruction.
* For example: [10, 5, -2] indicates that first it will do 10 steps, stop, then five steps, stop, and finally two steps. The final position will be (x: -5, y: 12)
* If the number of steps is negative, the robot will move in the opposite direction that it is ponting at.
* It takes the first steps on the "y" axis. We assume that it's ponting to the positive side of the "y" axis.
* The robot has a programming error: Every time it receives an instruction and ends it, it turns 90 degrees in opposite direction to the clockwise.

## 47. Most common vowel
### Make a function that receives a text and returns the vowel that repeats the most. If there is not any vowels, it'll returns a void list.

## 48. aDEVient calendar
### This is about an activity of a community which lasts 24 days and there is a gift a day to software, science and technology, and begins on December first.
### Make a functions that receives an object "date" (from the library datetime.date) and returns the next:
* If the date matches with the aDEViento calendar 2022: It'll return the gift corresponding to that day and what's the remaining time to enter the raffle of the day.
* If the date is before the beginning: It'll indicate how long until it stars
* If the date is after the beginning: It'll indicate how long has passed since the end.
#### Notes:
* We take into account that every day in the calendar begins at midnight 00:00:00 and ends at 23:59:59.
* We must work with date that includes year, month, day, hours, minutes and seconds.

## 49. Handle detector
### Make a function that is able to detect and return all the handles of a text just using regex. You must create a regex per case:
* User handle : begins with "@"
* Hashtag handle : begins with "#"
* Web Handle : begins with "www.", "http://", "https://" and ends with a domain (.com, .us, .uk...)

## 50. Encryption
### Make a function which is able to encrypt and decrypt text using the Karaca's encryption algorithm(You must find information about it).