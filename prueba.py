# primer commit
import pandas as pd

X = pd.read_csv('../ML_Diabetes/Diabetes-Data/data-01', sep='\t', header=None, names=['Fecha', 'Hora', 'Código', 'Valor'], dtype={'Fecha': str, 'Hora': str})
X.set_index('Fecha', inplace=True)

print(X.head())

