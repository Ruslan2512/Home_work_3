from datetime import datetime


def get_birthdays_per_week(users):
    monday_lst = ''
    tuesday_lst = ''
    wednesday_lst = ''
    thursday_lst = ''
    friday_lst = ''
    tpl = {}
    current_datetime = datetime.now()
    current_day = current_datetime.day
    current_month = current_datetime.month
    for i in users:
        for k, v in i.items():
            v = v.split('-')
            a = datetime(int(v[0]), int(v[1]), int(v[2]))
            day_of_birth = a.day
            month_of_birth = a.month
            if current_month != month_of_birth and current_day + 7 != day_of_birth:
                a = a.weekday()
                if a == 5 or a == 6 or a == 0:
                    monday_lst += k + ', '
                elif a == 1:
                    tuesday_lst += k + ', '
                elif a == 2:
                    wednesday_lst += k + ', '
                elif a == 3:
                    thursday_lst += k + ', '
                elif a == 4:
                    friday_lst += k + ', '
            else:
                continue
    
    if monday_lst != '':
        print(f'Monday: {monday_lst[:-2]}')
    if tuesday_lst != '': 
        print(f'Tuesday: {tuesday_lst[:-2]}')
    if wednesday_lst != '':   
        print(f'Wednesday: {wednesday_lst[:-2]}')
    if thursday_lst != '':
        print(f'Thursday: {thursday_lst[:-2]}')       
    if friday_lst != '':
        print(f'Friday: {friday_lst[:-2]}')            


get_birthdays_per_week([{'Bill': '1997-02-21', 'Jill': '1998-05-23', 'Kim': '1997-12-25', 'Jan': '1997-01-27', 'Kill': '1997-05-20', 'Thonny': '2023-02-13'}])