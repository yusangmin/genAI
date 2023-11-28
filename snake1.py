import pygame
import time
import random

pygame.init()

# 게임 화면 크기 설정
width = 800
height = 600
display = pygame.display.set_mode((width, height))

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 게임 속도 설정
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10

# 글꼴 설정
font_style = pygame.font.SysFont(None, 50)  # 게임에서 사용할 글꼴 설정
score_font = pygame.font.SysFont(None, 35)  # 점수 표시에 사용할 글꼴 설정

# 점수 표시 함수
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

# 게임 실행 함수
def gameLoop():
    game_over = False
    game_close = False

    # 초기 위치 설정
    x1 = width / 2
    y1 = height / 2

    # 위치 변경 값 설정
    x1_change = 0
    y1_change = 0

    # 뱀의 위치 정보를 저장하는 리스트
    snake_List = []
    Length_of_snake = 1

    # 먹이 위치 설정
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    # 게임 루프
    while not game_over:
        while game_close == True:
            display.fill(white)
            game_over_font = font_style.render("Game Over", True, red)
            display.blit(game_over_font, [width / 3, height / 3])
            score_text = score_font.render("Your Score: " + str(Length_of_snake - 1), True, black)
            display.blit(score_text, [width / 3, height / 2])
            pygame.display.update()

            # 게임 종료 후 재시작 또는 종료 선택 처리
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # 키 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:  # ESC 키를 누르면 게임 종료
                    game_over = True

        # 벽과 충돌했을 때 게임 종료
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 자신과 충돌했을 때 게임 종료
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        # 점수 표시
        score_text = score_font.render("Score: " + str(Length_of_snake - 1), True, black)
        display.blit(score_text, [0, 0])

        pygame.display.update()

        # 먹이를 먹었을 때
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
