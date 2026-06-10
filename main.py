Web VPython 3.2

SIZE = 300

# 춘식이의 얼굴
sphere(pos = vec(0,0,0) * SIZE, color = vec(203/255, 175/255,81/255), radius = 1 * SIZE)
sphere(pos = vec(0.8,0.8,0) * SIZE, color = vec(203/255, 175/255,81/255), radius = 0.2 * SIZE)
sphere(pos = vec(-0.8,0.8,0) * SIZE, color = vec(203/255, 175/255,81/255), radius = 0.2 * SIZE)

# 춘식이의 귀
sphere(pos = vec(0.1,0.25,0.95) * SIZE, color = color.white, radius = 0.15 * SIZE)
sphere(pos = vec(-0.1,0.25,0.95) * SIZE, color = color.white, radius = 0.15 * SIZE)

# 춘식이의 코
sphere(pos = vec(0,0.4,1) * SIZE, color = color.black, radius = 0.05 * SIZE)

# 춘식이의 눈 
sphere(pos = vec(0.3,0.5,0.8) * SIZE, color = color.black, radius = 0.1 * (SIZE * 0.24))
sphere(pos = vec(-0.3,0.5,0.8) * SIZE, color = color.black, radius = 0.1 * (SIZE * 0.24))

# 춘식이의 세포막 
sphere(pos = vec(0,0,0) * SIZE, color = color.green, radius = 0.3 * SIZE, opacity=0.5)

# 춘식이의 말 
label(text='아자스', pos = vec(1,1,0) * SIZE, height = 20)

# 춘식이의 핵 
n = sphere(pos = vec(0,0,0) * (SIZE/100), radius = 0.01 * SIZE, color=color.red, opacity=0.5)
label(text = 'im hack', pos = n.pos + vec(0,10,0))


#춘식이의단백질
curve(pos=[vec(- 10, 30, 20),vec(20,30,30),vec(10,-30,10),vec(-30,10,40),vec(-10,40,-50),vec(40,-40,-20),vec(40,-30,10),vec(10,40,-20),vec(-30,30,-20),vec(20,-20,-20), vec(20, 10, - 10)], color=color.yellow)


#춘식이의미토콘드리아
q = ring(pos=vec(47, 6, 20), axis=vec(1, 6, 0), size=vec(0.1, 8, 4), color=color.cyan)
label(text = 'im mitocondria', pos = q.pos + vec(0,10,0))

#춘식이의골지체
s=box(pos=vector(0, 20, 35),
    size=vector(10, 0.5, 10), 
    color=vec(0.55, 0.27, 0.07)) 
label(text = 'im gouljicha', pos = s.pos + vec(0,10,0))
    
#탈출핵
ball = sphere(pos = vec(0,0,0) * (SIZE/100), radius = 0.01 * SIZE, color=color.red, opacity=0.5)
ball_list = [ball]
ball.velocity = vec(1, 0, 0)
while True:
    rate(60)
    for b in ball_list:
        b.pos = b.pos + b.velocity * 0.1
