import pygame
import random
import time

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Animal(object):
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collision_detection(self, cat, mouse, height, width):
        if (cat.x + cat.width < mouse.x) or (mouse.x + mouse.width < cat.x) or (cat.y + cat.height < mouse.y) or (mouse.y + mouse.height < cat.y):
            return True
        else:
            return False

    def vacuum_collision(self, cat, vacuum, height, width):
        if (cat.x + cat.width < vacuum.x) or (vacuum.x + vacuum.width < cat.x) or (cat.y + cat.height < vacuum.y) or (vacuum.y + vacuum.height < cat.y):
            return True
        else:
            return False

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

class Vacuum(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.height = 128
        self.width = 128
        self.image = pygame.image.load("images/vacuum.png").convert_alpha()
        self.x = -128
        self.y = random.randint(128, 440)
        self.speed_x = 50
        self.speed_y = 0

    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x

class Mouse(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.height = 27
        self.width = 64
        self.image = pygame.image.load("images/mouse.png").convert_alpha()
        self.x = -64
        self.y = 500 #random.randint(64, 500)
        self.speed_x = random.randint(30, 50)
        self.speed_y = 0

    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x


def main():

    # --------- GAME INITIALIZATION --------- #

    # Background size
    width = 799
    height = 568

    # Initialize pygame
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sounds/boing2.wav')
    bg_music = pygame.mixer.Sound('sounds/bg_music.wav')
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Cat and Mouse')
    clock = pygame.time.Clock()

    # create objects and set game variables
    cat = Cat()
    mouse = Mouse()
    vacuum = Vacuum()
    caught_mice = set()
    mouse_counter = 0
    vacuum_counter = 0
    level = 0
    stop_game = False
    start_game = False

    # set countdown timer variables
    frame_count = 0
    frame_rate = 10
    start_time = 60

    # Show instructions at beginning of game
    show_instructions = True

    # Hide winner / loser blurbs and timer at beginning of game
    show_winner = False
    show_loser = False
    show_timer = False



    # Game loop
    while not stop_game:

        # --------- PRINT FUNCTIONS --------- #

        def print_instructions():
            font = pygame.font.Font(None, 30)
            font2 = pygame.font.Font(None, 25)
            text1 = font.render("CAT AND MOUSE", True, (255, 255, 255))
            text2 = font2.render("60 seconds on the clock!", True, (255, 255, 255))
            text3 = font2.render("Use the up and down keys to", True, (255, 255, 255))
            text4 = font2.render("move your cat up and down.", True, (255, 255, 255))
            text5 = font2.render("For every mouse you catch", True, (255, 255, 255))
            text6 = font2.render("you'll get a milk carton.", True, (255, 255, 255))
            text7 = font2.render("Get 10 milk cartons and you win!", True, (255, 255, 255))
            text8 = font2.render("Ready to play? (y / n)", True, (255, 255, 255))
            blurb = pygame.image.load("images/chat.png")
            screen.blit(blurb, (400, 90))
            screen.blit(text1, (500, 140))
            screen.blit(text2, (460, 190))
            screen.blit(text3, (460, 210))
            screen.blit(text4, (460, 230))
            screen.blit(text5, (460, 250))
            screen.blit(text6, (460, 270))
            screen.blit(text7, (460, 290))
            screen.blit(text8, (460, 310))

        def print_winner():
            font = pygame.font.Font(None, 30)
            font2 = pygame.font.Font(None, 25)
            text1 = font.render("CONGRATS YOU WON!", True, (255, 255, 255))
            text2 = font2.render("Very nice work.", True, (255, 255, 255))
            text3 = font2.render("Kitty now gets to drink all", True, (255, 255, 255))
            text4 = font2.render("this milk as his reward.", True, (255, 255, 255))
            text5 = font2.render("MEEEEEEOOOOOW", True, (255, 255, 255))
            text6 = font2.render("Do you want to play again? (y / n)", True, (255, 255, 255))
            blurb = pygame.image.load("images/chat.png")
            screen.blit(blurb, (400, 100))
            screen.blit(text1, (500, 150))
            screen.blit(text2, (440, 200))
            screen.blit(text3, (440, 220))
            screen.blit(text4, (440, 240))
            screen.blit(text5, (440, 260))
            screen.blit(text6, (440, 280))

        def print_level2():
            font = pygame.font.Font(None, 30)
            font2 = pygame.font.Font(None, 25)
            text1 = font.render("YOU PASSED LEVEL 1!", True, (255, 255, 255))
            text2 = font2.render("Very nice work.", True, (255, 255, 255))
            text3 = font2.render("For level 2 beware of the vacuum.", True, (255, 255, 255))
            text4 = font2.render("If you get hit by the vacuum you", True, (255, 255, 255))
            text5 = font2.render("lose all your milk!", True, (255, 255, 255))
            text6 = font2.render("Are you ready for level 2? (y / n)", True, (255, 255, 255))
            blurb = pygame.image.load("images/chat.png")
            screen.blit(blurb, (400, 100))
            screen.blit(text1, (500, 150))
            screen.blit(text2, (440, 200))
            screen.blit(text3, (440, 220))
            screen.blit(text4, (440, 240))
            screen.blit(text5, (440, 260))
            screen.blit(text6, (440, 280))

        def print_loser():
            font = pygame.font.Font(None, 30)
            font2 = pygame.font.Font(None, 25)
            text1 = font.render("OH NO TIME RAN OUT!", True, (255, 255, 255))
            text2 = font2.render("Very sad.", True, (255, 255, 255))
            text3 = font2.render("Kitty is so thirsty and", True, (255, 255, 255))
            text4 = font2.render("doesn't have enough milk to drink.", True, (255, 255, 255))
            text5 = font2.render("MEEEEEEOOOOOW", True, (255, 255, 255))
            text6 = font2.render("Do you want to play again? (y / n)", True, (255, 255, 255))
            blurb = pygame.image.load("images/chat.png")
            screen.blit(blurb, (400, 100))
            screen.blit(text1, (500, 150))
            screen.blit(text2, (440, 200))
            screen.blit(text3, (440, 220))
            screen.blit(text4, (440, 240))
            screen.blit(text5, (440, 260))
            screen.blit(text6, (440, 280))

        def print_background():
            background = pygame.image.load("images/background.jpg").convert_alpha()
            screen.blit(background, (0, 0))


        # --------- EVENT HANDLING --------- #

        for event in pygame.event.get():

            # Move cat with up and down arrows
            if event.type == pygame.KEYUP:
                cat.keyup(event)
            if event.type == pygame.KEYDOWN:
                cat.keydown(event)

                # If player hits "y"
                if event.key == 121:
                    # Hide blurbs
                    show_instructions = False
                    show_winner = False
                    show_loser = False
                    level += 1
                    print level

                    # Start game and timer, reset mice set
                    bg_music.play(-1)
                    start_game = True
                    show_timer = True
                    caught_mice = set()

                # Quit game if player hits "n"
                if event.key == 110:
                    return
            # Quit game if player hits red quit button
            if event.type == pygame.QUIT:
                stop_game = True


        # --------- GAME LOGIC --------- #

        # Draw cat, mouse and vacuum when game begins
        if start_game == True:
            cat.update(width, height)
            mouse.update()
            vacuum.update()

        # Counter for sending out a new mouse
        mouse_counter += 1
        if mouse_counter == 35:
            mouse = Mouse()
            mouse_counter = 0

        # Counter for sending out a new vacuum
        if level == 2:
            vacuum_counter += 1
            if vacuum_counter == 80:
                vacuum = Vacuum()
                vacuum_counter = 0

        # Draw background
        print_background()

        # Draw milk cartons
        milk = pygame.image.load("images/milk.png").convert_alpha()
        if len(caught_mice) >= 1:
            screen.blit(milk, (125, 510))
        if len(caught_mice) >= 2:
            screen.blit(milk, (160, 510))
        # if len(caught_mice) >= 3:
        #     screen.blit(milk, (195, 510))
        # if len(caught_mice) >= 4:
        #     screen.blit(milk, (230, 510))
        # if len(caught_mice) >= 5:
        #     screen.blit(milk, (265, 510))
        # if len(caught_mice) >= 6:
        #     screen.blit(milk, (300, 510))
        # if len(caught_mice) >= 7:
        #     screen.blit(milk, (335, 510))
        # if len(caught_mice) >= 8:
        #     screen.blit(milk, (370, 510))
        # if len(caught_mice) >= 9:
        #     screen.blit(milk, (405, 510))
        if len(caught_mice) == 3:
            # Winner scenario
            screen.blit(milk, (440, 510))
            show_timer = False
            start_game = False
            show_winner = True
            bg_music.stop()
            # reset animal positions and timer
            cat.x = 700
            cat.y = 472
            mouse.x = -64
            vacuum.x = -128
            frame_count = 0
            if level == 3:
                level = 1

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


        # --------- GAME DISPLAY --------- #

        # Show and hide instructions blurb
        if show_instructions == True:
            print_instructions()

        if show_winner == True and level == 1:
            print_level2()

        if show_winner == True and level == 2:
            print_winner()

        if show_loser == True:
            print_loser()

        # Show cat
        cat.render(screen)

        # Check for caught mice / show uncaught mice
        if cat.collision_detection(cat, mouse, height, width):
            mouse.render(screen)
        else:
            sound.play()
            caught_mice.add(mouse)

        # If player is on level 2, introduce vacuum
        if level == 2:
            if cat.vacuum_collision(cat, vacuum, height, width):
                vacuum.render(screen)
            else:
                try:
                    caught_mice.pop()
                    sound.play()
                except KeyError:
                    pass

        # Update display
        pygame.display.update()
        clock.tick(frame_rate)



    pygame.quit()

if __name__ == '__main__':
    main()
