import time
from pandas import DataFrame
import sqlite3
from .table import DataFrameTable


class WriteTable:
    def __init__(self, request_data_object):
        self.times = []  
        self.request = request_data_object
        self.table = DataFrameTable()
        
    def append(self):
        start = self.set_time()
        countries_data = self.request.get_data() 
        for data in countries_data:
            region = data[0]['region'] 
            country = data[0]['name']['common']

            for language in data[0]['languages'].values():
                self.table.append_row(region, country, language)
                end = self.set_time()
                self.times.append((end - start))
        
        
    def write(self):
          
        self.table.append_columns()
        self.df = DataFrame(self.table.table)
        self.df.insert(3,'time',self.times)
        print(self.df)
        
    def calculations(self):
        print(self.df['time'].sum())
        print(self.df['time'].min())
        print(self.df['time'].max())
        print(self.df['time'].mean())
        
    def export_json(self):
        self.df.to_json('./table.json',orient='records',lines=True)
        
    def export_to_sqlite(self):
        
        db_name = './tangelo.db'
        db = sqlite3.connect(db_name)
        self.df.to_sql('table_data',db)
        
    def set_time(self):
        
        return time.time()


