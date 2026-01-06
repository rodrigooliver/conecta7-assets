#!/usr/bin/env python3
"""
Script para processar o hinário e baixar MP3s
"""

import json
import urllib.request
import os
import time

def load_original_json():
    """Carrega o JSON original do hinário"""
    with open('hymns-original.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def download_mp3(url, filename):
    """Baixa um MP3"""
    try:
        print(f"  Baixando: {filename}...")
        urllib.request.urlretrieve(url, filename)
        return True
    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return False

def download_hymns_mp3s(start=1, end=10):
    """Baixa MP3s dos hinos"""
    data = load_original_json()
    hinos = data['hinos']
    
    os.makedirs('audio/pt', exist_ok=True)
    
    success = 0
    failed = 0
    
    for hino in hinos:
        num = hino['numero']
        if start <= num <= end:
            mp3_url = hino['url']
            filename = f"audio/pt/{hino['numero_view']}.mp3"
            
            if os.path.exists(filename):
                print(f"[{num}] Já existe: {hino['title']}")
                success += 1
                continue
            
            print(f"[{num}] {hino['title']}")
            
            if download_mp3(mp3_url, filename):
                success += 1
            else:
                failed += 1
            
            time.sleep(0.5)  # Pausa entre downloads
    
    print(f"\n✅ Sucesso: {success}")
    print(f"❌ Falhas: {failed}")

def create_conecta7_format():
    """Cria o JSON no formato do Conecta7 usando o original como fonte"""
    print("📝 Criando formato Conecta7...")
    
    data = load_original_json()
    
    # Mantém o arquivo original como referência
    # O app pode usar diretamente ou adaptar conforme necessário
    print(f"✅ Total de hinos disponíveis: {len(data['hinos'])}")
    print(f"✅ Arquivo original preservado em: hymns-original.json")

if __name__ == "__main__":
    import sys
    
    print("🎵 Processador do Hinário Adventista")
    print("=" * 50)
    print()
    
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python3 process-hymns.py test      # Baixa 10 primeiros")
        print("  python3 process-hymns.py 1 50      # Baixa hinos 1-50")
        print("  python3 process-hymns.py all       # Baixa todos (610)")
        print("  python3 process-hymns.py format    # Só processa formato")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "test":
        download_hymns_mp3s(1, 10)
    elif cmd == "all":
        print("⚠️  Isso vai baixar 610 MP3s (~1-2 GB)!")
        resp = input("Confirmar? (s/n): ")
        if resp.lower() == 's':
            download_hymns_mp3s(1, 610)
    elif cmd == "format":
        create_conecta7_format()
    elif len(sys.argv) == 3:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        download_hymns_mp3s(start, end)
    
    print("\n✅ Concluído!")

