import random
import time 
def GetRandomDate (starDate,endDate):
    print("printing randome date between",starDate ,"and",endDate)
    randomgenirator = random.random()
    dateformat = '%m/%D/%Y'

    startime = time.mktime(time.strptime(starDate , dateformat))
    endtime = time.mktime(time.strptime(endDate , dateformat))

    randomtime = startime + randomgenirator * (endtime - startime)
    randomdate = time.strftime(dateformat , time.localtime(randomtime))
    return randomdate
print("random date = ",GetRandomDate("1/1/2016" , "12/12/2018"))