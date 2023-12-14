# Classe

class Data(object):
    # Construtor
    def __init__(self, dia, mes, ano):
        self._valida_data(dia, mes, ano)
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Encapsulamento
    def setDia(self, dia):
        self._valida_data(dia,self._mes, self._ano)
        self.dia = dia

    def getDia(self):
        return self.dia

    def setMes(self, mes):
        self._valida_data(self._dia, mes, self._ano)
        self.mes = mes

    def getMes(self):
        return self.mes

    def setAno(self, ano):
        self._valida_data(self._dia, self._mes, ano)
        self.ano = ano

    def getAno(self):
        return self.ano

    def __str__(self):
        return (
            '\n Dia: ' + str(self.getDia())+
            '\n Mes: ' + str(self.getMes())+
            '\n Ano: ' + str(self.getAno())
        )
    def _valida_data(self, dia, mes, ano):
        if not (1 <= mes <= 12):
            raise ValueError('Data inválida, mês deve estar entre 1 e 12')

        dias_no_mes = {
            1: 31, 2: 29 if self.ano_bissexto(ano) else 28,
            3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31,
            11: 30, 12: 31
        }

        if not (1 <= dia <= dias_no_mes[mes]):
            raise ValueError(f"Dia: deve estar entre 1 e {dias_no_mes[mes]} para o mês {mes}")

    def ano_bissexto(self, ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)