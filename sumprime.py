import sympy
import sys
import random
from multiprocessing import Pool
import time

# Aumentando o limite de recursão para números grandes
sys.setrecursionlimit(10000)

# Função para gerar primos grandes aleatórios com n dígitos
def gerar_primos_aleatorios(digitos, limite_inferior=None, limite_superior=None):
    # Definir os limites de acordo com o número de dígitos
    limite_inferior = 10**(digitos - 1) if limite_inferior is None else limite_inferior
    limite_superior = 10**digitos if limite_superior is None else limite_superior
    
    # Gerar um número aleatório dentro do intervalo
    candidato = random.randint(limite_inferior, limite_superior)
    while True:
        # Encontrar o próximo primo maior ou igual ao candidato
        candidato = sympy.nextprime(candidato)
        if candidato >= limite_superior:
            break
        yield candidato

# Função para encontrar pares de primos P e Q que satisfaçam P + Q + 1 = P'
def verificar_par(p, q):
    p_mais_q_mais_1 = p + q + 1
    if sympy.isprime(p_mais_q_mais_1):
        return (p, q, p_mais_q_mais_1)
    return None

def encontrar_primos(digitos=1000, limite=1):
    contador = 0
    resultado = []
    
    # Usando multiprocessing para gerar primos e verificar a condição em paralelo
    with Pool() as pool:
        # Gerar primos P e Q em paralelo
        primos_p = gerar_primos_aleatorios(digitos)
        primos_q = gerar_primos_aleatorios(digitos)
        
        # Verificar as condições para pares de primos
        for p, q in zip(primos_p, primos_q):
            resultado_par = pool.apply(verificar_par, args=(p, q))
            if resultado_par:
                resultado.append(resultado_par)
                contador += 1
                if contador >= limite:
                    break
    
    # Exibir os resultados encontrados
    for r in resultado:
        print(f'Encontrado: P = {r[0]}, Q = {r[1]}, P\' = {r[2]}')
    print(f'Encontrei {contador} pares de primos.')

# Exemplo de execução
start_time = time.time()
encontrar_primos(digitos=1000, limite=1)
end_time = time.time()

print(f"Tempo total: {end_time - start_time:.2f} segundos")
