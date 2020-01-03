# Snake

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

snake_1 = [gamebox.from_color(200, 300, "blue", 10, 10)]
snake_2 = [gamebox.from_color(600, 300, "red", 10, 10)]
name = gamebox.from_image(400, 175, "http://www.thatsoftwaredude.com/images/post/snake-game-clone.png")
name.width = 400
ss = gamebox.load_sprite_sheet(
    'http://www.ruby2d.com/assets/img/learn/coin.png',
    1, 6)
coins = [gamebox.from_image(random.randrange(50,750), random.randrange(50,550), ss[0])]
for coin in coins:
    coin.width = 27
    coin.age = 0

start_screen = True
snake_1_score = 0
snake_2_score = 0
time = 21

def tick(keys):

    global snake_1_score
    global snake_2_score
    global coins
    global start_screen
    global time
    if start_screen:
        camera.clear("black")
        camera.draw("Daniel Nguyen (dvn5fg)", 20, "white", 700, 50)
        camera.draw("Jared Tewodros (jmt5rg)", 20, "white", 100, 50)
        camera.draw("Welcome to Snake!", 25, "white", 400, 250)
        camera.draw("Player 1 uses the AWSD keys to move. Player 2 uses the arrow keys to move.", 22, "white", 400, 300)
        camera.draw("There is a 20 second timer. If you crash into your opponent, the walls, or yourself, your opponent wins.", 22, "white", 400, 350)
        camera.draw("If you collect a coin, you get a point. If the timer runs out, the person with the most coins wins.", 22, "white", 400, 400)
        camera.draw("Press space to start the game.", 25, "white", 400, 450)
        camera.draw(name)
        camera.display()

    if pygame.K_SPACE in keys:
        start_screen = False

    if not start_screen:

        camera.clear("black")

        for snake in snake_1:
            camera.draw(snake)
        for snake in snake_2:
            camera.draw(snake)

        if pygame.K_w in keys:
            new = gamebox.from_color(snake_1[-1].x, snake_1[-1].y - 10, "blue", 10, 10)
            snake_1.append(new)

        if pygame.K_s in keys:
            new = gamebox.from_color(snake_1[-1].x, snake_1[-1].y + 10, "blue", 10, 10)
            snake_1.append(new)

        if pygame.K_a in keys:
            new = gamebox.from_color(snake_1[-1].x - 10, snake_1[-1].y, "blue", 10, 10)
            snake_1.append(new)

        if pygame.K_d in keys:
            new = gamebox.from_color(snake_1[-1].x + 10, snake_1[-1].y, "blue", 10, 10)
            snake_1.append(new)

        if pygame.K_UP in keys:
            new = gamebox.from_color(snake_2[-1].x, snake_2[-1].y - 10, "red", 10, 10)
            snake_2.append(new)

        if pygame.K_DOWN in keys:
            new = gamebox.from_color(snake_2[-1].x, snake_2[-1].y + 10, "red", 10, 10)
            snake_2.append(new)

        if pygame.K_LEFT in keys:
            new = gamebox.from_color(snake_2[-1].x - 10, snake_2[-1].y, "red", 10, 10)
            snake_2.append(new)

        if pygame.K_RIGHT in keys:
            new = gamebox.from_color(snake_2[-1].x + 10, snake_2[-1].y, "red", 10, 10)
            snake_2.append(new)

        for snake in snake_2:
            if snake.top < camera.top or snake.bottom > camera.bottom or snake.left < camera.left or \
                    snake.right > camera.right:
                camera.draw("BLUE Wins!", 40, "yellow", 400, 300)
                gamebox.pause()
            if snake_1[-1].touches(snake):
                if snake_1[-1].touches(snake_2[-1]):
                    camera.draw("TIE", 40, "yellow", 400, 300)
                    gamebox.pause()
                else:
                    camera.draw("RED Wins!", 40, "yellow", 400, 300)
                    gamebox.pause()

        for snake in snake_1:
            if snake.top < camera.top or snake.bottom > camera.bottom or snake.left < camera.left or \
                    snake.right > camera.right:
                camera.draw("RED Wins!", 40, "yellow", 400, 300)
                # gamebox.pause()
                if pygame.K_l in keys:
                    start_screen = True
                    snakes_1 = [gamebox.from_color(200, 300, "blue", 10, 10)]
                    snakes_2 = [gamebox.from_color(600, 300, "red", 10, 10)]

            if snake_2[-1].touches(snake):
                if snake_1[-1].touches(snake_2[-1]):
                    camera.draw("TIE", 40, "yellow", 400, 300)
                    # gamebox.pause()
                    if pygame.K_SPACE in keys:
                        # gamebox.unpause()
                        snake_1.x = 200
                        snake_1.y = 300
                        snake_2.x = 600
                        snake_2.y = 300

                else:
                    camera.draw("BLUE Wins!", 40, "yellow", 400, 300)
                    gamebox.pause()

        if len(snake_1) > 3:
            for i in range(len(snake_1)-4):
                if snake_1[-1].touches(snake_1[i]):
                    camera.draw("RED Wins!", 40, "yellow", 400, 300)
                    # gamebox.pause()
                    if pygame.K_SPACE in keys:
                        # gamebox.unpause()
                        snake_1.x = 200
                        snake_1.y = 300
                        snake_2.x = 600
                        snake_2.y = 300

        if len(snake_2) > 3:
            for i in range(len(snake_2)-4):
                if snake_2[-1].touches(snake_2[i]):
                    camera.draw("BLUE Wins!", 40, "yellow", 400, 300)
                    # gamebox.pause()
                    if pygame.K_SPACE in keys:
                        # gamebox.unpause()
                        snake_1.x = 200
                        snake_1.y = 300
                        snake_2.x = 600
                        snake_2.y = 300

        for coin in coins:
            coin.age += 0.5
            coin.image = ss[0 + int(coin.age % 6)]
            camera.draw(coin)
            if snake_1[-1].touches(coin):
                # new = gamebox.from_image(random.randrange(50, 750), random.randrange(50, 550), ss[0])
                # coins.append(new)
                coins.remove(coin)
                snake_1_score += 1
            if snake_2[-1].touches(coin):
                # new = gamebox.from_image(random.randrange(50,750), random.randrange(50,550), ss[0])
                # coins.append(new)
                coins.remove(coin)
                snake_2_score += 1

        time -= 1/30

        camera.draw("Time: " + str(int(time)), 20, "orange", 400, 50)

        if time < 0:
            if snake_1_score > snake_2_score:
                camera.draw("BLUE Wins!", 40, "yellow", 400, 300)
                # gamebox.pause()
                if pygame.K_SPACE in keys:
                    # gamebox.unpause()
                    snake_1.x = 200
                    snake_1.y = 300
                    snake_2.x = 600
                    snake_2.y = 300
            if snake_2_score > snake_1_score:
                camera.draw("RED Wins!", 40, "yellow", 400, 300)
                # gamebox.pause()
                if pygame.K_SPACE in keys:
                    # gamebox.unpause()
                    snake_1.x = 200
                    snake_1.y = 300
                    snake_2.x = 600
                    snake_2.y = 300
            if snake_2_score == snake_1_score:
                camera.draw("TIE", 40, "yellow", 400, 300)
                # gamebox.pause()
                if pygame.K_SPACE in keys:
                    # gamebox.unpause()
                    snake_1.x = 200
                    snake_1.y = 300
                    snake_2.x = 600
                    snake_2.y = 300

        camera.draw("Blue: " + str(snake_1_score), 20, "green", 50, 50)
        camera.draw("Red: " + str(snake_2_score), 20, "green", 750, 50)

        camera.display()

gamebox.timer_loop(30, tick)

# Flappy Bird

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

score = 0
final_score = 0
pipe_speed = -10
gravity = 0.5
game_start = False
game_start_score = False
pipe_bool = True

bird = gamebox.from_image(30, 250, "https://www.pinclipart.com/picdir/big/66-666407_flying-bird-clipart-bird-png-flappy-bird-birds.png")
bird.size = [25, 25]

ground = [gamebox.from_color(400, 590, "beige", 800, 20)]


pipes = [gamebox.from_color(500, 0, "green", 40, random.randrange(300, 450)), gamebox.from_color(500, 500, "green", 40, random.randrange(300, 450)),
        gamebox.from_color(1000, 0, "green", 40, random.randrange(300, 450)), gamebox.from_color(1000, 500, "green", 40, random.randrange(300, 450))]


def tick(keys):

    "Implements a flappy bird like game."

    global score
    global final_score
    global pipe_speed
    global game_start
    global game_start_score
    global pipe_bool
    global gravity

    camera.clear("blue")

    game_over = gamebox.from_text(400, 100, "Final Score: " + " " + str(final_score), 30, "white")

    if pygame.K_SPACE in keys:
        game_start = True
        game_start_score = True
        bird.speedy = -7
        bird.move(0, bird.speedy)
        keys.clear()

    if game_start:
        bird.speedy += gravity
        bird.y += bird.speedy
        for pipe in pipes:
            pipe.speedx = pipe_speed
            pipe.move(pipe_speed, 0)

    for pipe in pipes:
        if pipe.x < -40:
            pipe.size = [40, random.randint(200, 450)]
            pipe.x = 1000
            pipe_bool = True

    for pipe in pipes:
        if pipe.x < bird.x and pipe_bool:
            score += 1
            pipe_bool = False

    if bird.y < -50:
        bird.y = -49

    if bird.top < camera.top:
        final_score = score
        score = 0
        game_start = False

    for box in ground:
        if bird.touches(box):
            final_score = score
            score = 0
            game_start = False

    for pipe in pipes:
        if bird.touches(pipe):
            final_score = score
            score = 0
            game_start = False

    if game_start is False:
        pipes[0].x = 500
        pipes[1].x = 500
        pipes[2].x = 1000
        pipes[3].x = 1000
        bird.x = 100
        bird.y = 300
        pipe_bool = True
        if game_start_score is True:
            camera.draw(game_over)
        # score = 0

    for pipe in pipes:
        camera.draw(pipe)
    for box in ground:
        camera.draw(box)
    camera.draw(bird)
    camera.display()


gamebox.timer_loop(500, tick)
