# 📦 Guia Completo - Repositório de Assets Conecta7

## 📊 O que foi criado

### Estrutura (20 MB total)
```
conecta7-assets/                              # Na raiz do projeto
├── bibles/
│   ├── catalog.json                          # Catálogo de versões
│   └── versions/
│       ├── acf.json (3.8 MB) ✅
│       ├── arc.json (3.8 MB) ✅
│       ├── nvi.json (3.8 MB) ✅
│       └── ra.json (3.8 MB) ✅
├── books/
│   ├── catalog.json
│   └── ellen-white/                          # Pronto para adicionar livros
├── hymns/
│   ├── catalog.json
│   └── hinario-adventista/
│       ├── hymns.json                        # (a criar)
│       └── audio/                            # (a adicionar MP3s)
├── images/covers/                            # Capas de livros
├── README.md
└── update-and-push.sh                        # Script helper
```

**Importante**: A pasta já está no `.gitignore` do projeto principal. É um repositório git separado.

---

## 🚀 PASSO 1: Publicar no GitHub

O repositório já está configurado para: **https://github.com/rodrigooliver/conecta7-assets**

```bash
cd conecta7-assets

# Fazer push (primeira vez)
git push -u origin main
```

### Se pedir autenticação:
Crie um Personal Access Token em: https://github.com/settings/tokens
- Marque: `repo` (all)
- Use o token como senha

---

## 🔗 PASSO 2: Testar URLs

Teste no navegador:
```
https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/bibles/versions/acf.json
```

Deve mostrar o JSON da Bíblia! ✅

---

## 📱 PASSO 3: Atualizar App Mobile

### ✅ JÁ ESTÁ ATUALIZADO!

O arquivo já foi atualizado automaticamente:
```
mobile/lib/features/bible/domain/models/bible_version_source.dart
```

Agora o app usa suas URLs:
- ACF, ARC, NVI, RA → `rodrigooliver/conecta7-assets`

### Código completo (copiar e colar):

```dart
/// Catálogo de versões disponíveis para download
class BibleVersionsCatalog {
  static final List<BibleVersionSource> availableVersions = [
    // ACF
    BibleVersionSource(
      version: const BibleVersion(
        id: 'acf',
        name: 'Almeida Corrigida Fiel',
        abbreviation: 'ACF',
        language: 'pt-BR',
        description: 'Tradução fiel aos textos originais.',
        size: 4200000,
      ),
      downloadUrl: 'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/bibles/versions/acf.json',
      estimatedSize: 4200000,
      format: 'json',
    ),

    // ARC
    BibleVersionSource(
      version: const BibleVersion(
        id: 'arc',
        name: 'Almeida Revista e Corrigida',
        abbreviation: 'ARC',
        language: 'pt-BR',
        description: 'Versão clássica em português.',
        size: 4100000,
      ),
      downloadUrl: 'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/bibles/versions/arc.json',
      estimatedSize: 4100000,
      format: 'json',
    ),

    // NVI
    BibleVersionSource(
      version: const BibleVersion(
        id: 'nvi',
        name: 'Nova Versão Internacional',
        abbreviation: 'NVI',
        language: 'pt-BR',
        description: 'Tradução moderna e clara.',
        size: 4000000,
      ),
      downloadUrl: 'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/bibles/versions/nvi.json',
      estimatedSize: 4000000,
      format: 'json',
    ),

    // RA
    BibleVersionSource(
      version: const BibleVersion(
        id: 'ra',
        name: 'Almeida Revista e Atualizada',
        abbreviation: 'RA',
        language: 'pt-BR',
        description: 'Revisão moderna.',
        size: 4150000,
      ),
      downloadUrl: 'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/bibles/versions/ra.json',
      estimatedSize: 4150000,
      format: 'json',
    ),
  ];
}
```

---

## 🧪 PASSO 4: Testar

```bash
cd mobile
flutter clean
flutter pub get
flutter run
```

No app, tente baixar uma versão da Bíblia!

---

## 📝 Adicionar Mais Conteúdo

### Adicionar nova Bíblia:
```bash
cd conecta7-assets/bibles/versions
# Copie o arquivo JSON
git add .
git commit -m "feat: adicionar nova versão"
git push
```

### Adicionar livro:
1. Crie JSON em `books/ellen-white/nome-livro.json`
2. Atualize `books/catalog.json`
3. Commit e push

### Hinário:
- JSON já está pronto com 610 hinos
- Letras completas em português
- Estrutura otimizada (0.57 MB minificado)
- Áudios: usar estratégia específica conforme necessidade

**Script helper:**
```bash
cd conecta7-assets
./update-and-push.sh "feat: descrição"
```

---

## 📄 Formatos dos Arquivos

### Bíblia (JSON):
```json
[
  {
    "abbrev": "gn",
    "name": "Gênesis",
    "chapters": [
      [
        "No princípio criou Deus os céus e a terra.",
        "E a terra era sem forma e vazia..."
      ]
    ]
  }
]
```

### Livro (JSON):
```json
{
  "id": "caminho-cristo",
  "title": "Caminho a Cristo",
  "author": "Ellen G. White",
  "chapters": [
    {
      "number": 1,
      "title": "O Amor de Deus",
      "content": "A natureza testifica do amor..."
    }
  ]
}
```

### Hinário (JSON):
```json
{
  "id": "hinario-adventista",
  "hymns": [
    {
      "number": 1,
      "title": "Santo! Santo! Santo!",
      "author": "Reginald Heber",
      "verses": [
        {
          "number": 1,
          "lyrics": "Santo! Santo! Santo!\nDeus onipotente!"
        }
      ],
      "has_audio": true,
      "audio_filename": "001.mp3"
    }
  ]
}
```

---

## 🔧 Alternativa: Supabase Storage

Se GitHub não for suficiente (limite de 1GB), use Supabase Storage:

### 1. Criar bucket:
- Acesse Supabase Dashboard
- Storage → Create bucket
- Nome: `conecta7-assets`
- Marque como **público**

### 2. Fazer upload:
Via interface web ou script (veja exemplo abaixo)

### 3. URLs do Supabase:
```
https://[PROJECT].supabase.co/storage/v1/object/public/conecta7-assets/bibles/versions/acf.json
```

### Script de upload:
```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

await supabase.storage
  .from('conecta7-assets')
  .upload('bibles/versions/acf.json', file);
```

**Vantagens Supabase:**
- 50 GB gratuito (vs 1 GB GitHub)
- Sem limite de banda
- CDN global
- Melhor controle de acesso

---

## 🆘 Problemas Comuns

### Push falha (autenticação):
```bash
# Use Personal Access Token como senha
# Crie em: https://github.com/settings/tokens
git push -u origin main
```

### URL não funciona:
1. Aguarde 1-2 minutos (cache)
2. Verifique se repo está público
3. Teste: `curl -I URL`

### App não baixa:
1. Verifique se fez push
2. Teste URL no navegador
3. `flutter clean && flutter pub get`

---

## ✅ Checklist

- [x] Pasta conecta7-assets criada
- [x] 4 Bíblias baixadas
- [x] Catálogos configurados
- [x] Remote configurado
- [x] URLs atualizadas
- [x] App mobile atualizado ✅
- [x] Hinário Adventista adicionado (610 hinos) ✅
- [ ] **Push para GitHub** ← VOCÊ ESTÁ AQUI
- [ ] Testar URLs
- [ ] Testar no app

---

## 📞 Comandos Rápidos

```bash
# Ver status
cd conecta7-assets && git status

# Adicionar conteúdo
./update-and-push.sh "feat: novo conteúdo"

# Push manual
git add . && git commit -m "mensagem" && git push

# Listar arquivos
find . -type f -not -path './.git/*'
```

---

**Repositório**: https://github.com/rodrigooliver/conecta7-assets  
**Status**: ✅ Pronto para push  
**Próximo passo**: `git push -u origin main`

