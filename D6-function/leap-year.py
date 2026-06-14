# import calendar

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if calendar.isleap(year):
#         # print(f"{year} is a leap year.")
#         leap = True
#     else:
#         # print(f"{year} is not a leap year.")
#         pass

#     return leap

# year = int(input())
# print(is_leap(year))


def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap

year = 2000
print(is_leap(year))