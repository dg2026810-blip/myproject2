Web VPython 3.2

sphere(pos = vec(0,0,0) * 100, color = vec(203/255, 175/255,81/255), radius = 1 * 100)
sphere(pos = vec(0.8,0.8,0) * 100, color = vec(203/255, 175/255,81/255), radius = 0.2 * 100)
sphere(pos = vec(-0.8,0.8,0) * 100, color = vec(203/255, 175/255,81/255), radius = 0.2 * 100)

sphere(pos = vec(0.1,0.25,0.95) * 100, color = color.white, radius = 0.15 * 100)
sphere(pos = vec(-0.1,0.25,0.95) * 100, color = color.white, radius = 0.15 * 100)

sphere(pos = vec(0,0.4,1) * 100, color = color.black, radius = 0.05 * 100)

sphere(pos = vec(0.3,0.5,0.8) * 100, color = color.black, radius = 0.1 * 24)
sphere(pos = vec(-0.3,0.5,0.8) * 100, color = color.black, radius = 0.1 * 24)

sphere(pos = vec(0,0,0), color = color.green, radius = 50,opacity=0.5)

helix(pos=vec(0, 0, 0), axis=vec(20, 0, 0), color=color.red)

sphere(pos=vector(-2,0,0),radius=1, color=color.red, opacity=0.5)

label(text='',pos = vec(100,100,0))


# 2. 파라미터 설정
num_bases = 30        # 염기쌍 개수
radius = 1.5          # 나선 반경
height_step = 0.3     # 염기쌍 사이의 수직 거리
twist_step = 0.2      # 염기쌍 사이의 회전 각도

# 3. DNA 구조 생성
for i in range(num_bases):
    # 각도 및 높이 계산
    theta = i * twist_step
    y = i * height_step - (num_bases * height_step / 2) # 중심을 0으로 설정
    
    # 두 개의 나선(Backbone) 위치 계산 (180도 차이)
    pos1 = vector(radius * cos(theta), y, radius * sin(theta))
    pos2 = vector(radius * cos(theta + pi), y, radius * sin(theta + pi))
    
    # 염기(Nucleotide) - 나선 골격 그리기
    sphere(pos=pos1, radius=0.2, color=color.blue)
    sphere(pos=pos2, radius=0.2, color=color.red)
    
    # 염기쌍 연결 (Hydrogen Bond)
    cylinder(pos=pos1, axis=pos2-pos1, radius=0.05, color=color.white)

# 4. 카메라 뷰 설정
scene.camera.pos = vector(0, 0, 10)
scene.camera.axis = vector(0, 0, -10)

