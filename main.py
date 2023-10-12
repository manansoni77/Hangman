import pygame
import math
import random

pygame.init()

# constants
title_text = "xx HANGMAN! xx"
play_text = "play"
quit_text = "quit"
WIDTH, HEIGHT = 1000, 500
NO_IMAGES = 7
BUTTON_RADIUS = 20
BUTTON_GAP = 20
BGColor = 'white'
BTNColor = 'black'
TITLEColor = 'black'
# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
OPTIONS_FONT = pygame.font.SysFont('comicsans', 40)


# setup display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game')

# load images
images = []
for i in range(NO_IMAGES):
    image = pygame.image.load('./hangman'+str(i)+'.png')
    images.append(image)

# buttons
BORDER = (WIDTH-(BUTTON_RADIUS*26 + BUTTON_GAP*12))/2
letters = []
startx = BORDER + BUTTON_RADIUS
starty = 400
A = 65
for i in range(26):
    x = startx + ((i % 13) * (BUTTON_GAP + BUTTON_RADIUS*2))
    y = starty + ((i // 13) * (BUTTON_GAP + BUTTON_RADIUS*2))
    letters.append([x, y, chr(A+i), True])

# game variables
hangman_status = 0
guessed = []
words = ["DEVELOPER", "HELLOWORLD", "PYGAME"]
word = random.choice(words)
wrong_guess = 0


# game loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(BGColor)

    # title
    text = TITLE_FONT.render('DEVELOPER HANGMAN', 1, 'black')
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_' + ' '
    text = WORD_FONT.render(display_word, 1, 'black')
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, c, s = letter
        if not s:
            continue
        pygame.draw.circle(win, BTNColor, (x, y), BUTTON_RADIUS, 3)
        text = LETTER_FONT.render(c, 1, 'black')
        win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def displaymessage(message):
    pygame.time.delay(3000)
    win.fill('white')
    text = WORD_FONT.render(message, 1, 'black')
    win.blit(text, (WIDTH/2 - text.get_width() /
             2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, c, s = letter
                if not s:
                    continue
                dist = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                if dist < BUTTON_RADIUS:
                    letter[3] = False
                    if c not in word:
                        hangman_status += 1
                    guessed.append(c)

    draw()

    won = True

    for ltr in word:
        if ltr not in guessed:
            won = False

    if won:
        print('won')
        displaymessage('YOU WON!')
        break

    if hangman_status >= 6:
        print('lost')
        displaymessage('YOU LOST!')
        break


def titleScreen():
    win.fill(BGColor)
    text = TITLE_FONT.render(title_text, 1, TITLEColor)
    x = (WIDTH - text.get_width())/2
    y = (HEIGHT - text.get_height())/2 - 100
    win.blit(text, (x, y))
    text = OPTIONS_FONT.render(play_text, 1, TITLEColor)
    x = ((WIDTH - 200) - text.get_width())/2
    y = 300 - text.get_height()/2
    win.blit(text, (x, y))
    text = OPTIONS_FONT.render(quit_text, 1, TITLEColor)
    x = ((WIDTH + 200) - text.get_width())/2
    y = 300 - text.get_height()/2
    win.blit(text, (x, y))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    titleScreen()


# main()
pygame.quit()
