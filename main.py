#1 - Imports / bibliotecas
import pytest

#2 - class / classes

#3 - definitions - definicoes = metodos e funcoes
def somar(numero1, numero2):
    return numero1+numero2

def subtrair(numero1, numero2):
    return numero1-numero2

def multiplicar(numero1, numero2):
    return numero1*numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1/numero2
    else:
        return 'Nao e possivel dividir por zero.'

def dividir_try_except(numero1, numero2):
    try:
        return numero1/numero2
    except TypeError:
        if TypeError == ZeroDivisionError:
            return 'Nao e possivel dividir por zero.'
        elif TypeError == ArithmeticError:
            return 'Erro no calculo.'
        elif TypeError == ValueError:
            return 'Erro no valor.'
        else:
            return 'Erro desconhecido.'

# Testes
# Teste da funcao somar Longo
def test_somar():
    # 1- Configura / prepara
    numero1 = 8 #input / entrada
    numero2 = 5 #input / entrada
    resultado_esperado = 13 #output / saida

    # 2 - Executar
    resultado_atual = somar(numero1, numero2)

    # 3 - Check / Valida
    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('numero1,numero2,resultado',[
    (5,4,9), #teste 1
    (1,5,6), #teste 2
    (10,20,30), #teste 3
])# Teste da funcao somar Curto
def test_somar_compacto(numero1, numero2, resultado):
    assert somar(numero1, numero2) == resultado

def test_subtrair():
    assert subtrair(10, 5) == 5

def test_multiplicar():
    assert multiplicar(3, 4) == 12

# teste exemplo de divisao, nao é utilizado de forma geral
def test_dividir():
    assert dividir(8,4) == 2

#teste varios erros
@pytest.mark.parametrize('numero1, numero2, resultado',[
    (9,3,3),
    (8,4,2),
    (10,0,'Nao e possivel dividir por zero.'),
])
def test_dividir_try_exception(numero1,numero2,resultado):
    assert dividir_try_except(numero1, numero2) == resultado



    #teste positivo     mostra o resultado correto
    #                   avancar para a proxima etapa

    #teste negativo     mostrar a mensagem de erro

#--------------------------------------------------------------------------
# Dia 1: 100 Testes: 0 passaram
# Dia 2: 100 Testes: 5 passaram
# Dia 3: 100 Testes: 15 passaram
# Dia 4: 100 Testes: 30 passaram

# TDD - Desenvolvimento direcionado pelo teste
# Cria os esqueletos de classes, funcoes e metodos logo no inicio da Sprint
# Criar pelo menos 1 teste (feliz) para todas as funcoes e metodos
# Executar todos os testes unitarios diariamente para medir o progresso

if __name__ == '__main__':
    print(f'A somado de dois números é: {somar(1,2)}')
    print(f'A subtracao de dois números é: {subtrair(9, 5)}')
    print(f'A multiplicacao de dois números é: {multiplicar(5, 2)}')
    print(f'A divisao de dois números é: {dividir(15, 9)}')
    print(f'A divisao de dois números é: {dividir(5, 0)}')
