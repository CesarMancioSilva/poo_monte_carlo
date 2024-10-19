import pandas as pd

# Classe para carregar os dados
class dataLoader:
    def __init__(self,file_path):
        self.file_path = file_path
        self.data=None
    def load_data_csv(self):
        try:
            self.data=pd.read_csv(self.file_path)
            print(f'Dados de {self.file_path} carregados com sucesso.')
            return self.data
        except Exception as error:
            print(f'Não foi possivel carregar os dados: {error}')
