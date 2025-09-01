def media_recursiva(dados):
    def soma_conta(lst):
        total, qtd = 0, 0
        for item in lst:
            if isinstance(item, list):
                t, q = soma_conta(item)
                total += t
                qtd += q
            else:
                total += item
                qtd += 1
        return total, qtd

    soma, qtd = soma_conta(dados)
    return soma / qtd if qtd > 0 else 0


def ajustar_medias(catalogo, media_alvo):
    notas = [f["avaliacao"] for f in catalogo]
    media_atual = sum(notas) / len(notas)

    if media_atual == 0:
        fator = 1
    else:
        fator = media_alvo / media_atual

    for f in catalogo:
        f["avaliacao"] = round(f["avaliacao"] * fator, 1)

    return catalogo

def exportar_csv(catalogo, arquivo):
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("nome,diretor,avaliacao,data_lancamento,duracao_h,duracao_m,streaming\n")
        for filme in catalogo:
            linha = f"{filme['nome']},{filme['diretor']},{filme['avaliacao']},{filme['data_lancamento']},{filme['duracao'][0]},{filme['duracao'][1]},{filme['streaming']}\n"
            f.write(linha)

def main():
    dados = [[6.3, 2.1, [8.4, 4.2, 5.1], 9.6], 10, 4.7, 6.5]
    media_alvo = media_recursiva(dados)

    print("Média alvo:", media_alvo)

    from etapa2_estatisticas import ler_json
    catalogo = ler_json("catalogo_filmes.json")
    catalogo = ajustar_medias(catalogo, media_alvo)
    exportar_csv(catalogo, "catalogo_filmes_ajustado.csv")
    print("Arquivo CSV gerado com sucesso!")

if __name__ == "__main__":
    main()
