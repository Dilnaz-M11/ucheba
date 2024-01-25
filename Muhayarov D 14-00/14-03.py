def quarter(xcoord, ycoord: float):
    if xcoord > 0 and ycoord > 0:
        print("| четверть")
    elif xcoord < 0 and ycoord > 0:
        print("|| четверть")
    elif xcoord < 0 and ycoord < 0:
        print("||| четверть")
    else:
        print("IV четверть")


quarter(3, 4)