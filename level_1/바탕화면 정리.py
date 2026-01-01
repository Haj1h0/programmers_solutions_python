def solution(wallpaper):
    lux, luy, rdx, rdy = 50, 50, 0, 0
    for row, wp in enumerate(wallpaper):
        for col, file in enumerate(wp):
            if file == '#':
                lux = min(lux, row)
                luy = min(luy, col)
                rdx = max(rdx, row + 1)
                rdy = max(rdy, col + 1)
    
    answer = [lux, luy, rdx, rdy]
    return answer
