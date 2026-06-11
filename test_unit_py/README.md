# Uso de IA para geração de cenários de teste

## Função escolhida

`potencia(a, b)`

## Prompt utilizado

```
Crie uma tabela de planejamento de testes para a função abaixo:

def potencia(a, b):
    return a ** b

A tabela deve conter as colunas:
- ID do teste;
- cenário;
- entrada;
- resultado esperado;
- tipo de cenário;
- observação.

teste todos os cenarios desde a utilização de numeros negativos e também de strings. alem disso garanta a exercução me mostrando pelo menos 5 tipos de teste diferentes incluindo os resultados. me mostre observações a respeito dos cenarios criados me mostrando possiveis comportamentos esperados e inesperados

## Tabela de cenários gerada

| ID | Cenário | Entrada | Resultado esperado | Tipo de cenário | Observação |
|-----|------------------------------|----------------------|--------------------:|----------------|-------------------------------------------|
| T01 | Potência com inteiros positivos | `potencia(2, 3)` | `8` | Caso normal | Caso básico |
| T02 | Expoente zero | `potencia(5, 0)` | `1` | Caso de borda | Elemento neutro da potência |
| T03 | Base zero, expoente positivo | `potencia(0, 5)` | `0` | Caso de borda | Verifica comportamento com base zero |
| T04 | Expoente negativo | `potencia(2, -2)` | `0.25` | Caso normal | Resultado é float (inverso) |
| T05 | Base negativa com expoente ímpar | `potencia(-2, 3)` | `-8` | Caso normal | Mantém sinal negativo |
| T06 | Base negativa com expoente par | `potencia(-2, 2)` | `4` | Caso normal | Resultado positivo |
| T07 | Expoente fracionário | `potencia(9, 0.5)` | `3.0` | Caso de borda | Raiz quadrada |
| T08 | Tipo inválido para base | `potencia('a', 2)` | `TypeError` | Caso de erro | Entrada inválida - espera exceção |

## Análise dos cenários

- Aceitei todos os cenários sugeridos pela IA. Acrescentei explicitamente o caso de tipo inválido (T08) como verificação de erro.

## Código final dos testes (trechos adicionados em `test_calculadora.py`)

```
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(10, 2), 100)

    def test_potencia_expoente_negativo(self):
        self.assertAlmostEqual(potencia(2, -2), 0.25)

    def test_potencia_base_negativo_impar(self):
        self.assertEqual(potencia(-2, 3), -8)

    def test_potencia_base_negativo_par(self):
        self.assertEqual(potencia(-2, 2), 4)

    def test_potencia_expoente_fracionario(self):
        self.assertAlmostEqual(potencia(9, 0.5), 3.0)

    def test_potencia_tipo_invalido(self):
        with self.assertRaises(TypeError):
            potencia('a', 2)
```

## Resultado da execução dos testes

Comando executado:

```bash
python -m unittest test_calculadora.py
```

Saída obtida:

```
...........
----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK
```

## Observações finais

- Arquivos atualizados: `calculadora.py`, `test_calculadora.py`.
- Próximo passo sugerido: subir o repositório no GitHub e preencher o link abaixo.

Link do repositório no GitHub: (https://github.com/potaviocarv/unit_test_python)
