def is_leap_year(year):
   if year%4==0 and year%100!=0 or year%400==0:
       return 1
   else:
       return 0

if __name__=="__main__":
    year=int(input())
    print(is_leap_year(year))    