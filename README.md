Módulo python para consumir a API de dados abertos do Congresso Nacional

### Exemplo de uso
```python
from congredata import deputados
l = deputados.Deputados()
l.lista('html',ordem='ASC',ordenarPor='id')
```