# 1 - imports - bibliotecas trazer de fora
import pytest


# 2 - class   - classe conjunto de funionalidade
# 3 - definitions - definiçoes = metodo  criar ou testar
def print_hi(name):
    print(f'hi,{name}')


def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return 'Não dividiras por zero'


def dividir_try_except(numero1, numero2):
    try:
        return numero1 / numero2
    except TypeError:
    # return 'Não dividiras por zero'
        return TypeError



# Testes Unitarios / Testes de Unidades

# Teste da Função somar
def test_somar():
    # 1 -parte Configura / Prepara

    numero1 = 8  # input
    numero2 = 5  # input
    resultado_esperado = 13  # output

    # 2 - Executa

    resultado_atual = somar(numero1, numero2)

    # 3 - Check / Valida

    assert resultado_atual == resultado_esperado


class Val:
    pass


@pytest.mark.parametrize('numero1,numero2,resultado', [
    # valores
    (5, 4, 9),  # teste 1
    (3, 2, 5),  # teste 2
    (10, 6, 15),  # teste 3
])
def test_somar(numero1, numero2, resultado):
    try:
        assert somar(numero1, numero2) == resultado
    except AssertionError:
        print(f'Entrou no except: {AssertionError}')
        pass


def test_somar_resultado_negativo():
    assert somar(-1000, -2000) == -3000


# Teste funçao Subtrair
def test_subtrair():
    assert subtrair(5, 1)


def test_subtrair():
    assert subtrair(4, 2) == 2


def test_multipilicar():
    assert multiplicar(1, 1)


def test_multiplicar():
    assert multiplicar(2, 7) == 21


def test_dividir():
    assert dividir(8, 4) == 2


def test_dividir_por_zero():
    assert dividir(8, 0) == 'Não dividiras por zero'


def test_dividir_try_except_por_zero():
    assert dividir_try_except(8, 0) == 'Não dividiras por zero'


@pytest.mark.parametrize('numero1, numero2,resultado', [
    (8, 2, 4),
    (20, 4, 5),
    (10, 0, 'Não dividiras por zero')
])
def test_dividir_try_except(numero1, numero2, resultado):
    assert dividir_try_except(numero1, numero2) == resultado


# TESTE POSITIVO--> MOSTRAR O RESULTADO CORRETO
#               --> AVANÇAR PARA PROXIMA ETAPA

# TESTE NAGATIVO--> MOSTRAR A MENSAGAGEM DE ERRO
#


if __name__ == '__main__':
    print_hi('mario')

# soma  de 2 numeros
resultado = somar(4, 2)
print(f'o resultado da soma: {resultado}')

# subtração de 2 numeros
resultado = subtrair(5, 3)
print(f'o resultado da subtração:{resultado}')

# multiplicção
resultado = multiplicar(2, 4)
print(f'o resultado da multiplicação:{resultado}')

# divisao
resultado = dividir(9, 8)

print(f'o resultado da divisao:{resultado}')

#
