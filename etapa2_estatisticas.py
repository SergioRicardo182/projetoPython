def ler_json(arquivo):
    
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read().strip()[1:-1]
    blocos = [b.strip().lstrip("{").rstrip("}").strip() for b in conteudo.split("},")]
    
    filmes = []
    for bloco in blocos:
        if not bloco: continue
        filme = {}
        for linha in bloco.split("\n"):
            if not linha.strip(): continue
            chave, valor = linha.strip().split(":", 1)
            chave = chave.replace('"', "").strip()
            valor = valor.strip().rstrip(",")
            if valor.startswith('"'): valor = valor.strip('"')
            elif valor in ["true", "false"]: valor = valor == "true"
            elif valor.startswith("["): 
                h, m = valor[1:-1].split(",")
                valor = (int(h), int(m))
            else: valor = float(valor) if "." in valor else int(valor)
            filme[chave] = valor
        filmes.append(filme)
    return filmes


media = lambda lst: sum(lst)/len(lst) if lst else 0

def mediana(lst):
    s = sorted(lst); n = len(s); m = n//2
    return (s[m-1]+s[m])/2 if n%2==0 else s[m]

def filmes_acima_de(catalogo, nota=6.0):
    return [f["nome"] for f in catalogo if f["avaliacao"] > nota]

filmes_em_streaming = lambda c: [f["nome"] for f in c if f["streaming"]]

def filme_maior_menor_duracao(c):
    minutos = lambda d: d[0]*60+d[1]
    return max(c, key=lambda f: minutos(f["duracao"])), min(c, key=lambda f: minutos(f["duracao"]))

def moda_diretores(c):
    contagem = {}
    for f in c: contagem[f["diretor"]] = contagem.get(f["diretor"],0)+1
    return max(contagem, key=contagem.get)

def main():
    catalogo = ler_json("catalogo_filmes.json")
    notas = [f["avaliacao"] for f in catalogo]

    print("Média:", media(notas))
    print("Mediana:", mediana(notas))
    print("Filmes > 6:", filmes_acima_de(catalogo))
    print("Em streaming:", filmes_em_streaming(catalogo))

    maior, menor = filme_maior_menor_duracao(catalogo)
    print("Mais longo:", maior["nome"], maior["duracao"])
    print("Mais curto:", menor["nome"], menor["duracao"])

    print("Diretor mais comum:", moda_diretores(catalogo))


if __name__ == "__main__":
    main()
