def rectangle_overlap(a, b):
    ax, ay = [x[0] for x in a], [x[1] for x in a]
    min_ax, max_ax, min_ay, max_ay = min(ax), max(ax), min(ay), max(ay)
    check = False
    for pt in b:
        if max_ax >= pt[0] >= min_ax and max_ay >= pt[1] >= min_ay:
            check = True
            if check:
                break
    return check
