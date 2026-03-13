#  Função criada utilizando 'def'
def calcular_notas(lista_notas):
    #  Primeira função Built-in nova
    # Ela soma todos os valores de uma lista automaticamente
    total = sum(lista_notas)
 
    #  Segunda função Built-in nova
    # Ela conta quantos itens existem na lista
    quantidade = len(lista_notas)
    
    media = total / quantidade
    return media

# Criando uma lista de notas
minhas_notas = [8.5, 7.0, 9.2, 6.5]

# Chamando a função 
media_final = calcular_notas(minhas_notas)

print(f"Sua média final foi: {media_final:.2f}")

# Estrutura condicional (if else)
if media_final >= 7:
    print("Resultado: Parabéns, você foi aprovado!")
else:
    print("Resultado: Estude um pouco mais para a recuperação.")

