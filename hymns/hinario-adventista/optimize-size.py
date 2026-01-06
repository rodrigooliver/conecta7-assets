#!/usr/bin/env python3
"""
Remove campos duplicados para otimizar tamanho do JSON
"""

import json
import os

def optimize_json():
    print("🗜️  Otimizando tamanho do JSON...")
    print("=" * 50)
    
    # Carregar JSON
    with open('hymns-pt.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Informações comuns (mover para metadata)
    common_artist = "Hinário Adventista do 7º Dia"
    common_cover = "https://github.com/moser-jose/Hina7/releases/download/vHinos/capa.png"
    
    # Adicionar ao metadata
    data['metadata']['common'] = {
        'artist': common_artist,
        'cover_art': common_cover,
        'audio_base_url': 'https://github.com/moser-jose/Hina7/releases/download/vHinos/'
    }
    
    # Contar campos antes
    removed_artists = 0
    removed_covers = 0
    removed_audio_urls = 0
    
    # Remover campos duplicados de cada hino
    for hymn in data['hymns']:
        if hymn.get('artist') == common_artist:
            del hymn['artist']
            removed_artists += 1
        
        if hymn.get('cover_art') == common_cover:
            del hymn['cover_art']
            removed_covers += 1
        
        # Otimizar audio_url: remover base URL, manter só o nome do arquivo
        if hymn.get('audio_url'):
            audio_url = hymn['audio_url']
            # Extrair apenas o nome do arquivo
            if 'vHinos/' in audio_url:
                filename = audio_url.split('vHinos/')[-1]
                hymn['audio_file'] = filename
                del hymn['audio_url']
                removed_audio_urls += 1
    
    print(f"✅ Campos removidos:")
    print(f"   - artist: {removed_artists} ocorrências")
    print(f"   - cover_art: {removed_covers} ocorrências")
    print(f"   - audio_url → audio_file: {removed_audio_urls} ocorrências")
    print()
    
    # Salvar versão otimizada
    size_before = os.path.getsize('hymns-pt.json') / 1024 / 1024
    
    with open('hymns-pt.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    with open('hymns-pt.min.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    
    size_after = os.path.getsize('hymns-pt.json') / 1024 / 1024
    size_min = os.path.getsize('hymns-pt.min.json') / 1024 / 1024
    
    print(f"📊 Tamanhos:")
    print(f"   Antes:      {size_before:.2f} MB")
    print(f"   Depois:     {size_after:.2f} MB")
    print(f"   Minificado: {size_min:.2f} MB")
    print()
    
    reduction = ((size_before - size_after) / size_before) * 100
    print(f"💾 Economia: {size_before - size_after:.2f} MB ({reduction:.1f}%)")
    print()
    print("✅ JSON otimizado!")

if __name__ == "__main__":
    optimize_json()

