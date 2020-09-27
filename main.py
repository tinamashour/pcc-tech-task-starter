import http.client
import json
import pprint



list_of_team = {}
def english_premier_league_team_rank():
    """
    rank team based on point, goal diffrencess and goal for
    return: dic 
    """
    
    for rnd in data['rounds']:

        for match in rnd['matches']:

            if match['team1'] not in list_of_team:
                list_of_team[match['team1']] = {}
                create_team_feature(list_of_team[match['team1']])
            if match['team2'] not in list_of_team:
                list_of_team[match['team2']] = {}
                create_team_feature(list_of_team[match['team2']])

            calculate_win_and_losses(match)
            calculate_goals_for_and_against(match)
            calculate_point(match)

    calculate_goal_difference(match)
    ranked_list = compute_rank_list(list_of_team)
    ranked_teams = populate_rank_team_list(ranked_list)
    return  ranked_teams  


def create_team_feature(team):
    team['rank'] = 0
    team['wins'] = 0
    team['draws'] = 0
    team['losses'] = 0
    team['goals_for'] = 0
    team['goals_against'] = 0
    team['goal_difference'] = 0
    team['points'] = 0


def calculate_win_and_losses(match):
    team1_name = match['team1']
    team2_name = match['team2']
    if match['score']['ft'][0] > match['score']['ft'][1]:
        list_of_team[team1_name]['wins'] += 1
        list_of_team[team2_name]['losses'] += 1
    if match['score']['ft'][0] < match['score']['ft'][1]:
        list_of_team[team1_name]['losses'] += 1
        list_of_team[team2_name]['wins'] += 1
        

def calculate_goals_for_and_against(match):
    team1_name = match['team1']
    team2_name = match['team2']
    if match['score']['ft'][0] > match['score']['ft'][1]:
        list_of_team[team1_name]['goals_for'] += match['score']['ft'][0] 
        list_of_team[team1_name]['goals_against'] += match['score']['ft'][1]
    elif match['score']['ft'][0] < match['score']['ft'][1]:
        list_of_team[team2_name]['goals_for'] += match['score']['ft'][1]
        list_of_team[team2_name]['goals_against'] += match['score']['ft'][0]
    else:
        list_of_team[team1_name]['goals_for'] += match['score']['ft'][0] 
        list_of_team[team1_name]['goals_against'] += match['score']['ft'][1]
        list_of_team[team2_name]['goals_for'] += match['score']['ft'][1]
        list_of_team[team2_name]['goals_against'] += match['score']['ft'][0]
        list_of_team[team1_name]['draws'] += 1
        list_of_team[team2_name]['draws'] += 1


def calculate_point(match):
    team1_name = match['team1']
    team2_name = match['team2']
    if match['score']['ft'][0] > match['score']['ft'][1]:
        list_of_team[team1_name]['points'] +=  3
    elif match['score']['ft'][0] < match['score']['ft'][1]:    
        list_of_team[team2_name]['points'] +=  3
    else:
        list_of_team[team1_name]['points'] += 1
        list_of_team[team2_name]['points'] += 1


def calculate_goal_difference(match):
    for team in list_of_team:
        list_of_team[team]['goal_difference'] = list_of_team[team]['goals_for'] - list_of_team[team]['goals_against']


def compute_rank_list(list_of_team):
    rank_list = {} 
    for key, val in list_of_team.items():
        rank_list[key] = [list_of_team[key]['points'],\
                          list_of_team[key]['goal_difference'],\
                          list_of_team[key]['goals_for']]
    
    sort_orders = sorted(rank_list.items(),\
                     key=lambda x: x[1], reverse=True)
   
    rank_based_list = []
    for i in sort_orders:
        rank_based_list.append(i[0]) 
    return rank_based_list    


def populate_rank_team_list(ranked_list):
    ranked_teams = {}
    for team_name in ranked_list:
        ranked_teams[team_name]= list_of_team[team_name]
    return  ranked_teams.keys()    


if __name__ == "__main__":
    conn = http.client.HTTPSConnection("raw.githubusercontent.com")
    conn.request("GET", "/openfootball/football.json/master/2016-17/en.1.json")

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    data = json.loads(data)

    pprint.pprint(data)

    ranked_teams = english_premier_league_team_rank()
    pprint.pprint(ranked_teams)
   


