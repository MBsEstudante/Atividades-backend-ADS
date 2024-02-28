from datetime import datetime
import pytz

# Definindo o fuso horário para o Brasil
fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')

# Obtendo a data e o horário atual com o fuso horário do Brasil
data_hora_atual_brasil = datetime.now(fuso_horario_brasil)

# Formatando a data e o horário para exibição
formato = "%d/%m/%Y %H:%M:%S"  # Formato de data e hora
data_hora_formatada = data_hora_atual_brasil.strftime(formato)

# Mostrando a data e o horário atual do Brasil
print("Data e hora atual no Brasil:", data_hora_formatada)
