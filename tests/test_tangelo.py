"""##test
1. country has no language data
2. country has several languages
3. language is null
"""
#from app.main import RequestData
from app.dataframe import  DataFrameTable,  WriteTable
from app.request import RequestData, RequestInterface
from main import main_url
import pytest
 

class MockRequestDataClass(RequestInterface):
    def get_data(self): 
        #mock data
        self.data = [
            [  
            {
                'region':'Americas',
                'name':{
                    'common':'colombia'
                },
                'languages':{
                    'esp':'spanish'
                }   
            }     
            ],
            [  
            {
                'region':'any region',
                'name':{
                    'common':'mockcountry'
                },
                'languages':{
                    'lan':'xlanguage'
                }   
            }     
            ]
        ]
        return self.data
        
    

def test_incorrect_query_request():
    incorrect_country = 'nonamecountry'
    api_url = "https://example.com/api/"
    countries = ["fakecountry"]

    request_data = RequestData(main_url, countries)
    data = request_data.get_data()
    
    assert len(data) == 0
   
    
    

def test_not_all_countries_correct():
    incorrect_country = 'nonamecountry'
    api_url = "https://example.com/api/"
    countries = ["fakecountry","colombia","germany"]

    request_data = RequestData(main_url, countries)
    data = request_data.get_data()
    
    assert len(data) < len(countries)
    
    
def test_incorrect_parameters_passing():
    
    with pytest.raises(TypeError):
        table = DataFrameTable()
        table.append_row('region','country')# 2 out of 3 parameters
    
def test_encryption_method():
    
    table = DataFrameTable()
    table.append_row('region','country','language')# 2 out of 3 parameters
    
    assert len(table.language_column) == 1 and not table.language_column[0] == None
    
def test_incorrect_row_values_datatypes():
    
    
    error_count = 0
    
    data = [['hello','hello',3],
            [True,'hello','hello'],['hello',None,'hello']]
    
    table = DataFrameTable()
    for i in data:
        try:
            table.append_row(*i)
        except TypeError as e:
            error_count +=1

    assert error_count == 3
    
def test_time_column_length():
    
    """
        the array self.times in WriteTable class should be the same
        length as the length of the queried data 
    """
    request = MockRequestDataClass()
    writetable = WriteTable(request) 
    writetable.append ()
    
    assert len(writetable.times) == len (request.data)