import simple_draw as sd
sd.resolution = (1200, 600)

y = 500
x = 100

y2 = 450
x2 = 150
while True:
    sd.clear_screen()
    point_0 = sd.get_point(x,y)
    sd.snowflake(center=point_0, length=30)
    y -= 10
    if y < 50:
        break
    x = x + 10

    point_2 = sd.get_point(x2, y2)
    sd.snowflake(center=point_2, length=10)
    y2 -= 10
    if y2 < 50:
        break
    x2 = x2 + 5
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()