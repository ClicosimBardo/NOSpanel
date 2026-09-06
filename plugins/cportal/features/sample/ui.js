// CPortal sample feature - extension contract (C5).
// Exposes window.CPortalFeatures.<id> with mount(apiBase, tr).
window.CPortalFeatures = window.CPortalFeatures || {};
window.CPortalFeatures.sample = {
    id: 'sample',
    mount: function (apiBase, tr) {
        var banner = document.createElement('div');
        banner.className = 'cportal-feature-sample';
        banner.style.cssText = 'position:fixed;bottom:12px;right:12px;z-index:150;background:var(--card);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:8px;padding:8px 12px;font-size:12px;color:var(--muted);max-width:300px;';
        banner.textContent = tr('feature.sample.banner', 'CPortal sample feature active (edit plugins/cportal/features/sample/ui.js).');
        document.body.appendChild(banner);
    }
};
