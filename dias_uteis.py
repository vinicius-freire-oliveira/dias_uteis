from datetime import datetime, timedelta

def calcular_data_final(data_inicio, numero_dias_uteis):
    # Verificar se a data de início está no formato correto
    try:
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
    except ValueError:
        return "Formato de data inválido. Use AAAA-MM-DD."
    
    # Contador de dias úteis
    dias_uteis_contados = 0
    data_atual = data_inicio
    
    while dias_uteis_contados < numero_dias_uteis:
        data_atual += timedelta(days=1)
        # Verificar se o dia atual é um dia útil (não é fim de semana)
        if data_atual.weekday() < 5:
            dias_uteis_contados += 1
    
    return data_atual.strftime('%Y-%m-%d')

# Exemplo de uso
data_inicio = input("Digite a data de início (AAAA-MM-DD): ")
numero_dias_uteis = int(input("Digite o número de dias úteis: "))

data_final = calcular_data_final(data_inicio, numero_dias_uteis)
print(f"Data final após {numero_dias_uteis} dias úteis a partir de {data_inicio}: {data_final}")
