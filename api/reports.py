from flask import Blueprint, request

from api.constants import DAILY_REPORTS_URL
from api.enums import CSV
from api.utils import get_current_date, get_csv_url_by_date, get_country_statistics_by_column

import pandas as pd


reports_api = Blueprint('reports_api', __name__)


@reports_api.route('/api/reports/country', methods=['GET'])
def daily_report():
    """
    Returns current total statistic for provided country. 

    Request example: localhost:5000/api/reports/country?country=US

    Response example:
    {
        "active_cases": 3771412, 
        "confirmed_cases": 6276365, 
        "death_cases": 188941
    }
    """
    request_params = request.args.to_dict()
    country = request_params.get('country')
    date = get_current_date()
    url = get_csv_url_by_date(date)

    df = pd.read_csv(url, usecols=[CSV.COUNTRY, CSV.CONFIRMED, CSV.ACTIVE, CSV.DEATHS])
    country_df = df[df[CSV.COUNTRY] == country]
    confirmed_df = get_country_statistics_by_column(country_df, CSV.CONFIRMED)
    active_df = get_country_statistics_by_column(country_df, CSV.ACTIVE)
    deaths_df = get_country_statistics_by_column(country_df, CSV.DEATHS)

    response = {
        'active_cases': int(active_df.iloc[0]),
        'death_cases': int(deaths_df.iloc[0]),
        'confirmed_cases': int(confirmed_df.iloc[0]),
    }

    return response


@reports_api.route('/api/reports/confirmed', methods=['GET'])
def report_confirmed():
    """
    Returns top N countries by confirmed cases.

    Request: localhost:5000/api/reports/confirmed

    Response example:
    {
        'confirmed_cases': [('US', 50), ('India', 15), ...]
    }
    """
    date = get_current_date()
    url = get_csv_url_by_date(date)
    df = pd.read_csv(url, usecols=[CSV.COUNTRY, CSV.CONFIRMED])

    confirmed_df = get_country_statistics_by_column(df, CSV.CONFIRMED)

    response = {
        'confirmed_cases': [(country, count) for country, count in confirmed_df.iteritems()],
        }

    return response


@reports_api.route('/api/reports/active', methods=['GET'])
def report_active():
    """
    Returns top N countries by active cases.

    Request: localhost:5000/api/reports/active

    Response example:
    {
        'active_cases': [('Brasil', 50), ('Croatia', 15), ...]
    }
    """
    date = get_current_date()
    url = get_csv_url_by_date(date)
    df = pd.read_csv(url, usecols=[CSV.COUNTRY, CSV.ACTIVE])

    active_df = get_country_statistics_by_column(df, CSV.ACTIVE)

    response = {
        'active_cases': [(country, count) for country, count in active_df.iteritems()],
        }

    return response

@reports_api.route('/api/reports/deaths', methods=['GET'])
def report_deaths():
    """
    Returns top N countries by deaths cases.

    Request: localhost:5000/api/reports/deaths

    Response example:
    {
        'deaths_cases': [('UK', 50), ('Pakistan', 15), ...]
    }
    """
    date = get_current_date()
    url = get_csv_url_by_date(date)
    df = pd.read_csv(url, usecols=[CSV.COUNTRY, CSV.DEATHS])

    deaths_df = get_country_statistics_by_column(df, CSV.DEATHS)

    response = {
        'deaths_cases': [(country, count) for country, count in deaths_df.iteritems()],
        }

    return response