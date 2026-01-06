# 🚀 Próximos Passos - Publicar no GitHub

## ✅ O que já foi feito:

1. ✅ Criada pasta `conecta7-assets` no root do projeto
2. ✅ Adicionada ao `.gitignore` do projeto principal
3. ✅ Inicializado repositório git separado
4. ✅ Criada estrutura de pastas
5. ✅ Baixadas 4 versões da Bíblia (ACF, ARC, NVI, RA)
6. ✅ Criados arquivos de catálogo JSON
7. ✅ Feito commit inicial

## 📤 Para publicar no GitHub:

### 1. Criar repositório no GitHub

1. Acesse https://github.com/new
2. Configure:
   - **Nome do repositório**: `conecta7-assets`
   - **Descrição**: "Repositório público de assets para o app Conecta7"
   - **Visibilidade**: ✅ **Public** (importante!)
   - **NÃO** marque "Initialize with README" (já temos um)
3. Clique em **Create repository**

### 2. Conectar seu repositório local ao GitHub

Copie os comandos que aparecem na tela do GitHub, ou execute:

```bash
cd /Users/rodrigooliveiradesouza/Projects/conecta7/conecta7-assets

# Adicionar o remote (substitua SEU_USUARIO pelo seu usuário do GitHub)
git remote add origin https://github.com/SEU_USUARIO/conecta7-assets.git

# Renomear branch para main (se necessário)
git branch -M main

# Fazer o primeiro push
git push -u origin main
```

### 3. Verificar se funcionou

Acesse: `https://github.com/SEU_USUARIO/conecta7-assets`

Você deve ver todos os arquivos lá!

### 4. Testar as URLs

Teste se consegue acessar os arquivos:
```
https://raw.githubusercontent.com/SEU_USUARIO/conecta7-assets/main/bibles/versions/acf.json
```

Cole essa URL no navegador. Você deve ver o JSON da Bíblia ACF.

## 🔧 Atualizar o App Mobile

Depois de publicar, você precisa atualizar o app para usar suas URLs.

### Opção 1: Criar arquivo de configuração (Recomendado)

Crie o arquivo: `apps/mobile/lib/core/config/assets_config.dart`

```dart
/// Configuração das URLs do repositório de assets
class AssetsConfig {
  // Substitua SEU_USUARIO pelo seu usuário do GitHub
  static const String _githubUser = 'SEU_USUARIO';
  static const String baseUrl = 'https://raw.githubusercontent.com/$_githubUser/conecta7-assets/main';
  
  static String getBibleVersionUrl(String versionId) {
    return '$baseUrl/bibles/versions/$versionId.json';
  }
}
```

### Opção 2: Editar diretamente o arquivo existente

Edite: `apps/mobile/lib/features/bible/domain/models/bible_version_source.dart`

Encontre as linhas com:
```dart
downloadUrl: 'https://raw.githubusercontent.com/thiagobodruk/biblia/master/json/acf.json',
```

E substitua por:
```dart
downloadUrl: 'https://raw.githubusercontent.com/SEU_USUARIO/conecta7-assets/main/bibles/versions/acf.json',
```

Faça isso para todas as 4 versões (acf, arc, nvi, ra).

## 📝 Editar os Catálogos

Não esqueça de atualizar os catálogos JSON com seu usuário do GitHub!

Edite estes arquivos:
- `bibles/catalog.json`
- `books/catalog.json`
- `hymns/catalog.json`

Substitua `SEU_USUARIO` pelo seu usuário real do GitHub.

## 🎵 Próximos Passos - Adicionar Conteúdo

### Para adicionar livros:

1. Crie o arquivo JSON do livro em `books/ellen-white/`
2. Atualize `books/catalog.json`
3. Commit e push:
```bash
cd /Users/rodrigooliveiradesouza/Projects/conecta7/conecta7-assets
git add .
git commit -m "feat: adicionar livro [NOME]"
git push
```

### Para adicionar hinário:

1. Crie `hymns/hinario-adventista/hymns.json` com as letras
2. Adicione arquivos MP3 em `hymns/hinario-adventista/audio/`
3. Atualize `hymns/catalog.json`
4. Commit e push

**ATENÇÃO**: GitHub tem limite de 100MB por arquivo. Para áudios grandes:
- Use GitHub Releases
- Ou considere Supabase Storage (veja `SUPABASE_STORAGE_ASSETS.md`)

## 🔄 Comandos Úteis

### Ver status:
```bash
cd conecta7-assets
git status
```

### Adicionar arquivos novos:
```bash
git add .
git commit -m "feat: adicionar [descrição]"
git push
```

### Ver log de commits:
```bash
git log --oneline
```

## 📊 Estatísticas Atuais

Arquivos baixados:
- ✅ ACF: 3.8 MB
- ✅ ARC: 3.8 MB  
- ✅ NVI: 3.8 MB
- ✅ RA: 3.8 MB (cópia temporária de ACF)

**Nota sobre RA**: A versão RA é atualmente uma cópia da ACF porque não estava disponível no repositório original. Você pode substituir por uma versão real da RA se encontrar.

## 🆘 Problemas Comuns

### Erro: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/SEU_USUARIO/conecta7-assets.git
```

### Erro: "permission denied"
- Certifique-se de estar logado no GitHub
- Use HTTPS ou configure SSH keys

### Erro ao fazer push de arquivos grandes
- Use Git LFS: `git lfs install`
- Ou use GitHub Releases para arquivos > 100MB

## 📚 Documentação Adicional

Veja também:
- `../docs/ASSETS_SETUP.md` - Guia completo de setup
- `../docs/ASSETS_INTEGRATION.md` - Como integrar no app
- `../docs/SUPABASE_STORAGE_ASSETS.md` - Alternativa com Supabase

---

**Criado em**: 06/01/2026
**Pronto para publicar!** 🎉

