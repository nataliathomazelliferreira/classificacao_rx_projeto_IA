from PIL import Image
import os

pasta = r"C:\Users\natal\.vscode"
arquivos = []
for nome in os.listdir(pasta):
    if nome.startswith("rx_torax") or nome.startswith("rx_bacia"):
        classe = "Torax" if nome.startswith("rx_torax") else "Bacia"
        arquivos.append({"arquivo": nome, "classe": classe})

if not arquivos:
    print("Nenhum arquivo encontrado na pasta.")
    exit()

def analisar_imagem(nome_arquivo, limiar=128):
    """
    Abre a imagem, converte para escala de cinza e conta
    quantos pixels são claros e quantos são escuros.
    """
    img = Image.open(nome_arquivo).convert("L")  # escala de cinza
    pixels = list(img.getdata())
    total = len(pixels)

    brancos = sum(1 for p in pixels if p >= limiar)
    pretos = total - brancos

    perc_brancos = (brancos / total) * 100
    perc_pretos = (pretos / total) * 100

    return brancos, pretos, perc_brancos, perc_pretos

print("Gerando tabela de pixels...\n")

with open("tabela_pixels_rx.csv", "w", encoding="utf-8") as f:
    f.write("arquivo;classe;brancos;pretos;perc_brancos;perc_pretos\n")

    print(f"{'ARQUIVO':<25} | {'CLASSE':<6} | {'% BRANCOS':<10} | {'% PRETOS':<9}")
    print("-" * 70)

    for item in arquivos:
        nome = item["arquivo"]
        classe = item["classe"]

        caminho_completo = os.path.join(pasta, nome)

        if not os.path.exists(caminho_completo):
            print(f"ARQUIVO NÃO ENCONTRADO: {nome}")
            continue

        br, pr, pb, pp = analisar_imagem(caminho_completo)

        print(f"{nome:<25} | {classe:<6} | {pb:>9.2f}% | {pp:>8.2f}%")

        linha = f"{nome};{classe};{br};{pr};{pb:.2f};{pp:.2f}\n"
        f.write(linha)

print("\nTabela salva em: tabela_pixels_rx.csv")
print("Use esses valores no seu código de classificação / descida da colina.")