
class DataTransform:
    def __init__(self,data):
        self.data=data
    def add_column(self,nome_coluna,funcao):
        self.data[nome_coluna] = self.data.apply(funcao, axis=1)
        print(f'Nova coluna "{nome_coluna}" adicionada no Dataframe')
        return self.data
    def remove_column(self,nome_coluna):
        self.data.drop(columns=nome_coluna, inplace=True)
        return self.data
    def split_date(self,format,name): 
        match format:
            case 'dd/mm/yyyy':
                print(f'Formato dd/mm/yyyy da coluna "{name}" foi separado em colunas "Ano", "Mes" e "Dia" no Dataframe')
                self.data[['Dia', 'Mes', 'Ano']] = self.data[name].str.split('-', expand=True)
                return self.data
            case 'mm/dd/yyyy':
                print(f'Formato mm/dd/yyyy da coluna "{name}" foi separado em mais colunas "Ano", "Mes" e "Dia" no Dataframe')
                self.data[['Mes', 'Dia', 'Ano']] = self.data[name].str.split('-', expand=True)
                return self.data
            case 'yyyy/mm/dd':
                print(f'Formato yyyy/mm/dd da coluna "{name}" foi separado em mais colunas "Ano", "Mes" e "Dia" no Dataframe')
                self.data[['Ano', 'Mes', 'Dia']] = self.data[name].str.split('-', expand=True)
                return self.data
            case 'yyyy/dd/mm':
                print(f'Formato yyyy/dd/mm da coluna "{name}" foi separado em mais colunas "Ano", "Mes" e "Dia" no Dataframe')
                self.data[['Ano', 'Dia', 'Mes']] = self.data[name].str.split('-', expand=True)
                return self.data
