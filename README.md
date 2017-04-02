def days_in_month(year,month):
    if month==1 or month==3 or month==5 or  month==7 or month==8 or month==10 or month==12:
        return 31
    elif month==2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30


def is_leap_year(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False



def next_day(year,month,day):
    if day< days_in_month(year,month):
        return year,month,day+1
    else:
        if month<12:
            return year,month+1,1
        else:
            return year+1,1,1

def date_is_before(year1,month1,day1,year2,month2,day2):
    if year1<year2:
        return True
    if year1==year2:
        if month1<month2:
            return True
        elif month1 == month2:
            return day1<day2
    return False

def days_between_dates(year1,month1,day1,year2,month2,day2):
    assert  not date_is_before(year2,month2,day2,year1,month1,day1)
    days=0
    while date_is_before(year1,month1,day1,year2,month2,day2):
        year1,month1,day1=next_day(year1,month1,day1)
        days+=1
    return days

def test():
    assert days_between_dates(2013,1,1,2013,1,1)==0
    assert days_between_dates(2013, 1, 1,2013, 1, 2) == 1
    assert next_day(2013,1,1)==(2013,1,2)

    assert next_day(2013,4,30)==(2013,5,1)
    assert next_day(2012, 12,31)==(2013,1,1)
    assert next_day(2013,2,28)==(2013,3,1)
    assert next_day(2013, 9, 30)==(2013, 10, 1)
    assert days_between_dates(2012,1,1,2013,1,1)==366
    assert days_between_dates(2013,1,1,2014,1,1)==365
    assert days_between_dates(2013,1,24,2013,6,29)==156

    print "TESTCASES FINISHED......."



