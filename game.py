# build 2048 in python using pygame!!
import pygame
import random
from pygame import mixer

pygame.init()

# initial set up
WIDTH = 1550
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 45)

# 2048 game color library
colors = {0: (132,132,132),
          2: (160,82,45),
          4: (139,26,26),
          8: (91,91,91),
          16: (154,205,50),
          32: (113,113,198),
          64: (199,21,133),
          128: (255,110,180),
          256: (255,193,37),
          512: (72,209,204),
          1024: (139,119,101),
          2048: (30,30,30),
          'light text': (252, 252, 252),
          'dark text': (252,252,252),
          'other': (0, 0, 0),
          'bg': (0,0,0)}

# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ''
score = 0
file = open('high_score', 'r')
init_high = int(file.readline())
file.close()
high_score = init_high


#to get image on the screen
def image():
    image = pygame.image.load('logo_bg.png')
    imageX = 900
    imageY = 0
    screen.blit(image,(imageX,imageY))


# draw game over and restart text
def draw_over():
    pygame.draw.rect(screen, 'black', [80, 350, 600, 150], 0, 30)
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text1, (80, 350))
    screen.blit(game_over_text2, (80, 400))


# take your turn based on direction
def take_turn(direc, board):
    global score
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        mixer.music.load('Switch Popup.mp3')
                        mixer.music.play()
                        board[i - shift - 1][j] *= 2
                        score += board[i - shift - 1][j]
                        board[i - shift][j] = 0
                        merged[i - shift - 1][j] = True

    elif direc == 'DOWN':
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift += 1
                if shift > 0:
                    board[2 - i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                            and not merged[2 - i + shift][j]:
                        mixer.music.load('Switch Popup.mp3')
                        mixer.music.play()
                        board[3 - i + shift][j] *= 2
                        score += board[3 - i + shift][j]
                        board[2 - i + shift][j] = 0
                        merged[3 - i + shift][j] = True

    elif direc == 'LEFT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][j - shift] = board[i][j]
                    board[i][j] = 0
                if board[i][j - shift] == board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                        and not merged[i][j - shift]:
                    mixer.music.load('Switch Popup.mp3')
                    mixer.music.play()
                    board[i][j - shift - 1] *= 2
                    score += board[i][j - shift - 1]
                    board[i][j - shift] = 0
                    merged[i][j - shift - 1] = True

    elif direc == 'RIGHT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board[i][4 - j + shift] == board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                            and not merged[i][3 - j + shift]:
                        mixer.music.load('Switch Popup.mp3')
                        mixer.music.play()
                        board[i][4 - j + shift] *= 2
                        score += board[i][4 - j + shift]
                        board[i][3 - j + shift] = 0
                        merged[i][4 - j + shift] = True
    return board


# spawn in new pieces randomly when turns start
def new_pieces(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if board[row][col] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    if count < 1:
        full = True
    return board, full


# draw background for the board
def draw_board():
    pygame.draw.rect(screen,'Black', [80,80, 630, 630], 0, 10)
    score_text = font.render(f'Score: {score}', True, 'black')
    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
    screen.blit(score_text, (1000, 550))
    screen.blit(high_score_text, (1000, 650))



# draw tiles for game
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:# Text colour
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048: # Tile colour
                color = colors[value] 
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 145 + 130, i * 145 + 130, 95, 95], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 145 + 177, i * 145 + 177))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, (230,232,250), [j * 145 + 130, i * 145 + 130, 95, 95], 5, 15)  # This is for the border of every box


# main game loop

def main():
    global draw_board,draw_over,draw_pieces,take_turn,board_values,spawn_new,init_count,direction,score,high_score,game_over,init_high
    run = True
    while run:
        timer.tick(fps)
        screen.fill('white')
        image()
        draw_board()
        draw_pieces(board_values)
        if spawn_new or init_count < 2:
            board_values, game_over = new_pieces(board_values)
            spawn_new = False
            init_count += 1
        if direction != '':
            board_values = take_turn(direction, board_values)
            direction = ''
            spawn_new = True
        if game_over:
            draw_over()
            if high_score > init_high:
                file = open('high_score', 'w')
                file.write(f'{high_score}')
                file.close()
                init_high = high_score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'

                if game_over:
                    if event.key == pygame.K_RETURN:
                        board_values = [[0 for _ in range(4)] for _ in range(4)]
                        spawn_new = True
                        init_count = 0
                        score = 0
                        direction = ''
                        game_over = False

        if score > high_score:
            high_score = score

        pygame.display.flip()
    pygame.QUIT

