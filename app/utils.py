import pygame


def find_empty(box):
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 0:
                return (i, j)  # row, col
    return None


def is_valid(box, num, pos):
    # Check row
    for i in range(len(box[0])):
        if box[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(box)):
        if box[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if box[i][j] == num and (i,j) != pos:
                return False
    return True


def redraw_window(win, board, time, strikes):
    win.fill((255,255,255))
    # Draw time
    fnt = pygame.font.SysFont("symap", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw()


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60
    mat = " " + str(minute) + ":" + str(sec)
    return mat