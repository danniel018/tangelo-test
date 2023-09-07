from hashlib import sha1, sha256


               
class DataFrameTable:
    
    def __init__(self):
        
        self.table = {}
        self.region_column = []
        self.country_column = []
        self.language_column = []
                          
    def append_row(self,region:str, country:str, language:str):
        if not isinstance(region,str) or not isinstance(country,str) or not isinstance(language,str):
            raise TypeError("method parameters should be type str")
     
        self.region_column.append(region)
        self.country_column.append(country)
        self.language_column.append(self.__encrypt_data(language))
        
        
    def append_columns(self):
        self.table['region'] = self.region_column
        self.table['country'] = self.country_column
        self.table['language'] = self.language_column
        
    def __encrypt_data(self,message):
        return sha1(message.encode()).hexdigest()

