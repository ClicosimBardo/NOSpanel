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

## Pacote gerado no Gemini (`gemini/`, 2026-09-06)

Arquivos recebidos do fluxo de geração (Downloads → projeto). Dimensões validadas:

- PNG: `nospanel-logo-dark.png` / `nospanel-logo-light.png` (2400x509, RGBA); `nospanel-icon-512-maskable.png` (512x512, RGB); `nospanel-icon-192.png` (192x192, RGBA); `nospanel-apple-touch-icon.png` (180x180, RGB — opaco, correto); `nospanel-favicon-master.png` (256x256, RGBA).
- SVG (vetorial): `nospanel-logo-dark/light/red.svg` (4200x890), `nospanel-mark-dark/light.svg` (1660x890), `nospanel-favicon-master.svg` (256).

Gerados localmente em 2026-09-06 por derivação vetorial fiel: `nospanel-logo-red.png` (2400x509) e `nospanel-mark-dark.png`/`nospanel-mark-light.png` (1400x751) renderizados dos SVGs via Inkscape; `nospanel-favicon.ico` (16/24/32/48/64/128/256) montado do favicon-master; `nospanel-login-bg.png` (1920x1080) e `nospanel-og.png` (1200x630) compostos com a paleta da marca (Grafite `#0E1317` + Vermelho `#911418`). QA visual **concluído por Eduardo em 2026-09-06 — sem pendências**; pacote `gemini/` aprovado para uso no produto.

> `nospanel-marca (1).pdf` no Downloads é idêntico ao `nospanel-marca.pdf` já versionado (hash SHA-256 igual) — não duplicado.
