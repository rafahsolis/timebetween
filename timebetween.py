#!/usr/bin/python
import sys
import datetime

ussage = "ussage: ./timebetween date1 date2 \n(date format: dd-mm-yyyy | today) " \
         "\n examples:\n./timebetween 05-07-2010 09-04-2015\n./timebetween 05-07-2010"

def DatesToSubstract(date1, date2):
    '''
    DatesToSubstract returns a json with the result of substracting one date from another
    '''

    if date1 == 'today':
        datetype1 = datetime.datetime.now().date()
    else:
        datetype1 = datetime.datetime.strptime(date1, '%d-%m-%Y').date()

    if date2 == 'today':
        datetype2 = datetime.datetime.now().date()
    else:
        datetype2 = datetime.datetime.strptime(date2, '%d-%m-%Y').date()

    if datetype1 < datetype2:
        tmp = datetype1
        datetype1 = datetype2
        datetype2 = tmp

    numbisiestos = bisiestos(datetype2.year, datetype1.year)
    dif = (datetype1 - datetype2)
    years = (dif.days - numbisiestos) / 365

    if datetype1.month > datetype2.month:
        if datetype1.day >= datetype2.day:
            months = datetype1.month - datetype2.month
            days = datetype1.day - datetype2.day

        elif datetype1.day < datetype2.day:
            months = datetype1.month - datetype2.month - 1
            days = MonthNumDays(datetype2.month, datetype2.year) - datetype2.day + datetype1.day

    if datetype1.month == datetype2.month:
        if datetype1.day >= datetype2.day:
            months = datetype1.month - datetype2.month
            days = datetype1.day - datetype2.day

        elif datetype1.day < datetype2.day:
            months = 12 * (datetype1.year - datetype2.year) -1
            days = MonthNumDays(datetype2.month, datetype2.year) - datetype2.day + datetype1.day

    elif datetype1.month < datetype2.month:
        if datetype1.day >= datetype2.day:
            months = 12 + datetype1.month - datetype2.month
            days = datetype1.day - datetype2.day

        elif datetype1.day < datetype2.day:
            months = 12 + datetype1.month - datetype2.month - 1
            days = MonthNumDays(datetype2.month, datetype2.year) - datetype2.day + datetype1.day

    result = {}
    result['years'] = years
    result['months'] = months
    result['days'] = days
    result['from_day'] = datetype2.day
    result['from_month'] = datetype2.month
    result['from_year'] = datetype2.year
    result['to_day'] = datetype1.day
    result['to_month'] = datetype1.month
    result['to_year'] = datetype1.year
    return result


def bisiestos(start, end):
    '''
    Returns the number of years with 366 days between the start year and the end year.
    :param start:
    :param end:
    :return:
    '''
    years = range(start, end, 1)
    counter = 0
    for year in years:
        if bisiesto(year):
            counter += 1
    return counter


def bisiesto(year):
    '''
    Returns True if the year had 366 days and false if it had 365
    :param year: (yyyy)
    :return:
    '''
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def MonthNumDays(month, year):
    '''
    Returns the number of days in a given month and year.
    example: feb2thousand = MonthNumDays(2, 2000)
    :param month: (1-12)
    :param year: (yyyy)
    :return:
    '''
    if month == 2:
        if bisiesto(year):
            return 29
        else:
            return 28

    elif month <= 7:
        if month == 0:
            return 31
        elif month % 2 == 0:
            return 30
        else:
            return 31

    elif month > 7 and month <= 12:
        if month % 2 == 0:
            return 31
        else:
            return 30
    else:
        return None


def main():
    '''
    timebetween.py calculates the time elapsed between two dates. see ussage.
    :return:
    '''
    if len(sys.argv) < 3:
        print ussage
    elif len(sys.argv) == 3:
        timeElapsed = DatesToSubstract(sys.argv[1], sys.argv[2])
        print "Time elapsed from: {0}-{1}-{2} to: {3}-{4}-{5}".format(timeElapsed['from_day'],
                                                                      timeElapsed['from_month'], timeElapsed['from_year'],
                                                                      timeElapsed['to_day'], timeElapsed['to_month'],
                                                                      timeElapsed['to_year'])
        print "{0} years, {1} months, {2} days.".format(timeElapsed['years'], timeElapsed['months'], timeElapsed['days'])
    else:
        print "Options incorrect: ", ussage, sys.argv


if __name__ == '__main__':
    main()