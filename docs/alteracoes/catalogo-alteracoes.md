# Catálogo priorizado de alterações NosPanel (Fase 3)

> Produto da Fase 3: define o que será alterado, em que granularidade e como aplicar.
> Status em 2026-09-06: itens **T1 implementados** (Fase 4 concluída, commits cd4c255 a 759dd20);
> itens C1–C6 (CPortal) e R1 (rebranding) **aguardando aprovação**.

## Regras de aplicação (todas as fases)

- Cada linha do catálogo vira um ou mais commits **atômicos** conforme `docs/mapping/politica-fork.md`.
- Ordem recomendada: `T1` (concluído) → `C1..C6` (CPortal) → `R1` (rebranding, se aprovado).
- Não alterar `plugins/client_portal` upstream (portal segue intocado; formatação/tradução do portal pertence ao CPortal, item C4).
- Após cada commit: conferir paridade de `web/src/translations.js`, rodar `pytest` e atualizar o baseline em `docs/roteiro-nospanel.md`.

## T1 — Tropicalização v1 (Fase 4 — CONCLUÍDA)

| ID | Mudança | Status / decisão |
|---|---|---|
| T1.1 | Camada única de formatação (moeda BRL + decimais/milhar pt-BR) nos dashboards de custo/energia | Implementado: helpers `fmtMoney`/`fmtNum` em `web/src/ui.js` usados nos tabs Power/Carbon e Cost (`web/src/dashboard.js`); portal fica para o CPortal (C4). |
| T1.2 | Defaults do fork para novos deploys: `currency` BRL (cost/power) e `language` pt para usuários novos | Implementado: `costs.py`, `power.py`, `db.py` (defaults `'BRL'`); `users.py` cria usuário com `'pt-BR'`. Sem migração forçada de instalações existentes. |
| T1.3 | Datas `dd/mm/aaaa` e tempos relativos pt-BR | Parcial/mapeado: dashboards de custo/energia não exibem datas; adoção ampla de datas ficará no CPortal (C4) e numa varredura futura da UI — mantido como item aberto. |
| T1.4 | Revisão de termos das chaves `pt` | Implementado via **overrides pt-BR** (bloco `translations['pt-BR']` no fim de `web/src/translations.js`), sem editar as chaves `pt` upstream — menor atrito de merge. |
| T1.5 | Modelo de idioma | Decidido e implementado: **pt-BR** como código próprio (alias de `pt` + overrides), allowlist backend/frontend ampliada, seletor com "Português (Portugal)" e "Português (Brasil)", default do fork pt-BR. |

## C — Plugin CPortal (Fase 5 — aguardando aprovação)

| ID | Mudança | Escopo/impacto | Prioridade |
|---|---|---|---|
| C1 | Diretório `plugins/cportal` com `manifest.json`/`config.json` copiados da base (client_portal) | Plugin novo, isolado | P0 |
| C2 | Backend i18n: definir contrato de mensagens (código + texto traduzível) para erros/sucessos das rotas | `plugins/cportal/__init__.py` | P1 |
| C3 | i18n do portal: dicionário embutido (`pt-BR`/`en`) + idioma vindo da preferência do usuário | `plugins/cportal/portal.html` | P0 |
| C4 | Formatação BRL/pt-BR no portal (moeda, números, datas) reusando a camada T1 quando possível | portal.html | P0 |
| C5 | Arquitetura extensível v1: registro de features (feature = manifest próprio + hooks JS/API + i18n por feature), rota única `/portal` | Design + plugin | P0 |
| C6 | Testes do plugin (backend das rotas + smoke do portal) — hoje inexistentes no upstream | `tests/` | P1 |

## R — Rebranding opcional (Fase 6, mapeado)

| ID | Mudança | Escopo/impacto |
|---|---|---|
| R1 | Inventário de marca (título/subtítulo do app, chaves de tradução de brand, manifestos, README, `NOTICE`/licenciamento, changelog) | Documento de impacto; execução só após decisão |

## Pontos de decisão pendentes (discussão)

- Feature piloto do CPortal para provar o mecanismo de extensão (C5).
- Adoção ampla de formatação de datas pt-BR em toda a UI (extensão do T1.3).
- Inclusão de fases extras (CI do fork, ensaios de merge em `Testing`).
