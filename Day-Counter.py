def isLeapYear(year):
#check if the passed year is a leap year or not.
#it will subtract 4 until it reaches zero or less. if zero then it's a leap year.
#otherwise. it's not.
    if year >= 0:
        i = year
        while i > 0:
            i -= 4
        if i == 0:
            return True
        else:
            return False
    elif year <= 0:
        i = year
        while i < 0:
            i += 4
        if i == 0:
            return True
        else:
            return False

def comp_day(dim_, m):
    #find the number oof days between a specific day of a month
    #and the last day in that month
    dk = daysofmonth(m) - dim_
    return dk

def daysofmonth(m):
    #returns the number of days in a passed month
    if m <1 or m > 12:
        return -1
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m -= 1
    return daysOfMonths[m]

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    #calculate the number of days between 2 dates
    yy2 = y2 #passing variables into local ones so that we preserve passed ones (y1, d1...etc) 
    yy1 = y1 #so that their original values are accessible later for a different purpose.
    if y2 < y1:
        yy2 = y1
        yy1 = y2 #I want 'yy2' to hold the largest value

    ddf = comp_day(d1, m1)
    m1 += 1

    g = m1
    kx = 0

    if isLeapYear(yy1):
            ddf += 1 # add 1 day if the use passed year is a leap year.

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

#ex: this should print '7121'
#print daysBetweenDates(1997, 2, 1, 2016, 8, 1)
