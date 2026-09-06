# Prompt Gemini — Pacote de imagens a partir do logo NosPanel

> Uso: anexe o logo oficial (PNG/SVG) no Gemini e cole o prompt abaixo.
> Os nomes de entrega usam o prefixo `nospanel-*`; a tabela final mostra o mapeamento
> para os arquivos que o produto PegaProx/NosPanel espera (ver `docs/mapping/inventario-rebranding.md`).

## Antes de usar (preencher)

- Cor primária da marca: `#911418` (Vermelho NosPanel)
- Cores de apoio: `#0E1317` (Grafite) e `#DADBD4` (Creme)
- Fundo escuro do app: `#0c1117` (dashboard atual) — Grafite da marca `#0E1317` (ajuste se adotado)
- Fundo claro: `#f6f8fa` (tema claro) e branco `#ffffff`

## Fonte da marca\n\n- Folha oficial: `branding/nospanel-marca.pdf`; vetorial: `branding/nospanel-marca.svg`;
  amostras PNG em `branding/extracted/`. Anexe o logo (SVG/PNG) ao Gemini.

## Prompt principal (copiar e colar)

```text
Você é um designer de identidade digital. Vou anexar o logo oficial da marca
"NosPanel" (símbolo + lettering/wordmark). Com base SOMENTE nesse logo, gere o
pacote de imagens do produto descrito abaixo.

REGRAS GERAIS
- Use apenas os elementos do logo anexado: mesmo símbolo, proporções e lettering.
  NÃO recrie, reescreva nem troque a tipografia do texto "NosPanel".
- NÃO adicione slogans, taglines, outros textos ou elementos novos.
- Preserve a identidade cromática da marca. Paleta de referência: primária
  <COR_PRIMARIA>, apoio <COR_SECUNDARIA>, fundo escuro #0c1117, fundo claro
  branco/#f6f8fa.
- Entregue UM asset por imagem (nada de colagens, pranchetas, atlases ou marcas
  d'água). Nenhuma borda, sombra projetada ou moldura decorativa fora do símbolo.
- Transparência real (canal alfa) onde indicado. Cores em sRGB.
- Dimensões EXATAS em pixels, conforme cada item.

ENTREGAS
1. nospanel-logo-dark.png — 3000x3000 px, PNG transparente. Logo horizontal
   (símbolo + "NosPanel") em versão CLARA/neutra, para uso sobre fundos ESCUROS
   (#0c1117). Lettering legível e nítido.
2. nospanel-logo-light.png — 3000x3000 px, PNG transparente. Mesmo layout em
   versão ESCURA, para fundos CLAROS (branco/#f6f8fa).
3. nospanel-mark-dark.png — 3000x3000 px, PNG transparente. Somente o SÍMBOLO
   (sem texto), versão clara, para fundos escuros.
4. nospanel-mark-light.png — 3000x3000 px, PNG transparente. Somente o símbolo,
   versão escura, para fundos claros.
5. nospanel-icon-512.png — 512x512 px, PNG com FUNDO OPCIONAL PREENCHIDO (cor
   primária ou gradiente discreto da marca), símbolo centralizado ocupando no
   máximo 60% da área (zona segura para ícones "maskable"). Sem texto ou com
   lettering mínimo legível se o logo exigir; prefira só o símbolo.
6. nospanel-icon-192.png — 192x192 px, exatamente o mesmo desenho do item 5.
7. nospanel-favicon-master.png — 256x256 px, PNG transparente, símbolo SIMPLES e
   de alto contraste (sem lettering), reduzido para leitura em 16px — traços
   grossos, sem detalhes finos. Este arquivo será a fonte dos favicons.
8. nospanel-apple-touch-icon.png — 180x180 px, PNG SEM transparência (fundo
   sólido: cor primária ou #0c1117), símbolo centralizado com margem segura.
9. (opcional) nospanel-login-bg.png — 1920x1080 px, fundo escuro sutil com
   textura/gradiente discreto da marca e o logo claro pequeno (canto ou centro
   discreto), para tela de login.
10. (opcional) nospanel-og.png — 1200x630 px, para compartilhamento social: fundo
    da marca, logo e nome "NosPanel", sem excesso de texto.

AO FINAL
- Liste os arquivos gerados com dimensão e formato.
- Confirme o checklist: alfa preservado, lettering sem distorção/erro, fundos
  conforme pedido, símbolo dentro da zona segura nos ícones.
- Se algo não puder ser feito com fidelidade (ex.: lettering pequeno), aponte e
  sugira a correção em vez de inventar.
```

## Prompt curto (opcional, para itens individuais)

```text
Com base no logo anexado, gere <ITEM> conforme: <ESPECIFICACAO>. Mantenha o
lettering "NosPanel" idêntico, sem textos extras, transparência/alfa conforme o
caso e tamanho exato de <PIXELS>px.
```

## Mapeamento para os arquivos do produto

| Entrega gerada | Arquivo esperado no repo (após o rebranding R1) | Uso |
|---|---|---|
| nospanel-logo-dark.png | `images/pegaprox-logo-dark.png` (conteúdo) | Login/dashboard escuro, README |
| nospanel-logo-light.png | `images/pegaprox-logo-light.png` | Tema claro/corporativo, README |
| nospanel-mark-dark.png | `images/pegaprox-logo-square-dark.png` | Legado quadrado (opcional) |
| nospanel-mark-light.png | `images/pegaprox-logo-square-light.png` | Legado quadrado (opcional) |
| nospanel-icon-512.png | `images/pegaprox.png` (substituir) | PWA `manifest.webmanifest` (192/512) + notificações `sw.js` |
| nospanel-icon-192.png | idem (ou novo arquivo + manifest) | Ícone 192 PWA |
| nospanel-favicon-master.png | `images/favicon-16x16.png`, `favicon-32x32.png`, `favicon.ico` | Favicons (redimensionar/montar ICO offline) |
| nospanel-apple-touch-icon.png | `images/apple-touch-icon.png` | Home screen iOS |
| nospanel-login-bg.png | upload em Settings → Branding (`config/branding/login_bg.png`) | Fundo de login |
| nospanel-og.png | novo (docs/social) | Compartilhamento |

## Notas técnicas

- O Gemini (Imagen/Nano Banana) gera **raster (PNG)**: para o `favicon.ico` e
  redimensionamentos exatos, use o `nospanel-favicon-master.png` e monte/exporte
  localmente (ferramenta de imagem) em 16/24/32/48/64.
- Lettering pequeno costuma "quebrar": gere sempre em alta resolução e valide o
  texto "NosPanel" com zoom antes de aceitar.
- Se preferir fidelidade vetorial total (escalonável), mantenha o SVG original da
  marca como fonte e use o Gemini apenas para variações (ícones/fundos); os PNGs
  finais devem ser exportados do SVG quando possível.
