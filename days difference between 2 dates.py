#daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
#check if the passed year is a leap year or not.
#it will subtract 4 until it reaches zero or less. if zero then it's a leap year.
#otherwise. it's not.

    i = year
    while i > 0:
        i -= 4
    if i == 0:
        return True
    else:
        return False
        

def comp_day(dim_, m):
    
    dk = dim_
    while dk < daysofmonth(m):
        dk += 1
        if dk == daysofmonth(m):
            return dk  


def daysofmonth(m):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m -= 1
    return daysOfMonths[m]

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    yy2 = y2
    yy1 = y1
    if y2 < y1:
        yy2 = y1
        yy1 = y2

    dd1 = comp_day(d1, m1)
    ddf = dd1 - d1
    m1 += 1

    g = m1
    kx = 0

    if isLeapYear(yy1):
            ddf += 1

    while (yy1 <= yy2):
        kx += daysofmonth(g)
        
        if g >= 12:
            g = 1
            yy1 += 1

            if isLeapYear(yy1):
                ddf += 1

        elif g < 12:
            g +=1
            
        if yy1 == yy2:
            if g == m2:
                break

    kf = kx + ddf
    return kf + 1

print daysBetweenDates(1997, 2, 1, 2016, 8, 1)
