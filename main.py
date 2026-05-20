Web VPython 3.2
#춘식이의얼굴
sphere(pos = vec(0,0,0) * 100, color = vec(203/255, 175/255,81/255), radius = 1 * 100)
sphere(pos = vec(0.8,0.8,0) * 100, color = vec(203/255, 175/255,81/255), radius = 0.2 * 100)
sphere(pos = vec(-0.8,0.8,0) * 100, color = vec(203/255, 175/255,81/255), radius = 0.2 * 100)

#춘식이의귀
sphere(pos = vec(0.1,0.25,0.95) * 100, color = color.white, radius = 0.15 * 100)
sphere(pos = vec(-0.1,0.25,0.95) * 100, color = color.white, radius = 0.15 * 100)

#춘식이의코
sphere(pos = vec(0,0.4,1) * 100, color = color.black, radius = 0.05 * 100)

#춘식이의눈
sphere(pos = vec(0.3,0.5,0.8) * 100, color = color.black, radius = 0.1 * 24)
sphere(pos = vec(-0.3,0.5,0.8) * 100, color = color.black, radius = 0.1 * 24)

#춘식이의세포막
sphere(pos = vec(0,0,0), color = color.green, radius = 50,opacity=0.5)

#DNA조각
helix(pos=vec(0, 0, 0), axis=vec(20, 0, 0), color=color.red)

#춘식이의작은세포
sphere(pos=vector(-2,0,0),radius=1, color=color.red, opacity=0.5)

# 춘식이의말
label(text='아자스',pos = vec(100,100,0))
