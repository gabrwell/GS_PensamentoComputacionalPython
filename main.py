# Em main.py

from modulos.perfil import Perfil
from modulos.carreira import Carreira
from modulos.analisador import Analisador
from typing import List, Tuple


def carregar_dados_iniciais() -> Tuple[List[Carreira], Tuple[str, ...]]:
    """
    Cria e retorna os dados "mestres" do sistema:
    - Uma lista de Carreiras disponíveis.
    - Uma tupla de Competências-chave que serão avaliadas.
    """
    print("Carregando banco de dados de carreiras...")

    # 1. Definir as competências-chave que o sistema irá avaliar
    # Usamos uma tupla por ser imutável
    COMPETENCIAS_CHAVE = ("logica", "criatividade", "colaboracao", "adaptabilidade", "comunicacao", "lideranca")

    # 2. Criar as instâncias de Carreira
    lista_carreiras = []

    # Carreira 1
    c1 = Carreira(
        "Engenheiro de IA Ética",
        "Desenvolve sistemas de inteligência artificial justos, transparentes e seguros."
    )
    c1.adicionar_requisito("logica", 5)
    c1.adicionar_requisito("adaptabilidade", 4)
    c1.adicionar_requisito("comunicacao", 3)
    lista_carreiras.append(c1)

    # Carreira 2
    c2 = Carreira(
        "Designer de Experiência de Realidade Mista",
        "Cria ambientes imersivos e interativos (VR/AR) para educação e entretenimento."
    )
    c2.adicionar_requisito("criatividade", 5)
    c2.adicionar_requisito("colaboracao", 4)
    c2.adicionar_requisito("logica", 3)
    lista_carreiras.append(c2)

    # Carreira 3
    c3 = Carreira(
        "Gestor de Equipes Híbridas",
        "Lidera e motiva times que operam tanto remotamente quanto presencialmente."
    )
    c3.adicionar_requisito("comunicacao", 5)
    c3.adicionar_requisito("colaboracao", 5)
    c3.adicionar_requisito("lideranca", 4)
    c3.adicionar_requisito("adaptabilidade", 3)
    lista_carreiras.append(c3)

    # Carreira 4
    c4 = Carreira(
        "Analista de Cibersegurança Quântica",
        "Protege sistemas contra ameaças de computadores quânticos."
    )
    c4.adicionar_requisito("logica", 5)
    c4.adicionar_requisito("adaptabilidade", 5)
    c4.adicionar_requisito("criatividade", 2)
    lista_carreiras.append(c4)

    return lista_carreiras, COMPETENCIAS_CHAVE


def coletar_perfil_usuario(competencias_chave: Tuple[str, ...]) -> Perfil:
    """
    Cria a interface (CLI) para coletar os dados do usuário.
    """
    print("\n--- 🚀 Sistema de Orientação de Carreiras do Futuro ---")
    nome = input("Digite seu nome: ").strip()
    if not nome:
        nome = "Usuário Anônimo"

    perfil_usuario = Perfil(nome)

    print(f"\nOlá, {nome}! Vamos analisar seu perfil.")
    print("Por favor, dê uma nota de 1 (baixo) a 5 (alto) para cada competência:")

    for comp in competencias_chave:
        while True:
            try:
                # Trata a entrada do usuário
                nota_str = input(f"  - {comp.capitalize()}: ").strip()
                nota_int = int(nota_str)

                if 1 <= nota_int <= 5:
                    perfil_usuario.adicionar_competencia(comp, nota_int)
                    break  # Sai do loop 'while' e vai para a próxima competência
                else:
                    print("Nota inválida. Por favor, digite um número entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número (ex: 3).")

    return perfil_usuario


def exibir_resultados(perfil: Perfil, recomendacoes: List[Tuple[int, Carreira]]):
    """
    Formata e exibe os resultados da análise para o usuário.
    """
    print(f"\n--- 🌟 Recomendações para {perfil.nome} ---")

    if not recomendacoes:
        print("Não foi possível gerar recomendações com base no seu perfil.")
        return

    for i, (score, carreira) in enumerate(recomendacoes):
        print(f"\n{i + 1}. {carreira.nome} (Compatibilidade: {score} pontos)")
        print(f"   Descrição: {carreira.descricao}")

        # Gerar trilha de aprimoramento (gaps)
        gaps = Analisador.identificar_gaps(perfil, carreira)

        if gaps:
            print("   Trilha de Aprimoramento Sugerida:")
            for comp, diff in gaps:
                print(f"     - {comp.capitalize()}: (Melhorar {diff} ponto(s))")
        else:
            print("   ✅ Parabéns! Você atende a todos os requisitos mínimos desta carreira!")


def main():
    """
    Função principal que orquestra a execução do programa.
    """
    # 1. Preparação: Carregar dados de carreiras e competências
    carreiras_disponiveis, competencias_chave = carregar_dados_iniciais()

    # 2. Entrada: Coletar dados do usuário e criar o Perfil
    perfil_usuario = coletar_perfil_usuario(competencias_chave)

    # 3. Processamento: Chamar o Analisador
    recomendacoes = Analisador.gerar_recomendacoes(perfil_usuario, carreiras_disponiveis)

    # 4. Saída: Exibir os resultados formatados
    exibir_resultados(perfil_usuario, recomendacoes)

    print("\n--- Análise Concluída ---")


if __name__ == "__main__":
    main()