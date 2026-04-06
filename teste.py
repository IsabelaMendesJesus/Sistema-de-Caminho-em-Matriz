import pytest
from trabalho import fromCodeToMap, calculaCusto

# teste de conversão do codigo para matriz
def test_fromCodeToMap_basico():
    codigo = "0 0 5; 0 1 3; 1 0 2;"
    mapa = fromCodeToMap(codigo)

    assert mapa[0][0] == 5
    assert mapa[0][1] == 3
    assert mapa[1][0] == 2


# teste de cenários para calculo de custo
@pytest.mark.parametrize("matriz,caminho,esperado", [
    ([[1,1],[1,1]], [0,1], 3),
    ([[2,2],[2,2]], [0,1], 6),
    ([[1,2],[3,4]], [0,1], 7)
])
def test_calculaCusto_varios_casos(matriz, caminho, esperado):
    resultado = calculaCusto(matriz, caminho)
    assert resultado == esperado


# teste caminho vazio
def test_caminho_vazio():
    matriz = [[5]]
    caminho = []

    assert calculaCusto(matriz, caminho) == 5