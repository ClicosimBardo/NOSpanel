# NosPanel — Roteiro de Análise, Tropicalização e Plugin CPortal

> Documento de discussão e aprovação. Nenhuma alteração de código foi aplicada.
> Fases 0–5 concluídas; Fase 6 (rebranding) em execução desde 2026-09-06.

## Contexto e objetivo

PegaProx é a base do fork NosPanel. O fork deve:

- Manter mudanças **atômicas** (unidades independentes, cherry-pick/rebaseáveis) sobre a base upstream.
- Facilitar o merge/rebase de atualizações do PegaProx (`main` + `Testing`).
- Tropicalizar o produto para o Brasil (moeda BRL, formato numérico/decimal, datas, idioma pt-BR e termos).
- Entregar um novo plugin **CPortal** — evolução internacionalizada do plugin `client_portal` — com arquitetura extensível para novas funções com mínimo impacto no projeto principal.

## Decisões já tomadas

| Tema | Decisão |
|---|---|
| Local de análise/fork | Clone único em `C:\Projetos\nospanel` |
| Sincronização upstream | Acompanhar `main` e `Testing` do PegaProx |
| Tropicalização v1 | Pacote ampliado (moeda/decimais/datas/idioma + termos pt-BR) |
| CPortal × client_portal | Fork isolado + documento de portabilidade; upstream intocado |
| Extensibilidade CPortal | Arquitetura extensível já na v1 (registro de features) |
| Rebranding | Fase opcional, apenas mapeada (sem execução agora) |

## Baseline do clone (Fase 0)

- Remote `upstream` → `https://github.com/PegaProx/project-pegaprox.git`
- `main` local = `45f331210aa9da1c09d6570ce4157490fc21b0a7` (`upstream/main`)
- `tracking-testing` local = `09c2c089b7b254071978141a1ce56668fd96ad6b` (`upstream/Testing`)
- `version.json`: 1.1.0 (build 2026.08.31) — atualizar esta tabela a cada sincronização.

## Fases

- **Fase 0 — Ambiente e clone** (concluída): clone, renomear remote para `upstream`, rastreio de `Testing`, baseline acima.
- **Fase 1 — Análise e mapeamento** (concluída): Serena ativo no projeto `nospanel`; mapas em `docs/mapping/`.
- **Fase 2 — Documentação-base** (concluída): este roteiro, `docs/mapping/politica-fork.md`, `docs/mapping/mapa-modulos.md`, `docs/mapping/inventario-client-portal.md` e `docs/mapping/mapa-tropicalizacao.md`.
- **Fase 3 — Catálogo de alterações** (concluída): `docs/alteracoes/catalogo-alteracoes.md` define as mudanças candidatas, granularidade de commits e regras de aplicação — **aguarda aprovação**.
- **Fase 4 — Tropicalização v1** (concluída em 2026-09-06): itens `T1` implementados em commits atômicos `cd4c255`, `df3f07b`, `c72ab9a` e `759dd20` (defaults BRL/pt-BR, suporte pt-BR e formatação locale nos dashboards de custo/energia).
- **Fase 5 — Plugin CPortal** (concluída em 2026-09-06): itens `C1`–`C6` implementados nos commits `3ff18d8`, `4ccc36e` e `dec1a94` (rota `/cportal`, plugin `cportal` com i18n pt-BR/en + registry de features + feature `sample`, contrato de mensagens e testes smoke).
- **Fase 6 — Rebranding** (execução autorizada em 2026-09-06): inventário em `docs/mapping/inventario-rebranding.md`; camada 1 (assets/identidade) concluída em `8979bd2`; camadas de strings/traduções, back-end e empacotamento em andamento.

## Entregáveis por diretório

- `docs/roteiro-nospanel.md` — este documento (ponto de entrada).
- `docs/mapping/` — mapas e inventários da análise.
- `docs/alteracoes/` — catálogo priorizado das mudanças (Fase 3).

## Pontos em aberto para discussão

- Feature piloto do CPortal (ex.: custo mensal em BRL por VM) — decidir após aprovação do catálogo.
- Repositório remoto oficial NosPanel (GitHub) e política de contribuição/licença.
- Inclusão de fases extras (ex.: CI do fork, testes de regressão de merge).
