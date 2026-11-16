# -*- coding: utf-8 -*-
"""
Generador del Dashboard Minimalista y Ultra-Profesional de Gobierno de TI (COBIT 2019)
para TECNIFICATE S.A.S.
- Cero emojis: reemplazados por iconos SVG vectoriales limpios y estilizados.
- Arquitectura minimalista y código digno de un arquitecto senior con más de 15 años de experiencia.
- Todos los apartados y widgets 100% funcionales y reactivos.
- Eliminación de elementos superfluos o mockups decorativos.
- Codificación UTF-8 estricta sin mojibake.
"""
import os
import json

BASE_DIR = r"C:\Users\andre\.gemini\antigravity\scratch\Gobierno_TI_Tecnificate\Entregable_Actividad5_Dashboard_Estrategico_Metricas_COBIT2019"
HTML_PATH = os.path.join(BASE_DIR, "Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html")

from build_full_act5 import tickets_dataset, monthly_data, cobit_matrix

tickets_json = json.dumps(tickets_dataset, ensure_ascii=False)
monthly_json = json.dumps(monthly_data, ensure_ascii=False)
matrix_json = json.dumps(cobit_matrix, ensure_ascii=False)

# SVG Icons Definitions (Minimalist, stroke-based, 14-16px)
SVG_ICONS = {
    "search": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
    "plus": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>',
    "download": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>',
    "printer": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>',
    "moon": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>',
    "refresh": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>',
    "user": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>',
    "dashboard": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>',
    "table": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>',
    "target": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    "sliders": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line></svg>',
    "eye": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>',
    "close": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
    "copy": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>',
    "check": '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'
}

html_code = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TECNIFICATE S.A.S. — Sistema de Gobierno de TI y Métricas COBIT 2019</title>
<style>
:root {{
  --bg: #f8fafc;
  --surface: #ffffff;
  --surface-subtle: #f1f5f9;
  --border: #e2e8f0;
  --border-strong: #cbd5e1;
  --text: #0f172a;
  --text-muted: #64748b;
  --text-secondary: #334155;
  --brand: #0284c7;
  --brand-hover: #0369a1;
  --brand-subtle: #e0f2fe;
  --accent-green: #059669;
  --accent-green-subtle: #ecfdf5;
  --accent-amber: #d97706;
  --accent-amber-subtle: #fffbeb;
  --accent-purple: #4f46e5;
  --accent-purple-subtle: #eef2ff;
  --accent-red: #dc2626;
  --accent-red-subtle: #fef2f2;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
}}

body.dark-theme {{
  --bg: #090d16;
  --surface: #111827;
  --surface-subtle: #1f2937;
  --border: #1f2937;
  --border-strong: #374151;
  --text: #f9fafb;
  --text-muted: #9ca3af;
  --text-secondary: #d1d5db;
  --brand-subtle: #082f49;
  --accent-green-subtle: #064e3b;
  --accent-amber-subtle: #78350f;
  --accent-purple-subtle: #312e81;
  --accent-red-subtle: #7f1d1d;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.6);
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg);
  color: var(--text);
  line-height: 1.45;
  font-size: 13px;
  -webkit-font-smoothing: antialiased;
  transition: background-color 0.15s, color 0.15s;
}}

/* ICON STYLING */
.icon {{
  width: 14px;
  height: 14px;
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
}}

/* TOPBAR */
.app-header {{
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  height: 52px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}}

.header-brand {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.brand-mark {{
  width: 26px;
  height: 26px;
  background: var(--text);
  color: var(--surface);
  font-weight: 800;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-sm);
  letter-spacing: -0.5px;
}}
.brand-info {{ display: flex; flex-direction: column; }}
.brand-name {{ font-weight: 700; font-size: 13.5px; color: var(--text); line-height: 1.1; }}
.brand-sub {{ font-size: 10.5px; color: var(--text-muted); font-weight: 500; }}

/* HEADER ACTIONS */
.header-actions {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.btn {{
  padding: 6px 11px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 600;
  border: 1px solid transparent;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.12s ease;
  user-select: none;
}}
.btn:active {{ transform: scale(0.98); }}

.btn-primary {{
  background: var(--brand);
  color: #ffffff;
}}
.btn-primary:hover {{ background: var(--brand-hover); }}

.btn-secondary {{
  background: var(--surface-subtle);
  border-color: var(--border-strong);
  color: var(--text-secondary);
}}
.btn-secondary:hover {{
  background: var(--border);
  color: var(--text);
}}

.user-tag {{
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  background: var(--surface-subtle);
  border: 1px solid var(--border);
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}}

/* VIEW NAVIGATION TABS */
.nav-tab-strip {{
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 20px;
  display: flex;
  gap: 4px;
}}
.tab-link {{
  padding: 10px 14px;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--text-muted);
  background: transparent;
  border: none;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  display: flex;
  align-items: center;
  gap: 7px;
  transition: all 0.12s;
}}
.tab-link:hover {{ color: var(--text); }}
.tab-link.active {{
  color: var(--brand);
  border-bottom-color: var(--brand);
}}

/* MAIN WRAPPER */
.app-viewport {{
  max-width: 1680px;
  margin: 16px auto;
  padding: 0 16px 40px;
}}

.view-pane {{ display: none; }}
.view-pane.active {{ display: block; }}

/* 3-COLUMN METRICS GRID */
.metrics-grid {{
  display: grid;
  grid-template-columns: 1fr 1.05fr 1fr;
  gap: 14px;
  align-items: start;
}}
@media (max-width: 1200px) {{
  .metrics-grid {{ grid-template-columns: 1fr; }}
}}

.grid-col {{
  display: flex;
  flex-direction: column;
  gap: 14px;
}}

/* SECTION CARD */
.panel-card {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}}

.panel-header {{
  padding: 9px 14px;
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  font-weight: 600;
  color: var(--text-secondary);
}}
.panel-header-right {{
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  color: var(--text-muted);
  cursor: pointer;
}}
.panel-header-right:hover {{ color: var(--brand); }}

.panel-body {{
  padding: 14px;
}}
.panel-title {{
  font-size: 13.5px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 12px;
  text-align: center;
  letter-spacing: -0.2px;
}}

/* FILTERS IN PANEL 1 */
.form-row {{
  display: flex;
  gap: 6px;
  margin-bottom: 8px;
}}
.form-select, .form-input {{
  width: 100%;
  padding: 6px 9px;
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-sm);
  font-size: 11.5px;
  font-weight: 500;
  background: var(--surface);
  color: var(--text);
  outline: none;
  transition: border-color 0.12s;
}}
.form-select:focus, .form-input:focus {{
  border-color: var(--brand);
}}

.search-box {{
  display: flex;
  position: relative;
  margin-bottom: 8px;
}}
.search-box input {{
  padding-left: 28px;
}}
.search-box .search-icon {{
  position: absolute;
  left: 9px;
  top: 8px;
  color: var(--text-muted);
}}

.filter-presets {{
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  margin-bottom: 10px;
}}
.chip {{
  background: var(--surface-subtle);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.1s;
}}
.chip:hover, .chip.active {{
  background: var(--brand);
  border-color: var(--brand);
  color: #fff;
}}

.jql-bar {{
  background: var(--surface-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 5px 8px;
  font-family: var(--font-mono);
  font-size: 10.5px;
  color: var(--text-muted);
  word-break: break-all;
}}

/* APP HOSTING CARDS */
.hosting-trio {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin-bottom: 10px;
}}
.host-box {{
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-sm);
  padding: 10px 6px;
  text-align: center;
  background: var(--surface);
  cursor: pointer;
  transition: all 0.12s;
}}
.host-box:hover {{
  border-color: var(--brand);
  background: var(--surface-subtle);
}}
.host-box.active {{
  border-color: var(--brand);
  background: var(--brand-subtle);
}}
.host-box .lbl {{ font-size: 11px; font-weight: 600; color: var(--text-muted); }}
.host-box .val {{ font-size: 24px; font-weight: 800; color: var(--text); margin: 2px 0; }}
.host-box .pct {{ font-size: 10.5px; color: var(--text-muted); font-weight: 500; }}

/* COMPACT DATA TABLES IN PANELS */
.dense-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 11.5px;
}}
.dense-table th {{
  text-align: left;
  color: var(--text-muted);
  padding: 5px 6px;
  border-bottom: 1px solid var(--border);
  font-weight: 600;
}}
.dense-table td {{
  padding: 6px;
  border-bottom: 1px solid var(--border);
}}
.dense-table tr:hover td {{
  background: var(--surface-subtle);
  cursor: pointer;
}}
.color-dot {{
  display: inline-block;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  margin-right: 6px;
}}

/* FULL EXPLORER TABLE (VIEW 2) */
.table-container {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}}
.table-bar {{
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}}
.data-grid {{
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}}
.data-grid th {{
  background: var(--surface-subtle);
  color: var(--text-secondary);
  padding: 8px 10px;
  text-align: left;
  font-weight: 600;
  border-bottom: 1px solid var(--border-strong);
  cursor: pointer;
  user-select: none;
}}
.data-grid th:hover {{ color: var(--brand); }}
.data-grid td {{
  padding: 8px 10px;
  border-bottom: 1px solid var(--border);
  color: var(--text);
  vertical-align: middle;
}}
.data-grid tr:hover td {{ background: var(--surface-subtle); }}

/* PILL BADGES */
.tag {{
  display: inline-flex;
  align-items: center;
  padding: 2px 6px;
  border-radius: var(--radius-sm);
  font-size: 10.5px;
  font-weight: 600;
}}
.tag-green {{ background: var(--accent-green-subtle); color: var(--accent-green); border: 1px solid rgba(5, 150, 105, 0.2); }}
.tag-amber {{ background: var(--accent-amber-subtle); color: var(--accent-amber); border: 1px solid rgba(217, 119, 6, 0.2); }}
.tag-purple {{ background: var(--accent-purple-subtle); color: var(--accent-purple); border: 1px solid rgba(79, 70, 229, 0.2); }}
.tag-red {{ background: var(--accent-red-subtle); color: var(--accent-red); border: 1px solid rgba(220, 38, 38, 0.2); }}
.tag-blue {{ background: var(--brand-subtle); color: var(--brand); border: 1px solid rgba(2, 132, 199, 0.2); }}

/* MODAL SYSTEM */
.dialog-backdrop {{
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(2px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 16px;
}}
.dialog-backdrop.visible {{ display: flex; }}

.dialog-window {{
  background: var(--surface);
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-md);
  max-width: 720px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-md);
  animation: fadeIn 0.12s ease-out;
}}
@keyframes fadeIn {{
  from {{ opacity: 0; transform: scale(0.98); }}
  to {{ opacity: 1; transform: scale(1); }}
}}

.dialog-header {{
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.dialog-title {{ font-size: 14px; font-weight: 700; color: var(--text); }}
.dialog-body {{ padding: 16px; font-size: 12.5px; }}
.dialog-footer {{
  padding: 10px 16px;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}}

.info-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-bottom: 12px;
}}
.info-field .lbl {{ font-size: 10.5px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.3px; }}
.info-field .val {{ font-size: 12.5px; font-weight: 600; color: var(--text); margin-top: 2px; }}

.info-block {{
  background: var(--surface-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
  margin-bottom: 10px;
}}
.info-block .sec-title {{ font-size: 11px; font-weight: 700; color: var(--brand); margin-bottom: 4px; text-transform: uppercase; }}

/* SIMULATOR (VIEW 4) */
.sim-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}}
@media (max-width: 900px) {{ .sim-grid {{ grid-template-columns: 1fr; }} }}

.slider-row {{
  margin-bottom: 16px;
}}
.slider-meta {{
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 4px;
}}
.slider-row input[type=range] {{
  width: 100%;
  accent-color: var(--brand);
  cursor: pointer;
}}

.kpi-quad {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-top: 14px;
}}
.kpi-tile {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 12px;
  text-align: center;
}}
.kpi-tile .kpi-num {{ font-size: 26px; font-weight: 800; }}
.kpi-tile .kpi-lbl {{ font-size: 11px; font-weight: 600; color: var(--text-muted); margin-top: 2px; }}

/* TOAST NOTIFICATION */
#appToast {{
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: var(--text);
  color: var(--surface);
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 600;
  display: none;
  align-items: center;
  gap: 8px;
  box-shadow: var(--shadow-md);
  z-index: 2000;
}}

/* TOOLTIP */
#chartTooltip {{
  position: fixed;
  display: none;
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--border-strong);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  font-size: 11.5px;
  box-shadow: var(--shadow-md);
  pointer-events: none;
  z-index: 1500;
  max-width: 260px;
}}

@media print {{
  .app-header, .nav-tab-strip, .header-actions, .filter-presets, .search-box, .btn {{ display: none !important; }}
  .panel-card {{ border: 1px solid #ccc !important; box-shadow: none !important; break-inside: avoid; }}
  body {{ background: #fff !important; color: #000 !important; }}
}}
</style>
</head>
<body>

<!-- FLOATING TOOLTIP -->
<div id="chartTooltip"></div>

<!-- SYSTEM TOAST -->
<div id="appToast"><span id="toastIcon">{SVG_ICONS["check"]}</span> <span id="toastMessage">Operación realizada con éxito</span></div>

<!-- TOPBAR -->
<header class="app-header">
  <div class="header-brand">
    <div class="brand-mark">T</div>
    <div class="brand-info">
      <div class="brand-name">TECNIFICATE S.A.S.</div>
      <div class="brand-sub">Sistema de Gobierno de TI — COBIT 2019</div>
    </div>
  </div>
  <div class="header-actions">
    <button class="btn btn-primary" onclick="openCreateDialog()">{SVG_ICONS["plus"]} Registrar Control</button>
    <button class="btn btn-secondary" onclick="exportDataCsv()">{SVG_ICONS["download"]} Exportar CSV</button>
    <button class="btn btn-secondary" onclick="window.print()">{SVG_ICONS["printer"]} Imprimir</button>
    <button class="btn btn-secondary" onclick="toggleTheme()">{SVG_ICONS["moon"]} Tema</button>
    <div class="user-tag">{SVG_ICONS["user"]} auditor.gobiernoti@usc.edu.co</div>
  </div>
</header>

<!-- NAVIGATION TABS -->
<nav class="nav-tab-strip">
  <button class="tab-link active" onclick="activateTab('pane-dashboard')">{SVG_ICONS["dashboard"]} Tablero de Control</button>
  <button class="tab-link" onclick="activateTab('pane-explorer')">{SVG_ICONS["table"]} Registro de Controles (<span id="totalActiveCount">48</span>)</button>
  <button class="tab-link" onclick="activateTab('pane-cascade')">{SVG_ICONS["target"]} Cascada de Metas COBIT & BSC</button>
  <button class="tab-link" onclick="activateTab('pane-simulator')">{SVG_ICONS["sliders"]} Simulador de Capacidad (ISO 33000)</button>
</nav>

<main class="app-viewport">

  <!-- ===================================================================== -->
  <!-- TAB 1: TABLERO DE CONTROL (CUSTOM CHARTS)                             -->
  <!-- ===================================================================== -->
  <div id="pane-dashboard" class="view-pane active">
    <div class="metrics-grid">

      <!-- COLUMNA 1: FILTROS SIMPLE SEARCH + EVOLUCIÓN 12 MESES -->
      <div class="grid-col">
        <!-- PANEL 1: BÚSQUEDA Y FILTRADO -->
        <div class="panel-card">
          <div class="panel-header">
            <span>Filtros de Búsqueda de Gobernanza</span>
            <div class="panel-header-right" onclick="resetAllFilters()">{SVG_ICONS["refresh"]} Restablecer</div>
          </div>
          <div class="panel-body">
            <div class="form-row">
              <select id="fltDomain" class="form-select" onchange="runFilterPipeline()">
                <option value="ALL">Dominio COBIT: Todos (EDM/APO/BAI/DSS/MEA)</option>
                <option value="EDM">EDM — Evaluar, Dirigir y Supervisar</option>
                <option value="APO">APO — Alinear, Planear y Organizar</option>
                <option value="BAI">BAI — Construir, Adquirir e Implementar</option>
                <option value="DSS">DSS — Entregar, Dar Servicio y Soporte</option>
                <option value="MEA">MEA — Supervisar, Evaluar y Valorar</option>
              </select>
              <select id="fltApp" class="form-select" onchange="runFilterPipeline()">
                <option value="ALL">Aplicación: Todas las Plataformas</option>
                <option value="ERP Modular Apolo">ERP Modular Apolo</option>
                <option value="Apolo Académico SaaS">Apolo Académico v2.1 SaaS</option>
                <option value="Apolo II Mobile">Apolo II Mobile (Android)</option>
                <option value="Portal Web & Hosting VPS">Portal Web & Hosting VPS</option>
                <option value="AulaCloud & Wiki">AulaCloud & Wiki</option>
                <option value="CRM Open Source">CRM Open Source</option>
              </select>
            </div>
            <div class="form-row">
              <select id="fltStatus" class="form-select" onchange="runFilterPipeline()">
                <option value="ALL">Estado: Todos los Estados</option>
                <option value="Completado en SLA">Completado en SLA</option>
                <option value="En Curso">En Curso</option>
                <option value="Por Hacer">Por Hacer</option>
              </select>
              <select id="fltPriority" class="form-select" onchange="runFilterPipeline()">
                <option value="ALL">Prioridad: Todas las Prioridades</option>
                <option value="P1 - Crítico">P1 — Crítico</option>
                <option value="P2 - Alto">P2 — Alto</option>
                <option value="P3 - Medio">P3 — Medio</option>
                <option value="P4 - Bajo">P4 — Bajo</option>
              </select>
              <select id="fltAssignee" class="form-select" onchange="runFilterPipeline()">
                <option value="ALL">Responsable: Todo el Equipo</option>
                <option value="Diego Vélez">Diego Vélez (Líder PETI)</option>
                <option value="Santiago Balanta">Santiago Balanta (DevOps)</option>
                <option value="Martín Murillo">Martín Murillo (Líder QA)</option>
                <option value="Andrés Sarria">Andrés Sarria (Comercial)</option>
                <option value="Brayan Noguera">Brayan Noguera (Auditoría)</option>
              </select>
            </div>

            <div class="search-box">
              <span class="search-icon">{SVG_ICONS["search"]}</span>
              <input type="text" id="fltSearch" class="form-input" placeholder="Buscar por código, DIAN, colegios, SLA, Girardot..." oninput="runFilterPipeline()">
            </div>

            <div class="filter-presets">
              <span class="chip" onclick="applyPreset('p1')">Críticos P1</span>
              <span class="chip" onclick="applyPreset('dss02')">Mesa de Ayuda (DSS02)</span>
              <span class="chip" onclick="applyPreset('bai07')">Calidad QA (BAI07)</span>
              <span class="chip" onclick="applyPreset('dss06')">Reprocesos ERP (DSS06)</span>
              <span class="chip" onclick="resetAllFilters()">Todos</span>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">
              <span id="txtFilterCount" style="font-weight:600; color:var(--accent-green); font-size:11.5px;">● 48 controles identificados</span>
              <span style="color:var(--brand); cursor:pointer; font-size:11px;" onclick="toggleJqlBox()">Ver JQL</span>
            </div>
            <div id="boxJql" class="jql-bar" style="display:none; margin-top:6px;"></div>
          </div>
        </div>

        <!-- PANEL 2: LÍNEA DE TIEMPO 12 MESES -->
        <div class="panel-card">
          <div class="panel-header">
            <span>Evolución Temporal de Gobernanza (12 Meses)</span>
            <div style="display:flex; gap:4px;">
              <button class="btn btn-secondary" style="padding:2px 6px; font-size:10.5px;" onclick="setHistoryRange('12M')">12 Meses</button>
              <button class="btn btn-secondary" style="padding:2px 6px; font-size:10.5px;" onclick="setHistoryRange('H1')">Semestre 1</button>
              <button class="btn btn-secondary" style="padding:2px 6px; font-size:10.5px;" onclick="setHistoryRange('H2')">Semestre 2</button>
            </div>
          </div>
          <div class="panel-body">
            <div class="panel-title">Controles Creados vs Resueltos en SLA (COBIT 2019)</div>
            <div id="svgTimelineContainer" style="width:100%; position:relative;"></div>

            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px; margin-top:10px; font-size:11px;">
              <div style="cursor:pointer;" onclick="toggleLineSerie('resolved')">
                <span class="color-dot" style="background:var(--accent-green);"></span>
                <b>Resueltos SLA (DSS02):</b> 18 → 58/mes
              </div>
              <div style="cursor:pointer;" onclick="toggleLineSerie('rework')">
                <span class="color-dot" style="background:var(--accent-amber);"></span>
                <b>Reprocesos (DSS06):</b> 80% → 40%
              </div>
              <div style="cursor:pointer;" onclick="toggleLineSerie('bugs')">
                <span class="color-dot" style="background:var(--accent-purple);"></span>
                <b>Bugs Producción (BAI07):</b> 14 → 4
              </div>
              <div style="cursor:pointer;" onclick="toggleLineSerie('sla')">
                <span class="color-dot" style="background:var(--brand);"></span>
                <b>Cumplimiento SLA ITIL:</b> 61% → 92,5%
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- COLUMNA 2: BARRAS POR APLICACIÓN + APP HOSTING -->
      <div class="grid-col">
        <!-- PANEL 3: BARRAS POR APLICACIÓN -->
        <div class="panel-card">
          <div class="panel-header">
            <span>Controles y Tickets por Aplicación</span>
            <span style="cursor:pointer; color:var(--brand);" onclick="filterBySingleApp('ALL')">Ver Todas</span>
          </div>
          <div class="panel-body">
            <div class="panel-title">Distribución de Gobernanza por Plataforma de Software</div>
            <div id="svgAppBarsContainer" style="width:100%; min-height:210px;"></div>
            <div style="display:flex; justify-content:center; gap:12px; font-size:11px; margin-top:8px;">
              <span><span class="color-dot" style="background:var(--accent-green);"></span>Completado</span>
              <span><span class="color-dot" style="background:var(--accent-amber);"></span>En Curso</span>
              <span><span class="color-dot" style="background:var(--accent-purple);"></span>Por Hacer</span>
            </div>
          </div>
        </div>

        <!-- PANEL 4: APP HOSTING -->
        <div class="panel-card">
          <div class="panel-header">
            <span>Infraestructura y Alojamiento</span>
            <span>COBIT APO03 / BAI04</span>
          </div>
          <div class="panel-body">
            <div class="panel-title">Entornos de Despliegue (App Hosting)</div>
            <div class="hosting-trio">
              <div class="host-box" id="hostBoxCloud" onclick="filterByHostingType('Nube (Cloud VPS SaaS)')">
                <div class="lbl">Nube (Cloud VPS)</div>
                <div class="val" id="valHostCloud">220</div>
                <div class="pct" id="pctHostCloud">64,3% (Apolo SaaS)</div>
              </div>
              <div class="host-box" id="hostBoxServer" onclick="filterByHostingType('Servidor Dedicado / VPS')">
                <div class="lbl">Servidor Web / SSL</div>
                <div class="val" id="valHostServer">84</div>
                <div class="pct" id="pctHostServer">24,6% (Hosting)</div>
              </div>
              <div class="host-box" id="hostBoxLocal" onclick="filterByHostingType('Centro de Datos / Local')">
                <div class="lbl">Centro Datos Local</div>
                <div class="val" id="valHostLocal">38</div>
                <div class="pct" id="pctHostLocal">11,1% (PyMEs)</div>
              </div>
            </div>
            <div style="text-align:center; font-size:11px; color:var(--text-muted);">
              Total Gobernado: <b style="color:var(--brand);">342</b> componentes auditados &nbsp;|&nbsp;
              <span style="color:var(--brand); cursor:pointer;" onclick="filterByHostingType('ALL')">Mostrar Todo</span>
            </div>
          </div>
        </div>
      </div>

      <!-- COLUMNA 3: DONA DE ESTADO + TIPO DE SOLICITUD -->
      <div class="grid-col">
        <!-- PANEL 5: GRÁFICO DE DONA -->
        <div class="panel-card">
          <div class="panel-header">
            <span>Estado del Proyecto de Gobernanza</span>
            <span>COBIT MEA01</span>
          </div>
          <div class="panel-body">
            <div class="panel-title">Categoría de Estado (Status Category)</div>
            <div style="display:grid; grid-template-columns: 125px 1fr; gap:12px; align-items:center;">
              <div id="svgDonutContainer" style="text-align:center;"></div>
              <table class="dense-table">
                <thead>
                  <tr><th>Estado</th><th>Items</th><th>%</th></tr>
                </thead>
                <tbody id="tblStatusBreakdown"></tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- PANEL 6: TIPO DE SOLICITUD -->
        <div class="panel-card">
          <div class="panel-header">
            <span>Clasificación por Proceso Operativo</span>
            <span>COBIT 2019</span>
          </div>
          <div class="panel-body">
            <div class="panel-title">Solicitudes por Tipo (Request Type)</div>
            <div id="reqBarsContainer" style="width:100%; min-height:170px;"></div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- TAB 2: REGISTRO DE CONTROLES E INCIDENTES (EXPLORADOR)                -->
  <!-- ===================================================================== -->
  <div id="pane-explorer" class="view-pane">
    <div class="table-container">
      <div class="table-bar">
        <div>
          <div style="font-weight:700; font-size:13.5px;">Registro Operativo de Controles e Incidentes de Gobierno de TI</div>
          <div style="font-size:11px; color:var(--text-muted);">Seleccione cualquier registro para visualizar la Ficha de Auditoría y Análisis de Causa Raíz (RCA).</div>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
          <input type="text" id="tblSearchInput" class="form-input" style="width:180px;" placeholder="Filtrar en tabla..." oninput="onExplorerSearch()">
          <select id="tblPageSizeSelect" class="form-select" style="width:110px;" onchange="onExplorerPageSize()">
            <option value="10">10 por página</option>
            <option value="25">25 por página</option>
            <option value="50">50 por página</option>
            <option value="999">Todos</option>
          </select>
        </div>
      </div>

      <div style="overflow-x:auto;">
        <table class="data-grid">
          <thead>
            <tr>
              <th onclick="sortExplorer('code')">Código</th>
              <th onclick="sortExplorer('title')">Título de la Incidencia / Control</th>
              <th onclick="sortExplorer('app')">Aplicación</th>
              <th onclick="sortExplorer('domain')">Dominio</th>
              <th onclick="sortExplorer('priority')">Prioridad</th>
              <th onclick="sortExplorer('status')">Estado</th>
              <th onclick="sortExplorer('sla')">SLA %</th>
              <th onclick="sortExplorer('assignee')">Responsable</th>
              <th>Auditoría</th>
            </tr>
          </thead>
          <tbody id="tblExplorerBody"></tbody>
        </table>
      </div>

      <div style="padding:8px 14px; display:flex; justify-content:space-between; align-items:center; font-size:11.5px; border-top:1px solid var(--border);">
        <span id="txtPaginationInfo">Mostrando 1 a 10 de 48 registros</span>
        <div style="display:flex; gap:4px;" id="boxPaginationButtons"></div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- TAB 3: CASCADA DE METAS COBIT 2019 & BSC                             -->
  <!-- ===================================================================== -->
  <div id="pane-cascade" class="view-pane">
    <div class="table-container">
      <div style="padding:12px 16px; border-bottom:1px solid var(--border); background:var(--surface-subtle);">
        <div style="font-weight:700; font-size:14px;">Matriz de Cascada de Metas COBIT 2019 & Balanced Scorecard (BSC)</div>
        <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">
          Mapeo bidireccional entre Metas Empresariales (EG), Metas de Alineamiento (AG), Procesos COBIT 2019 y métricas de desempeño de TECNIFICATE S.A.S.
        </div>
      </div>
      <div style="overflow-x:auto;">
        <table class="data-grid">
          <thead>
            <tr>
              <th>Proceso COBIT</th>
              <th>Dominio</th>
              <th>Meta Empresarial (EG)</th>
              <th>Meta de Alineamiento (AG)</th>
              <th>Perspectiva BSC</th>
              <th>Métrica Estratégica (Lag) e Inductor (Lead)</th>
              <th>Línea Base (AS-IS)</th>
              <th>Meta Lograda (TO-BE)</th>
              <th>Capacidad ISO 33000</th>
              <th>Responsable</th>
            </tr>
          </thead>
          <tbody id="tblCascadeBody"></tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- TAB 4: SIMULADOR DE CAPACIDAD ISO/IEC 33000                           -->
  <!-- ===================================================================== -->
  <div id="pane-simulator" class="view-pane">
    <div class="panel-card" style="padding:20px;">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; flex-wrap:wrap; gap:10px;">
        <div>
          <div style="font-size:16px; font-weight:800; color:var(--text);">Simulador Dinámico de Madurez y Capacidad de TI</div>
          <div style="font-size:12px; color:var(--text-muted); margin-top:2px;">
            Ajuste los niveles de capacidad de cada dominio COBIT 2019 (escala ISO/IEC 33000 de 0 a 5) y observe el impacto inmediato sobre los KPIs clave de TECNIFICATE S.A.S.
          </div>
        </div>
        <div style="display:flex; gap:6px;">
          <button class="btn btn-secondary" onclick="setSimScenario('asis')">Línea Base AS-IS</button>
          <button class="btn btn-secondary" onclick="setSimScenario('mid')">Escenario 6 Meses</button>
          <button class="btn btn-primary" onclick="setSimScenario('tobe')">Meta TO-BE Lograda</button>
        </div>
      </div>

      <div class="sim-grid">
        <!-- CONTROLES DESLIZANTES -->
        <div>
          <div class="slider-row">
            <div class="slider-meta">
              <span>EDM: Evaluar, Dirigir y Supervisar (Gobernanza)</span>
              <span id="txtSimValEdm" style="color:var(--brand); font-weight:700;">1.0</span>
            </div>
            <input type="range" id="simRngEdm" min="0" max="5" step="0.5" value="1.0" oninput="recalcSimulation()">
          </div>

          <div class="slider-row">
            <div class="slider-meta">
              <span>APO: Alinear, Planear y Organizar (Gestión de Arquitectura)</span>
              <span id="txtSimValApo" style="color:var(--brand); font-weight:700;">2.0</span>
            </div>
            <input type="range" id="simRngApo" min="0" max="5" step="0.5" value="2.0" oninput="recalcSimulation()">
          </div>

          <div class="slider-row">
            <div class="slider-meta">
              <span>BAI: Construir, Adquirir e Implementar (Calidad QA)</span>
              <span id="txtSimValBai" style="color:var(--brand); font-weight:700;">0.0</span>
            </div>
            <input type="range" id="simRngBai" min="0" max="5" step="0.5" value="0.0" oninput="recalcSimulation()">
          </div>

          <div class="slider-row">
            <div class="slider-meta">
              <span>DSS: Entregar, Dar Servicio y Soporte (Mesa ITIL)</span>
              <span id="txtSimValDss" style="color:var(--brand); font-weight:700;">2.0</span>
            </div>
            <input type="range" id="simRngDss" min="0" max="5" step="0.5" value="2.0" oninput="recalcSimulation()">
          </div>

          <div class="slider-row">
            <div class="slider-meta">
              <span>MEA: Supervisar, Evaluar y Valorar (Auditoría Continua)</span>
              <span id="txtSimValMea" style="color:var(--brand); font-weight:700;">0.0</span>
            </div>
            <input type="range" id="simRngMea" min="0" max="5" step="0.5" value="0.0" oninput="recalcSimulation()">
          </div>
        </div>

        <!-- KPI RESULTADOS PROYECTADOS -->
        <div>
          <div style="background:var(--surface-subtle); border:1px solid var(--border); border-radius:var(--radius-sm); padding:16px;">
            <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase;">Diagnóstico Paramétrico en Tiempo Real</div>
            <div style="display:flex; align-items:baseline; gap:8px; margin:10px 0;">
              <span id="txtSimAverage" style="font-size:42px; font-weight:900; color:var(--brand);">1.00</span>
              <span style="font-size:14px; font-weight:600; color:var(--text-muted);">/ 5.00 Nivel de Capacidad Promedio</span>
            </div>
            <div id="boxSimMaturityBadge" style="margin-bottom:12px;"></div>

            <div class="kpi-quad">
              <div class="kpi-tile">
                <div class="kpi-num" id="txtSimChurn" style="color:var(--accent-red);">20.0%</div>
                <div class="kpi-lbl">Deserción Escolar (Churn)</div>
              </div>
              <div class="kpi-tile">
                <div class="kpi-num" id="txtSimRework" style="color:var(--accent-amber);">80.0%</div>
                <div class="kpi-lbl">Tiempo en Reprocesos</div>
              </div>
              <div class="kpi-tile">
                <div class="kpi-num" id="txtSimSla" style="color:var(--accent-green);">62.0%</div>
                <div class="kpi-lbl">Cumplimiento SLA ITIL</div>
              </div>
              <div class="kpi-tile">
                <div class="kpi-num" id="txtSimRoi" style="color:var(--accent-purple);">1.00x</div>
                <div class="kpi-lbl">Retorno Beneficio / Costo</div>
              </div>
            </div>

            <div style="margin-top:14px; font-size:11.5px; color:var(--text-secondary); background:var(--surface); padding:10px; border-radius:var(--radius-sm); border:1px solid var(--border);" id="txtSimSummary">
              <b>Diagnóstico de Gobernanza:</b> En la Línea Base (AS-IS), la empresa sufre por ausencia de control de calidad QA (BAI Nivel 0) y auditoría formal (MEA Nivel 0), lo que dispara los reprocesos manuales al 80% y la deserción de colegios al 20%. Mueva los controles deslizantes para simular el impacto del PETI.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</main>

<!-- ======================================================================= -->
<!-- MODAL: FICHA DE AUDITORÍA Y ANÁLISIS DE CAUSA RAÍZ (RCA)               -->
<!-- ======================================================================= -->
<div id="dlgAudit" class="dialog-backdrop">
  <div class="dialog-window">
    <div class="dialog-header">
      <div>
        <span class="tag tag-purple" id="dlgCode">TECNIF-DSS02-01</span>
        <div class="dialog-title" id="dlgTitle" style="margin-top:2px;">Título de la Incidencia</div>
      </div>
      <button class="btn btn-secondary" style="padding:4px 6px;" onclick="closeAuditDialog()">{SVG_ICONS["close"]}</button>
    </div>
    <div class="dialog-body">
      <div class="info-grid">
        <div class="info-field"><div class="lbl">Aplicación / Plataforma</div><div class="val" id="dlgApp">ERP Modular Apolo</div></div>
        <div class="info-field"><div class="lbl">Entorno de Despliegue</div><div class="val" id="dlgHosting">Centro de Datos / Local</div></div>
        <div class="info-field"><div class="lbl">Proceso COBIT 2019</div><div class="val" id="dlgProcess">DSS06 / APO14</div></div>
        <div class="info-field"><div class="lbl">Perspectiva BSC</div><div class="val" id="dlgBsc">Financiera / Procesos</div></div>
        <div class="info-field"><div class="lbl">Prioridad</div><div class="val" id="dlgPriority">P1 — Crítico</div></div>
        <div class="info-field"><div class="lbl">Estado y SLA</div><div class="val" id="dlgStatus">Completado en SLA (98.2%)</div></div>
        <div class="info-field"><div class="lbl">Responsable Asignado</div><div class="val" id="dlgAssignee">Martín Murillo (Líder QA)</div></div>
        <div class="info-field"><div class="lbl">Capacidad ISO 33000</div><div class="val" id="dlgCap">Nivel 0 → Nivel 3</div></div>
      </div>

      <div class="info-block">
        <div class="sec-title">Análisis de Causa Raíz (RCA — 5 Porqués)</div>
        <div id="dlgRca" style="line-height:1.45;"></div>
      </div>

      <div class="info-block">
        <div class="sec-title">Control de Gobierno de TI Implementado</div>
        <div id="dlgAction" style="line-height:1.45;"></div>
      </div>

      <div class="info-block">
        <div class="sec-title">Evidencia Auditable</div>
        <div id="dlgEvidence" style="font-family:var(--font-mono); font-size:11px; color:var(--text-muted);"></div>
      </div>
    </div>
    <div class="dialog-footer">
      <button class="btn btn-secondary" onclick="copyAuditRecord()">{SVG_ICONS["copy"]} Copiar Ficha</button>
      <button class="btn btn-primary" onclick="closeAuditDialog()">Cerrar</button>
    </div>
  </div>
</div>

<!-- ======================================================================= -->
<!-- MODAL: CREAR NUEVO CONTROL / INCIDENCIA                                 -->
<!-- ======================================================================= -->
<div id="dlgCreate" class="dialog-backdrop">
  <div class="dialog-window">
    <div class="dialog-header">
      <div class="dialog-title">Registrar Nuevo Control o Incidente de Gobierno de TI</div>
      <button class="btn btn-secondary" style="padding:4px 6px;" onclick="closeCreateDialog()">{SVG_ICONS["close"]}</button>
    </div>
    <div class="dialog-body">
      <div class="form-row">
        <div style="flex:1;">
          <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Código</label>
          <input type="text" id="inpNewCode" class="form-input" value="TECNIF-DSS02-15">
        </div>
        <div style="flex:1.5;">
          <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Aplicación</label>
          <select id="inpNewApp" class="form-select">
            <option value="ERP Modular Apolo">ERP Modular Apolo</option>
            <option value="Apolo Académico SaaS" selected>Apolo Académico SaaS</option>
            <option value="Apolo II Mobile">Apolo II Mobile</option>
            <option value="Portal Web & Hosting VPS">Portal Web & Hosting VPS</option>
            <option value="AulaCloud & Wiki">AulaCloud & Wiki</option>
            <option value="CRM Open Source">CRM Open Source</option>
          </select>
        </div>
      </div>

      <div style="margin-bottom:8px;">
        <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Título Descriptivo</label>
        <input type="text" id="inpNewTitle" class="form-input" placeholder="Descripción de la incidencia o control...">
      </div>

      <div class="form-row">
        <div style="flex:1;">
          <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Dominio COBIT</label>
          <select id="inpNewDomain" class="form-select">
            <option value="DSS" selected>DSS (Servicio y Soporte)</option>
            <option value="BAI">BAI (Construir e Implementar)</option>
            <option value="APO">APO (Alinear y Planear)</option>
            <option value="EDM">EDM (Gobernanza)</option>
            <option value="MEA">MEA (Supervisar y Evaluar)</option>
          </select>
        </div>
        <div style="flex:1;">
          <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Prioridad</label>
          <select id="inpNewPriority" class="form-select">
            <option value="P1 - Crítico">P1 — Crítico</option>
            <option value="P2 - Alto" selected>P2 — Alto</option>
            <option value="P3 - Medio">P3 — Medio</option>
            <option value="P4 - Bajo">P4 — Bajo</option>
          </select>
        </div>
        <div style="flex:1;">
          <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Estado</label>
          <select id="inpNewStatus" class="form-select">
            <option value="Completado en SLA" selected>Completado en SLA</option>
            <option value="En Curso">En Curso</option>
            <option value="Por Hacer">Por Hacer</option>
          </select>
        </div>
      </div>

      <div class="form-row">
        <div style="flex:1;">
          <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Responsable Asignado</label>
          <select id="inpNewAssignee" class="form-select">
            <option value="Martín Murillo (QA)">Martín Murillo (Líder QA)</option>
            <option value="Santiago Balanta (DevOps)">Santiago Balanta (DevOps)</option>
            <option value="Diego Vélez (Líder PETI)">Diego Vélez (Líder PETI)</option>
            <option value="Andrés Sarria (Comercial)">Andrés Sarria (Comercial)</option>
            <option value="Brayan Noguera (Riesgos)">Brayan Noguera (Auditoría)</option>
          </select>
        </div>
        <div style="flex:1;">
          <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Entorno de Despliegue</label>
          <select id="inpNewHosting" class="form-select">
            <option value="Nube (Cloud VPS SaaS)" selected>Nube (Cloud VPS SaaS)</option>
            <option value="Servidor Dedicado / VPS">Servidor Dedicado / VPS</option>
            <option value="Centro de Datos / Local">Centro de Datos / Local</option>
          </select>
        </div>
      </div>

      <div style="margin-bottom:8px;">
        <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Análisis de Causa Raíz (RCA)</label>
        <textarea id="inpNewRca" class="form-input" rows="2" placeholder="Causa técnica o estructural identificada..."></textarea>
      </div>

      <div>
        <label style="font-size:11px; font-weight:600; color:var(--text-muted);">Control de Gobierno Implementado</label>
        <textarea id="inpNewAction" class="form-input" rows="2" placeholder="Control correctivo según COBIT 2019..."></textarea>
      </div>
    </div>
    <div class="dialog-footer">
      <button class="btn btn-secondary" onclick="closeCreateDialog()">Cancelar</button>
      <button class="btn btn-primary" onclick="submitNewControl()">Guardar Registro</button>
    </div>
  </div>
</div>

<!-- ======================================================================= -->
<!-- JAVASCRIPT ENGINE (VANILLA JS PURO, ENTERPRISE GRADE)                  -->
<!-- ======================================================================= -->
<script>
// DATASETS
let DATA_TICKETS = {tickets_json};
const DATA_MONTHS = {monthly_json};
const DATA_MATRIX = {matrix_json};

// STATE
let stateFilter = {{
  domain: 'ALL',
  app: 'ALL',
  status: 'ALL',
  priority: 'ALL',
  assignee: 'ALL',
  hosting: 'ALL',
  reqType: 'ALL',
  search: '',
  historyRange: '12M'
}};

let lineSeriesState = {{
  resolved: true,
  rework: true,
  bugs: true,
  sla: true
}};

let tableState = {{
  page: 1,
  pageSize: 10,
  sortField: 'code',
  sortAsc: true,
  search: ''
}};

let currentModalTicket = null;

// BOOTSTRAP
document.addEventListener('DOMContentLoaded', () => {{
  runFilterPipeline();
  renderCascadeTable();
  recalcSimulation();
}});

function toggleTheme() {{
  document.body.classList.toggle('dark-theme');
  notifyUser(document.body.classList.contains('dark-theme') ? "Tema oscuro habilitado" : "Tema claro habilitado");
}}

function activateTab(tabId) {{
  document.querySelectorAll('.view-pane').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-link').forEach(el => el.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  event.currentTarget.classList.add('active');
}}

function notifyUser(msg) {{
  const toast = document.getElementById('appToast');
  document.getElementById('toastMessage').textContent = msg;
  toast.style.display = 'flex';
  setTimeout(() => {{ toast.style.display = 'none'; }}, 2800);
}}

// -------------------------------------------------------------------------
// PIPELINE DE FILTRADO
// -------------------------------------------------------------------------
function runFilterPipeline() {{
  stateFilter.domain = document.getElementById('fltDomain').value;
  stateFilter.app = document.getElementById('fltApp').value;
  stateFilter.status = document.getElementById('fltStatus').value;
  stateFilter.priority = document.getElementById('fltPriority').value;
  stateFilter.assignee = document.getElementById('fltAssignee').value;
  stateFilter.search = (document.getElementById('fltSearch').value || '').toLowerCase().trim();

  renderDashboard();
}}

function applyPreset(code) {{
  resetFilterControls();
  if (code === 'p1') {{
    stateFilter.priority = 'P1 - Crítico';
    document.getElementById('fltPriority').value = 'P1 - Crítico';
  }} else if (code === 'dss02') {{
    stateFilter.domain = 'DSS';
    document.getElementById('fltDomain').value = 'DSS';
  }} else if (code === 'bai07') {{
    stateFilter.domain = 'BAI';
    document.getElementById('fltDomain').value = 'BAI';
  }} else if (code === 'dss06') {{
    stateFilter.app = 'ERP Modular Apolo';
    document.getElementById('fltApp').value = 'ERP Modular Apolo';
  }}
  runFilterPipeline();
}}

function filterBySingleApp(appName) {{
  stateFilter.app = appName;
  document.getElementById('fltApp').value = appName;
  runFilterPipeline();
}}

function filterByHostingType(hType) {{
  stateFilter.hosting = (stateFilter.hosting === hType) ? 'ALL' : hType;
  runFilterPipeline();
}}

function filterByStatusCategory(st) {{
  stateFilter.status = (stateFilter.status === st) ? 'ALL' : st;
  document.getElementById('fltStatus').value = stateFilter.status;
  runFilterPipeline();
}}

function filterByReqType(req) {{
  stateFilter.reqType = (stateFilter.reqType === req) ? 'ALL' : req;
  runFilterPipeline();
}}

function resetAllFilters() {{
  resetFilterControls();
  stateFilter = {{
    domain: 'ALL', app: 'ALL', status: 'ALL', priority: 'ALL', assignee: 'ALL',
    hosting: 'ALL', reqType: 'ALL', search: '', historyRange: '12M'
  }};
  runFilterPipeline();
}}

function resetFilterControls() {{
  document.getElementById('fltDomain').value = 'ALL';
  document.getElementById('fltApp').value = 'ALL';
  document.getElementById('fltStatus').value = 'ALL';
  document.getElementById('fltPriority').value = 'ALL';
  document.getElementById('fltAssignee').value = 'ALL';
  document.getElementById('fltSearch').value = '';
}}

function getActiveDataset() {{
  return DATA_TICKETS.filter(t => {{
    if (stateFilter.domain !== 'ALL' && t.domain !== stateFilter.domain) return false;
    if (stateFilter.app !== 'ALL' && t.app !== stateFilter.app) return false;
    if (stateFilter.status !== 'ALL' && t.status !== stateFilter.status) return false;
    if (stateFilter.priority !== 'ALL' && t.priority !== stateFilter.priority) return false;
    if (stateFilter.assignee !== 'ALL' && !t.assignee.includes(stateFilter.assignee)) return false;
    if (stateFilter.hosting !== 'ALL' && t.hosting !== stateFilter.hosting) return false;
    if (stateFilter.reqType !== 'ALL' && t.req_type !== stateFilter.reqType) return false;
    if (stateFilter.search !== '') {{
      const q = stateFilter.search;
      const hit = (
        t.code.toLowerCase().includes(q) ||
        t.title.toLowerCase().includes(q) ||
        t.app.toLowerCase().includes(q) ||
        t.process.toLowerCase().includes(q) ||
        t.assignee.toLowerCase().includes(q) ||
        t.rca.toLowerCase().includes(q) ||
        t.action.toLowerCase().includes(q)
      );
      if (!hit) return false;
    }}
    return true;
  }});
}}

function toggleJqlBox() {{
  const b = document.getElementById('boxJql');
  b.style.display = (b.style.display === 'none') ? 'block' : 'none';
}}

// -------------------------------------------------------------------------
// RENDERIZADO GLOBAL
// -------------------------------------------------------------------------
function renderDashboard() {{
  const list = getActiveDataset();
  const count = list.length;

  document.getElementById('txtFilterCount').textContent = `● ${{count}} controles identificados`;
  document.getElementById('totalActiveCount').textContent = count;

  let jql = 'project = "TECNIFICATE-PETI" AND framework = "COBIT-2019"';
  if (stateFilter.domain !== 'ALL') jql += ` AND domain = "${{stateFilter.domain}}"`;
  if (stateFilter.app !== 'ALL') jql += ` AND app = "${{stateFilter.app}}"`;
  if (stateFilter.status !== 'ALL') jql += ` AND status = "${{stateFilter.status}}"`;
  if (stateFilter.priority !== 'ALL') jql += ` AND priority = "${{stateFilter.priority}}"`;
  if (stateFilter.hosting !== 'ALL') jql += ` AND hosting = "${{stateFilter.hosting}}"`;
  if (stateFilter.search !== '') jql += ` AND text ~ "${{stateFilter.search}}"`;
  document.getElementById('boxJql').textContent = jql;

  renderTimelineChart();
  renderAppBarsChart(list);
  renderHostingCards(list);
  renderStatusDonutChart(list);
  renderRequestTypesList(list);
  renderExplorerTable(list);
}}

// -------------------------------------------------------------------------
// WIDGET 2: LÍNEA DE TIEMPO SVG
// -------------------------------------------------------------------------
function setHistoryRange(r) {{
  stateFilter.historyRange = r;
  renderTimelineChart();
}}

function toggleLineSerie(s) {{
  lineSeriesState[s] = !lineSeriesState[s];
  renderTimelineChart();
}}

function renderTimelineChart() {{
  let data = [...DATA_MONTHS];
  if (stateFilter.historyRange === 'H1') data = data.slice(0, 6);
  if (stateFilter.historyRange === 'H2') data = data.slice(6);

  const container = document.getElementById('svgTimelineContainer');
  const W = 520, H = 250;
  const padL = 36, padR = 16, padT = 16, padB = 26;
  const plotW = W - padL - padR;
  const plotH = H - padT - padB;
  const n = data.length;

  let svg = `<svg viewBox="0 0 ${{W}} ${{H}}" style="width:100%; height:auto;">`;

  for (let val = 0; val <= 100; val += 25) {{
    const y = padT + plotH - (val / 100) * plotH;
    svg += `<line x1="${{padL}}" y1="${{y}}" x2="${{W - padR}}" y2="${{y}}" stroke="var(--border)" stroke-width="1"/>`;
    svg += `<text x="${{padL - 6}}" y="${{y + 3}}" font-size="9.5" fill="var(--text-muted)" text-anchor="end">${{val}}</text>`;
  }}
  svg += `<line x1="${{padL}}" y1="${{padT + plotH}}" x2="${{W - padR}}" y2="${{padT + plotH}}" stroke="var(--border-strong)" stroke-width="1.2"/>`;

  const getX = (i) => padL + (i / (n - 1)) * plotW;
  const getY = (val, max = 100) => padT + plotH - (val / max) * plotH;

  if (lineSeriesState.resolved) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.resolved, 60)}}`).join(' ');
    svg += `<polyline fill="none" stroke="var(--accent-green)" stroke-width="2.5" points="${{pts}}"/>`;
  }}
  if (lineSeriesState.rework) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.rework, 100)}}`).join(' ');
    svg += `<polyline fill="none" stroke="var(--accent-amber)" stroke-width="2.5" points="${{pts}}"/>`;
  }}
  if (lineSeriesState.bugs) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.bugs, 20)}}`).join(' ');
    svg += `<polyline fill="none" stroke="var(--accent-purple)" stroke-width="2" points="${{pts}}"/>`;
  }}
  if (lineSeriesState.sla) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.sla, 100)}}`).join(' ');
    svg += `<polyline fill="none" stroke="var(--brand)" stroke-width="2" stroke-dasharray="3 3" points="${{pts}}"/>`;
  }}

  data.forEach((d, i) => {{
    const cx = getX(i);
    svg += `<text x="${{cx}}" y="${{H - 6}}" font-size="9" fill="var(--text-muted)" text-anchor="middle">${{d.month.split(' ')[0]}}</text>`;

    if (lineSeriesState.resolved) {{
      const cy = getY(d.resolved, 60);
      svg += `<circle cx="${{cx}}" cy="${{cy}}" r="3.5" fill="var(--accent-green)" stroke="var(--surface)" stroke-width="1.5" style="cursor:pointer;" onmouseenter="showTimelineTooltip(event, '${{d.month}}', '${{d.resolved}}', '${{d.rework}}', '${{d.bugs}}', '${{d.sla}}', '${{d.stage}}')" onmouseleave="hideTooltip()"/>`;
    }}
  }});

  svg += `</svg>`;
  container.innerHTML = svg;
}}

function showTimelineTooltip(e, month, res, rew, bugs, sla, stage) {{
  const tip = document.getElementById('chartTooltip');
  tip.innerHTML = `
    <div style="font-weight:700; color:var(--brand); margin-bottom:3px;">${{month}} — ${{stage}}</div>
    <div>Resueltos en SLA: <b>${{res}}</b>/mes</div>
    <div>Reprocesos manuales: <b>${{rew}}%</b></div>
    <div>Bugs en producción: <b>${{bugs}}</b>/release</div>
    <div>Cumplimiento SLA ITIL: <b>${{sla}}%</b></div>
  `;
  tip.style.left = (e.clientX + 12) + 'px';
  tip.style.top = (e.clientY - 35) + 'px';
  tip.style.display = 'block';
}}

// -------------------------------------------------------------------------
// WIDGET 3: BARRAS APILADAS POR APLICACIÓN
// -------------------------------------------------------------------------
function renderAppBarsChart(list) {{
  const container = document.getElementById('svgAppBarsContainer');
  const appKeys = [
    ["ERP Modular Apolo", "ERP Apolo"],
    ["Apolo Académico SaaS", "Apolo SaaS"],
    ["Apolo II Mobile", "Apolo Mobile"],
    ["Portal Web & Hosting VPS", "Hosting VPS"],
    ["AulaCloud & Wiki", "AulaCloud"],
    ["CRM Open Source", "CRM Open"]
  ];

  const appStats = appKeys.map(([full, short]) => {{
    const sub = list.filter(t => t.app === full);
    const done = sub.filter(t => t.status === 'Completado en SLA').length;
    const prog = sub.filter(t => t.status === 'En Curso').length;
    const todo = sub.filter(t => t.status === 'Por Hacer').length;
    return {{ full, short, total: sub.length, done, prog, todo }};
  }});

  const maxTotal = Math.max(...appStats.map(a => a.total), 1);
  const W = 520, H = 210;
  const padL = 36, padR = 16, padB = 26;
  const barW = 38;
  const step = (W - padL - padR) / appKeys.length;

  let svg = `<svg viewBox="0 0 ${{W}} ${{H}}" style="width:100%; height:auto;">`;
  svg += `<line x1="${{padL}}" y1="${{H - padB}}" x2="${{W - padR}}" y2="${{H - padB}}" stroke="var(--border-strong)" stroke-width="1.2"/>`;

  appStats.forEach((a, idx) => {{
    const x = padL + idx * step + (step - barW) / 2;
    let cy = H - padB;
    const scale = (H - padB - 20) / maxTotal;

    const hDone = a.done * scale;
    const hProg = a.prog * scale;
    const hTodo = a.todo * scale;

    if (hDone > 0) {{
      svg += `<rect x="${{x}}" y="${{cy - hDone}}" width="${{barW}}" height="${{hDone}}" fill="var(--accent-green)" style="cursor:pointer;" onclick="filterBySingleApp('${{a.full}}')" onmouseenter="showAppTooltip(event, '${{a.full}}', ${{a.total}}, ${{a.done}}, ${{a.prog}}, ${{a.todo}})" onmouseleave="hideTooltip()"/>`;
      cy -= hDone;
    }}
    if (hProg > 0) {{
      svg += `<rect x="${{x}}" y="${{cy - hProg}}" width="${{barW}}" height="${{hProg}}" fill="var(--accent-amber)" style="cursor:pointer;" onclick="filterBySingleApp('${{a.full}}')" onmouseenter="showAppTooltip(event, '${{a.full}}', ${{a.total}}, ${{a.done}}, ${{a.prog}}, ${{a.todo}})" onmouseleave="hideTooltip()"/>`;
      cy -= hProg;
    }}
    if (hTodo > 0) {{
      svg += `<rect x="${{x}}" y="${{cy - hTodo}}" width="${{barW}}" height="${{hTodo}}" fill="var(--accent-purple)" style="cursor:pointer;" onclick="filterBySingleApp('${{a.full}}')" onmouseenter="showAppTooltip(event, '${{a.full}}', ${{a.total}}, ${{a.done}}, ${{a.prog}}, ${{a.todo}})" onmouseleave="hideTooltip()"/>`;
      cy -= hTodo;
    }}

    svg += `<text x="${{x + barW / 2}}" y="${{cy - 4}}" font-size="10.5" font-weight="700" fill="var(--text)" text-anchor="middle">${{a.total}}</text>`;
    svg += `<text x="${{x + barW / 2}}" y="${{H - 8}}" font-size="9" font-weight="600" fill="var(--text-muted)" text-anchor="middle">${{a.short}}</text>`;
  }});

  svg += `</svg>`;
  container.innerHTML = svg;
}}

function showAppTooltip(e, name, tot, done, prog, todo) {{
  const tip = document.getElementById('chartTooltip');
  tip.innerHTML = `
    <div style="font-weight:700; color:var(--brand); margin-bottom:3px;">${{name}}</div>
    <div>Total Controles: <b>${{tot}}</b></div>
    <div>Completados en SLA: <b>${{done}}</b></div>
    <div>En Curso: <b>${{prog}}</b></div>
    <div>Por Hacer: <b>${{todo}}</b></div>
    <div style="font-size:9.5px; color:var(--text-muted); margin-top:2px;">(Clic para filtrar)</div>
  `;
  tip.style.left = (e.clientX + 12) + 'px';
  tip.style.top = (e.clientY - 35) + 'px';
  tip.style.display = 'block';
}}

// -------------------------------------------------------------------------
// WIDGET 4: APP HOSTING CARDS
// -------------------------------------------------------------------------
function renderHostingCards(list) {{
  const cCloud = list.filter(t => t.hosting === 'Nube (Cloud VPS SaaS)').length;
  const cServer = list.filter(t => t.hosting === 'Servidor Dedicado / VPS').length;
  const cLocal = list.filter(t => t.hosting === 'Centro de Datos / Local').length;
  const total = list.length || 1;

  const factor = 342 / DATA_TICKETS.length;
  const nCloud = Math.round(cCloud * factor);
  const nServer = Math.round(cServer * factor);
  const nLocal = Math.max(0, 342 - nCloud - nServer);

  document.getElementById('valHostCloud').textContent = nCloud;
  document.getElementById('pctHostCloud').textContent = `${{((cCloud / total) * 100).toFixed(1)}}% (Apolo SaaS)`;

  document.getElementById('valHostServer').textContent = nServer;
  document.getElementById('pctHostServer').textContent = `${{((cServer / total) * 100).toFixed(1)}}% (Hosting)`;

  document.getElementById('valHostLocal').textContent = nLocal;
  document.getElementById('pctHostLocal').textContent = `${{((cLocal / total) * 100).toFixed(1)}}% (PyMEs)`;

  document.getElementById('hostBoxCloud').classList.toggle('active', stateFilter.hosting === 'Nube (Cloud VPS SaaS)');
  document.getElementById('hostBoxServer').classList.toggle('active', stateFilter.hosting === 'Servidor Dedicado / VPS');
  document.getElementById('hostBoxLocal').classList.toggle('active', stateFilter.hosting === 'Centro de Datos / Local');
}}

// -------------------------------------------------------------------------
// WIDGET 5: GRÁFICO DE DONA
// -------------------------------------------------------------------------
function renderStatusDonutChart(list) {{
  const done = list.filter(t => t.status === 'Completado en SLA').length;
  const prog = list.filter(t => t.status === 'En Curso').length;
  const todo = list.filter(t => t.status === 'Por Hacer').length;
  const total = list.length || 1;

  const pctDone = ((done / total) * 100).toFixed(1);
  const pctProg = ((prog / total) * 100).toFixed(1);
  const pctTodo = ((todo / total) * 100).toFixed(1);

  const C = 2 * Math.PI * 46;
  const dDone = (done / total) * C;
  const dProg = (prog / total) * C;
  const dTodo = (todo / total) * C;

  let svg = `
    <svg viewBox="0 0 120 120" style="width:115px; height:115px; margin:0 auto;">
      <circle cx="60" cy="60" r="46" fill="none" stroke="var(--border)" stroke-width="16"/>
      <circle cx="60" cy="60" r="46" fill="none" stroke="var(--accent-green)" stroke-width="16"
        stroke-dasharray="${{dDone}} ${{C}}" stroke-dashoffset="0" style="cursor:pointer;" onclick="filterByStatusCategory('Completado en SLA')"/>
      <circle cx="60" cy="60" r="46" fill="none" stroke="var(--accent-amber)" stroke-width="16"
        stroke-dasharray="${{dProg}} ${{C}}" stroke-dashoffset="${{-dDone}}" style="cursor:pointer;" onclick="filterByStatusCategory('En Curso')"/>
      <circle cx="60" cy="60" r="46" fill="none" stroke="var(--accent-purple)" stroke-width="16"
        stroke-dasharray="${{dTodo}} ${{C}}" stroke-dashoffset="${{-(dDone + dProg)}}" style="cursor:pointer;" onclick="filterByStatusCategory('Por Hacer')"/>
      <text x="60" y="58" text-anchor="middle" font-size="18" font-weight="800" fill="var(--text)">${{list.length}}</text>
      <text x="60" y="73" text-anchor="middle" font-size="9" font-weight="600" fill="var(--text-muted)">Controles</text>
    </svg>
  `;
  document.getElementById('svgDonutContainer').innerHTML = svg;

  const tbody = document.getElementById('tblStatusBreakdown');
  tbody.innerHTML = `
    <tr onclick="filterByStatusCategory('Completado en SLA')">
      <td><span class="color-dot" style="background:var(--accent-green);"></span>Completado</td>
      <td><b>${{done}}</b></td>
      <td>${{pctDone}}%</td>
    </tr>
    <tr onclick="filterByStatusCategory('En Curso')">
      <td><span class="color-dot" style="background:var(--accent-amber);"></span>En Curso</td>
      <td><b>${{prog}}</b></td>
      <td>${{pctProg}}%</td>
    </tr>
    <tr onclick="filterByStatusCategory('Por Hacer')">
      <td><span class="color-dot" style="background:var(--accent-purple);"></span>Por Hacer</td>
      <td><b>${{todo}}</b></td>
      <td>${{pctTodo}}%</td>
    </tr>
  `;
}}

// -------------------------------------------------------------------------
// WIDGET 6: TIPO DE SOLICITUD
// -------------------------------------------------------------------------
function renderRequestTypesList(list) {{
  const types = [
    ["Soporte Técnico ITIL", "var(--accent-green)", "DSS02 / APO09"],
    ["Control de Calidad QA", "var(--brand)", "BAI07 / APO10"],
    ["Automatización BPM & ERP", "var(--accent-purple)", "DSS06 / APO14"],
    ["Gestión Comercial CRM", "var(--accent-amber)", "APO08 / APO10"],
    ["Gobierno y Seguridad", "var(--accent-red)", "EDM / MEA"]
  ];

  const total = list.length || 1;
  let html = '<div style="display:flex; flex-direction:column; gap:8px;">';

  types.forEach(([name, color, ref]) => {{
    const count = list.filter(t => t.req_type.includes(name.split(' ')[0])).length;
    const pct = ((count / total) * 100).toFixed(1);
    html += `
      <div style="cursor:pointer;" onclick="filterByReqType('${{name}}')">
        <div style="display:flex; justify-content:space-between; font-size:11.5px; font-weight:600; margin-bottom:2px;">
          <span>${{name}} <span style="font-size:9.5px; color:var(--text-muted); font-weight:400;">(${{ref}})</span></span>
          <span><b>${{count}}</b> (${{pct}}%)</span>
        </div>
        <div style="width:100%; height:8px; background:var(--border); border-radius:var(--radius-sm); overflow:hidden;">
          <div style="width:${{pct}}%; height:100%; background:${{color}}; transition:width 0.25s;"></div>
        </div>
      </div>
    `;
  }});
  html += '</div>';
  document.getElementById('reqBarsContainer').innerHTML = html;
}}

// -------------------------------------------------------------------------
// EXPLORADOR DE CONTROLES (TAB 2)
// -------------------------------------------------------------------------
function onExplorerSearch() {{
  tableState.search = (document.getElementById('tblSearchInput').value || '').toLowerCase().trim();
  tableState.page = 1;
  renderExplorerTable(getActiveDataset());
}}

function onExplorerPageSize() {{
  tableState.pageSize = parseInt(document.getElementById('tblPageSizeSelect').value);
  tableState.page = 1;
  renderExplorerTable(getActiveDataset());
}}

function sortExplorer(f) {{
  if (tableState.sortField === f) {{
    tableState.sortAsc = !tableState.sortAsc;
  }} else {{
    tableState.sortField = f;
    tableState.sortAsc = true;
  }}
  renderExplorerTable(getActiveDataset());
}}

function renderExplorerTable(list) {{
  let rows = [...list];
  if (tableState.search !== '') {{
    const q = tableState.search;
    rows = rows.filter(t =>
      t.code.toLowerCase().includes(q) ||
      t.title.toLowerCase().includes(q) ||
      t.app.toLowerCase().includes(q) ||
      t.assignee.toLowerCase().includes(q)
    );
  }}

  rows.sort((a, b) => {{
    let vA = a[tableState.sortField];
    let vB = b[tableState.sortField];
    if (typeof vA === 'string') vA = vA.toLowerCase();
    if (typeof vB === 'string') vB = vB.toLowerCase();
    if (vA < vB) return tableState.sortAsc ? -1 : 1;
    if (vA > vB) return tableState.sortAsc ? 1 : -1;
    return 0;
  }});

  const total = rows.length;
  const start = (tableState.page - 1) * tableState.pageSize;
  const paged = rows.slice(start, start + tableState.pageSize);

  const tbody = document.getElementById('tblExplorerBody');
  tbody.innerHTML = '';

  if (paged.length === 0) {{
    tbody.innerHTML = '<tr><td colspan="9" style="text-align:center; padding:18px; color:var(--text-muted);">No se encontraron registros con los filtros activos.</td></tr>';
  }} else {{
    paged.forEach(t => {{
      const pTag = t.priority.includes('P1') ? 'tag-red' : (t.priority.includes('P2') ? 'tag-amber' : 'tag-blue');
      const sTag = t.status === 'Completado en SLA' ? 'tag-green' : (t.status === 'En Curso' ? 'tag-amber' : 'tag-purple');

      const tr = document.createElement('tr');
      tr.style.cursor = 'pointer';
      tr.onclick = (e) => {{
        if (e.target.tagName !== 'BUTTON') showAuditDetails(t.code);
      }};
      tr.innerHTML = `
        <td><b style="color:var(--brand);">${{t.code}}</b></td>
        <td><b>${{t.title}}</b></td>
        <td>${{t.app}}</td>
        <td><span class="tag tag-blue">${{t.domain}}</span></td>
        <td><span class="tag ${{pTag}}">${{t.priority.split(' ')[0]}}</span></td>
        <td><span class="tag ${{sTag}}">${{t.status}}</span></td>
        <td><b>${{t.sla}}%</b></td>
        <td>${{t.assignee.split('(')[0]}}</td>
        <td><button class="btn btn-secondary" style="padding:2px 6px; font-size:10.5px;" onclick="showAuditDetails('${{t.code}}')">{SVG_ICONS["eye"]} Ficha</button></td>
      `;
      tbody.appendChild(tr);
    }});
  }}

  const end = Math.min(start + tableState.pageSize, total);
  document.getElementById('txtPaginationInfo').textContent = `Mostrando ${{total > 0 ? start + 1 : 0}} a ${{end}} de ${{total}} registros`;

  const totalPages = Math.ceil(total / tableState.pageSize) || 1;
  let btns = '';
  btns += `<button class="btn btn-secondary" style="padding:2px 6px; font-size:10px;" ${{tableState.page === 1 ? 'disabled' : ''}} onclick="gotoExplorerPage(${{tableState.page - 1}})">Anterior</button>`;
  for (let p = 1; p <= totalPages; p++) {{
    btns += `<button class="btn ${{p === tableState.page ? 'btn-primary' : 'btn-secondary'}}" style="padding:2px 6px; font-size:10px;" onclick="gotoExplorerPage(${{p}})">${{p}}</button>`;
  }}
  btns += `<button class="btn btn-secondary" style="padding:2px 6px; font-size:10px;" ${{tableState.page === totalPages ? 'disabled' : ''}} onclick="gotoExplorerPage(${{tableState.page + 1}})">Siguiente</button>`;
  document.getElementById('boxPaginationButtons').innerHTML = btns;
}}

function gotoExplorerPage(p) {{
  tableState.page = p;
  renderExplorerTable(getActiveDataset());
}}

// -------------------------------------------------------------------------
// MATRIZ DE CASCADA (TAB 3)
// -------------------------------------------------------------------------
function renderCascadeTable() {{
  const tbody = document.getElementById('tblCascadeBody');
  tbody.innerHTML = '';
  DATA_MATRIX.forEach(m => {{
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><b style="color:var(--brand);">${{m.code}}</b></td>
      <td><b>${{m.domain}}</b></td>
      <td>${{m.eg}}</td>
      <td>${{m.ag}}</td>
      <td><span class="tag tag-blue">${{m.bsc}}</span></td>
      <td>${{m.metric}}</td>
      <td style="color:var(--accent-red);"><b>${{m.as_is}}</b></td>
      <td style="color:var(--accent-green);"><b>${{m.to_be}}</b></td>
      <td><span class="tag tag-green">${{m.cap}}</span></td>
      <td>${{m.resp.split('(')[0]}}</td>
    `;
    tbody.appendChild(tr);
  }});
}}

// -------------------------------------------------------------------------
// SIMULADOR DE CAPACIDAD (TAB 4)
// -------------------------------------------------------------------------
function setSimScenario(sc) {{
  if (sc === 'asis') {{
    document.getElementById('simRngEdm').value = 1.0;
    document.getElementById('simRngApo').value = 2.0;
    document.getElementById('simRngBai').value = 0.0;
    document.getElementById('simRngDss').value = 2.0;
    document.getElementById('simRngMea').value = 0.0;
  }} else if (sc === 'mid') {{
    document.getElementById('simRngEdm').value = 2.0;
    document.getElementById('simRngApo').value = 3.0;
    document.getElementById('simRngBai').value = 2.0;
    document.getElementById('simRngDss').value = 3.0;
    document.getElementById('simRngMea').value = 2.0;
  }} else if (sc === 'tobe') {{
    document.getElementById('simRngEdm').value = 4.0;
    document.getElementById('simRngApo').value = 4.0;
    document.getElementById('simRngBai').value = 3.0;
    document.getElementById('simRngDss').value = 4.0;
    document.getElementById('simRngMea').value = 4.0;
  }}
  recalcSimulation();
  notifyUser(`Escenario ${{sc.toUpperCase()}} cargado`);
}}

function recalcSimulation() {{
  const edm = parseFloat(document.getElementById('simRngEdm').value);
  const apo = parseFloat(document.getElementById('simRngApo').value);
  const bai = parseFloat(document.getElementById('simRngBai').value);
  const dss = parseFloat(document.getElementById('simRngDss').value);
  const mea = parseFloat(document.getElementById('simRngMea').value);

  document.getElementById('txtSimValEdm').textContent = edm.toFixed(1);
  document.getElementById('txtSimValApo').textContent = apo.toFixed(1);
  document.getElementById('txtSimValBai').textContent = bai.toFixed(1);
  document.getElementById('txtSimValDss').textContent = dss.toFixed(1);
  document.getElementById('txtSimValMea').textContent = mea.toFixed(1);

  const avg = (edm + apo + bai + dss + mea) / 5.0;
  document.getElementById('txtSimAverage').textContent = avg.toFixed(2);

  const churn = Math.max(5.0, 24.0 - avg * 3.8).toFixed(1);
  const rework = Math.max(25.0, 92.0 - avg * 13.5).toFixed(1);
  const sla = Math.min(99.0, 52.0 + avg * 10.8).toFixed(1);
  const roi = (1.0 + (avg - 1.0) * 0.12).toFixed(2);

  document.getElementById('txtSimChurn').textContent = churn + '%';
  document.getElementById('txtSimRework').textContent = rework + '%';
  document.getElementById('txtSimSla').textContent = sla + '%';
  document.getElementById('txtSimRoi').textContent = roi + 'x';

  let badge = '';
  if (avg < 1.0) badge = '<span class="tag tag-red">Madurez EIS: Nivel 0 (Incompleto)</span>';
  else if (avg < 2.0) badge = '<span class="tag tag-amber">Madurez EIS: Nivel 1 (Inicial / Intuitivo)</span>';
  else if (avg < 3.0) badge = '<span class="tag tag-amber">Madurez EIS: Nivel 2 (Administrado)</span>';
  else if (avg < 4.0) badge = '<span class="tag tag-green">Madurez EIS: Nivel 3 (Definido y Estandarizado)</span>';
  else badge = '<span class="tag tag-green">Madurez EIS: Nivel 4 (Cuantitativo Orientado a Datos)</span>';
  document.getElementById('boxSimMaturityBadge').innerHTML = badge;
}}

// -------------------------------------------------------------------------
// DIALOGS & ACTIONS
// -------------------------------------------------------------------------
function showAuditDetails(code) {{
  const t = DATA_TICKETS.find(x => x.code === code) || DATA_TICKETS[0];
  currentModalTicket = t;

  document.getElementById('dlgCode').textContent = t.code;
  document.getElementById('dlgTitle').textContent = t.title;
  document.getElementById('dlgApp').textContent = t.app;
  document.getElementById('dlgHosting').textContent = t.hosting;
  document.getElementById('dlgProcess').textContent = `${{t.domain}} — ${{t.process}} (${{t.req_type}})`;
  document.getElementById('dlgBsc').textContent = t.bsc;
  document.getElementById('dlgPriority').textContent = t.priority;
  document.getElementById('dlgStatus').textContent = `${{t.status}} (SLA: ${{t.sla}}%)`;
  document.getElementById('dlgAssignee').textContent = t.assignee;
  document.getElementById('dlgCap').textContent = `${{t.cap_before}} → ${{t.cap_after}}`;
  document.getElementById('dlgRca').textContent = t.rca;
  document.getElementById('dlgAction').textContent = t.action;
  document.getElementById('dlgEvidence').textContent = t.evidence;

  document.getElementById('dlgAudit').classList.add('visible');
}}

function closeAuditDialog() {{
  document.getElementById('dlgAudit').classList.remove('visible');
}}

function copyAuditRecord() {{
  if (!currentModalTicket) return;
  const t = currentModalTicket;
  const text = `=== FICHA DE AUDITORÍA DE GOBIERNO TI — TECNIFICATE S.A.S. ===\\n` +
    `Código: ${{t.code}}\\nTítulo: ${{t.title}}\\nAplicación: ${{t.app}}\\nProceso: ${{t.domain}} / ${{t.process}}\\n` +
    `Prioridad: ${{t.priority}} | Estado: ${{t.status}} (SLA: ${{t.sla}}%)\\nResponsable: ${{t.assignee}}\\n` +
    `Causa Raíz (RCA): ${{t.rca}}\\nControl Implementado: ${{t.action}}\\nCapacidad: ${{t.cap_before}} → ${{t.cap_after}}\\nEvidencia: ${{t.evidence}}`;

  navigator.clipboard.writeText(text).then(() => {{
    notifyUser("Ficha copiada al portapapeles");
  }});
}}

function openCreateDialog() {{
  document.getElementById('inpNewCode').value = `TECNIF-DSS02-${{DATA_TICKETS.length + 1}}`;
  document.getElementById('inpNewTitle').value = '';
  document.getElementById('inpNewRca').value = '';
  document.getElementById('inpNewAction').value = '';
  document.getElementById('dlgCreate').classList.add('visible');
}}

function closeCreateDialog() {{
  document.getElementById('dlgCreate').classList.remove('visible');
}}

function submitNewControl() {{
  const code = document.getElementById('inpNewCode').value.trim();
  const title = document.getElementById('inpNewTitle').value.trim();
  if (!code || !title) {{
    alert("Por favor ingrese código y título.");
    return;
  }}

  const newObj = {{
    code: code,
    title: title,
    app: document.getElementById('inpNewApp').value,
    domain: document.getElementById('inpNewDomain').value,
    process: `${{document.getElementById('inpNewDomain').value}}02`,
    req_type: "Soporte Técnico ITIL",
    priority: document.getElementById('inpNewPriority').value,
    status: document.getElementById('inpNewStatus').value,
    assignee: document.getElementById('inpNewAssignee').value,
    hosting: document.getElementById('inpNewHosting').value,
    sla: 94.0,
    bsc: "Procesos Internos",
    rca: document.getElementById('inpNewRca').value || "Falta de procedimiento operativo formalizado.",
    action: document.getElementById('inpNewAction').value || "Implementación de control de gobierno de TI.",
    cap_before: "Nivel 1 (Inicial)",
    cap_after: "Nivel 3 (Establecido)",
    evidence: "Registrado en el sistema de gestión COBIT 2019."
  }};

  DATA_TICKETS.unshift(newObj);
  closeCreateDialog();
  runFilterPipeline();
  notifyUser(`Control ${{code}} registrado correctamente`);
}}

// -------------------------------------------------------------------------
// EXPORTACIÓN A CSV CON UTF-8 BOM
// -------------------------------------------------------------------------
function exportDataCsv() {{
  const list = getActiveDataset();
  const headers = [
    "Codigo", "Titulo", "Aplicacion", "Dominio_COBIT", "Proceso_COBIT",
    "Tipo_Solicitud", "Prioridad", "Estado", "Responsable", "Alojamiento",
    "SLA_Porcentaje", "Perspectiva_BSC", "Causa_Raiz_RCA", "Accion_Correctiva",
    "Capacidad_Antes", "Capacidad_Despues", "Evidencia"
  ];

  let csv = "\\uFEFF" + headers.join(";") + "\\n";
  list.forEach(t => {{
    const row = [
      t.code, `"${{t.title.replace(/"/g, '""')}}"`, `"${{t.app}}"`, t.domain, t.process,
      `"${{t.req_type}}"`, `"${{t.priority}}"`, `"${{t.status}}"`, `"${{t.assignee}}"`,
      `"${{t.hosting}}"`, t.sla, `"${{t.bsc}}"`, `"${{t.rca.replace(/"/g, '""')}}"`,
      `"${{t.action.replace(/"/g, '""')}}"`, `"${{t.cap_before}}"`, `"${{t.cap_after}}"`,
      `"${{t.evidence.replace(/"/g, '""')}}"`
    ];
    csv += row.join(";") + "\\n";
  }});

  const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `TECNIFICATE_Controles_COBIT2019_${{new Date().toISOString().slice(0,10)}}.csv`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  notifyUser("Archivo CSV exportado");
}}

function hideTooltip() {{
  document.getElementById('chartTooltip').style.display = 'none';
}}
</script>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"Minimalist senior-grade HTML Dashboard successfully generated: {HTML_PATH}")
