from main import english_premier_league_team_rank
import http.client
import json
import pprint
import unittest



def test_english_premier_league_team_rank():
    conn = http.client.HTTPSConnection("raw.githubusercontent.com")
    conn.request("GET", "/openfootball/football.json/master/2016-17/en.1.json")

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    test_data = json.loads(data)
    actual_result =  english_premier_league_team_rank(test_data)

    expected_result = ['Middlesbrough FC',
                        'Swansea City FC',
                        'Tottenham Hotspur FC',
                        'Stoke City FC',
                        'Burnley FC',
                        'Manchester City FC',
                        'Hull City AFC',
                        'Sunderland AFC',
                        'Crystal Palace FC',
                        'Leicester City FC',
                        'Manchester United FC',
                        'Watford FC',
                        'West Bromwich Albion FC',
                        'Chelsea FC',
                        'West Ham United FC',
                        'Southampton FC',
                        'Everton FC',
                        'Liverpool FC',
                        'Arsenal FC',
                        'AFC Bournemouth']

    assert actual_result == expected_result


def test_english_premier_league_team_rank_with_wrong_result():
    conn = http.client.HTTPSConnection("raw.githubusercontent.com")
    conn.request("GET", "/openfootball/football.json/master/2016-17/en.1.json")

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    test_data = json.loads(data)
    actual_result =  english_premier_league_team_rank(test_data)
    
    expected_result = ['Middlesbrough FC',
                        'Swansea City FC',
                        'Tottenham Hotspur FC',
                        'Stoke City FC',
                        'Burnley FC',
                        'Manchester City FC',
                        'Hull City AFC',
                        'Sunderland AFC',
                        'Arsenal FC'
                        ]

    assert actual_result != expected_result
