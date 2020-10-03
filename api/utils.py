from api.constants import DAILY_REPORTS_URL, TOP_N_STATISTIC
from api.enums import CSV
from datetime import datetime, timedelta

def get_current_date() -> str:
    """
    Calculates and formats current date.
    :return: current date in M/D/Y format
    """
    current_date = datetime.today() - timedelta(days=1)
    formatted_current_date = current_date.strftime("%m-%d-%Y")

    return formatted_current_date

def get_csv_url_by_date(date) -> str:
    """
    Formats URL for CSV dataset.
    :return: formatted url
    """
    return '{0}{1}.csv'.format(DAILY_REPORTS_URL, date)

def get_country_statistics_by_column(df, column):
    """
    Calculates summed statistic for provided column.
    :return: dataframe for summed statistic
    """
    return df.groupby(CSV.COUNTRY)[column].sum().sort_values(ascending=False).head(TOP_N_STATISTIC)