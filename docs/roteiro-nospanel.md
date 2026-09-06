# NosPanel — Roteiro de Análise, Tropicalização e Plugin CPortal

> Documento de discussão e aprovação. Nenhuma alteração de código foi aplicada.
> Fases 0–3 executadas em 2026-09-06; Fases 4–6 permanecem pendentes de aprovação.

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
- **Fase 4 — Tropicalização v1** (planejada): executar itens do catálogo `T1` quando aprovados; somente commits atômicos.
- **Fase 5 — Plugin CPortal** (planejada): executar itens do catálogo `C1`–`C6` quando aprovados.
- **Fase 6 — Rebranding opcional** (mapeada): inventário de impacto de marca (título, chaves de tradução, manifestos, README, licenciamento) para decisão futura.

## Entregáveis por diretório

- `docs/roteiro-nospanel.md` — este documento (ponto de entrada).
- `docs/mapping/` — mapas e inventários da análise.
- `docs/alteracoes/` — catálogo priorizado das mudanças (Fase 3).

## Pontos em aberto para discussão

- Feature piloto do CPortal (ex.: custo mensal em BRL por VM) — decidir após aprovação do catálogo.
- Repositório remoto oficial NosPanel (GitHub) e política de contribuição/licença.
- Inclusão de fases extras (ex.: CI do fork, testes de regressão de merge).
