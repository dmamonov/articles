if True:
    for r in range(0, 256, 64):
        for g in range(0, 256, 64):
            for b in range(0, 256, 64):
                print(f"\033[48;2;{r};{g};{b}m  {r:3},{g:3},{b:3}  \033[0m", end=" ")
            print()
        print()


def h_to_rgb(h: int) -> tuple[int, int, int]:
    h = h % 360  # wrap hue to [0, 360)
    x = 1 - abs((h / 60) % 2 - 1)

    r, g, b = 0.0, 0.0, 0.0
    if h < 60:
        r, g = 1.0, x
    elif h < 120:
        r, g = x, 1.0
    elif h < 180:
        g, b = 1.0, x
    elif h < 240:
        g, b = x, 1.0
    elif h < 300:
        r, b = x, 1.0
    else:
        r, b = 1.0, x

    r, g, b = [n * 255 for n in (r, g, b)]
    return int(r), int(g), int(b)


for h in range(0, 360, 15):
    r, g, b = h_to_rgb(h)
    print(f"\033[48;2;{r};{g};{b}m  {h:3}° ({r:3},{g:3},{b:3})  \033[0m", end=" ")
    print()




