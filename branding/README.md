# Marca NosPanel — fonte e amostras extraídas

## Fontes (vetoriais, fidelidade total)
- `nospanel-marca.pdf` — folha de marca original (1 página, 100% vetorial).
- `nospanel-marca.svg` — conversão vetorial (Inkscape/poppler) da mesma folha.
  Prefira estes arquivos para exportações finais exatas (PNG/ICO em qualquer
  tamanho) em ferramenta vetorial ou no fluxo do Gemini.

## O que a folha contém (spec oficial)
- Logo completo — fundo escuro e fundo claro.
- Símbolo — fundo escuro e fundo claro.
- Aplicações de ícone: 512 maskable, 192, favicon 256, apple-touch 180.
- Paleta: Vermelho `#911418`, Grafite `#0E1317`, Creme `#DADBD4`.
- Especificação: tipografia Saira ExtraBold Italic (800).

## Amostras extraídas (`extracted/`)
PNGs transparentes (RGBA), recortados por região da folha com remoção do chip de
fundo — *amostras para uso/QA*, não substituem a exportação vetorial final:
- `nospanel-logo-dark.png` / `nospanel-logo-light.png`
- `nospanel-mark-dark.png` / `nospanel-mark-light.png`
- `nospanel-icon-512-maskable.png`, `nospanel-icon-192.png`
- `nospanel-favicon-master.png`, `nospanel-apple-touch-icon.png`

## Mapeamento para os arquivos do produto
Ver `docs/design/prompt-gemini-imagens-logo-nospanel.md` (tabela "Mapeamento").
Os arquivos finais do app continuam sendo `images/pegaprox-*.png|.ico` até a
execução do rebranding (item R1).

## QA recomendado
- Este ambiente não exibe imagens: **abra as amostras e o SVG para conferir**
  lettering "NOSPANEL", cores e recortes antes de usar.
- Variantes "fundo claro" (sobre chip branco) são as mais sensíveis ao recorte
  porque Creme `#DADBD4` ≈ branco — confirme que nenhuma parte do símbolo sumiu.
- `apple-touch-icon` final deve ter fundo opaco (sem alpha) — montar na exportação.
- `favicon.ico` multi-tamanho (16/24/32/48/64) — montar a partir de
  `nospanel-favicon-master.png` (ou do SVG).
