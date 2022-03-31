# Roulette-with-Python

Developing this text game was really fun for me because of how much I personally enjoy the game of roulette and how challenging it was to design at first. It was also a great opportunity to grow my knowledge of python and implement what I've learned into this project. 

# Strategy
My starting point for the project was to develop the game with the methods I was most comfortable with, since it's my first personal project. The program consists of defined functions for each bet and empty lists to store inputted data from the player. The idea is that the program asks the player one by one if they would like to bet in each of the 11 bets the game has to offer. After placing how much money the player would like to wager, the input value is then compared to each bets unique function. Each defined function has a dictionary filled with every possible key-value pair that covers the outcome of each unique bet. The tricky part was covering numbers that had more than one method of winning money for the player. My solution to that was to make more defined fuctions with dictionarys for bets that involved multiple numbers. 

# Room for Improvement 
Although the program runs fine, there are a good amount of areas to improve on. 
To start, the project lacks OOP (Object Oriented Programming). When I revisit this project I am looking to rework the whole 'defined function' system so the program has more space complexity. The code also has a lot of repition for how each 'while' function is structured; OOP will help elimnate all code that is continously repeated. 
Another area for improvement is utilizing NumPy to gain more familiarity with the library while achieving a faster running program. NumPy will help the code take up less memory because of its memory management features. NumPy will also provide a solution for how the data is inputted for certain bets. The bets that have multiple numbers involved for its input require that you place the numbers from least to greatest and have them seperated by commas. NumPy will help get rid of that restriction because of the ascending and descending feature it has to offer for arrays (lists). NumPy will help organize the inputted list from the player in a format that will be recognized by the game in any order the player chooses. 

# Additional Features for the Future
I would love to implement the PyGame library for this project and make the game more visually appealing. Currently the game has no visual and in order to play the game more strategically you would have to look at an image of a roulette table off another source. Pygame has the tools to develop a board for the game that will allow the player to place there bets by clicking buttons instead of typing everything out. 
