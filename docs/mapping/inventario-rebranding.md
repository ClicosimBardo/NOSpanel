# Inventário de impacto — Rebranding PegaProx → NosPanel (R1)

> Documento de impacto (Fase 6, item R1 do catálogo). **Nada foi alterado** — apenas mapeamento
> para decisão futura. Contagens: ocorrências de "PegaProx" (case-insensitive) no baseline de 2026-09-06.

## Visão geral (contagens no repo)

| Área | Ocorrências | Observação |
|---|---|---|
| `web/index.html` | ~1086 | App compilado: título, login, logo, rodapé, versão, textos |
| `web/src/` | ~1074 | Fontes (equivalente ao index.html + comentários) |
| `version.json` | 117 | Changelog descreve releases "PegaProx X.Y.Z" |
| `README.md` | 74 | Marca, links, sponsors |
| `plugins/` | 162 | Nomes/textos de plugins (ex.: Client Portal) |
| `pegaprox/*.py` | 91 arquivos | `constants.py` (28), logs, audit, mensagens |
| `debian/` + `packaging/` + `systemd/` | 33+21+7 | Nomes de serviço/pacote (`pegaprox`, `/opt/PegaProx`) |
| `NOTICE` | 11 | Atribuições/licença |
| `images/` | 0 (nomes genéricos) | Logos `pegaprox-logo-*.png` usados por referência |
| `web/manifest.webmanifest` | 4 | Nome do app (PWA) |

## Categorias de mudança

- **Marca visível no produto**: `web/index.html`/`web/src` (título da aba, login `PegaProx`, chaves de tradução por idioma que embutem a marca, logo/img, `manifest.webmanifest`, `sw.js`, versão no rodapé).
- **Código/identidade**: `pegaprox/constants.py` (nome/versão), mensagens de log/audit, prefixos de chaves (`pegaprox-language`, `pegaprox-time-format`) que persistem em `localStorage` — renomear quebra preferências antigas; manter alias de leitura.
- **Empacotamento/operação**: `debian/`, `packaging/`, `systemd/`, `update.sh`/`patch.sh` (caminhos `/opt/PegaProx`, serviço `pegaprox`) — renomear exige migração de instalações.
- **Ecosistema/plugins**: `plugins/*/manifest.json` e strings (nome "Client Portal" etc.), checagem de `trusted` por autor começar com "PegaProx" em `pegaprox/api/plugins.py`.
- **Legal/comunidade**: `NOTICE`, `LICENSE` (AGPL), atribuições de contribuidores no `version.json`; o fork deve manter créditos originais (AGPL §7) e adicionar marca própria sem apagar a upstream.

## Recomendações para decisão

- Executar o rebranding em **commits atômicos por categoria**, mantendo a marca upstream intacta no código-fonte que segue o merge (ex.: usar apenas um "brand layer" no índice/traduções) para minimizar conflitos a cada sync.
- Decidir explicitamente: (a) troca total dos textos; (b) marca dual "NosPanel (fork de PegaProx)"; (c) manter nomes internos (`pegaprox-*`) e trocar só o visível.
- `localStorage`/chaves de sessão com prefixo `pegaprox-*` devem permanecer legíveis (compatibilidade), mesmo se a UI passar a exibir "NosPanel".
- Licença: manter `LICENSE`/`NOTICE` upstream e adicionar aviso de fork; não remover atribuições dos autores originais.

## Status

- Mapeamento: **concluído** (este documento).
- Execução do rebranding: **não autorizada** — depende de decisão (item R1 do catálogo).
