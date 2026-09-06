# Mapa de módulos — PegaProx base (clone NosPanel)

> Gerado na Fase 1 via Serena MCP (projeto ativo: `nospanel` em `C:\Projetos\nospanel`).

## Estrutura raiz

- `pegaprox/` — aplicação Python/Flask.
  - `api/` — blueprints HTTP (ex.: `costs.py`, `plugins.py`, `users.py`, `settings.py`, `helpers.py`).
  - `core/` — serviços internos (`manager.py`, `db.py`, `pbs.py`, `dbcrypto.py`).
  - `utils/` — helpers (`auth.py`, `rbac.py`, `audit.py`, `sanitization.py`).
  - `background/`, `models/`, `cli/` — tarefas agendadas, modelos/permissões e CLI.
- `plugins/` — diretório de plugins carregados dinamicamente (`client_portal`, `status_page`, `notifications`, `proxmox-ha`, `hello_world`).
- `web/` — frontend: `index.html` (SPA React embutido/compilado) + fontes em `web/src/*.js`.
- `static/` — CSS/JS servidos estaticamente.
- `tests/` — suíte pytest (integração/authz/smoke etc.).
- `docs/`, `debian/`, `packaging/`, `systemd/`, `examples/`, `misc/`, `images/`.

## Pontos de interesse para o NosPanel

- **i18n do app principal**: `web/src/translations.js` — dicionário único por idioma; idiomas presentes: `de, en, es, fr, it, ko, pl, pt, zh`. Lookup `t()` com fallback para `en` (`web/index.html`). Preferência de idioma do usuário é por conta (servidor, coluna `users.language`); aplicada após login se existir no dicionário.
- **Moeda/custos**: `pegaprox/api/costs.py` (defaults EUR em `_DEFAULT_RATES`) e tabelas `cost_rates`/`power_rates` com `currency TEXT DEFAULT 'EUR'` em `pegaprox/core/db.py`. A UI do cost dashboard já oferece BRL entre as opções de moeda, mas sem formatação locale (símbolo/decimais) nos pontos verificados.
- **Loader de plugins**: `pegaprox/api/plugins.py` — manifest JSON, `register_plugin_route(plugin_id, path, handler)`, whitelist de `frontend_route`, frontend roteado em `/api/plugins/<id>/api/...`; página de plugin autocontida (ex.: `/portal`) serve por rota própria.
- **Client Portal**: ver `docs/mapping/inventario-client-portal.md`.
- **Formatação de números/horas**: uso intenso de `toFixed()`/sufixos manuais (`GB/TB`) no frontend e no `portal.html`; sem camada única de formatação (alvo da Tropicalização).

## Serena (uso recorrente)

- Projeto: `nospanel` → `C:\Projetos\nospanel` (ativo).
- Consultas simbólicas para arquivos Python (overview de símbolos, referências) funcionam; arquivos grandes como `web/index.html` e `web/src/*.js` devem ser explorados por `rg` (padrões) por serem linhas muito longas.
