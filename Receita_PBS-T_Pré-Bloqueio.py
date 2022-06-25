print('Cálculadora de reagentes para PBS-T 0,3% e Pré-Bloqueio')

pbst = float(input('Quanto de PBS-T 0,3% Você precisa?(Em Ml)\n'))

pre_bloqueio = float(input('Quanto de pré bloqueio você precisa?(Em Ml)\n'))


def pbst0():
    print('Você vai precisar dessa quantidade de triton-X em microlitros')
    print(float(((3 * pbst) / 1000) * 1000))
pbst0()

def prebloqueio():
    print('Você vai precisar dessa quantidade de BSA em miligramas')
    print(float((0.1 * pre_bloqueio) / 10) * 1000)
prebloqueio()

Crédito = input('Feito por Lucas Vicente')