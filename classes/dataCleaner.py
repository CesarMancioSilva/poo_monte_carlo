class dataCleaner:
    def __init__(self,data):
        self.data = data
    def remove_na(self):
        try:
            self.data = self.data.dropna()
            print('Valores nulos (NA) removidos do Dataframe')
            return self.data
        except Exception as error:
            print(f'Erro para remover NA: {error}')
    
    def remove_duplicated(self):
        try:
            self.data = self.data.drop_duplicates()
            print('Valores duplicados removidos do Dataframe')
            return self.data
        except Exception as error:
            print(f"Erro na remoção de duplicadas: {error}")