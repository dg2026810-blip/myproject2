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

# 춘식이의 세포막 (전체 크기에 맞춰 위치와 반지름 확대)
sphere(pos = vec(0,0,0) * SIZE, color = color.green, radius = 0.3 * SIZE, opacity=0.5)

# 춘식이의 작은세포 (전체 크기에 맞춰 위치와 반지름 확대)
sphere(pos = vec(-2,0,0) * (SIZE/10), radius = 0.01 * SIZE, color=color.red, opacity=0.5)

# 춘식이의 말 (글자 크기와 배치 위치 확대)
label(text='아자스', pos = vec(1,1,0) * SIZE, height = 20)
