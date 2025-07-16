import json
import os

CAMINHO_ARQUIVO = "chamados.json"

def carregar_chamados():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r") as f:
        return json.load(f)

def salvar_chamados(chamados):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(chamados, f, indent=4)

def gerar_id(chamados):
    if not chamados:
        return 1
    return max(c["id"] for c in chamados) + 1
