#Cat and Mouse
---
##[Live Demo](http://juliemdyer.com/video.html)
Link shows a screen video of me playing the game.

##What It Is
Cat and Mouse is an interactive single player game. In order to play the user must have Python and Pygame installed on their computer.
Mice run across the screen from left to right, fast and frequent. Player moves cat up and down at the right of the screen. If cat collides with mouse it is "caught". For each mouse the player catches they gain a milk carton.

##Languages used
* Python
* Pygame module

##Challenges
###Mouse collision sound
I wanted a single sound effect to play when a mouse collided with the cat. What ended up happening was a bunch of sounds would piggyback on each other and play quickly right after each other. I added some print statements to the code where the collisions was happening and realized the computer was registering multiple collisions instead of just one.
Solution: The solution was to make a copy of the caught_mice set. This set was keeping track of the number of mice that had been caught at any given time. I compared the length of the caught_mice set to the copy. If the original set is larger than the copy then that means a mouse has been caught and we want to play a sound. Then I re-set the copy to the original set to be ready to check again. This fixed the multiple sound effect problem.

```python
# Check for caught mice / show uncaught mice
if cat.collision_detection(cat, mouse, height, width):
    mouse.render(screen)
else:
    # sound.play()
    caught_mice.add(mouse)

if len(caught_mice) > len(caught_mice_copy):
    mouse.play_sound()
    caught_mice_copy = set(caught_mice)
```

###Adding a second level
I had trouble finding a way to keep track of what level the player was on. My initial idea was to just add a Level counter that initialized at 0, and would add 1 during the win scenario. But when I printed this out to the console it added 1 a bunch of times so the counter continued to increase.
Solution: I had to add the level counter in the Event Handling section. the level is increased when a player hits the 'y' key after each level. I don't think this is a great solution because if the y key gets hit during the game for any reason the counter will be off, and the levels wont work correctly. So I'd like to re-visit this and come up with a better solution.

```python
# If player hits "y"
if event.key == 121:
    # Hide blurbs
    show_instructions = False
    show_winner = False
    show_loser = False
    level += 1

    # Start game and timer, reset mice set
    bg_music.play(-1)
    start_game = True
    show_timer = True
    caught_mice = set()
```

##More Code Snippets
Cat Object. keydown and keyup functions create smooth movement for the cat. The update function checks the bounds of the cat and keeps it from being able to move outside the screen.

```python
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.height = 78
        self.width = 96
        self.image = pygame.image.load("images/cat.png").convert_alpha()
        self.x = 700
        self.y = 472
        self.speed_x = 0
        self.speed_y = 0

    def keydown(self, event):
        if event.key == KEY_DOWN:
            self.speed_y = 10
        elif event.key == KEY_UP:
            self.speed_y = -10

    def keyup(self, event):
        if event.key == KEY_DOWN:
            self.speed_y = 0
        elif event.key == KEY_UP:
            self.speed_y = 0

    def update(self, width, height):
        # Check top and bottom (keep cat in bounds)
        if self.y < 0:
            self.y = 0
        if self.y + self.height > height:
            self.y = height - self.height
        else:
            self.y += self.speed_y
```

Game timer. If countdown gets to 0 Loser scenario runs and resets animal positions, timer and shows the loser blurb.

```python
# Draw timer
if show_timer == True:
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    seconds = total_seconds % 61
    output_string = ": %s" % seconds
    font = pygame.font.Font(None, 50)
    time_text = font.render(output_string, True, (255, 255, 255))
    timer_pic = pygame.image.load("images/stopwatch.png").convert_alpha()
    screen.blit(timer_pic, [505, 520])
    screen.blit(time_text, [540, 520])
    frame_count += 1
    if seconds == 0:
        # Loser scenario
        show_timer = False
        start_game = False
        show_loser = True
        bg_music.stop()
        # reset animal positions and timer
        cat.x = 700
        cat.y = 472
        mouse.x = -64
        vacuum.x = -128
        frame_count = 0
```

#Game Walkthrough
---

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
![alt text](https://github.com/juliemdyer/Cat-and-Mouse/blob/master/screenshots/winner_screen.png).
