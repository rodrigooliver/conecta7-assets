#!/bin/bash

# Script para baixar MP3s do Hinário Adventista
# Fonte: https://github.com/moser-jose/Hina7

echo "🎵 Download de MP3s do Hinário Adventista"
echo "=========================================="
echo ""

# Criar pasta de áudio se não existir
mkdir -p audio/pt

# Contador
TOTAL=610
CURRENT=0

# Função para baixar um hino
download_hymn() {
    local num=$1
    local padded=$(printf "%03d" $num)
    
    # URL do MP3 (seguindo o padrão do repositório original)
    # Você precisará ajustar o nome do arquivo baseado no JSON
    local url="https://github.com/moser-jose/Hina7/releases/download/vHinos/${padded}.*.mp3"
    
    echo "[$CURRENT/$TOTAL] Baixando hino $padded..."
    
    # Tente baixar (pode falhar se o nome exato não corresponder)
    # curl -L -f -s -o "audio/pt/${padded}.mp3" "$url" 2>/dev/null
    
    CURRENT=$((CURRENT + 1))
}

# Opções de download
echo "Escolha uma opção:"
echo "1) Baixar primeiros 10 hinos (teste)"
echo "2) Baixar todos os 610 hinos (pode demorar ~1 hora)"
echo "3) Baixar range específico"
echo ""
read -p "Opção: " opcao

case $opcao in
    1)
        echo "Baixando primeiros 10 hinos..."
        for i in {1..10}; do
            download_hymn $i
        done
        ;;
    2)
        echo "Baixando todos os 610 hinos..."
        echo "⚠️  Isso pode demorar bastante!"
        read -p "Confirmar? (s/n): " confirma
        if [ "$confirma" = "s" ]; then
            for i in {1..610}; do
                download_hymn $i
                sleep 0.5  # Pausa para não sobrecarregar
            done
        fi
        ;;
    3)
        read -p "Número inicial: " inicio
        read -p "Número final: " fim
        echo "Baixando hinos de $inicio a $fim..."
        for i in $(seq $inicio $fim); do
            download_hymn $i
        done
        ;;
esac

echo ""
echo "✅ Download concluído!"
echo "📊 Arquivos baixados: $(ls -1 audio/pt/*.mp3 2>/dev/null | wc -l)"

# NOTA: Este script é um template
# Você precisará ajustar as URLs baseado nos nomes reais dos arquivos MP3
# Consulte o JSON original (hymns-original.json) para os nomes corretos

