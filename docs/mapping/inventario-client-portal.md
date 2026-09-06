# Inventário do plugin Client Portal (base do CPortal)

> Fonte: `plugins/client_portal/` do PegaProx (baseline em `docs/roteiro-nospanel.md`). CPortal nascerá deste inventário.

## Arquivos e estrutura

- `manifest.json` — id `client_portal`, name "Client Portal", `has_frontend: true`, `frontend_route: /portal`.
- `config.json` — configuração do hoster (título, ações permitidas, recursos visíveis, snapshots, ISO, CT create, destroy).
- `__init__.py` — backend Flask (~940 linhas): carrega config, monta a lista de VMs do cliente via ACLs e expõe ações.
- `portal.html` — página autocontida (~946 linhas, SPA em JS puro): login, lista de VMs, console noVNC, snapshots, ISO, troca de senha, teardown. **100% em inglês, sem camada i18n** (`lang="en"`, strings hard-coded), usa `sessionStorage` (`portal-sid`), tema claro/escuro por CSS vars e CSP própria.

## Endpoints registrados (`register()`)

`config`, `my-vms`, `ct/create-options`, `ct/create`, `vm/destroy-options`, `vm/destroy`, `vm/power`, `vm/console`, `vm/snapshots`, `vm/snapshot-rollback`, `vm/snapshot-delete`, `account/change-password`, `vm/isos`, `vm/iso-mount`, `vm/iso-unmount`, `snapshot-policies`.

## Config atual (`config.json`)

- `portal_title`, `allowed_actions` (default: `vm.view/start/stop/console`), `show_resource_usage`, `show_ip_addresses`, `allow_password_change`, `allow_snapshots`, `max_snapshots_per_vm`, `custom_logo_url`, `theme_color`, `allow_iso_mount`, `iso_storage`, `allowed_isos`, `allow_ct_create`, `allow_destroy`, `ct_create` (cluster/node/storage/bridge/templates/limites).

## Segurança e autorização usadas

- RBAC: `load_vm_acls`, `user_can_access_vm`, `get_user_permissions`, `get_user_pool_vmids`, `load_users`, `ROLE_ADMIN`.
- Padrões de auditoria: `log_audit` em ações (ex.: `portal.guest_destroyed`, `portal.acl_cleanup_failed`).
- Histórico de hardening: CSP, reverse proxy para console VNC, ACL cleanup pós-destroy (IDOR/BOLA).

## Observações para o CPortal

- Strings de erro/sucesso do backend estão em inglês e retornam ao cliente como texto — internacionalizar = decisão de contrato (ver catálogo, item C2).
- Não há testes dedicados do plugin em `tests/` (nenhum arquivo `*portal*`/`*plugin*`); CPortal deve introduzir testes.
- Divergências intencionais entre `client_portal` upstream e `cportal` devem ser registradas aqui, com data e motivo.
