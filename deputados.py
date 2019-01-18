class Deputados:
    
    def __init__(self):
        self.endpoint = "https://dadosabertos.camara.leg.br/api/v2/deputados?"

    def lista(self, tipo = 'json', **kwargs):
        """lista todos os deputados da legislatura atual.

        Parameters
        ----------
        id : `integer`
        Número(s) identificador(es) de um deputado, separados por vírgulas.
        nome : string
        Parte do nome  do parlamentar.
        idLegislatura : integer
        Número(s) identificador(es) de uma ou mais legislatura(s) de que os parlamentares tenham participado, separados por vírgulas.
        siglaUf : string
        Uma ou mais sigla(s) de unidades federativas Se ausente, serão retornados deputados de todos os estados.
        siglaPartido : string
        Uma ou mais sigla(s) de partidos aos quais sejam filiados os deputados. Atenção: partidos diferentes podem usar a mesma sigla em diferentes legislaturas!
        siglaSexo : string
        Letra que designe o gênero dos parlamentares que se deseja buscar, sendo M para masculino e F para feminino
        pagina : integer
        Número da página de resultados, a partir de 1, que se deseja obter com a requisição, contendo o número de itens definido pelo parâmetro itens. Se omitido, assume o valor 1.
        itens : integer
        Número máximo de itens na página que se deseja obter com esta requisição.
        dataInicio : string
        Data de início de um intervalo de tempo, no formato AAAA-MM-DD.
        dataFim : string
        Data de término de um intervalo de tempo, no formato AAAA-MM-DD.
        ordem : string
        O sentido da ordenação: asc para A a Z ou 0 a 9, e desc para Z a A ou 9 a 0. Default ASC
        ordenarPor : string
        Nome do campo pelo qual a lista deve ser ordenada: id, idLegislatura, nome, siglaUF ou siglaPartido Default nome
        """
        import requests

        tipo = tipo
        endpoint = self.endpoint
        parametros = []
        dados = ''

        for parametro in kwargs:
            parametros.append(parametro +"="+kwargs[parametro])

        endpoint_parametros = "&".join(parametros)
        url = endpoint+endpoint_parametros

        r = requests.get(url)
        retorno = r.json()

        if tipo == 'pdf':
            pass
        elif tipo == 'ods':
            pass
        elif tipo == 'odf':
            pass
        else:
            dados = retorno

        return dados

    def detalhes(self, **kwargs):
        pass