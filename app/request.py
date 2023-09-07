from requests import get
from json import loads


class RequestInterface:
    def get_data(self) -> list:
        pass



class RequestData(RequestInterface):
    
    def __init__(self, api_url, countries):
        self.api_url = api_url
        self.countries = countries
        
    def get_data(self):
        
        countries_data = []
        for country in self.countries:
            query = get(self.api_url+country)
            if query.status_code == 200:
                json_data = loads(query.content)
                countries_data.append(json_data)
        
        return countries_data
    
        
  