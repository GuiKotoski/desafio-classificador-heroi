# 1. Entrada de Dados
nome_heroi = str(input("Digite o nome do herói: "))

# Laço de repetição para garantir que o XP seja um número válido
while True:
    entrada_xp = input("Digite o xp do herói: ")
    
    # Validação sem exception: .isdigit() verifica se o texto só tem números
    if entrada_xp.isdigit():
        xp_heroi = int(entrada_xp) # Agora que temos certeza, convertemos com segurança
        break # Sai do laço de repetição
    else:
        print("Erro! Por favor, digite apenas números inteiros para o XP.")

# 2. Estrutura de Decisão para definir o nível
if xp_heroi < 1000:
    nivel = "Ferro"
elif xp_heroi <= 2000:
    nivel = "Bronze"
elif xp_heroi <= 5000:
    nivel = "Prata"
elif xp_heroi <= 7000:
    nivel = "Ouro"
elif xp_heroi <= 8000:
    nivel = "Platina"
elif xp_heroi <= 9000:
    nivel = "Ascendente"
elif xp_heroi <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# 3. Saída formatada
print(f"\nO Herói de nome **{nome_heroi}** está no nível de **{nivel}**")