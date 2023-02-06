# Modules
from utils import *
from utils.mnist_model import predict_num

# -- MAIN -- #
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Number Predictor")

# --------------------------------- #
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid
# --------------------------------- #

def draw_grid(grid, win=WIN):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pg.draw.rect(win, pixel, (j*PIXEL_SIZE, i*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    pg.draw.line(win, WHITE, (0, ROWS*PIXEL_SIZE), (WIDTH, ROWS*PIXEL_SIZE))
# --------------------------------- #

def main(grid, win=WIN):
    win.fill(BG_COLOR)
    draw_grid(grid)

    for btn in buttons:
        btn.draw(win)

    pg.display.update()
# --------------------------------- #

def get_pixel(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if (row >= ROWS) or (col >= COLS):
        return None

    return row, col
# --------------------------------- #


button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 100, 50, "Predict"),
    Button(120, button_y, 100, 50, "Clear"),
    Button(230, button_y, (WIDTH - 250), 50, "Prediction Result")
]

# RUN LOOP
grid = init_grid(ROWS, COLS, BG_COLOR)
draw_color = WHITE

run = True
clock = pg.time.Clock()

while run:
    clock.tick(FPS)

    for event in pg.event.get():
        if (event.type == pg.QUIT):
            run = False

        if (pg.mouse.get_pressed()[0]):
            pos = pg.mouse.get_pos()
            pixel = get_pixel(pos)
            if (pixel):
                row, col = pixel
                grid[row][col] = draw_color
            else:
                for btn in buttons:
                    if (btn.clicked(pos)):
                        if (btn.text == "Clear"):
                            grid = init_grid(ROWS, COLS, BG_COLOR)
                            buttons[-1].text = "Prediction Result"

                        elif (btn.text == "Predict"):
                            prediction = predict_num(grid, ROWS, COLS)
                            if (prediction):
                                num, con = prediction
                                buttons[-1].text = f"Number = {num} | {con}%"
                            else:
                                buttons[-1].text = "idk wtf is this, man!"

    main(grid)


pg.quit()