"""CPortal plugin (NosPanel fork of Client Portal) - layout & contract smoke tests."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / 'plugins' / 'cportal'
FEATURES = PLUGIN / 'features'


def _load_json(p):
    return json.loads(p.read_text(encoding='utf-8'))


def test_cportal_plugin_layout():
    for name in ('manifest.json', 'config.json', 'portal.html', '__init__.py'):
        assert (PLUGIN / name).is_file(), name


def test_cportal_manifest_identity():
    m = _load_json(PLUGIN / 'manifest.json')
    assert m['id'] == 'cportal'
    assert m['name'] == 'CPortal'
    assert m.get('has_frontend') is False


def test_cportal_config_ptbr_defaults():
    c = _load_json(PLUGIN / 'config.json')
    assert c.get('default_language') == 'pt-BR'
    assert isinstance(c.get('features'), list)
    assert c.get('portal_title') == 'CPortal'


def test_cportal_portal_uses_cportal_api_namespace():
    html = (PLUGIN / 'portal.html').read_text(encoding='utf-8')
    assert 'plugins/cportal/api' in html
    assert 'plugins/client_portal/api' not in html


def test_cportal_portal_has_i18n_and_br_formatting_hooks():
    html = (PLUGIN / 'portal.html').read_text(encoding='utf-8')
    assert 'function tr(key, fallback)' in html
    assert 'function loadFeatures()' in html
    assert 'toLocaleString(' in html  # pt-BR formatting helper present


def test_cportal_sample_feature_manifest():
    m = _load_json(FEATURES / 'sample' / 'manifest.json')
    assert m['id'] == 'sample'
    assert m.get('default_enabled') is False
    assert (FEATURES / 'sample' / 'ui.js').is_file()


def test_cportal_backend_registers_own_namespace_and_registry():
    src = (PLUGIN / '__init__.py').read_text(encoding='utf-8')
    assert "register_plugin_route('cportal'," in src
    assert 'FEATURES_DIR' in src
    assert '_resolve_language' in src
    assert 'feature/%s/ui.js' in src


def test_cportal_core_route_serves_portal_page():
    src = (ROOT / 'pegaprox' / 'api' / 'settings.py').read_text(encoding='utf-8')
    assert "@bp.route('/cportal')" in src
    assert 'def cportal_page' in src
    assert "'plugins', 'cportal', 'portal.html'" in src
