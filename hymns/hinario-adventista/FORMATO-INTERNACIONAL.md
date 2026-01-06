# 🌍 Formato Internacional do Hinário

## 📊 Comparação de Formatos

### Arquivos disponíveis:

| Arquivo | Tamanho | Descrição |
|---------|---------|-----------|
| `hymns-original.json` | 1.08 MB | Formato original (Moser José) |
| `hymns-international.json` | 0.88 MB | Formato internacional (legível) |
| `hymns-international.min.json` | 0.68 MB | Formato minificado (produção) |

## 🔄 Mapeamento de Chaves

### Formato Original → Internacional

| Original (PT) | Internacional (EN) | Tipo |
|---------------|-------------------|------|
| `titulo` | `title` | string |
| `ingles` | `title_en` | string |
| `numero` | `number` | number |
| `numero_view` | `number_display` | string |
| `categoria` | `category` | string |
| `sub_categoria` | `subcategory` | string |
| `autores` | `authors` | array |
| `texto_biblico` | `scripture_reference` | string |
| `url` | `audio_url` | string |
| `artwork` | `cover_art` | string |
| `artist` | `artist` | string |
| `estrofes` | `verses` | array |
| `coro` | `chorus` | object |

### Metadados

| Original | Internacional |
|----------|---------------|
| `autor` | `metadata.source.author` |
| `github` | `metadata.source.github` |
| `versao` | `metadata.version` |
| `ultima_atualizacao` | `metadata.source.original_update` |

## 📝 Estrutura do JSON Internacional

### Metadados
```json
{
  "metadata": {
    "id": "adventist-hymnal-pt-br",
    "title": "Hinário Adventista do Sétimo Dia",
    "language": "pt-BR",
    "edition": "2023",
    "total_hymns": 610,
    "version": 109,
    "last_updated": "2026-01-06",
    "source": {
      "author": "Moser José",
      "github": "https://github.com/moser-jose",
      "url": "https://hinario-adventista.vercel.app/",
      "original_update": "07-02-2021"
    }
  }
}
```

### Categorias
```json
{
  "categories": [
    {
      "id": 1,
      "name": "Adoração",
      "background": "adoracao.jpg",
      "subcategories": [
        {
          "name": "Adoração e Louvor",
          "hymns_range": "1 - 20"
        }
      ]
    }
  ]
}
```

### Hinos
```json
{
  "hymns": [
    {
      "id": 1,
      "number": 1,
      "number_display": "001",
      "title": "Ó Deus de Amor",
      "title_en": "Before Jehova's Awful Throne",
      "category": "Adoração",
      "subcategory": "Adoração e Louvor",
      "authors": [
        {
          "name": "Isaac Watts (1674 - 1748)"
        }
      ],
      "scripture_reference": "Gênesis 1:1",
      "audio_url": "URL_DO_MP3",
      "cover_art": "URL_DA_CAPA",
      "artist": "Hinário Adventista do 7º Dia",
      "verses": [
        {
          "number": "I",
          "lyrics": "Ó Deus de amor,\nvimos nós te adorar..."
        }
      ],
      "chorus": {
        "label": "Coro",
        "lyrics": "Texto do coro..."
      }
    }
  ]
}
```

## 🎯 Vantagens do Formato Internacional

### ✅ Chaves em Inglês
- Padrão internacional
- Fácil integração com outros sistemas
- Melhor para desenvolvedores globais

### ✅ Estrutura Mais Limpa
- Metadados separados
- Categorias organizadas
- Hierarquia clara

### ✅ Menor Tamanho
- Original: 1.08 MB
- Internacional: 0.88 MB (18% menor)
- Minificado: 0.68 MB (37% menor)

### ✅ Compatibilidade
- Mantém todos os dados originais
- Adiciona estrutura de metadados
- Facilita multi-idioma

## 💻 Uso no App

### Carregar JSON Internacional
```dart
final response = await dio.get(
  'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/hymns/hinario-adventista/hymns-international.json'
);

final data = response.data;

// Metadados
final metadata = data['metadata'];
print(metadata['title']);         // "Hinário Adventista..."
print(metadata['total_hymns']);   // 610
print(metadata['language']);      // "pt-BR"

// Categorias
final categories = data['categories'];
for (var category in categories) {
  print(category['name']);
  for (var sub in category['subcategories']) {
    print('  ${sub['name']}: ${sub['hymns_range']}');
  }
}

// Hinos
final hymns = data['hymns'];
final hymn = hymns[0];

print(hymn['title']);              // "Ó Deus de Amor"
print(hymn['title_en']);           // "Before Jehova's Awful Throne"
print(hymn['number']);             // 1
print(hymn['category']);           // "Adoração"

// Letras
for (var verse in hymn['verses']) {
  print('${verse['number']}: ${verse['lyrics']}');
}

// Coro (se existir)
if (hymn['chorus'] != null) {
  print('Coro: ${hymn['chorus']['lyrics']}');
}
```

### Usar Versão Minificada (Produção)
```dart
// Mais rápido para download
final url = 'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/hymns/hinario-adventista/hymns-international.min.json';
```

## 🔄 Reconverter se Necessário

```bash
cd conecta7-assets/hymns/hinario-adventista

# Reconverter do original
python3 convert-to-international.py
```

## 🌍 Multi-idioma (Futuro)

### Estrutura preparada:
```
hymns/
├── hinario-adventista-pt/
│   └── hymns-international.json  (Português)
├── hymnal-adventist-en/
│   └── hymns-international.json  (English)
└── himnario-adventista-es/
    └── hymns-international.json  (Español)
```

### Catálogo multi-idioma:
```json
{
  "hymnals": [
    {
      "id": "adventist-hymnal-pt",
      "language": "pt-BR",
      "url": ".../hymns-international.json"
    },
    {
      "id": "adventist-hymnal-en",
      "language": "en",
      "url": ".../hymns-international.json"
    },
    {
      "id": "adventist-hymnal-es",
      "language": "es",
      "url": ".../hymns-international.json"
    }
  ]
}
```

## 📦 TypeScript Types (Opcional)

```typescript
interface HymnalMetadata {
  id: string;
  title: string;
  language: string;
  edition: string;
  total_hymns: number;
  version: number;
  last_updated: string;
  source: {
    author: string;
    github: string;
    url: string;
    original_update: string;
  };
}

interface Hymn {
  id: number;
  number: number;
  number_display: string;
  title: string;
  title_en?: string;
  category: string;
  subcategory: string;
  authors: Array<{ name: string }>;
  scripture_reference?: string;
  audio_url?: string;
  cover_art?: string;
  artist: string;
  verses: Array<{
    number: string;
    lyrics: string;
  }>;
  chorus?: {
    label?: string;
    lyrics: string;
  } | null;
}

interface Hymnal {
  metadata: HymnalMetadata;
  categories: Array<Category>;
  hymns: Array<Hymn>;
}
```

## ✅ Checklist

- [x] Converter formato original para internacional
- [x] Criar versão minificada
- [x] Atualizar catálogo
- [x] Documentar estrutura
- [ ] Testar no app
- [ ] Adicionar outros idiomas (en, es)

---

**Última atualização**: 06/01/2026  
**Versão**: 1.0

