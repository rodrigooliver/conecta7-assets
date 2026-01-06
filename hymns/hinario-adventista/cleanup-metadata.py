#!/usr/bin/env python3
"""
Remove campos desnecessários do metadata
"""

import json

def cleanup_json():
    print("🧹 Limpando metadata...")
    
    # Carregar JSON
    with open('hymns-international.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Remover campos do metadata
    if 'metadata' in data:
        old_metadata = data['metadata'].copy()
        
        # Manter apenas campos essenciais
        data['metadata'] = {
            'id': old_metadata['id'],
            'title': old_metadata['title'],
            'language': old_metadata['language'],
            'edition': old_metadata['edition'],
            'total_hymns': old_metadata['total_hymns']
        }
    
    # Salvar versão normal
    with open('hymns-international.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Salvar versão minificada
    with open('hymns-international.min.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    
    print("✅ Campos removidos:")
    print("  - metadata.version")
    print("  - metadata.last_updated")
    print("  - metadata.source")
    
    # Comparar tamanhos
    import os
    size_normal = os.path.getsize('hymns-international.json') / 1024 / 1024
    size_min = os.path.getsize('hymns-international.min.json') / 1024 / 1024
    
    print(f"\n📊 Tamanhos finais:")
    print(f"  Normal:     {size_normal:.2f} MB")
    print(f"  Minificado: {size_min:.2f} MB")
    
    print("\n✅ Arquivos atualizados!")

if __name__ == "__main__":
    cleanup_json()

