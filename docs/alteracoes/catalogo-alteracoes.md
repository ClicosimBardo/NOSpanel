# Catálogo priorizado de alterações NosPanel (Fase 3)

> Produto da Fase 3: define o que será alterado, em que granularidade e como aplicar. **Aguardando aprovação — nenhum item foi implementado.**

## Regras de aplicação (todas as fases)

- Cada linha do catálogo vira um ou mais commits **atômicos** conforme `docs/mapping/politica-fork.md`.
- Ordem recomendada: `T1` (Tropicalização) → `C1..C6` (CPortal) → `R1` (rebranding, se aprovado).
- Não alterar `plugins/client_portal` upstream; mudanças de tradução do app restringem-se às chaves/idiomas afetados.
- Após cada commit: conferir paridade de `web/src/translations.js`, rodar `pytest` e atualizar o baseline em `docs/roteiro-nospanel.md`.

## T1 — Tropicalização v1 (Fase 4)

| ID | Mudança | Escopo/impacto | Prioridade |
|---|---|---|---|
| T1.1 | Camada única de formatação no frontend (moeda BRL + decimais/milhar pt-BR) usada nos dashboards de custo/energia e no portal | Frontend/`web/index.html`; commits pequenos por ponto de uso | P0 |
| T1.2 | Defaults do fork para novos deploys: `currency` BRL (cost/power) e `language` `pt` para usuários novos | Backend defaults (`costs.py`, `db.py`) — sem migração forçada de instalações existentes | P0 |
| T1.3 | Datas `dd/mm/aaaa` e tempos relativos pt-BR nos pontos mapeados | Frontend + portal | P1 |
| T1.4 | Revisão de termos das chaves `pt` (paridade + ajustes BR) | Somente `web/src/translations.js` (chaves `pt`) | P1 |
| T1.5 | Decidir modelo de idioma: manter `pt` único (recomendado) ou introduzir `pt-BR` (mexe em allowlist/backend/UI) | Backend `users.py` + frontend | Decisão |

## C — Plugin CPortal (Fase 5)

| ID | Mudança | Escopo/impacto | Prioridade |
|---|---|---|---|
| C1 | Diretório `plugins/cportal` com `manifest.json`/`config.json` copiados da base (client_portal) | Plugin novo, isolado | P0 |
| C2 | Backend i18n: definir contrato de mensagens (código + texto traduzível) para erros/sucessos das rotas | `plugins/cportal/__init__.py` | P1 |
| C3 | i18n do portal: dicionário embutido (`pt`/`en`) + idioma vindo da preferência do usuário | `plugins/cportal/portal.html` | P0 |
| C4 | Formatação BRL/pt-BR no portal (moeda, números, datas) reusando camada T1 quando possível | portal.html | P0 |
| C5 | Arquitetura extensível v1: registro de features (feature = manifest próprio + hooks JS/API + i18n por feature), rota única `/portal` | Design + plugin | P0 |
| C6 | Testes do plugin (backend das rotas + smoke do portal) — hoje inexistentes no upstream | `tests/` | P1 |

## R — Rebranding opcional (Fase 6, mapeado)

| ID | Mudança | Escopo/impacto |
|---|---|---|
| R1 | Inventário de marca (título/subtítulo do app, chaves de tradução de brand, manifestos, README, `NOTICE`/licenciamento, changelog) | Documento de impacto; execução só após decisão |

## Pontos de decisão pendentes (discussão)

- T1.5 (modelo de idioma `pt` vs `pt-BR`).
- Feature piloto do CPortal para provar o mecanismo de extensão (C5).
- Inclusão de fases extras (CI do fork, ensaios de merge em `Testing`).
