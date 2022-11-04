#### 코드 실행 전 터미널창에 "pip install pygame"을 입력해주세요

# 파이게임 모듈 불러오기
import pygame, sys
from pygame.locals import *

# 게임 초기화 함수
def gameInit():
	global gameStart
	gameStart = False
	stick.centerx = width/2
	ball.centerx = stick.centerx
	ball.bottom = stick.top



pygame.init()  # 파이게임 모듈을 사용하는데 필요한 기본 세팅

# 게임화면 사이즈 조절 
width = 424   # 가로 폭
height = 430  # 세로 높이

screen = pygame.display.set_mode((width,height))   # 게임화면을 width, height으로 설정하고 screen 이란 객체로 화면을 정의

stick = pygame.Rect(187,412,50,8)    # 막대에 대한 정보 정의, Rect(x좌표, y좌표, 폭, 높이)
ball = pygame.Rect(206,400,12,12)    # 공에 대한 정보 정의


# 벽돌 만들기 #
brickList=[]    # 벽돌 객체들을 담는 리스트
x=15     # 벽돌 생성 초기 x좌표
y=10     # 벽돌 생성 초기 y좌표

# 벽돌을 생성할 x, y값만 변화시켜 벽돌 정보 생성 후 brickList에 저장
for i in range(11):
	for j in range(12):
		brick = pygame.Rect(x,y,32,13)
		brickList.append(brick)
		x+=33
	x= 15
	y+= 14

vel = [-5,-5]        # 공의 속도 [x방향 속도, y방향 속도]

gameStart = False    # 게임 시작 여부를 확인하는 변수
  
gameInit()           # 게임 초기화


# 게임 시작
while True:
    screen.fill((0,0,0))                            # 화면을 검은색으로 칠함
    pygame.draw.rect(screen, (255,255,255),stick)   # 막대를 화면에 그리기
    pygame.draw.rect(screen,(255,0,0),ball)         # 공을 화면에 그리기

    # 벽돌들을 화면에 그리기
    for brick in brickList:
        pygame.draw.rect(screen,(0,0,255),brick)

    if gameStart:
        # 막대 움직임 
        keyInput = pygame.key.get_pressed()
        if keyInput[K_LEFT] and stick.left >=0:     # 왼쪽키를 누를때 막대의 왼쪽 좌표가 0보다 크면
            stick.left -=10                         # 막대의 왼쪽좌표를 10씩 줄인다

        elif keyInput[K_RIGHT] and stick.right<= width:     # 오른쪽 키를 누를때 막대의 오른쪽 좌표가 width보다 작으면
            stick.right +=10                                # 막대의 오른쪽 좌표를 10만큼 옮긴다

        # 공 움직임
        ball.x += vel[0]
        ball.y+=vel[1]

        if ball.left<0 or ball.right > width:       # 공의 왼쪽좌표가 0보다 작거나 오른쪽 좌표가 width보다 크면(공이 오른쪽 왼쪽 벽을 벗어나면)
            vel[0] *= -1                            # 공의 x 방향을 반대로 설정한다
        if ball.top <0:                             # 공의 위쪽 좌표가 0보다 작으면(공이 위쪽 선을 벗어나면)
            vel[1] *= -1                            # 공의 y 방향을 반대로 설정한다
        if ball.bottom>height:                      # 공의 아래 좌표가 height보다 크면(공이 아래선을 벗어나면)
            gameInit()                              # 게임을 초기화 한다


        if ball.colliderect(stick):                 # 공이 막대와 충돌하면
            vel[1] *=-1                             # 공의 y 방향을 반대로 설정한다
        
    for brick in brickList:                         # brickList의 벽돌들을 하나씩 탐색함
        if ball.colliderect(brick):                 # 공이 벽돌과 충돌하면
            brickList.remove(brick)                 # 충돌한 벽돌을 리스트에서 제거한다
            vel[1] *=-1                             # 공의 y방향을 반대로 설정한다
	
    #
    for event in pygame.event.get():
        if event.type == QUIT:                      # 종료 이벤트 발생 시 게임 종료
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:      # 스페이스바를 누르면
            gameStart = True                                    # gameStart 변수를 True로 설정
    
    

    pygame.display.update()

