# Rock-Paper-Scissors
Rock Paper Scissors game created with basic concepts

- Game starts by prompting you for a name using f string

- Then addresses you with name and starts the game from the function call

- A while loop is used to count the number of rounds played using an increment variable "i"

- Text is shown asking for user input and user gets appropriate response for invalid input.
 - This is done with the inputcheck function which has 4 parts:
  - first try for integers
  - second try for floats
  - third try for strings over the length : This is done by creating an error for strings with exactly one length to exit the try and more than one to print the error message
  - fourth try for inputs that are single character but not in array like "h": this is done by calling inmoves() function
     - inmoves() function is used to iterate through the moves array and check if user's input is present. If it is, it gets the index value and stores it and returns 1, else returns 0
    after the check from the inmoves function, if the input is present, we get num = return 1 and 1/ num = 1/1 = 1 and we can exit out of the loop with the False statement after.
    However if it is not present, we get an error at 1 / num because 1 cannot divide 0 and we are pushed to the except to print the error message

- if user selects option to exit, they would be exited with departing message

- an array called moves is used to store the possible options the user can select, and the index of the option selected is stored

- randint is used as computer guess and the integer is used as the index. example if the randint = 1, that means the computer guessed "Scissors" because moves[1] = "Scissors"

- now the win array is a bit more complex to understand.
 - i paired the index of winner and loser on a left to right. example (paper,rock), indices = (0,1). however when i used this, my compare function could not differentiate between (0,1) and (1,0)
 so i add the digits. 01 = 1, (scissors, paper) have indices (1,2) = 12, (paper, rock) have indices (2,0) = 20. It was the easiest way to form that array.

- Now the compare function takes in three inputs, (guess, uii, win). It then puts guesses number infront of users guess to check who won in the win array. 
   If the number is in win, that means the computer's guess won since it was the first digit and vice versa

- After comparison, the score array is updated based on who won and left untouched if a tie happened and the next round starts

- the game runs until one person gets a score of three after which it calls the finish function for an ending message based on who won.
