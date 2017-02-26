#Cat and Mouse
---
##[Live Demo](http://juliemdyer.com/video.html)

##What It Is
Cat and Mouse is an interactive single player game. In order to play the user must have Python and Pygame installed on their computer.

##Languages used
    * Python
    * Pygame module



#Game Walkthrough
---
##How To Play
Mice run across the screen from left to right, fast and frequent.
Player moves cat up and down at the right of the screen. If cat collides with mouse it is "caught"
For each mouse the player catches they gain a milk carton.

##Game Initialization
Instructions pop up telling the player how to play and the object of the game. Player can start game (hit key 'y'), or exit and close the game (hit key 'n').
60 second timer and music starts.
Player now has ability to move cat up and down using the arrow keys and start catching mice.
![alt text](https://github.com/juliemdyer/Cat-and-Mouse/blob/master/screenshots/start_screen.png)

##Level 1
60 second countdown timer starts. If a mouse is caught a sound effect plays and milk carton appears at the bottom of the screen.
![alt text](https://github.com/juliemdyer/Cat-and-Mouse/blob/master/screenshots/Level_1.png)

##Level 1 Passed
If player collects 10 milk cartons, the player advances to Level 2 and the below screen appears. Cat automatically repositions to the bottom right corner of the screen. Player can choose to continue to Level 2 (hit key 'y') or quit game (hit key 'n').
![alt text](https://github.com/juliemdyer/Cat-and-Mouse/blob/master/screenshots/level2_screen.png)

##Level 2
60 second countdown timer starts. For level 2 a vacuum cleaner 'enemy' is introduced. The player must avoid the vacuum cleaner or they lose all their milk points and must start over.
![alt text](https://github.com/juliemdyer/Cat-and-Mouse/blob/master/screenshots/Level_2.png)

##Loser
If time runs out, and player doesn't have all 10 milk cartons, player loses. This can happen on either Level 1 or Level 2. Cat automatically repositions to the bottom right corner of the screen.
Text blurb pops up with a message and asks the player if they want to play again.
![alt text](https://github.com/juliemdyer/Cat-and-Mouse/blob/master/screenshots/loser_screen.png)

##Winner
If the player catches 10 mice on Level 2 the win screen appears. Cat automatically repositions to the bottom right corner of the screen. Player can choose to start game over, beginning at Level 1 again (hit key 'y') or quit game (hit key 'n').
![alt text](https://github.com/juliemdyer/Cat-and-Mouse/blob/master/screenshots/winner_screen.png)
