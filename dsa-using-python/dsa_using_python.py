##################################################
#                 Date data type                 #
##################################################
# Extracts a collection of birth dates from the user and determines if each individual is >= 21 years old

# inherits from the inbuilt datetime.date class
import datetime
class Date(datetime.date):
    pass

def main():
    # Date before which a person must have been born to be 21 or older now (assuming this year is 2009)
    bornBefore = Date(1988, 1, 6)

    # Extract birth dates from the user and check if they are >= 21 yrs old
    date = promptAndExtractDate()
    while date is not None:
        if date <= bornBefore:
            print("Is at least 21 years old: ", date)
        date = promptAndExtractDate()

# Prompts for and extracts the Gregorian date components. Returns a Date object or None when the user has finished entering dates.
def promptAndExtractDate():
    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return Date(year, month, day)

# Call the main routine
main()

# Implements a proleptic Gregorian calendar date as a Julian day number.
class Date:
    # initializes a date object, which comes with a julian day attribute
    def __init__(self, year, month, day):
        # initialize julian day as 0
        self._julianDay = 0
        # assert followed by error msg
        assert self._isValidGregorian(year, month, day), "Invalid Gregorian date."
    
        tmp = 0
        if month < 3:
            tmp = -1
        # formula to calculate julian day
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + (367 * (month - 2 - tmp * 12) // 12) - (3 * ((year + 4900 + tmp) // 100) // 4)

    # extracts Gregorian date component
    def year(self):
        # returns y from (y, m, d)
        return (self._toGregorian())[0]

    def month(self):
        # returns m from (y, m, d)
        return (self._toGregorian())[1]

    def day(self):
        # returns d from (y, m, d)
        return (self._toGregorian())[2]
    
    # returns day of the week as an int between 0 (Monday) and 6 (Sunday)
    def dayOfWeek(self):
        year, month, day = self._toGregorian()
        # if month = 1, 2
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7
    
    # returns date as string in Gregorian format
    def __str__(self):
        year, month, day = self._toGregorian()
        return "%04d/%02d/%02d" % (year, month, day)
    
    # Date comparison
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay
    
    # later
    def __lt__(self, otherDate):
        return self._julianDay > otherDate._julianDay

    # earlier
    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay
    
    # returns the Gregorian date as a tuple (year, month, day)
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - 12 * A
        year = 100 * (B - 49) + year + A
        return (year, month, day)
    
    # gets the English name of the month of a Gregorian date object
    def monthName(self):
        year, month, day = self._toGregorian()
        if month == 1:
            return "January"
        elif month == 2:
            return "Feburary"
        elif month == 3:
            return "March"
        elif month == 4:
            return "April"
        elif month == 5:
            return "May"
        elif month == 6:
            return "June"
        elif month == 7:
            return "July"
        elif month == 8:
            return "August"
        elif month == 9:
            return "September"
        elif month == 10:
            return "October"
        elif month == 11:
            return "November"
        elif month == 12:
            return "December"
    
    # checks whether a Gregorian date is in a leap year
    def isLeapYear(self):
        year, month, day = self._toGregorian()
        return year // 4 == 0
    
    # returns the number of days between this date and otherDate
    def numDays(self, otherDate):
        return abs(self._julianDay - otherDate._julianDay)
    
    # advances a Gregorian date by a given number of days
    def advanceBy(self, days):
        newJulianDay = max(self._julianDay + days, 0)
        def julianToGregorian(julianDay):
            A = julianDay + 68569
            B = 4 * A // 146097
            A = A - (146097 * B + 3) // 4
            year = 4000 * (A + 1) // 1461001
            A = A - (1461 * year // 4) + 31
            month = 80 * A // 2447
            day = A - (2447 * month // 80)
            A = month // 11
            month = month + 2 - 12 * A
            year = 100 * (B - 49) + year + A
            return (year, month, day)
        return julianToGregorian(newJulianDay)
    
    def _isValidGregorian(self, year, month ,day):
        return (year >= -4714 and month >= 1 and month <= 12 and day >= 1 and day <= 31)

bDay = Date(1997, 5, 23)
bDay.__str__()
bDay.advanceBy(1)
bDay.advanceBy(-1)
bDay2 = Date(1983, 1, 12)
bDay.numDays(bDay2)
bDay.__lt__(bDay2)
bDay.__le__(bDay2)

##################################################
#                 Bag data type                  #
##################################################
# List-based
class Bag:
    # initializes empty bag with empty list
    def __init__(self):
        self._theItems = list()
    
    # returns the number of items in the bag
    def __len__(self):
        return len(self._theItems)
    
    # checks if an item is contained in the bag
    def __contains__(self, item):
        return item in self._theItems
    
    # adds a new item to the bag
    def __add__(self, item):
        self._theItems.append(item)
    
    # removes an item from the bag and returns it
    def __remove__(self, item):
        assert item in self._theItems, "item not in bag."
        index = self._theItems.index(item)
        return self._theItems.pop(index)
    
    # iterator
    def __iter__(self, item):
        pass