# Teste data

from data import Data

try:
    Calendario = Data(-2, 12, 2023)
except ValueError as e:
    print(f"Erro ao criar a data! {e}")
    Calendario = None

# Exibição do meu calendário
if Calendario is not None:
    print('\n\t\t\t ---- Data ----')
    print(Calendario)
else:
    print('-'* 65)
    print("A data é inválida, não é possível exibir o calendário.")
    print('-' * 65)
