
class Perfil:
    """
    Representa o perfil de um usuário e suas competências avaliadas.
    """
    def __init__(self, nome: str):
        """
        Inicializa um novo perfil de usuário.

        Args:
            nome (str): O nome do usuário.
        """
        self.nome = nome
        self.competencias: dict[str, int] = {}

    def adicionar_competencia(self, competencia: str, nota: int):
        """
        Adiciona ou atualiza a nota de uma competência do usuário.

        Args:
            competencia (str): O nome da competência (ex: "logica").
            nota (int): A nota que o usuário se atribuiu (1 a 5).
        """
        if 1 <= nota <= 5:
            self.competencias[competencia.lower()] = nota
        else:
            print(f"AVISO: Nota inválida ({nota}) para '{competencia}'. Ignorando.")

    def get_competencias(self) -> dict[str, int]:
        """
        Retorna o dicionário de competências do usuário.
        """
        return self.competencias

    def __str__(self) -> str:
        """Representação textual do objeto Perfil."""
        return f"Perfil de {self.nome} ({len(self.competencias)} competências avaliadas)"