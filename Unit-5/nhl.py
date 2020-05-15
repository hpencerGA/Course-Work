# starter code
import requests
class NhlTeams:
    def __init__(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
        self.nhl_stats = response['teams']
        
    def get_team_names(self):
        teams = []
        for team in self.nhl_stats:
            teams.append(team['teamName'])
        return teams

    def conferences(self):
        eastern = 0
        western = 0
        for team in self.nhl_stats:
            if team['conference']['name'] == 'Western':
                western += 1
            if team['conference']['name'] == 'Eastern':
                eastern += 1
                
        print(eastern,western)

    def get_oldest_team(self):
        oldest_team = ()
        last_year = 2020
        for team in self.nhl_stats:
            if int(team['firstYearOfPlay']) <= last_year:
                last_year = int(team['firstYearOfPlay'])
                oldest_team = team     #['teamName'] if need team name not full team 
        
        return oldest_team
                
            #compare each team with one anothers first year of play date and store oldest date

#when working with this data its a good idea to get an idea of what it looks like
#class solution

'''
    def get_oldest_team(self):
        #can sort it as a list from oldest to newest 
        sorted_list = sorted(self.nhl_stats, key = lambda k: k['firstYearOfPlay'] )  #use sorted function to sort the data
        #using a lambda function. A function that can be written on one line, unlikely need to call it anywhere else in the code
        #with lambda left of colum input pass to the lambda function to the right is the ouput
        #example
        #my_func(a):
           # return a*a
        #lambda a: a*a
        print(sorted_list[0]['name'])
'''


nhl_teams = NhlTeams()
print(nhl_teams.get_team_names())
nhl_teams.conferences()
print(nhl_teams.get_oldest_team())


#Write a method get_team_names that returns all the names of the nhl teams
#Write a method win_count that returns ech team and the number of times it has won the nhl
#Write a method conferences that displays the number of teams in the eastern and western conferences
#Write a method get_oldest_team that returns the team that has the oldest first year of play.
'''
{'abbreviation': 'VGK',
  'active': True,
  'conference': {'id': 5, 'link': '/api/v1/conferences/5', 'name': 'Western'},
  'division': {'abbreviation': 'P',
               'id': 15,
               'link': '/api/v1/divisions/15',
               'name': 'Pacific',
               'nameShort': 'PAC'},
  'firstYearOfPlay': '2016',
  'franchise': {'franchiseId': 38,
                'link': '/api/v1/franchises/38',
                'teamName': 'Golden Knights'},
  'franchiseId': 38,
  'id': 54,
  'link': '/api/v1/teams/54',
  'locationName': 'Vegas',
  'name': 'Vegas Golden Knights',
  'officialSiteUrl': 'http://www.vegasgoldenknights.com/',
  'shortName': 'Vegas',
  'teamName': 'Golden Knights',
  'venue': {'city': 'Las Vegas',
            'id': 5178,
            'link': '/api/v1/venues/5178',
            'name': 'T-Mobile Arena',
            'timeZone': {'id': 'America/Los_Angeles',
                         'offset': -7,
                         'tz': 'PDT'}}}]

{'abbreviation': 'LAK',
  'active': True,
  'conference': {'id': 5, 'link': '/api/v1/conferences/5', 'name': 'Western'},
  'division': {'abbreviation': 'P',
               'id': 15,
               'link': '/api/v1/divisions/15',
               'name': 'Pacific',
               'nameShort': 'PAC'},
  'firstYearOfPlay': '1967',
  'franchise': {'franchiseId': 14,
                'link': '/api/v1/franchises/14',
                'teamName': 'Kings'},
  'franchiseId': 14,
  'id': 26,
  'link': '/api/v1/teams/26',
  'locationName': 'Los Angeles',
  'name': 'Los Angeles Kings',
  'officialSiteUrl': 'http://www.lakings.com/',
  'shortName': 'Los Angeles',
  'teamName': 'Kings',
  'venue': {'city': 'Los Angeles',
            'id': 5081,
            'link': '/api/v1/venues/5081',
            'name': 'STAPLES Center',
            'timeZone': {'id': 'America/Los_Angeles',
                         'offset': -7,
                         'tz': 'PDT'}}},
'''

