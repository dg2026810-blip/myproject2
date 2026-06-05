1. #제목:춘식이 in DNA㈜
2. 춘식이를 만들고 (춘식이 코드는 복사함) 춘식이 안에 있는 세포들의 코드를 만들었고 색도 다양하게 만들었고 여러가지를 만들고 싶었지만 아직 그코드를 실행을 못했다
3. 춘식이 안에 세포막 (초록색)과 세포(빨간색)으로 코드를 짰고 DNA코드를 미리 계싼해 놓고 마무리를 하였다★
4. 춘식이 안에 세포와 DAN를 표현할 생각에 벌써부터 재미있을 것 같다♬
  
Chunsik in DNA

Constructing Chunsik. I wrote code to make Chunsik do Aja.

I wrote code using Chunsik's cell membrane (green) and cell (red).

Interesting.
기본 개념: 나선형 계단 만들기♥
DNA 구조는 마치 중앙 기둥을 중심으로 빙글빙글 돌아가며 올라가는 계단과 같다
구(Sphere): 계단의 양쪽 손잡이 (인산-당 뼈대)
실린더(Cylinder): 계단의 발판 (염기쌍)

Python
y = i * spacing # 위로 한 칸씩 올라가고
theta = i * angle_step # 옆으로 조금씩 회전한다
i가 커질수록 y값이 커져서 위로 올라가고, theta(각도)가 커져서 회전하게 된다
 두 개의 뼈대 만들기
Python
pos1 = vec(x1, y, z1) # 첫 번째 나선의 위치
pos2 = vec(x2, y, z2) # 두 번째 나선의 위치 (1번의 반대편)
pos1이 오른쪽이라면, pos2는 정확히 반대편(theta + pi, 즉 180도 뒤)에 위치하게 설정했습니다. 그래야 DNA 특유의 대칭 구조가 만들어짐
3D 물체 배치하기
Python
sphere(pos=pos1, radius=0.4, color=color.cyan)
sphere: pos1 위치에 파란색(Cyan) 공을 놓습니다. (왼쪽 뼈대)
Python
cylinder(pos=pos1, axis=pos2 - pos1, radius=0.1, color=color.white)
cylinder: 이 부분이 핵심이고
pos: 막대기가 시작되는 지점 (pos1)
axis: 막대기가 뻗어나가는 방향과 길이인데 pos2 - pos1이라고 쓰면 결과적으로 두 뼈대 사이를 연결하는 하얀색 염기쌍 막대가 만들어진다

4. 요약
이 코드는 for 반복문을 40번 돌면서 다음과 같은 일을 한다 이번 층은 몇 도 회전하고 얼마나 높이 있을까 계산 왼쪽 끝과 오른쪽 끝에 공을 하나씩 놓자 (뼈대 생성) 두 공 사이에 막대기를 연결 (염기쌍 생성)이걸 40번 반복하면 우리 눈앞에 멋진 3D 
DNA 구조가 나타나는 것


위 내용은 AI를 사용하여 마이토콘드리아와 단백질을 다시 만들것이다

단백질 구조 curve코드로 만들었다 #아직 DNA는 만들지 못하였다 ( 너무 어려움)
미토콘드리아를 추가로 만들었다 

세포에에 속해있는 골지체를 만들었다 

#춘식이의골지체
w = ribbon_shape = shapes.rectangle(width=2, height=0.1)
ribbon_path = []
steps = 200
for i in range(steps):
    x = float(i) / 10
    y = 2.5 * sin(1.5 * x)
    z = 0
    ribbon_path.append(vec(x, y, z))
strip = extrusion(path=ribbon_path, shape=ribbon_shape, color=vec(0.55, 0.27, 0.07))
선생님의 조언으로 세포들이 다 말을 할 수 있었다
세포마다 라벨을 붙여줬다

