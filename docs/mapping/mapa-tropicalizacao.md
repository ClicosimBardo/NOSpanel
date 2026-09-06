# Mapa de Tropicalização — pontos que dependem de locale/moeda/formato

> Inventário (Fase 1) dos pontos onde BRL, decimais/milhar, datas e pt-BR se aplicam. Base para o catálogo `T1`.

## Backend (Python)

- `pegaprox/api/costs.py` — `_DEFAULT_RATES` com `currency: 'EUR'`; tarifas em float (decimais com `.`); resposta devolve código da moeda.
- `pegaprox/core/db.py` — colunas `currency TEXT DEFAULT 'EUR'` nas tabelas `cost_rates` e `power_rates` (linhas ~1775 e ~1796); linha `__default__` criada no primeiro run.
- `pegaprox/api/users.py` — preferência `language` por usuário; allowlist sem variante regional: `en, de, es, fr, it, pt, nl, pl, ru, zh, ja, ko` (vazio = default).
- `pegaprox/core/db.py` (~256) — coluna `users.language TEXT DEFAULT ''`.
- Não há serviço de formatação monetária no backend; valores são transmitidos crus.

## Frontend do app principal

- `web/src/translations.js` — dicionário `pt` único (sem `pt-BR`); idiomas: `de, en, es, fr, it, ko, pl, pt, zh`; `t()` com fallback `en`.
- `web/index.html` — linguagem default aplicada no login pela preferência do usuário; formatação de números via `toFixed()`/sufixos manuais; preferência de formato de hora em `localStorage` (`pegaprox-time-format`); cost dashboard com campo `currency` (default `'EUR'`, lista já inclui `BRL`).
- Sem uso de `Intl.NumberFormat`/`toLocaleString` nos pontos verificados → sem separador de milhar/decimal conforme locale.

## Plugin Client Portal

- `plugins/client_portal/portal.html` — `lang="en"`, strings/datas/formatos em inglês, `toFixed()` + sufixos (`GB/TB`); sem tradução e sem moeda hoje.

## Unidades e formatos citados como alvo (pt-BR)

- Moeda: `R$ 1.234,56` (símbolo + milhar `.` + decimal `,`).
- Números: decimais com vírgula em percentuais/tarifas exibidas.
- Datas: `dd/mm/aaaa`; tempos relativos em pt-BR.
- Termos: revisão das chaves `pt` (ex.: painéis de custo, template library, drift) e textos do portal.
