from enum import Enum

'''
Column names from CSV dataset.
'''
class CSV(str, Enum):
    ACTIVE = 'Active'
    CONFIRMED = 'Confirmed'
    DEATHS = 'Deaths'
    COUNTRY = 'Country_Region'