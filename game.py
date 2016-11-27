import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
character1 = gamebox.from_color(400, 300, "red", 30, 30)
character1.yspeed = 0
character2 = gamebox.from_color(350, 300, "blue", 30, 30)
character2.yspeed = 0
enemy1 = gamebox.from_color(320, 459, "green", 20, 20)
enemy1.yspeed = 0
enemy2 = gamebox.from_color(380, 459, "green", 20, 20)
enemy2.yspeed = 0
ground = gamebox.from_color(-100, 600, "cyan", 3000, 50)
ceiling = gamebox.from_color(-100, -10, "cyan", 3000, 50)
left_wall = gamebox.from_color(0, 300, "cyan", 15, 1000)
right_wall = gamebox.from_color(800, 300, "cyan", 15, 1000)
walls = [ground, ceiling, left_wall,right_wall]
coins = [gamebox.from_color(300, 450, "yellow", 12, 12)]

time = 1980
score = 0
score2 = 0
lives = 5
lives2 = 5

def tick(keys):
    global time,score,score2,lives,lives2
    time -= 1
    camera.clear("black")

    seconds = str(int((time / ticks_per_second))).zfill(3)
#Moving the character
    if pygame.K_RIGHT in keys:
        character1.x += 3
    if pygame.K_LEFT in keys:
        character1.x -= 3
    if pygame.K_UP in keys:
        character1.y -= 3
    if pygame.K_DOWN in keys:
        character1.y += 3

    if pygame.K_d in keys:
        character2.x += 3
    if pygame.K_a in keys:
        character2.x -= 3
    if pygame.K_w in keys:
        character2.y -= 3
    if pygame.K_s in keys:
        character2.y += 3

    for wall in walls:
        camera.draw(wall)

#Moving the enemy
    if enemy1.x < character1.x:
        enemy1.x += 1
    if enemy1.x > character1.x:
        enemy1.x -= 1
    if enemy1.y < character1.y:
        enemy1.y += 1
    if enemy1.y > character1.y:
        enemy1.y -= 1
    if enemy1.touches(character1):
        lives -= 1
        character1.x = random.randint(20, 600)
        character1.y = random.randint(20, 400)
        camera.draw(character1)

    if enemy2.x < character2.x:
        enemy2.x += 1
    if enemy2.x > character2.x:
        enemy2.x -= 1
    if enemy2.y < character2.y:
        enemy2.y += 1
    if enemy2.y > character2.y:
        enemy2.y -= 1
    if enemy2.touches(character2):
        lives2 -= 1
        character2.x = random.randint(20, 600)
        character2.y = random.randint(20, 400)
        camera.draw(character2)
        
#if the character or enemy touches a wall stop character movement
    for wall in walls:
        if character1.touches(wall):
            character1.yspeed = 0
        if character1.touches(wall):
            character1.move_to_stop_overlapping(wall)
        if character2.touches(wall):
            character2.yspeed = 0
        if character2.touches(wall):
            character2.move_to_stop_overlapping(wall)
        if enemy1.touches(wall):
            enemy1.yspeed = 0
        if enemy1.touches(wall):
            enemy1.move_to_stop_overlapping(wall)
        if enemy2.touches(wall):
            enemy2.yspeed = 0
        if enemy2.touches(wall):
            enemy2.move_to_stop_overlapping(wall)

#if character collects a coin add 1 to score
    for coin in coins:
        if character1.touches(coin):
            score += 1
            coins.remove(coin)
        if character2.touches(coin):
            score2 += 1
            coins.remove(coin)
        camera.draw(coin)

#When lives = 0 then display a message saying that the other player wins
    if lives == 0:
        player1_wins = gamebox.from_text(400, 400, "Player 2 Wins!" , "arial", 24, "white")
        camera.draw(player1_wins)
        gamebox.pause()
    if lives2 == 0:
        player2_wins = gamebox.from_text(400, 400, "Player 1 Wins!" , "arial", 24, "white")
        camera.draw(player2_wins)
        gamebox.pause()

#time 
    if time % 100 == 0:
        coin_x = random.randint(50, 750)
        coin_y = random.randint(100, 700)
        coins.append(gamebox.from_color(coin_x, coin_y, "yellow", 12, 12))

#display score and which player wins after game ends       
    if int(seconds) <= 0:
        if score > score2:
            p1_wins = gamebox.from_text(400, 400, "Player 1 Wins!" , "arial", 24, "white")
            camera.draw(p1_wins)
        if score2 > score2:
            p2_wins = gamebox.from_text(400, 400, "Player 2 Wins!" , "arial", 24, "white")
            camera.draw(p2_wins)
        camera.display()
        gamebox.pause()



    time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, "arial", 24, "white")
    score_box = gamebox.from_text(100, 30, "Score Player1: " + str(score), "arial", 24, "red")
    health_box = gamebox.from_text(100,50, "Lives Player 1:" + str(lives),"arial", 24,"red")
    score_box2 = gamebox.from_text(100, 70, "Score Player 2: " + str(score2), "arial", 24, "blue")
    health_box2 = gamebox.from_text(100,90, "Lives Player 2:" + str(lives2),"arial", 24,"blue")
    camera.draw(character1)
    camera.draw(character2)
    camera.draw(ground)
    camera.draw(time_box)
    camera.draw(score_box)
    camera.draw(health_box)
    camera.draw(score_box2)
    camera.draw(health_box2)
    camera.draw(enemy1)
    camera.draw(enemy2)
    camera.display()
ticks_per_second = 33


# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
