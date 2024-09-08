# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder

# - unless the year is also divisible by 400 with no remainder

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


leap = is_leap_year(1989)
print(leap)

leap = is_leap_year(2000)
print(leap)


def is_leap_year2(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


leap = is_leap_year2(2000)
print(leap)


def leapyr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False


print(leapyr(2040))
