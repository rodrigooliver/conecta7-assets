#!/bin/bash

# Script para atualizar e fazer push de assets para o GitHub
# Uso: ./update-and-push.sh "mensagem do commit"

set -e

echo "🚀 Conecta7 Assets - Update & Push"
echo "=================================="
echo ""

# Verificar se está no diretório correto
if [ ! -f "README.md" ] || [ ! -d ".git" ]; then
    echo "❌ Erro: Execute este script dentro da pasta conecta7-assets/"
    exit 1
fi

# Verificar se foi passada uma mensagem de commit
if [ -z "$1" ]; then
    echo "❌ Erro: Forneça uma mensagem de commit"
    echo "Uso: ./update-and-push.sh \"mensagem do commit\""
    echo ""
    echo "Exemplos:"
    echo "  ./update-and-push.sh \"feat: adicionar livro Caminho a Cristo\""
    echo "  ./update-and-push.sh \"fix: corrigir catálogo de bíblias\""
    echo "  ./update-and-push.sh \"docs: atualizar README\""
    exit 1
fi

COMMIT_MESSAGE="$1"

echo "📋 Verificando status..."
git status --short

echo ""
echo "➕ Adicionando arquivos..."
git add -A

echo ""
echo "📊 Arquivos que serão commitados:"
git status --short

echo ""
echo "💾 Fazendo commit..."
git commit -m "$COMMIT_MESSAGE" || {
    echo "⚠️  Nada para commitar ou erro no commit"
    exit 1
}

echo ""
echo "📤 Fazendo push para GitHub..."
git push

echo ""
echo "✅ Pronto! Assets atualizados com sucesso!"
echo ""
echo "🔗 Verifique no GitHub:"
git remote get-url origin 2>/dev/null || echo "https://github.com/rodrigooliver/conecta7-assets"
echo ""

