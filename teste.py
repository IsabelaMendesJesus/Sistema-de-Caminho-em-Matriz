import pytest
from trabalho import fromCodeToMap, calculaCusto

# 🔹 Teste 1 — conversão de código para matriz
def test_fromCodeToMap_basico():
    codigo = "0 0 5; 0 1 3; 1 0 2;"
    mapa = fromCodeToMap(codigo)

    assert mapa[0][0] == 5
    assert mapa[0][1] == 3
    assert mapa[1][0] == 2


# 🔹 Teste 2 — vários cenários para cálculo de custo
@pytest.mark.parametrize("matriz,caminho,esperado", [
    ([[1,1],[1,1]], [0,1], 3),
    ([[2,2],[2,2]], [0,1], 6),
    ([[1,2],[3,4]], [0,1], 7)
])
def test_calculaCusto_varios_casos(matriz, caminho, esperado):
    resultado = calculaCusto(matriz, caminho)
    assert resultado == esperado