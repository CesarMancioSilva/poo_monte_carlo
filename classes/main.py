import pandas as pd

from classes.dataLoader import dataLoader
from classes.dataCleaner import dataCleaner
from classes.dataTransform import DataTransform

def extract_data(file_path):
    data = dataLoader(file_path).load_data_csv()
    cleaner = dataCleaner(data)
    cleaner.remove_na()
    cleaner.remove_duplicated()
    data_cleaned =cleaner.data
    return data_cleaned

def transform_data(data,type,**kwargs):
    transformState = DataTransform(data)
    match type:
        case 'add_column':
            data_transformed = transformState.add_column(kwargs['name'],kwargs['function'])
            return data_transformed
        case 'remove_column':
            data_transformed = transformState.remove_column(kwargs['name'])
            return data_transformed
        case 'split_date':
            data_transformed = transformState.split_date(kwargs['format'],kwargs['name'])
            return data_transformed



def visualize_data(data,type,**kwargs):
    match type:
        case 'bar': print()
        case 'hist': print()
        case 'setor': print()