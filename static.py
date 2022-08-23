COLUMN_NAMES_DICT = {
    'full_grouped': {
        'New cases': 'NewCases',
        'New deaths': 'NewDeaths',
        'New recovered': 'NewRecovered',
        'WHO Region': 'WHO_Region'
    },
    'worldometer_data': {
        'Serious,Critical': 'Serious/Critical',
        'Tot Cases/1M pop': 'TotalCases/1MPop',
        'Deaths/1M pop': 'Deaths/1MPop',
        'Tests/1M pop': 'Tests/1MPop',
        'WHO Region': 'WHO_Region'
    },
    'covid_19_clean_complete': {
        'WHO Region': 'WHO_Region'
    },
    'country_wise_latest': {
        'New cases': 'NewCases',
        'New deaths': 'NewDeaths',
        'New recovered': 'NewRecovered',
        'Deaths / 100 Cases': 'Deaths/100Cases',
        'Recovered / 100 Cases': 'Recovered/100Cases',
        'Deaths / 100 Recovered': 'Deaths/100Recovered',
        'Confirmed last week': 'ConfirmedLastWeek',
        '1 week change': '1WeekChange',
        '1 week % increase': '1WeekPctIncrease',
        'WHO Region': 'WHO_Region'
    },
    'usa_county_wise': {},
    'day_wise': {
        'New cases': 'NewCases',
        'New deaths': 'NewDeaths',
        'New recovered': 'NewRecovered',
        'Deaths / 100 Cases': 'Deaths/100Cases',
        'Recovered / 100 Cases': 'Recovered/100Cases',
        'Deaths / 100 Recovered': 'Deaths/100Recovered',
        'No. of countries': 'NumberOfCountries'
    }
}


COLUMN_TYPES_DICT = {
    'full_grouped': {
        'str': ['Country/Region', 'WHO_Region'],
        'int': ['Confirmed', 'Deaths', 'Recovered', 'Active', 'NewCases', 'NewDeaths', 'NewRecovered'],
        'date': ['Date']
    },
    'worldometer_data': {
        'str': ['Country/Region', 'Continent', 'WHO_Region'],
        'int': ['Population', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 
                'NewRecovered', 'ActiveCases', 'Serious/Critical', 'TotalCases/1MPop', 'Deaths/1MPop', 
                'TotalTests', 'Tests/1MPop']
    },
    'covid_19_clean_complete': {
        'str': ['Province/State', 'Country/Region', 'WHO_Region'],
        'int': ['Confirmed', 'Deaths', 'Recovered', 'Active'],
        'float': ['Lat', 'Long'],
        'date': ['Date']    
    },
    'country_wise_latest': {
        'str': ['Country/Region', 'WHO_Region'],
        'int': ['Confirmed', 'Deaths', 'Recovered', 'Active', 'NewCases', 'NewDeaths', 'NewRecovered', 
                'ConfirmedLastWeek', '1WeekChange'],
        'float': ['Deaths/100Cases', 'Recovered/100Cases', 'Deaths/100Recovered', '1WeekPctIncrease']
    },
    'usa_county_wise': {
        'str': ['iso2', 'iso3', 'Admin2', 'Province_State', 'Country_Region', 'Combined_Key'],
        'int': ['UID', 'code3', 'FIPS', 'Confirmed', 'Deaths'],
        'float': ['Lat', 'Long_'],
        'date': ['Date']   
    },
    'day_wise': {
        'int': ['Confirmed', 'Deaths', 'Recovered', 'Active', 'NewCases', 'NewDeaths', 'NewRecovered', 
                'NumberOfCountries'],
        'float': ['Deaths/100Cases', 'Recovered/100Cases', 'Deaths/100Recovered'],
        'date': ['Date'] 
    }
}