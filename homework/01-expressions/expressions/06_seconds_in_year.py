""" calculate seconds in a year"""
days_in_year:int=365
hours_in_day:int=24
min_in_hour:int=60
seconds_in_minute=60
# seconds in year = days_in_year *hours_in_day * min_in_hour * seconds_in_minute

def main():
    seconds_in_year=  days_in_year *hours_in_day * min_in_hour * seconds_in_minute
    print(f" There are  \033[1;3m\033[32m{seconds_in_year}\033[0m seconds in a year")
if __name__=="__main__":
    main()