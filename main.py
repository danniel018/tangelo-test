from app.request import RequestData
from app.dataframe import WriteTable

countries = [
'Namibia',
'Niger',
'colombia',
'canada',
'germany',
'japan',
'australia',
'russia'
]

main_url = 'https://restcountries.com/v3.1/name/'

def run():
    request = RequestData(main_url, countries)
    writetable = WriteTable(request) 
    writetable.append ()
    writetable.write()
    writetable.calculations()
    writetable.export_json()
    writetable.export_to_sqlite()
    
if __name__ == "__main__":
    run()