# Hinário Adventista do Sétimo Dia

## 📊 Informações

- **Total de hinos**: 610
- **Idioma**: Português (Brasil)
- **Fonte**: [Hina7 por Moser José](https://github.com/moser-jose/Hina7)
- **Formato**: JSON + MP3

## 📁 Arquivos

### `hymns-original.json` (1.1 MB)
JSON completo com:
- 610 hinos com letras completas
- Categorias e subcategorias
- Autores e informações bíblicas
- Links para MP3s originais

### `hymns-pt.json`
Metadados estruturados no formato Conecta7

### `audio/pt/`
Arquivos MP3 dos hinos (~2 MB cada)

## ⚠️ Importante: Tamanho dos Arquivos

**Cálculo:**
- 610 hinos × 2 MB = **~1.2 GB total**
- GitHub limite gratuito = 1 GB
- **PROBLEMA**: Áudios completos excedem limite do GitHub!

## 💡 Soluções

### Opção 1: GitHub Releases
```bash
# Criar release com áudios
gh release create v1.0.0 audio/pt/*.mp3
```
- Limite: 2 GB por release
- URLs ficam em: `github.com/USER/repo/releases/download/v1.0.0/001.mp3`

### Opção 2: Supabase Storage (Recomendado)
```bash
# Upload para Supabase
supabase storage create conecta7-assets
supabase storage upload audio/pt/*.mp3
```
- Limite: 50 GB gratuito
- CDN global
- URLs: `PROJECT.supabase.co/storage/v1/object/public/...`

### Opção 3: Manter Link Externo
- Usar URLs originais do Moser José
- Não hospedar localmente
- Menor controle, mas sem custo de storage

## 📥 Download de MP3s

### Baixar primeiros 10 (teste):
```bash
python3 process-hymns.py test
```

### Baixar range específico:
```bash
python3 process-hymns.py 1 50    # Hinos 1-50
python3 process-hymns.py 100 200 # Hinos 100-200
```

### Baixar todos (610 hinos = 1.2 GB):
```bash
python3 process-hymns.py all
```

**⏱️ Tempo estimado**: 30-60 minutos

## 📦 Estrutura do JSON

```json
{
  "id": 1,
  "title": "Ó Deus de Amor",
  "numero": 1,
  "numero_view": "001",
  "categoria": "Adoração",
  "sub_categoria": "Adoração e Louvor",
  "autores": [...],
  "texto_biblico": "Gênesis 1:1",
  "url": "URL_DO_MP3",
  "coro": [...],
  "estrofes": [...]
}
```

## 🎯 Próximos Passos

### Adicionar outros idiomas:
- [ ] Inglês (English Hymnal)
- [ ] Espanhol (Himnario Adventista)
- [ ] Outros idiomas

### Estrutura para multi-idioma:
```
hymns/
├── hinario-adventista/
│   ├── audio/
│   │   ├── pt/    # Português
│   │   ├── en/    # Inglês
│   │   └── es/    # Espanhol
│   ├── hymns-pt.json
│   ├── hymns-en.json
│   └── hymns-es.json
```

## 🔐 Direitos Autorais

- **Hinos tradicionais**: Domínio público
- **JSON estruturado**: Moser José (MIT License)
- **Gravações (MP3s)**: Verificar permissões

⚠️ **Importante**: Certifique-se de ter permissões para distribuir as gravações.

## 🚀 Uso no App

### Carregar hinário:
```dart
// URL do JSON
final url = 'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/hymns/hinario-adventista/hymns-original.json';

// Carregar
final response = await dio.get(url);
final data = response.data;

// Acessar hinos
final hinos = data['hinos'];
```

### Tocar MP3:
```dart
// URL do áudio
final audioUrl = 'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/hymns/hinario-adventista/audio/pt/001.mp3';

// Ou usar URL original se não hospedar localmente
final audioUrl = hino['url']; // URL do GitHub original
```

## 📊 Status Atual

- [x] JSON completo baixado (1.1 MB)
- [x] Script de download de MP3s criado
- [x] 10 primeiros hinos baixados (teste)
- [ ] Decidir estratégia de storage (GitHub/Supabase/Externo)
- [ ] Baixar todos os 610 MP3s (se hospedar localmente)
- [ ] Adicionar capas e imagens
- [ ] Adicionar outros idiomas

## 🔗 Links Úteis

- **Repositório original**: https://github.com/moser-jose/Hina7
- **App web**: https://hinario-adventista.vercel.app/
- **JSON original**: https://raw.githubusercontent.com/moser-jose/Hina7/main/src/api/hinario.json

---

**Última atualização**: 06/01/2026  
**Status**: ✅ Estrutura pronta, 10 hinos de exemplo

