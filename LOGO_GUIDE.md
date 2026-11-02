# 🎨 Guia de Uso dos Logos Conecta7

## 📦 Variações Disponíveis

### 1. **logo.svg** - Principal (Gradiente)
- **Uso**: Interface web, aplicativo, apresentações digitais
- **Características**: Gradiente azul moderno com sombra sutil
- **Fundo**: Claro ou transparente
- **Tamanho recomendado**: 200x200px ou maior

### 2. **logo-white.svg** - Versão Clara
- **Uso**: Fundos escuros, splash screens, modo noturno
- **Características**: Branco puro com efeito de brilho
- **Fundo**: Escuro ou gradientes escuros
- **Tamanho recomendado**: 200x200px ou maior

### 3. **logo-simple.svg** - Compacto
- **Uso**: Ícones pequenos, menus, navegação
- **Características**: Versão otimizada para tamanhos reduzidos
- **Fundo**: Claro ou transparente
- **Tamanho recomendado**: 64x64px até 120x120px

### 4. **logo-mono.svg** - Monocromático Azul
- **Uso**: Impressões coloridas, bordados, estampas
- **Características**: Cor única #1E40AF, sem gradiente
- **Fundo**: Claro
- **Tamanho recomendado**: Qualquer tamanho

### 5. **logo-black.svg** - Preto
- **Uso**: Impressões P&B, documentos formais, carimbos
- **Características**: Preto sólido, máxima compatibilidade
- **Fundo**: Claro
- **Tamanho recomendado**: Qualquer tamanho

### 6. **favicon.svg** - Ícone do Navegador
- **Uso**: Favicon do site, PWA icons
- **Características**: Fundo branco com bordas arredondadas
- **Tamanho**: 64x64px (otimizado para navegadores)

## 🎯 Elementos do Design

### Componentes Principais
- **C**: Representa "Conecta"
- **7**: Representa o número simbólico
- **Cruz**: Símbolo adventista minimalista
- **Linha de base**: Elemento de conexão e unidade

### Paleta de Cores
```
Gradiente Principal:
- #2563EB (Azul vibrante)
- #3B82F6 (Azul médio)
- #1E40AF (Azul profundo)

Alternativas:
- #FFFFFF (Branco)
- #000000 (Preto)
```

## 📐 Especificações Técnicas

### Espaçamento Mínimo
- Margem ao redor: 10% do tamanho total
- Não redimensionar abaixo de 32x32px

### Área de Proteção
Mantenha uma área livre equivalente a 15% da altura do logo em todos os lados.

### Tamanhos Recomendados

#### Web
- Hero/Banner: 400x400px
- Card/Thumbnail: 200x200px
- Menu/Navegação: 64x64px
- Favicon: 64x64px

#### Mobile
- Splash Screen: 512x512px
- App Icon: 192x192px
- Notificação: 96x96px

#### Impressão
- A4 (300dpi): 2362x2362px
- Business Card: 600x600px
- Banner: Mínimo 1000x1000px

## ❌ Não Fazer

1. ❌ Não rotacionar o logo
2. ❌ Não alterar as proporções (manter aspect ratio)
3. ❌ Não adicionar sombras/efeitos extras ao logo-mono ou logo-black
4. ❌ Não usar logo.svg (gradiente) em impressão P&B
5. ❌ Não alterar as cores do gradiente
6. ❌ Não separar os elementos (C, 7, cruz)
7. ❌ Não usar em fundos que competem visualmente

## ✅ Boas Práticas

1. ✅ Use sempre a versão apropriada para o contexto
2. ✅ Mantenha espaço respiratório ao redor
3. ✅ Teste em diferentes tamanhos antes de publicar
4. ✅ Prefira formato SVG quando possível (escalável)
5. ✅ Use logo-white em fundos escuros para máximo contraste
6. ✅ Para impressão P&B, use sempre logo-black.svg

## 🔄 Conversão para Outros Formatos

### Para PNG (com fundo transparente)
```bash
# Instalar librsvg
brew install librsvg  # macOS
# ou
apt-get install librsvg2-bin  # Linux

# Converter
rsvg-convert -h 512 logo.svg > logo-512.png
rsvg-convert -h 1024 logo.svg > logo-1024.png
```

### Para iOS App Icons
```bash
# Gerar todos os tamanhos necessários
rsvg-convert -h 180 logo.svg > logo-180.png  # iPhone @3x
rsvg-convert -h 120 logo.svg > logo-120.png  # iPhone @2x
rsvg-convert -h 60 logo.svg > logo-60.png    # iPhone @1x
```

### Para Android App Icons
```bash
rsvg-convert -h 192 logo.svg > logo-xxxhdpi.png  # xxxhdpi
rsvg-convert -h 144 logo.svg > logo-xxhdpi.png   # xxhdpi
rsvg-convert -h 96 logo.svg > logo-xhdpi.png     # xhdpi
rsvg-convert -h 72 logo.svg > logo-hdpi.png      # hdpi
rsvg-convert -h 48 logo.svg > logo-mdpi.png      # mdpi
```

## 📱 Uso no Projeto

### Web (React/Vite)
```tsx
import logo from '/logo.svg'

<img src={logo} alt="Conecta7" width="200" />
```

### Mobile (Flutter)
```dart
// assets/icons/logo.svg
SvgPicture.asset(
  'assets/icons/logo.svg',
  width: 200,
  height: 200,
)
```

### HTML
```html
<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />

<!-- Logo -->
<img src="/logo.svg" alt="Conecta7" width="200" height="200" />
```

## 🎨 Identidade Visual

O logo do Conecta7 combina:
- **Modernidade**: Gradiente suave e linhas limpas
- **Espiritualidade**: Cruz adventista integrada
- **Conexão**: Elementos fluidos que se complementam
- **Profissionalismo**: Design minimalista e balanceado

---

**Versão**: 2.0  
**Última atualização**: Janeiro 2026  
**Criado por**: Conecta7 Team

