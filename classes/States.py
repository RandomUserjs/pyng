import os
import sys
import json
import pygame as pg
from classes.Caminhos import Caminho

class States:
    def salvar_config(self, layout_selecionado):
        caminho = Caminho()
        caminho_config = caminho.obter_caminho_config()
        data = {"keyboard_layout": layout_selecionado}
        try:
            with open(caminho_config, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception:
            # best-effort: try writing plain text
            try:
                with open(caminho_config, 'w', encoding='utf-8') as f:
                    f.write(str(layout_selecionado))
            except Exception:
                pass
    def carregar_config(self):
        caminho = Caminho()
        caminho_config = caminho.obter_caminho_config()
        if not os.path.exists(caminho_config):
            return None
        try:
            with open(caminho_config, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            # fallback: try reading as plain text with a single value
            try:
                with open(caminho_config, 'r', encoding='utf-8') as f:
                    valor = f.read().strip()
                    if valor in ["querty", "colemak"]:
                        return {"keyboard_layout": valor}
            except Exception:
                return None
        return None