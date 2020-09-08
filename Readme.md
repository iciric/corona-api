This project is about creating a small API microservice which provides relevant statistics about Corona virus.

Technologies used:
 - Python 3
 - Flask 
 - Pandas 
 - Docker

Datasets were pulled from https://github.com/CSSEGISandData/COVID-19 - Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University.

Instructions for running Corona API:

1. position inside project's directory 
2. docker-compose build
3. docker-compose up
4. send request to http://localhost:5000/api/...

List of current supported API endpoints (documented in api/reports.py):

    - /api/reports/country?country={country} 
    - /api/reports/confirmed
    - /api/reports/active
    - /api/reports/deaths