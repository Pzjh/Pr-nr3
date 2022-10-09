# **Battleships in Python**

This version of battleships is played on an 8x8 board where the player has to find the ships
within the given amount of turns.
The game runs in Code Institute's Heroku terminal.  

The game can be found here [Link to the Game](https://project3battship.herokuapp.com/).  

![The Game](/images/Project3S.png "Battleships Game")  

## **How to play**

The player will be asked to pick a row and a column that they wish to shoot at.  
The program will then tell the player if they hit one of the ships or if they missed.  
Hits will generate a **X** on the board while misses will show up as a **O**.  
the player will then continue to guess until they have run out of turns or they have sunk all  
of the ships.  

## **Features** 

---

- Random ship placement
- Input validation
  - Will not acceptcoordinates that are not on the board
  - Will not accept the same answer
  - Only accepts single digit numbers and letters

### **Coming Features**

- Different game modes
- Ships bigger than 1 slot
- Let player position their ships
- Option to face the computer
- Highscores

## **Testing**

---

I haev been testing the project on my own  
by doing manual tests in the terminal.
The PEP8 test site seems to not exist anymore and i couldn't  
find a replacement so i have not checked the code in a third party  
tool.

### **Bugs**

- There is a bug where the game will crash if the players  
guess is blank and sometimes when the input is a number and a letter.
- Sometimes when you open the terminal things will move slightly or  
not show up at all but reopening the terminal again will usually move things back.  

## **Deployment**

---

The project was deployed using Heroku and Code Institute's mock terminal.
It was done using the following steps.
- Fork or Clone this repository
- Create a new Heroku app
- Set the buildbacks to **Python** and **NodeJS** in that order
- Link the Heroku app to the repository
- Click on **Deploy**

## **Credits**

---

- Code Institute for the deployment terminal