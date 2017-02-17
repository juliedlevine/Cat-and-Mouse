import pygame
import random
import time
from time import gmtime, strftime

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Cat(object):
    def __init__(self):
        self.height = 96
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
        # DISABLE LEFT AND RIGHT FOR NOW
        # elif event.key == KEY_LEFT:
        #     self.speed_x = -5
        # elif event.key == KEY_RIGHT:
        #     self.speed_x = 5

    def keyup(self, event):
        if event.key == KEY_DOWN:
            self.speed_y = 0
        elif event.key == KEY_UP:
            self.speed_y = 0
        # DISABLE LEFT AND RIGHT FOR NOW
        # elif event.key == KEY_LEFT:
        #     self.speed_x = 0
        # elif event.key == KEY_RIGHT:
        #     self.speed_x = 0

    def update(self, width, height):
        if self.y < 0: # Check top
            self.y = 0
        if self.y + self.height > height: # Check bottom
            self.y = height - self.height
        else:
            self.y += self.speed_y

        if self.x < 0: # Check left
            self.x = 0
        elif self.x + self.width > width: # Check right
            self.x = width - self.width
        else:
            self.x += self.speed_x

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Mouse(object):
    def __init__(self):
        self.height = 64
        self.width = 64
        self.image = pygame.image.load("images/mouse.png").convert_alpha()
        self.x = -64
        self.y = random.randint(64, 500)
        self.speed_x = random.randint(30, 60)
        self.speed_y = 0

    def update(self):
        self.y += self.speed_y
        self.x += self.speed_x

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

def main():

    def print_instructions():
        font = pygame.font.Font(None, 20)
        text1 = font.render("CAT AND MOUSE", True, (255, 255, 255))
        text2 = font.render("Catch as many mice as you can!", True, (255, 255, 255))
        text3 = font.render("For every 5 mice you catch", True, (255, 255, 255))
        text4 = font.render("you'll get a milk carton.", True, (255, 255, 255))
        text5 = font.render("Get 4 milk cartons and you win!", True, (255, 255, 255))
        text6 = font.render("Ready to play? (y / n)", True, (255, 255, 255))
        blurb = pygame.image.load("images/chat.png")
        screen.blit(blurb, (250, 150))
        screen.blit(text1, (320, 200))
        screen.blit(text2, (280, 220))
        screen.blit(text3, (280, 240))
        screen.blit(text4, (315, 260))
        screen.blit(text5, (280, 280))
        screen.blit(text6, (315, 300))

    def print_winner():
        font = pygame.font.Font(None, 20)
        text1 = font.render("CONGRATS YOU WON", True, (255, 255, 255))
        text2 = font.render("Nice work.", True, (255, 255, 255))
        text3 = font.render("Now kitty gets to drink all", True, (255, 255, 255))
        text4 = font.render("this milk as his award.", True, (255, 255, 255))
        text5 = font.render("MEEEEEEEOOOOW", True, (255, 255, 255))
        text6 = font.render("Want to play again? (y / n)", True, (255, 255, 255))
        blurb = pygame.image.load("images/chat.png")
        screen.blit(blurb, (250, 150))
        screen.blit(text1, (320, 200))
        screen.blit(text2, (280, 220))
        screen.blit(text3, (280, 240))
        screen.blit(text4, (280, 260))
        screen.blit(text5, (280, 280))
        screen.blit(text6, (305, 300))

    def collision_detection():
        if (cat.x + 96 < mouse.x) or (mouse.x + 64 < cat.x) or (cat.y + 64 < mouse.y) or (mouse.y + 64 < cat.y):
            return True
        else:
            return False

    width = 799
    height = 568

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Cat and Mouse')
    clock = pygame.time.Clock()

    # Game initialization

    cat = Cat()
    mouse = Mouse()
    caught_mice = set()
    counter = 0
    stop_game = False
    start_game = False

    # Show instructions at beginning of game
    show_instructions = True

    # Hide winner blurb at beginning of game
    show_winner = False

    while not stop_game:

        #Counter for sending out a new mouse
        counter += 1
        if counter >= 30:
            mouse = Mouse()
            counter = 0

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                cat.keydown(event)
            if event.type == pygame.KEYUP:
                cat.keyup(event)
            if event.type == pygame.KEYDOWN:
                if event.key == 121:
                    # If you want to start playing, Hide blurbs
                    show_instructions = False
                    show_winner = False
                    # Start game
                    start_game = True
                    caught_mice = set()
                # Quit game if player hits "y"
                if event.key == 110:
                    return
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Start game when player hits "y"
        if start_game == True:
            cat.update(width, height)
            mouse.update()

        # Draw background
        background = pygame.image.load("images/background.jpg").convert_alpha()
        screen.blit(background, (0, 0))

        # Draw milk cartons
        milk = pygame.image.load("images/milk.png").convert_alpha()
        if len(caught_mice) >= 5:
            screen.blit(milk, (200, 510))
        if len(caught_mice) >= 10:
            screen.blit(milk, (240, 510))
        if len(caught_mice) >= 15:
            screen.blit(milk, (280, 510))
        if len(caught_mice) == 20:
            screen.blit(milk, (320, 510))
            start_game = False
            show_winner = True

        # Game timer
        seconds_counter = strftime("00:%S", gmtime())
        font = pygame.font.Font(None, 50)
        time_text = font.render(seconds_counter, True, (255, 255,255))
        screen.blit(time_text, (510, 520))

        ##### GAME DISPLAY ######
        # Show and hide instructions blurb
        if show_instructions == True:
            print_instructions()

        # Show and hide winner blurb
        if show_winner == True:
            print_winner()

        cat.render(screen)
        # Check for caught mice
        if collision_detection():
            mouse.render(screen)
        else:
            caught_mice.add(mouse)


        pygame.display.update()
        clock.tick(10)


    pygame.quit()


if __name__ == '__main__':
    main()
