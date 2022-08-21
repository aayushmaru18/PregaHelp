# estimating due date
# estimating date of conception
# estimating best time for routine anatomy ultrasound

# https://flo.health/tools/due-date-calculator
# https://www.lifestylemedicalcenters.com/need-a-pregnancy-calculator-which-one-should-you-use/

'''
It's important to remember that your due date is only an estimate — most babies are born between 38 and 42 weeks 
from the first day of their mom's LMP and only a small percentage of women actually deliver on their due date.
'''

'''
the first trimester is from week 1 to the end of week 12
the second trimester is from week 13 to the end of week 26
the third trimester is from week 27 to the end of the pregnancy
'''

import datetime
from dateutil.relativedelta import relativedelta

class Calculate_EDD():
    
    def __init__(self, last_menstrual_period, average_cycle_length, current_date=datetime.date.today()):
        
        self.last_menstrual_period = last_menstrual_period
        self.average_cycle_length = average_cycle_length
        self.current_date = current_date

    def calculate(self):
        add_9_months = self.last_menstrual_period + relativedelta(months=9)
        sub_21_days = add_9_months - relativedelta(days=21)
        final = sub_21_days + relativedelta(days=self.average_cycle_length)

        return(final)

    def Gestation_Age(self):
        diff = abs(self.last_menstrual_period - self.current_date).days
        gestation_age_weeks = diff//7

        return(gestation_age_weeks)

# if __name__ == "__main__":
#     year = int(input('Enter a year: '))
#     month = int(input('Enter a month: '))
#     day = int(input('Enter a day: '))

#     last_menstrual_period = datetime.date(year, month, day)
   
#     EDD = Calculate_EDD(last_menstrual_period, 31)
    
#     print()
#     print("First day of last menstrual period: ",last_menstrual_period.strftime('%d-%m-%Y'))
#     print("Estimated Due Date = ",EDD.calculate().strftime('%d-%m-%Y'))
#     print()
#     print(f"Gestation Age: { EDD.Gestation_Age()} weeks")