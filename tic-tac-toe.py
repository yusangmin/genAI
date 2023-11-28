import pygame
import sys
import random

# 게임 화면 초기화
pygame.init()
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

# 게임 변수 초기화
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]
player = "X"
game_over = False
game_mode = 1  # 1: 사람 vs 사람, 2: 사람 vs 컴퓨터

# 게임 보드 그리기


def draw_board():
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 2)

    for row in range(3):
        for col in range(3):
            x = col * 100 + 50
            y = row * 100 + 50
            if board[row][col] == "X":
                font = pygame.font.Font(None, 80)
                text = font.render("X", True, (0, 0, 0))
                text_rect = text.get_rect(center=(x, y))
                screen.blit(text, text_rect)
            elif board[row][col] == "O":
                font = pygame.font.Font(None, 80)
                text = font.render("O", True, (0, 0, 0))
                text_rect = text.get_rect(center=(x, y))
                screen.blit(text, text_rect)

# 승리 조건 확인


def check_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# 게임 종료 후 재시작


def restart_game():
    global board, player, game_over
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    player = "X"
    game_over = False

# 컴퓨터 차례


def computer_turn():
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        if check_win("O"):
            game_over = True
        else:
            player = "X"


# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_r:
                restart_game()
            elif event.key == pygame.K_1:
                game_mode = 1
                restart_game()
            elif event.key == pygame.K_2:
                game_mode = 2
                restart_game()
            elif event.key == pygame.K_c:
                if not game_over:
                    game_mode = 2
                    restart_game()
                    player = "X"
                    computer_turn()
            elif event.key == pygame.K_p:
                if not game_over:
                    game_mode = 1
                    restart_game()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // 100
                clicked_col = mouseX // 100
                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player
                    if check_win(player):
                        game_over = True
                    else:
                        if game_mode == 1:
                            player = "O" if player == "X" else "X"
                        elif game_mode == 2:
                            player = "X"
                            computer_turn()

    draw_board()
    pygame.display.update()