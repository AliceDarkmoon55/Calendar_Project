import local


language = str(input(local.Choose_language))

if language == local.language1:
    birthday = local.birthday1
    date = local.date1
    day, month, year = map(str, input(birthday).split('.'))
    now_day, now_month, now_year = map(str, input(date).split('.'))
    not_born = local.not_born1
    g_calendar = local.g_calendar1
    e_calendar = local.e_calendar1
    dateError = local.dateError1
    today = local.today1

elif language == local.language2:
    birthday = local.birthday2
    date = local.date2
    day, month, year = map(str, input(birthday).split('.'))
    now_day, now_month, now_year = map(str, input(date).split('.'))
    not_born = local.not_born2
    g_calendar = local.g_calendar2
    e_calendar = local.e_calendar2
    dateError = local.dateError2
    today = local.today2

else:
    print(local.langError)


day = int(day)
month = int(month)
year = int(year)
now_day = int(now_day)
now_month = int(now_month)
now_year = int(now_year)

if month > 12:
    print(dateError)
if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day > 31:
    print(dateError)
elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
    print(dateError)
elif year % 4 == 0 and year % 100 != 0 and month == 2 and day > 29:
    print(dateError)
elif year % 400 == 0 and month == 2 and day > 29:
    print(dateError)
elif month == 2 and day > 28:
    print(dateError)

if now_month > 12:
    print(dateError)
elif (now_month == 1 or now_month == 3 or now_month == 5 or now_month == 7 or now_month == 8 or now_month == 10 or
      now_month == 12) and now_day > 31:
    print(dateError)
elif (now_month == 4 or now_month == 6 or now_month == 9 or now_month == 11) and now_day > 30:
    print(dateError)
elif now_year % 4 == 0 and now_year % 100 != 0 and now_month == 2 and now_day > 29:
    print(dateError)
elif now_year % 400 == 0 and now_month == 2 and now_day > 29:
    print(dateError)
elif now_month == 2 and now_day > 28:
    print(dateError)

greg_age = now_year - year
if now_month < month:
    greg_age = greg_age - 1
elif now_month == month and now_day < day:
    greg_age = greg_age - 1

east_age = now_year - year + 1


if now_year < year:
    print(not_born)
elif now_year == year and now_month < month:
    print(not_born)
elif now_year == year and now_month == month and now_day < day:
    print(not_born)
elif now_year == year and now_month == month and now_day == day:
    print(g_calendar, today)
    print(e_calendar, '1')
else:
    print(g_calendar, greg_age)
    print(e_calendar, east_age)
