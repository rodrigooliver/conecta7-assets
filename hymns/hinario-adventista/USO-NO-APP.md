# 📱 Como Usar o Hinário no App

## 📊 Estrutura Otimizada

O JSON foi otimizado removendo campos duplicados. Informações comuns foram movidas para `metadata.common`.

### Estrutura do JSON:

```json
{
  "metadata": {
    "id": "adventist-hymnal-pt-br",
    "title": "Hinário Adventista do Sétimo Dia",
    "language": "pt-BR",
    "edition": "2023",
    "total_hymns": 610,
    "common": {
      "artist": "Hinário Adventista do 7º Dia",
      "cover_art": "https://github.com/moser-jose/Hina7/releases/download/vHinos/capa.png",
      "audio_base_url": "https://github.com/moser-jose/Hina7/releases/download/vHinos/"
    }
  },
  "categories": [...],
  "hymns": [
    {
      "id": 1,
      "number": 1,
      "number_display": "001",
      "title": "Ó Deus de Amor",
      "title_en": "Before Jehova's Awful Throne",
      "category": "Adoração",
      "subcategory": "Adoração e Louvor",
      "authors": [...],
      "scripture_reference": "Gênesis 1:1",
      "audio_file": "001.O.Deus.de.Amor.mp3",  ← Apenas o nome!
      "verses": [...],
      "chorus": {...}
    }
  ]
}
```

## 💡 Campos Otimizados

### Antes (Duplicado 610x):
```json
{
  "artist": "Hinário Adventista do 7º Dia",
  "cover_art": "https://github.com/.../capa.png",
  "audio_url": "https://github.com/.../001.O.Deus.de.Amor.mp3"
}
```

### Depois (1x no metadata):
```json
{
  "metadata": {
    "common": {
      "artist": "...",
      "cover_art": "...",
      "audio_base_url": "https://github.com/.../vHinos/"
    }
  },
  "hymns": [{
    "audio_file": "001.O.Deus.de.Amor.mp3"  ← Só o nome
  }]
}
```

## 🔧 Como Usar no App (Flutter/Dart)

### 1. Carregar o JSON:

```dart
import 'package:dio/dio.dart';

class HymnalRepository {
  final Dio _dio;
  
  Future<Map<String, dynamic>> loadHymnal() async {
    final response = await _dio.get(
      'https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/hymns/hinario-adventista/hymns-pt.min.json'
    );
    
    return response.data;
  }
}
```

### 2. Criar Modelo com Campos Computados:

```dart
class Hymn {
  final int id;
  final int number;
  final String numberDisplay;
  final String title;
  final String? titleEn;
  final String category;
  final String subcategory;
  final List<Author> authors;
  final String? scriptureReference;
  final String audioFile;
  final List<Verse> verses;
  final Chorus? chorus;
  
  // Metadata comum (passado do JSON principal)
  final String commonArtist;
  final String commonCoverArt;
  final String audioBaseUrl;
  
  Hymn({
    required this.id,
    required this.number,
    required this.numberDisplay,
    required this.title,
    this.titleEn,
    required this.category,
    required this.subcategory,
    required this.authors,
    this.scriptureReference,
    required this.audioFile,
    required this.verses,
    this.chorus,
    required this.commonArtist,
    required this.commonCoverArt,
    required this.audioBaseUrl,
  });
  
  // Campos computados (reconstruídos)
  String get artist => commonArtist;
  String get coverArt => commonCoverArt;
  String get audioUrl => audioBaseUrl + audioFile;
  
  factory Hymn.fromJson(
    Map<String, dynamic> json,
    Map<String, dynamic> common,
  ) {
    return Hymn(
      id: json['id'],
      number: json['number'],
      numberDisplay: json['number_display'],
      title: json['title'],
      titleEn: json['title_en'],
      category: json['category'],
      subcategory: json['subcategory'],
      authors: (json['authors'] as List)
          .map((a) => Author.fromJson(a))
          .toList(),
      scriptureReference: json['scripture_reference'],
      audioFile: json['audio_file'],
      verses: (json['verses'] as List)
          .map((v) => Verse.fromJson(v))
          .toList(),
      chorus: json['chorus'] != null 
          ? Chorus.fromJson(json['chorus']) 
          : null,
      // Passar dados comuns
      commonArtist: common['artist'],
      commonCoverArt: common['cover_art'],
      audioBaseUrl: common['audio_base_url'],
    );
  }
}
```

### 3. Parser Completo:

```dart
class HymnalData {
  final HymnalMetadata metadata;
  final List<Category> categories;
  final List<Hymn> hymns;
  
  HymnalData({
    required this.metadata,
    required this.categories,
    required this.hymns,
  });
  
  factory HymnalData.fromJson(Map<String, dynamic> json) {
    final metadata = HymnalMetadata.fromJson(json['metadata']);
    final common = json['metadata']['common'];
    
    return HymnalData(
      metadata: metadata,
      categories: (json['categories'] as List)
          .map((c) => Category.fromJson(c))
          .toList(),
      hymns: (json['hymns'] as List)
          .map((h) => Hymn.fromJson(h, common))
          .toList(),
    );
  }
}

class HymnalMetadata {
  final String id;
  final String title;
  final String language;
  final String edition;
  final int totalHymns;
  final CommonData common;
  
  HymnalMetadata({
    required this.id,
    required this.title,
    required this.language,
    required this.edition,
    required this.totalHymns,
    required this.common,
  });
  
  factory HymnalMetadata.fromJson(Map<String, dynamic> json) {
    return HymnalMetadata(
      id: json['id'],
      title: json['title'],
      language: json['language'],
      edition: json['edition'],
      totalHymns: json['total_hymns'],
      common: CommonData.fromJson(json['common']),
    );
  }
}

class CommonData {
  final String artist;
  final String coverArt;
  final String audioBaseUrl;
  
  CommonData({
    required this.artist,
    required this.coverArt,
    required this.audioBaseUrl,
  });
  
  factory CommonData.fromJson(Map<String, dynamic> json) {
    return CommonData(
      artist: json['artist'],
      coverArt: json['cover_art'],
      audioBaseUrl: json['audio_base_url'],
    );
  }
}
```

### 4. Uso no App:

```dart
// Carregar hinário
final hymnalData = await hymnalRepository.loadHymnal();
final hymnal = HymnalData.fromJson(hymnalData);

// Acessar metadados
print(hymnal.metadata.title);        // "Hinário Adventista..."
print(hymnal.metadata.totalHymns);   // 610
print(hymnal.metadata.common.artist); // "Hinário Adventista do 7º Dia"

// Listar hinos
for (final hymn in hymnal.hymns) {
  print('${hymn.numberDisplay} - ${hymn.title}');
  
  // Acessar campos computados
  print('Artista: ${hymn.artist}');        // Vem do metadata.common
  print('Capa: ${hymn.coverArt}');         // Vem do metadata.common
  print('Áudio: ${hymn.audioUrl}');        // Construído automaticamente
  
  // Letras
  for (final verse in hymn.verses) {
    print('${verse.number}: ${verse.lyrics}');
  }
  
  // Coro
  if (hymn.chorus != null) {
    print('Coro: ${hymn.chorus!.lyrics}');
  }
}

// Tocar áudio
final player = AudioPlayer();
await player.play(hymn.audioUrl);  // URL completa reconstruída
```

### 5. Widget Exemplo:

```dart
class HymnCard extends StatelessWidget {
  final Hymn hymn;
  
  const HymnCard({required this.hymn});
  
  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        leading: CircleAvatar(
          backgroundImage: NetworkImage(hymn.coverArt),
          child: Text(hymn.numberDisplay),
        ),
        title: Text(hymn.title),
        subtitle: Text('${hymn.category} • ${hymn.artist}'),
        trailing: IconButton(
          icon: Icon(Icons.play_arrow),
          onPressed: () => _playAudio(hymn.audioUrl),
        ),
        onTap: () => _showLyrics(hymn),
      ),
    );
  }
}
```

## 🎯 Vantagens da Otimização

### ✅ Tamanho Reduzido
- **26.8% menor** (280 KB economizados)
- Download mais rápido
- Menos uso de memória

### ✅ Manutenção Facilitada
- Alterar artista/capa em 1 lugar só
- Menos redundância
- Estrutura mais limpa

### ✅ URLs Flexíveis
- Fácil mudar base URL
- Suporte a múltiplos CDNs
- Cache mais eficiente

## 📦 Tamanhos Finais

| Arquivo | Tamanho | Uso |
|---------|---------|-----|
| `hymns-pt.json` | 0.76 MB | Desenvolvimento |
| `hymns-pt.min.json` | 0.57 MB | ⭐ Produção |
| `hymns-original.json` | 1.08 MB | Backup |

## 🔗 URLs

**Produção (recomendado):**
```
https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/hymns/hinario-adventista/hymns-pt.min.json
```

**Desenvolvimento:**
```
https://raw.githubusercontent.com/rodrigooliver/conecta7-assets/main/hymns/hinario-adventista/hymns-pt.json
```

---

**Última atualização**: 06/01/2026  
**Versão otimizada**: 1.0

