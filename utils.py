from config import DAILY_REPORTS_URL, TOP_N_STATISTIC
from enums import CSV
from datetime import datetime, timedelta

'''
Returns current date in M/D/Y format.
'''
def get_current_date():
    current_date = datetime.today() - timedelta(days=1)
    formatted_current_date = current_date.strftime("%m-%d-%Y")

    return formatted_current_date

'''
Formats and returns URL for CSV dataset.
'''
def get_csv_url_by_date(date):
    return '{0}{1}.csv'.format(DAILY_REPORTS_URL, date)

'''
Returns summed statistic for provided column.
'''
def get_country_statistics_by_column(df, column):
    return df.groupby(CSV.COUNTRY)[column].sum().sort_values(ascending=False).head(TOP_N_STATISTIC)