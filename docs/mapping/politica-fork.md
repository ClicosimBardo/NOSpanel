# Política do fork NosPanel — remotes, branches, commits e portabilidade

## Remotes e branches

- `upstream` → PegaProx (URL em `docs/roteiro-nospanel.md`). Nunca recebe push.
- `main` local: base = `upstream/main` + commits atômicos NosPanel.
- `tracking-testing` local: rastreia `upstream/Testing` para ensaios de merge/antecipação de conflitos.
- `origin` (futuro): repositório oficial NosPanel a ser criado; adicionar quando existir.

## Regras de commit atômico

- Um commit = uma unidade lógica revertível/cherry-pickável de forma isolada.
- Mensagens no padrão do upstream (ex.: `docs:`, `feat:`, `fix:`, `i18n:` + contexto e ref quando aplicável).
- Proibido misturar formatação/refactor com mudança de comportamento no mesmo commit.
- Mudanças em áreas com forte evolução upstream (ex.: `web/src/translations.js`, `plugins/client_portal`) devem ser **menores possíveis** e documentar a chave/arquivo alterado na mensagem.
- Commits de documentação (como os das Fases 0–3) são atômicos e isolados de código.

## Sincronização com upstream (`main` + `Testing`)

1. `git fetch upstream` (traz `main` e `Testing`).
2. `git rebase main` sobre `upstream/main` (preferir rebase a merge para manter linha limpa).
3. Resolver conflitos guiado pelos mapas deste diretório e pela checklist de portabilidade.
4. Rodar a suíte (`pytest`) e conferir os pontos mapeados (moeda/i18n/plugins).
5. Atualizar a tabela de baseline em `docs/roteiro-nospanel.md`.
6. Para validar compatibilidade futura: rebase ensaio de um commit NosPanel sobre `tracking-testing` e repetir testes.

## Checklist de portabilidade (usar em cada sync)

- [ ] Conflito em `translations.js`/`web/index.html`? Conferir chaves novas vs. traduções NosPanel (`pt`).
- [ ] Mudanças em `pegaprox/api/costs.py` ou tabelas `cost_rates`/`power_rates`? Rever defaults/moeda do NosPanel.
- [ ] Mudanças em `plugins/client_portal`? Aplicar correções equivalentes ao CPortal (ver inventário) OU registrar divergência intencional.
- [ ] Mudanças no loader/API de plugins (`pegaprox/api/plugins.py`)? Verificar compatibilidade do CPortal.
- [ ] Novas chaves de i18n do app? Manter paridade `pt` e atualizar termos BR.

## Portabilidade Client Portal → CPortal

- CPortal é fork isolado: correções upstream do `client_portal` **não chegam automaticamente**.
- Toda sync deve comparar o diff upstream de `plugins/client_portal` e decidir: portar para `plugins/cportal` (commit próprio) ou registrar divergência deliberada em `docs/mapping/inventario-client-portal.md`.
