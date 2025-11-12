# Em modulos/carreira.py

class Carreira:
    """
    Representa uma carreira profissional com seus requisitos de competência.
    """
    def __init__(self, nome: str, descricao: str):
        """
        Inicializa uma nova carreira.

        Args:
            nome (str): O nome da carreira (ex: "Engenheiro de IA Ética").
            descricao (str): Uma breve descrição da carreira.
        """
        self.nome = nome
        self.descricao = descricao
        # Armazena os requisitos como: {"logica": 5, "criatividade": 3}
        self.requisitos: dict[str, int] = {}

    def adicionar_requisito(self, competencia: str, nota_minima: int):
        """
        Adiciona ou atualiza a nota mínima de uma competência para esta carreira.

        Args:
            competencia (str): O nome da competência (ex: "logica").
            nota_minima (int): A nota mínima necessária (1 a 5).
        """
        if 1 <= nota_minima <= 5:
            # Garante que a chave seja sempre minúscula para consistência
            self.requisitos[competencia.lower()] = nota_minima
        else:
            print(f"AVISO: Nota mínima inválida ({nota_minima}) para '{competencia}'. Ignorando.")

    def get_requisitos(self) -> dict[str, int]:
        """
        Retorna o dicionário de requisitos da carreira.
        """
        return self.requisitos

    def __str__(self) -> str:
        """Representação textual do objeto Carreira."""
        return f"{self.nome} - Requisitos: {len(self.requisitos)} competências."