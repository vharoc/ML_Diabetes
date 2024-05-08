# primer commit
import pandas as pd

X_train = pd.read_csv('../ML_Diabetes/Diabetes-Data/data-01', sep='\t', header=None, names=['Fecha', 'Hora', 'Código', 'Valor'], dtype={'Fecha': str, 'Hora': str})
X_test = pd.read_csv('../ML_Diabetes/Diabetes-Data/data-02', sep='\t', header=None, names=['Fecha', 'Hora', 'Código', 'Valor'], dtype={'Fecha': str, 'Hora': str})

X_train.set_index('Fecha', inplace=True)
X_test.set_index('Fecha', inplace=True)

print(X_train.head())
print()
print(X_test.head())

