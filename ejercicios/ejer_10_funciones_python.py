# write your function here
def population_density(a, b):
    return a / b


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# write your function here
def readable_timedelta(days):
    # use integer division to get the number of weeks
    week = days // 7
    # use % to get the number of days that remain
    days_rest = days % 7
    return "{} week(s) and {} day(s)".format(round(week), round(days_rest))


# test your function
print(readable_timedelta(1))  # 1 d
print(readable_timedelta(6))  # 6 d
print(readable_timedelta(7))  # 1 w
print(readable_timedelta(9))  # 1 w 2 d
print(readable_timedelta(9921))  # 1174 w 2 d
print(readable_timedelta(4555))  # 650 w 5 d
print(readable_timedelta(4842))  # 691 w 5 d
