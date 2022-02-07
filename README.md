# ConvB-UFSC
Códigos referentes à disciplina de conversão B

Nesse repositório se encontra uma função que cácula os parâmetros do circuito equivalente para um motor de indução trifásico a partir dos resultados dos ensaios em vazio e de rotor travado. Os detalhes do cálculo são discutivos no documento pdf.

## Requisitos
É preciso possuir _python 3_ instalado na sua máquina, bem como as bibliotecas:
- numpy;
- cmath e
- scipy.

## Como utilizar

Inicialmente, é necessário realizar o download do arquivo, bem como de suas dependências. Uma vez baixado o arquivo "ensaios_motor.py", basta criar um arquivo .py no mesmo diretório e importar a função:

```
from ensaios_motor import ensaios
```

A função calcula os parâmetros do circuito equivalente para um motor de indução trifásico e retorna os parâmetros R, X, rf e xm, bem como os imprime na linha de comando.
Rt são os valores do ensaio com rotor travado, em que Rt = [Tensão de linha, Corrente de linha, Potência trifásica};
Vz são os valores do ensaio em vazio, em que Vz = [Tensão de linha, Corrente de linha, Potência trifásica];
Pr são os valores de potência em função da tensão de alimentação, em que Pr = [[V0, V1, V2, ...], [P0, P1, P2, ...]].
