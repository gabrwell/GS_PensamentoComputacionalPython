# Em modulos/analisador.py

from modulos.perfil import Perfil
from modulos.carreira import Carreira
from typing import List, Tuple

class Analisador:
    """
    Classe utilitária que contém a lógica para analisar perfis
    e gerar recomendações de carreira.
    """

    @staticmethod
    def calcular_compatibilidade(perfil: Perfil, carreira: Carreira) -> int:
        """
        Calcula uma pontuação de compatibilidade entre um perfil e uma carreira.
        A lógica de pontuação pode ser ajustada conforme necessário.
        """
        pontuacao = 0
        competencias_perfil = perfil.get_competencias()
        requisitos_carreira = carreira.get_requisitos()

        if not requisitos_carreira:
            return 0 # Não há requisitos para comparar

        for competencia, nota_req in requisitos_carreira.items():
            # Pega a nota do perfil, ou 0 se ele não tiver a competência
            nota_perfil = competencias_perfil.get(competencia, 0)

            # Lógica condicional para pontuação
            if nota_perfil >= nota_req:
                pontuacao += 2  # Atende ou supera o requisito
            elif nota_perfil == nota_req - 1:
                pontuacao += 1  # Está próximo
            else:
                pontuacao -= 1  # Longe de atender

        return pontuacao

    @staticmethod
    def gerar_recomendacoes(perfil: Perfil, lista_carreiras: List[Carreira], top_n: int = 3) -> List[Tuple[int, Carreira]]:
        """
        Gera uma lista com as 'top_n' carreiras mais recomendadas.

        Retorna:
            List[Tuple[int, Carreira]]: Uma lista de tuplas, onde cada tupla
                                        contém (pontuação, objeto Carreira).
        """
        pontuacoes = []
        for carreira in lista_carreiras:
            score = Analisador.calcular_compatibilidade(perfil, carreira)
            pontuacoes.append((score, carreira))

        # Ordena a lista de tuplas pela pontuação (primeiro item da tupla),
        # do maior para o menor.
        pontuacoes.sort(key=lambda item: item[0], reverse=True)

        return pontuacoes[:top_n]

    @staticmethod
    def identificar_gaps(perfil: Perfil, carreira: Carreira) -> List[Tuple[str, int]]:
        """
        Identifica as competências que o perfil precisa melhorar
        para uma carreira específica.

        Retorna:
            List[Tuple[str, int]]: Lista de tuplas (competencia, diferenca_necessaria).
        """
        gaps = []
        competencias_perfil = perfil.get_competencias()
        requisitos_carreira = carreira.get_requisitos()

        for competencia, nota_req in requisitos_carreira.items():
            nota_perfil = competencias_perfil.get(competencia, 0)
            if nota_perfil < nota_req:
                diferenca = nota_req - nota_perfil
                gaps.append((competencia, diferenca))

        return gaps