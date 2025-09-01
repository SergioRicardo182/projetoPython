def obter_filme():

    nome = input("Digite o nome do filme: ").strip()
    while not nome:
        nome = input("Nome não pode ser vazio. Digite o nome do filme: ").strip()

    diretor = input("Digite o nome do diretor: ").strip()
    while not diretor:
        diretor = input("Diretor não pode ser vazio. Digite o nome do diretor: ").strip()

    while True:
        avaliacao = input("Digite a avaliação do filme (0 a 10): ").strip()
        if avaliacao.replace(".", "", 1).isdigit():
            avaliacao = float(avaliacao)
            if 0 <= avaliacao <= 10:
                break
        print("Avaliação inválida. Digite um número entre 0 e 10.")

    while True:
        data = input("Digite a data de lançamento (dd/mm/aaaa): ").strip()
        partes = data.split("/")
        if len(partes) == 3 and all(p.isdigit() for p in partes):
            dia, mes, ano = partes
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and len(ano) == 4:
                break
        print("Data inválida! Use o formato dd/mm/aaaa.")

    while True:
        horas = input("Digite a duração em horas: ").strip()
        minutos = input("Digite os minutos: ").strip()
        if horas.isdigit() and minutos.isdigit():
            horas, minutos = int(horas), int(minutos)
            if horas >= 0 and 0 <= minutos < 60:
                duracao = (horas, minutos)
                break
        print("Duração inválida.")

    while True:
        streaming = input("Está disponível em serviços de streaming? (s/n): ").strip().lower()
        if streaming in ["s", "n"]:
            streaming = True if streaming == "s" else False
            break
        print("Digite apenas 's' ou 'n'.")

    return {
        "nome": nome,
        "diretor": diretor,
        "avaliacao": avaliacao,
        "data_lancamento": data,
        "duracao": duracao,
        "streaming": streaming
    }


def exportar_json(lista, arquivo):
    """Gera um JSON manualmente (sem usar biblioteca)"""
    conteudo = "[\n"
    for i, filme in enumerate(lista):
        conteudo += "  {\n"
        conteudo += f'    "nome": "{filme["nome"]}",\n'
        conteudo += f'    "diretor": "{filme["diretor"]}",\n'
        conteudo += f'    "avaliacao": {filme["avaliacao"]},\n'
        conteudo += f'    "data_lancamento": "{filme["data_lancamento"]}",\n'
        conteudo += f'    "duracao": [{filme["duracao"][0]}, {filme["duracao"][1]}],\n'
        conteudo += f'    "streaming": {"true" if filme["streaming"] else "false"}\n'
        conteudo += "  }"
        if i < len(lista) - 1:
            conteudo += ","
        conteudo += "\n"
    conteudo += "]"

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)


def main():
    catalogo = []
    print("=== Cadastro de Filmes ===")

    while True:
        filme = obter_filme()
        catalogo.append(filme)

        continuar = input("Deseja cadastrar outro filme? (s/n): ").strip().lower()
        if continuar != "s":
            break

    exportar_json(catalogo, "catalogo_filmes.json")
    print("Catálogo salvo em 'catalogo_filmes.json'")


if __name__ == "__main__":
    main()
