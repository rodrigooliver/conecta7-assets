#!/usr/bin/env python3
"""
Converte o hinário para formato internacional com chaves em inglês
"""

import json
from datetime import datetime

def convert_hymn(hino):
    """Converte um hino para formato internacional"""
    converted = {
        "id": hino["id"],
        "number": hino["numero"],
        "number_display": hino["numero_view"],
        "title": hino["title"],
        "title_en": hino.get("ingles"),
        "category": hino["categoria"],
        "subcategory": hino["sub_categoria"],
        "authors": [
            {
                "name": autor["nome"]
            }
            for autor in hino.get("autores", [])
            if autor.get("nome")
        ],
        "scripture_reference": hino.get("texto_biblico"),
        "audio_url": hino.get("url"),
        "cover_art": hino.get("artwork"),
        "artist": hino.get("artist", "Hinário Adventista do 7º Dia"),
        "verses": [
            {
                "number": estrofe["numero"],
                "lyrics": estrofe["estrofe"]
            }
            for estrofe in hino.get("estrofes", [])
        ],
        "chorus": None
    }
    
    # Adicionar coro se existir
    coros = hino.get("coro", [])
    if coros and coros[0].get("coro"):
        converted["chorus"] = {
            "label": coros[0].get("nome_coro"),
            "lyrics": coros[0]["coro"]
        }
    
    return converted

def convert_category(categoria):
    """Converte categoria para formato internacional"""
    return {
        "id": categoria["id"],
        "name": categoria["categoria"],
        "background": categoria.get("background"),
        "subcategories": [
            {
                "name": sub["title"],
                "hymns_range": sub["hinos"]
            }
            for sub in categoria.get("sub_categorias", [])
        ]
    }

def main():
    print("🌍 Convertendo para formato internacional...")
    
    # Carregar JSON original
    with open('hymns-original.json', 'r', encoding='utf-8') as f:
        original = json.load(f)
    
    # Criar estrutura internacional
    international = {
        "metadata": {
            "id": "adventist-hymnal-pt-br",
            "title": "Hinário Adventista do Sétimo Dia",
            "language": "pt-BR",
            "edition": "2023",
            "total_hymns": len(original["hinos"]),
            "version": original.get("versao"),
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "source": {
                "author": original.get("autor"),
                "github": original.get("github"),
                "url": original.get("url"),
                "original_update": original.get("ultima_atualizacao")
            }
        },
        "categories": [
            convert_category(cat) 
            for cat in original.get("categorias", [])
        ],
        "hymns": [
            convert_hymn(hino) 
            for hino in original["hinos"]
        ]
    }
    
    # Salvar arquivo internacionalizado
    with open('hymns-international.json', 'w', encoding='utf-8') as f:
        json.dump(international, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Arquivo criado: hymns-international.json")
    print(f"📊 Total de hinos: {len(international['hymns'])}")
    print(f"📂 Total de categorias: {len(international['categories'])}")
    
    # Criar arquivo compacto (sem espaços)
    with open('hymns-international.min.json', 'w', encoding='utf-8') as f:
        json.dump(international, f, ensure_ascii=False, separators=(',', ':'))
    
    print(f"✅ Arquivo compacto criado: hymns-international.min.json")
    
    # Comparar tamanhos
    import os
    size_original = os.path.getsize('hymns-original.json') / 1024 / 1024
    size_intl = os.path.getsize('hymns-international.json') / 1024 / 1024
    size_min = os.path.getsize('hymns-international.min.json') / 1024 / 1024
    
    print(f"\n📊 Tamanhos:")
    print(f"  Original:       {size_original:.2f} MB")
    print(f"  Internacional:  {size_intl:.2f} MB")
    print(f"  Minificado:     {size_min:.2f} MB")

if __name__ == "__main__":
    main()

