import requests
import json
import pprint

class Covid:
    #fetch_statistics to get all the latest covid realted stats on all countries and store the result in an instance variable
    def fetch_statistics(self):
         url = "https://covid-193.p.rapidapi.com/statistics"
         headers = {
         'x-rapidapi-host': "covid-193.p.rapidapi.com",
         'x-rapidapi-key': "5c1506d255msh3a068fd74628662p1ed5aajsn04920b5323ec"
         }
         response = requests.request("GET", url, headers=headers).json()
         self.covid_data = response['response']
         
         url = "https://covid-193.p.rapidapi.com/countries"

         headers = {
         'x-rapidapi-host': "covid-193.p.rapidapi.com",
         'x-rapidapi-key': "5c1506d255msh3a068fd74628662p1ed5aajsn04920b5323ec"
         }

         response = requests.request("GET", url, headers=headers).json()
         self.country_list = response['response']
 
         self.covid_countries = [country for country in self.covid_data if country['country'] in self.country_list]
         self.covid_region = [region for region in self.covid_data if region['country'] not in self.country_list]


    #write a method top_ten that gets the data for the countires with top ten most cases
    def top_ten(self):
        total_cases = lambda case: - (case['cases']['total'])   #case is a name for a variable # made it a negative because want to sort reverse largest number first
        self.covid_countries.sort(key = total_cases)


        
        return self.covid_countries[0:10]
    #write a method get_country stats that accepts the name and returns that country data
    def get_country_stats(self,country):
        for data in self.covid_countries:
            if data['country'] == country:
                return data
    
    def show_regional_stats(self):
        for regional_data in self.covid_region:
            print(regional_data['country']) 
            print(regional_data['cases']['active'],'Active Cases')
            print(regional_data['cases']['critical'],'Critical Cases')
            print(regional_data['cases']['recovered'],'recovered Cases')
            print(regional_data['deaths']['total'],'total deaths')
    
    def tests_unavailable(self):
       return [country for country in self.covid_countries if country['tests']['total'] == None ] 
    

    def stats_to_file(self,file_name):
        text_file = open(file_name, 'a')
        for data in self.covid_countries:
            text_file.write(str(data['country']) + ':') 
            text_file.write(str(data['cases']['active']) + ' Active Cases')
            text_file.write(str(data['cases']['critical']) + 'Critical Cases')
            text_file.write(str(data['cases']['recovered']) + 'recovered Cases')
            text_file.write(str(data['deaths']['total']) + 'total deaths \r\n')
            
        text_file.close()


ap_covid = Covid()
ap_covid.fetch_statistics()
ap_covid.get_country_stats('Canada') 
ap_covid.show_regional_stats()
ap_covid.tests_unavailable()
ap_covid.stats_to_file('covid_data.txt')


''''
{'country': 'Yemen',
               'cases': {'new': '+1',
                         'active': 1,
                         'critical': 0,
                         'recovered': 0,
                         'total': 1},
               'deaths': {'new': None, 'total': 0},
               'tests': {'total': None},
               'day': '2020-04-19',
               'time': '2020-04-19T20:00:11+00:00'}]}
'''

