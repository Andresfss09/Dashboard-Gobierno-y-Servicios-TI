# -*- coding: utf-8 -*-
"""
Script que escribe Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html
Garantiza 100% español, codificación UTF-8 pura sin mojibake, e interactividad total.
"""
import os
import json

BASE_DIR = r"C:\Users\andre\.gemini\antigravity\scratch\Gobierno_TI_Tecnificate\Entregable_Actividad5_Dashboard_Estrategico_Metricas_COBIT2019"
HTML_PATH = os.path.join(BASE_DIR, "Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html")

# Importar dataset de build_full_act5
from build_full_act5 import tickets_dataset, monthly_data, cobit_matrix

tickets_json = json.dumps(tickets_dataset, ensure_ascii=False)
monthly_json = json.dumps(monthly_data, ensure_ascii=False)
matrix_json = json.dumps(cobit_matrix, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TECNIFICATE S.A.S. — Sistema de Gobernanza y Métricas COBIT 2019</title>
<style>
:root {{
  --bg-page: #f1f5f9;
  --bg-card: #ffffff;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --text-subtle: #475569;
  --border-color: #cbd5e1;
  --border-light: #e2e8f0;
  --primary: #0284c7;
  --primary-hover: #0369a1;
  --navy: #0f172a;
  --indigo: #4f46e5;
  --emerald: #10b981;
  --amber: #f59e0b;
  --rose: #ef4444;
  --cyan: #06b6d4;
  --card-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.03);
}}

body.dark-mode {{
  --bg-page: #0b1120;
  --bg-card: #1e293b;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-subtle: #cbd5e1;
  --border-color: #334155;
  --border-light: #1e293b;
  --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-page);
  color: var(--text-main);
  min-height: 100vh;
  line-height: 1.5;
  transition: background-color 0.2s, color 0.2s;
}}

/* BARRA SUPERIOR ESTILO ATLASSIAN JIRA CLOUD */
.topbar {{
  background: var(--bg-card);
  border-bottom: 1px solid var(--border-color);
  padding: 0 20px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}}

.topbar-left {{
  display: flex;
  align-items: center;
  gap: 18px;
}}

.brand-badge {{
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 800;
  font-size: 16px;
  color: var(--text-main);
  text-decoration: none;
}}

.brand-badge .logo-icon {{
  width: 34px;
  height: 34px;
  background: linear-gradient(135deg, #0284c7, #4f46e5);
  color: #fff;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 18px;
}}

.jira-menu {{
  display: flex;
  gap: 16px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--text-muted);
}}

.jira-menu span {{
  cursor: pointer;
  padding: 6px 4px;
  border-bottom: 2px solid transparent;
  transition: all 0.15s;
}}

.jira-menu span:hover {{
  color: var(--primary);
}}

.topbar-right {{
  display: flex;
  align-items: center;
  gap: 10px;
}}

.btn {{
  padding: 7px 14px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  border: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: background 0.15s, transform 0.05s;
}}
.btn:active {{ transform: scale(0.98); }}

.btn-primary {{ background: var(--primary); color: #fff; }}
.btn-primary:hover {{ background: var(--primary-hover); }}

.btn-dark {{ background: #0f172a; color: #fff; }}
.btn-dark:hover {{ background: #1e293b; }}

.btn-outline {{
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--text-main);
}}
.btn-outline:hover {{ background: rgba(0,0,0,0.03); }}

.user-badge {{
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  color: #1d4ed8;
  padding: 5px 12px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
}}
body.dark-mode .user-badge {{
  background: #1e3a8a;
  border-color: #3b82f6;
  color: #bfdbfe;
}}

/* BARRA DE VISTAS Y PESTAÑAS */
.view-tabs-bar {{
  background: var(--bg-card);
  border-bottom: 1px solid var(--border-color);
  padding: 0 20px;
  display: flex;
  gap: 8px;
  overflow-x: auto;
}}

.tab-btn {{
  padding: 12px 18px;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--text-muted);
  border: none;
  background: transparent;
  cursor: pointer;
  border-bottom: 3px solid transparent;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
}}

.tab-btn:hover {{ color: var(--primary); }}
.tab-btn.active {{
  color: var(--primary);
  border-bottom-color: var(--primary);
}}

/* CONTENEDOR PRINCIPAL */
.main-container {{
  max-width: 1720px;
  margin: 18px auto;
  padding: 0 18px 40px;
}}

.view-content {{ display: none; }}
.view-content.active {{ display: block; }}

/* GRID DEL TABLERO PRINCIPAL (ESTILO CUSTOM CHARTS) */
.custom-charts-grid {{
  display: grid;
  grid-template-columns: 1fr 1.05fr 1fr;
  gap: 16px;
  align-items: start;
}}

@media (max-width: 1200px) {{
  .custom-charts-grid {{ grid-template-columns: 1fr; }}
}}

.col-stack {{
  display: flex;
  flex-direction: column;
  gap: 16px;
}}

/* WIDGET CARD */
.widget-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
  overflow: hidden;
  transition: transform 0.15s, box-shadow 0.15s;
}}

.widget-card.top-red {{ border-top: 4px solid var(--rose); }}
.widget-card.top-green {{ border-top: 4px solid var(--emerald); }}
.widget-card.top-amber {{ border-top: 4px solid var(--amber); }}
.widget-card.top-blue {{ border-top: 4px solid var(--primary); }}
.widget-card.top-indigo {{ border-top: 4px solid var(--indigo); }}

.widget-hdr {{
  padding: 10px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border-light);
}}

.widget-hdr-right {{
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}}

.widget-body {{
  padding: 16px;
}}

.widget-title {{
  text-align: center;
  font-size: 15.5px;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 12px;
}}

/* FILTROS Y BÚSQUEDA RÁPIDA (SIMPLE SEARCH) */
.filter-row {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 10px;
}}

.filter-select {{
  padding: 7px 10px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  font-size: 12.5px;
  font-weight: 600;
  background: var(--bg-page);
  color: var(--text-main);
  cursor: pointer;
  outline: none;
  flex: 1;
  min-width: 140px;
}}
.filter-select:focus {{
  border-color: var(--primary);
  box-shadow: 0 0 0 2px rgba(2, 132, 199, 0.15);
}}

.search-input-box {{
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
}}

.search-input-box input {{
  flex: 1;
  padding: 8px 12px;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  font-size: 13px;
  background: var(--bg-page);
  color: var(--text-main);
  outline: none;
}}
.search-input-box input:focus {{
  border-color: var(--primary);
  box-shadow: 0 0 0 2px rgba(2, 132, 199, 0.15);
}}

.quick-presets {{
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}}

.preset-chip {{
  background: var(--bg-page);
  border: 1px solid var(--border-color);
  color: var(--text-subtle);
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 11.5px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
}}
.preset-chip:hover, .preset-chip.active {{
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}}

.filter-meta {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  font-weight: 700;
  padding-top: 4px;
}}

.jql-preview {{
  background: var(--bg-page);
  border: 1px dashed var(--border-color);
  border-radius: 6px;
  padding: 6px 10px;
  font-family: monospace;
  font-size: 11.5px;
  color: var(--text-subtle);
  margin-top: 8px;
  word-break: break-all;
}}

/* APP HOSTING CARDS */
.hosting-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-bottom: 12px;
}}

.hosting-card {{
  border: 3px solid var(--primary);
  border-radius: 10px;
  padding: 12px 6px;
  text-align: center;
  background: var(--bg-card);
  cursor: pointer;
  transition: all 0.15s;
}}
.hosting-card:hover {{
  transform: translateY(-2px);
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
}}
.hosting-card.active {{
  background: rgba(2, 132, 199, 0.08);
  box-shadow: 0 0 0 2px var(--primary);
}}
.hosting-card.amber {{ border-color: var(--amber); }}
.hosting-card.amber.active {{ background: rgba(245, 158, 11, 0.08); }}
.hosting-card.indigo {{ border-color: var(--indigo); }}
.hosting-card.indigo.active {{ background: rgba(79, 70, 229, 0.08); }}

.hosting-card .h-lbl {{ font-size: 12px; font-weight: 700; color: var(--text-subtle); }}
.hosting-card .h-num {{ font-size: 26px; font-weight: 800; color: var(--primary); margin: 3px 0; }}
.hosting-card.amber .h-num {{ color: var(--amber); }}
.hosting-card.indigo .h-num {{ color: var(--indigo); }}
.hosting-card .h-sub {{ font-size: 11px; color: var(--text-muted); font-weight: 600; }}

/* TABLAS COMPACTAS DENTRO DE WIDGETS */
.widget-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}}
.widget-table th {{
  text-align: left;
  color: var(--text-muted);
  padding: 6px;
  border-bottom: 1px solid var(--border-light);
}}
.widget-table td {{
  padding: 6px;
  border-bottom: 1px solid var(--border-light);
}}
.widget-table tr:hover td {{
  background: rgba(0,0,0,0.02);
  cursor: pointer;
}}

.dot {{
  display: inline-block;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  margin-right: 6px;
}}

/* TOOLTIP INTERACTIVO FLOTANTE */
#globalTooltip {{
  position: fixed;
  display: none;
  background: rgba(15, 23, 42, 0.95);
  color: #fff;
  padding: 10px 14px;
  border-radius: 8px;
  font-size: 12px;
  pointer-events: none;
  z-index: 9999;
  box-shadow: 0 8px 16px rgba(0,0,0,0.25);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255,255,255,0.15);
  max-width: 280px;
}}

/* TABLA DE EXPLORADOR DE CONTROLES (VISTA 2) */
.full-table-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
  overflow: hidden;
}}

.table-toolbar {{
  padding: 14px 18px;
  border-bottom: 1px solid var(--border-light);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}}

.data-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}}
.data-table th {{
  background: var(--navy);
  color: #fff;
  padding: 10px 12px;
  text-align: left;
  font-weight: 700;
  cursor: pointer;
  user-select: none;
}}
.data-table th:hover {{ background: #1e293b; }}
.data-table td {{
  padding: 10px 12px;
  border-bottom: 1px solid var(--border-light);
  vertical-align: middle;
}}
.data-table tr:nth-child(even) td {{ background: rgba(0,0,0,0.015); }}
.data-table tr:hover td {{ background: rgba(2, 132, 199, 0.05); }}

.badge {{
  display: inline-flex;
  align-items: center;
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 11.5px;
  font-weight: 700;
}}
.badge-green {{ background: #dcfce7; color: #15803d; }}
.badge-amber {{ background: #fef3c7; color: #b45309; }}
.badge-indigo {{ background: #e0e7ff; color: #4338ca; }}
.badge-red {{ background: #fee2e2; color: #b91c1c; }}
.badge-blue {{ background: #e0f2fe; color: #0369a1; }}

/* MODALES */
.modal-overlay {{
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(4px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  padding: 16px;
}}
.modal-overlay.active {{ display: flex; }}

.modal-box {{
  background: var(--bg-card);
  border-radius: 12px;
  max-width: 760px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-color);
  animation: modalIn 0.18s ease-out;
}}
@keyframes modalIn {{
  from {{ opacity: 0; transform: scale(0.96); }}
  to {{ opacity: 1; transform: scale(1); }}
}}

.modal-hdr {{
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-light);
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.modal-hdr h3 {{ font-size: 17px; font-weight: 800; color: var(--text-main); }}
.modal-close {{
  background: transparent; border: none; font-size: 20px; cursor: pointer; color: var(--text-muted);
}}

.modal-body {{ padding: 20px; font-size: 13.5px; }}
.modal-ftr {{
  padding: 14px 20px;
  border-top: 1px solid var(--border-light);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}}

.detail-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-bottom: 16px;
}}
.detail-item .lbl {{ font-size: 11.5px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; }}
.detail-item .val {{ font-size: 13.5px; font-weight: 600; color: var(--text-main); margin-top: 2px; }}

.detail-block {{
  background: var(--bg-page);
  border: 1px solid var(--border-light);
  border-radius: 8px;
  padding: 12px 14px;
  margin-bottom: 14px;
}}
.detail-block .lbl {{ font-size: 12px; font-weight: 800; color: var(--primary); margin-bottom: 4px; }}

/* TOAST DE NOTIFICACIONES */
#toastBox {{
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #10b981;
  color: #fff;
  padding: 12px 20px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);
  display: none;
  z-index: 11000;
  align-items: center;
  gap: 8px;
}}

/* SIMULADOR DE CAPACIDAD (VISTA 4) */
.simulator-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 24px;
  box-shadow: var(--card-shadow);
}}

.slider-group {{
  margin-bottom: 20px;
}}
.slider-hdr {{
  display: flex;
  justify-content: space-between;
  font-weight: 700;
  font-size: 13.5px;
  margin-bottom: 6px;
}}
.slider-group input[type=range] {{
  width: 100%;
  accent-color: var(--primary);
  cursor: pointer;
}}

.kpi-outcome-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-top: 20px;
}}
.kpi-outcome {{
  background: var(--bg-page);
  border: 1px solid var(--border-light);
  border-radius: 8px;
  padding: 14px;
  text-align: center;
}}
.kpi-outcome .num {{ font-size: 28px; font-weight: 900; color: var(--primary); }}
.kpi-outcome .lbl {{ font-size: 12px; font-weight: 700; color: var(--text-muted); margin-top: 4px; }}

@media print {{
  .topbar, .view-tabs-bar, .filter-row, .search-input-box, .quick-presets, .btn {{ display: none !important; }}
  .widget-card {{ break-inside: avoid; border: 1px solid #ccc !important; box-shadow: none !important; }}
  body {{ background: #fff !important; color: #000 !important; }}
}}
</style>
</head>
<body>

<!-- TOOLTIP FLOTANTE GLOBAL -->
<div id="globalTooltip"></div>

<!-- TOAST ALERT -->
<div id="toastBox">✓ <span id="toastMsg">Acción completada con éxito</span></div>

<!-- BARRA SUPERIOR DE JIRA / TECNIFICATE -->
<header class="topbar">
  <div class="topbar-left">
    <a href="#" class="brand-badge">
      <div class="logo-icon">T</div>
      <span>TECNIFICATE S.A.S. — Gobernanza COBIT 2019</span>
    </a>
    <nav class="jira-menu">
      <span>Mi Trabajo</span>
      <span>Proyectos ▾</span>
      <span>Filtros ▾</span>
      <span style="color:var(--primary); border-bottom-color:var(--primary);">Tableros ▾</span>
      <span>Personas ▾</span>
      <span>Métricas BSC ▾</span>
    </nav>
  </div>
  <div class="topbar-right">
    <button class="btn btn-primary" onclick="openCreateModal()">+ Nuevo Control / Ticket</button>
    <button class="btn btn-outline" onclick="exportCsv()">📥 Exportar CSV (UTF-8)</button>
    <button class="btn btn-dark" onclick="window.print()">🖨️ Imprimir Reporte</button>
    <button class="btn btn-outline" onclick="toggleDarkMode()">🌓 Modo Oscuro</button>
    <span class="user-badge">👤 Diego Vélez (Líder PETI) | auditor.gobiernoti@usc.edu.co</span>
  </div>
</header>

<!-- BARRA DE PESTAÑAS DE VISTA -->
<div class="view-tabs-bar">
  <button class="tab-btn active" onclick="switchTab('tab-dashboard')">📊 Tablero Principal (Custom Charts)</button>
  <button class="tab-btn" onclick="switchTab('tab-explorer')">📑 Explorador de Controles e Incidentes (<span id="tabCount">48</span>)</button>
  <button class="tab-btn" onclick="switchTab('tab-cascade')">🎯 Cascada de Metas COBIT 2019 & BSC</button>
  <button class="tab-btn" onclick="switchTab('tab-simulator')">📈 Simulador Interactivo de Madurez (ISO 33000)</button>
</div>

<main class="main-container">

  <!-- ===================================================================== -->
  <!-- VISTA 1: TABLERO PRINCIPAL (ESTILO JIRA CUSTOM CHARTS)                -->
  <!-- ===================================================================== -->
  <div id="tab-dashboard" class="view-content active">
    <div class="custom-charts-grid">

      <!-- COLUMNA 1: FILTROS SIMPLE SEARCH + EVOLUCIÓN 12 MESES -->
      <div class="col-stack">
        <!-- WIDGET 1: FILTROS DE BÚSQUEDA RÁPIDA -->
        <div class="widget-card top-red">
          <div class="widget-hdr">
            <span>▾ Búsqueda Rápida de Gobernanza (Simple Search)</span>
            <div class="widget-hdr-right" onclick="resetFilters()">🔄 Limpiar Filtros</div>
          </div>
          <div class="widget-body">
            <div class="filter-row">
              <select id="selDomain" class="filter-select" onchange="applyFilters()">
                <option value="ALL">Dominio COBIT: Todos (EDM/APO/BAI/DSS/MEA)</option>
                <option value="EDM">EDM: Evaluar, Dirigir y Supervisar (Gobernanza)</option>
                <option value="APO">APO: Alinear, Planear y Organizar (Gestión)</option>
                <option value="BAI">BAI: Construir, Adquirir e Implementar (Gestión)</option>
                <option value="DSS">DSS: Entregar, Dar Servicio y Soporte (Gestión)</option>
                <option value="MEA">MEA: Supervisar, Evaluar y Valorar (Gestión)</option>
              </select>
              <select id="selApp" class="filter-select" onchange="applyFilters()">
                <option value="ALL">Aplicación: Todas las 6 Plataformas</option>
                <option value="ERP Modular Apolo">ERP Modular Apolo (PyMEs / Local)</option>
                <option value="Apolo Académico SaaS">Apolo Académico v2.1 (SaaS Cloud)</option>
                <option value="Apolo II Mobile">Apolo II Mobile (App Android)</option>
                <option value="Portal Web & Hosting VPS">Portal Web & Hosting VPS (SSL)</option>
                <option value="AulaCloud & Wiki">AulaCloud & Wiki Videotutoriales</option>
                <option value="CRM Open Source">CRM Open Source & Partners</option>
              </select>
            </div>
            <div class="filter-row">
              <select id="selStatus" class="filter-select" onchange="applyFilters()">
                <option value="ALL">Estado: Todos los Estados</option>
                <option value="Completado en SLA">Completado en SLA (Resuelto)</option>
                <option value="En Curso">En Curso (En Ejecución)</option>
                <option value="Por Hacer">Por Hacer (Pendiente)</option>
              </select>
              <select id="selPriority" class="filter-select" onchange="applyFilters()">
                <option value="ALL">Prioridad: Todas las Prioridades</option>
                <option value="P1 - Crítico">P1 - Crítico (Alto Impacto)</option>
                <option value="P2 - Alto">P2 - Alto (Operación)</option>
                <option value="P3 - Medio">P3 - Medio (Mejora)</option>
                <option value="P4 - Bajo">P4 - Bajo (Rutina)</option>
              </select>
              <select id="selAssignee" class="filter-select" onchange="applyFilters()">
                <option value="ALL">Responsable: Todo el Equipo PETI</option>
                <option value="Diego Vélez">Diego Vélez (Líder PETI / Gerente)</option>
                <option value="Santiago Balanta">Santiago Balanta (Arquitectura DevOps)</option>
                <option value="Martín Murillo">Martín Murillo (Líder QA y Calidad)</option>
                <option value="Andrés Sarria">Andrés Sarria (Comercial y Procesos)</option>
                <option value="Brayan Noguera">Brayan Noguera (Riesgos y Auditoría)</option>
              </select>
            </div>

            <div class="search-input-box">
              <input type="text" id="searchInput" placeholder="Buscar por código, causa raíz, DIAN, colegios, SLA, Girardot..." oninput="applyFilters()">
              <button class="btn btn-primary" onclick="applyFilters()">Buscar</button>
            </div>

            <div class="quick-presets">
              <span class="preset-chip" onclick="setPreset('criticos')">🚨 Solo Críticos P1</span>
              <span class="preset-chip" onclick="setPreset('itil')">⏱️ Soporte ITIL (DSS02)</span>
              <span class="preset-chip" onclick="setPreset('qa')">🐞 Bugs QA (BAI07)</span>
              <span class="preset-chip" onclick="setPreset('erp')">🔄 Reprocesos ERP (DSS06)</span>
              <span class="preset-chip" onclick="resetFilters()">🔄 Todos</span>
            </div>

            <div class="filter-meta">
              <span style="color:var(--emerald);" id="filterFoundText">● 48 controles e incidentes encontrados</span>
              <span style="color:var(--primary); cursor:pointer;" onclick="toggleJqlPreview()">Ver Consulta JQL</span>
            </div>
            <div id="jqlBox" class="jql-preview" style="display:none;">
              project = "TECNIFICATE-PETI" AND framework = "COBIT-2019"
            </div>
          </div>
        </div>

        <!-- WIDGET 2: LÍNEA DE TIEMPO 12 MESES (INTERACTIVA) -->
        <div class="widget-card top-green">
          <div class="widget-hdr">
            <span>▾ Evolución Temporal de Gobernanza — Últimos 12 Meses</span>
            <div style="display:flex; gap:6px;">
              <button class="btn btn-outline" style="padding:2px 8px; font-size:11px;" onclick="setTimeRange('12M')">12 Meses</button>
              <button class="btn btn-outline" style="padding:2px 8px; font-size:11px;" onclick="setTimeRange('H1')">Semestre 1 (AS-IS)</button>
              <button class="btn btn-outline" style="padding:2px 8px; font-size:11px;" onclick="setTimeRange('H2')">Semestre 2 (TO-BE)</button>
            </div>
          </div>
          <div class="widget-body">
            <div class="widget-title">Controles Creados y Resueltos en SLA (COBIT 2019)</div>
            <div id="timelineSvgWrap" style="width:100%; position:relative;"></div>
            
            <div style="display:grid; grid-template-columns: repeat(2, 1fr); gap:8px; margin-top:12px; font-size:11.5px;">
              <div style="cursor:pointer;" onclick="toggleSeries('resolved')">
                <span class="dot" style="background:#10b981;"></span>
                <b id="lblResolved">Resueltos en SLA (DSS02):</b> 18 → 58/mes
              </div>
              <div style="cursor:pointer;" onclick="toggleSeries('rework')">
                <span class="dot" style="background:#f59e0b;"></span>
                <b id="lblRework">Reprocesos Manuales (DSS06):</b> 80% → 40%
              </div>
              <div style="cursor:pointer;" onclick="toggleSeries('bugs')">
                <span class="dot" style="background:#4f46e5;"></span>
                <b id="lblBugs">Bugs en Producción (BAI07):</b> 16 → 4 (-71%)
              </div>
              <div style="cursor:pointer;" onclick="toggleSeries('sla')">
                <span class="dot" style="background:#0284c7;"></span>
                <b id="lblSla">Cumplimiento SLA ITIL:</b> 61% → 92,5%
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- COLUMNA 2: BARRAS APILADAS POR APLICACIÓN + APP HOSTING -->
      <div class="col-stack">
        <!-- WIDGET 3: CONTROLES POR APLICACIÓN -->
        <div class="widget-card top-amber">
          <div class="widget-hdr">
            <span>▾ Tickets y Controles Abiertos por Aplicación</span>
            <span style="font-size:11px; color:var(--primary); cursor:pointer;" onclick="filterByApp('ALL')">Ver Todas</span>
          </div>
          <div class="widget-body">
            <div class="widget-title">Distribución de Gobernanza por Plataforma de Software</div>
            <div id="appBarsWrap" style="width:100%; min-height:220px;"></div>
            <div style="display:flex; justify-content:center; gap:14px; font-size:11.5px; margin-top:8px;">
              <span><span class="dot" style="background:#10b981;"></span>Completado</span>
              <span><span class="dot" style="background:#f59e0b;"></span>En Curso</span>
              <span><span class="dot" style="background:#4f46e5;"></span>Por Hacer</span>
              <span><span class="dot" style="background:#ef4444;"></span>Crítico P1</span>
            </div>
          </div>
        </div>

        <!-- WIDGET 4: APP HOSTING -->
        <div class="widget-card top-blue">
          <div class="widget-hdr">
            <span>▾ Infraestructura y Alojamiento de Aplicaciones</span>
            <span>COBIT APO03 / BAI04</span>
          </div>
          <div class="widget-body">
            <div class="widget-title">Alojamiento de Aplicaciones (App Hosting)</div>
            <div class="hosting-grid">
              <div class="hosting-card" id="cardCloud" onclick="filterByHosting('Nube (Cloud VPS SaaS)')">
                <div class="h-lbl">Nube (Cloud VPS)</div>
                <div class="h-num" id="hCloudVal">220</div>
                <div class="h-sub" id="hCloudPct">64,3% (Apolo SaaS)</div>
              </div>
              <div class="hosting-card amber" id="cardServer" onclick="filterByHosting('Servidor Dedicado / VPS')">
                <div class="h-lbl">Servidor Web / SSL</div>
                <div class="h-num" id="hServerVal">84</div>
                <div class="h-sub" id="hServerPct">24,6% (Hosting)</div>
              </div>
              <div class="hosting-card indigo" id="cardLocal" onclick="filterByHosting('Centro de Datos / Local')">
                <div class="h-lbl">Centro de Datos Local</div>
                <div class="h-num" id="hLocalVal">38</div>
                <div class="h-sub" id="hLocalPct">11,1% (PyMEs)</div>
              </div>
            </div>
            <div style="text-align:center; font-size:12px; color:var(--text-subtle); font-weight:700;">
              Total Gobernado: <span style="color:var(--primary);" id="hTotalVal">342</span> componentes &nbsp;|&nbsp;
              <span style="color:var(--emerald); cursor:pointer;" onclick="filterByHosting('ALL')">Mostrar Todo</span>
            </div>
          </div>
        </div>
      </div>

      <!-- COLUMNA 3: DONA DE ESTADO + TIPO DE SOLICITUD -->
      <div class="col-stack">
        <!-- WIDGET 5: CATEGORÍA DE ESTADO DEL PROYECTO -->
        <div class="widget-card top-blue">
          <div class="widget-hdr">
            <span>▾ Categoría de Estado de Gobernanza</span>
            <span>COBIT MEA01</span>
          </div>
          <div class="widget-body">
            <div class="widget-title">Estado del Proyecto de Gobernanza (Status Category)</div>
            <div style="display:grid; grid-template-columns: 140px 1fr; gap:12px; align-items:center;">
              <div id="donutWrap" style="text-align:center;"></div>
              <table class="widget-table">
                <thead>
                  <tr><th>Estado</th><th>Items</th><th>%</th></tr>
                </thead>
                <tbody id="statusTableBody"></tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- WIDGET 6: TIPO DE SOLICITUD Y PROCESO COBIT -->
        <div class="widget-card top-indigo">
          <div class="widget-hdr">
            <span>▾ Tipo de Solicitud y Proceso de Gobierno</span>
            <span>COBIT 2019</span>
          </div>
          <div class="widget-body">
            <div class="widget-title">Solicitudes por Dominio Operativo (Request Type)</div>
            <div id="reqTypesWrap" style="width:100%; min-height:180px;"></div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- VISTA 2: EXPLORADOR DETALLADO DE CONTROLES E INCIDENTES               -->
  <!-- ===================================================================== -->
  <div id="tab-explorer" class="view-content">
    <div class="full-table-card">
      <div class="table-toolbar">
        <div>
          <h3 style="font-size:16px; font-weight:800;">Registro Operativo de Controles e Incidentes de Gobierno de TI</h3>
          <p style="font-size:12px; color:var(--text-muted);">Haga clic en cualquier fila para abrir la Ficha de Auditoría y Análisis de Causa Raíz (RCA).</p>
        </div>
        <div style="display:flex; gap:10px; align-items:center;">
          <input type="text" id="tableSearchInput" placeholder="Filtrar en tabla..." style="padding:6px 12px; border:1px solid var(--border-color); border-radius:6px; font-size:12.5px;" oninput="onTableSearch()">
          <select id="tablePageSize" style="padding:6px; border:1px solid var(--border-color); border-radius:6px; font-size:12.5px;" onchange="onPageSizeChange()">
            <option value="10">10 por página</option>
            <option value="25">25 por página</option>
            <option value="50">50 por página</option>
            <option value="999">Todos</option>
          </select>
        </div>
      </div>

      <div style="overflow-x:auto;">
        <table class="data-table">
          <thead>
            <tr>
              <th onclick="sortTable('code')">Código ⇕</th>
              <th onclick="sortTable('title')">Título de la Incidencia / Control ⇕</th>
              <th onclick="sortTable('app')">Aplicación ⇕</th>
              <th onclick="sortTable('domain')">Dominio ⇕</th>
              <th onclick="sortTable('priority')">Prioridad ⇕</th>
              <th onclick="sortTable('status')">Estado ⇕</th>
              <th onclick="sortTable('sla')">SLA % ⇕</th>
              <th onclick="sortTable('assignee')">Responsable ⇕</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody id="ticketsTableBody"></tbody>
        </table>
      </div>

      <div style="padding:12px 18px; display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border-light); font-size:12.5px;">
        <span id="tablePaginationInfo">Mostrando 1 a 10 de 48 registros</span>
        <div style="display:flex; gap:6px;" id="paginationBtns"></div>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- VISTA 3: CASCADA DE METAS COBIT 2019 & BSC                            -->
  <!-- ===================================================================== -->
  <div id="tab-cascade" class="view-content">
    <div class="full-table-card">
      <div style="padding:16px 20px; border-bottom:1px solid var(--border-light); background:var(--bg-page);">
        <h3 style="font-size:17px; font-weight:800; color:var(--text-main);">Matriz Estratégica de Cascada de Metas COBIT 2019 & Balanced Scorecard (BSC)</h3>
        <p style="font-size:13px; color:var(--text-muted); margin-top:4px;">
          Alineación sistemática entre Metas de Empresa (EG), Metas de Alineamiento (AG), Procesos COBIT 2019 y métricas estratégicas de TECNIFICATE S.A.S.
        </p>
      </div>
      <div style="overflow-x:auto;">
        <table class="data-table">
          <thead>
            <tr>
              <th>Proceso COBIT</th>
              <th>Dominio</th>
              <th>Meta Empresarial (EG)</th>
              <th>Meta de Alineamiento (AG)</th>
              <th>Perspectiva BSC</th>
              <th>Métrica Estratégica e Inductor Operativo</th>
              <th>Línea Base (AS-IS)</th>
              <th>Meta Lograda (TO-BE)</th>
              <th>Capacidad ISO 33000</th>
              <th>Responsable</th>
            </tr>
          </thead>
          <tbody id="matrixTableBody"></tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- ===================================================================== -->
  <!-- VISTA 4: SIMULADOR INTERACTIVO DE MADUREZ ISO 33000                   -->
  <!-- ===================================================================== -->
  <div id="tab-simulator" class="view-content">
    <div class="simulator-card">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:20px; flex-wrap:wrap; gap:12px;">
        <div>
          <h2 style="font-size:20px; font-weight:800; color:var(--text-main);">Simulador Dinámico de Madurez y Capacidad de Gobierno de TI</h2>
          <p style="font-size:13.5px; color:var(--text-muted); margin-top:4px;">
            Ajuste los niveles de capacidad de cada dominio COBIT 2019 (escala ISO/IEC 33000 de 0 a 5) y observe el impacto inmediato sobre los KPIs clave de TECNIFICATE S.A.S.
          </p>
        </div>
        <div style="display:flex; gap:8px;">
          <button class="btn btn-outline" onclick="loadSimScenario('asis')">Cargar AS-IS (Línea Base)</button>
          <button class="btn btn-outline" onclick="loadSimScenario('mid')">Cargar 6 Meses</button>
          <button class="btn btn-primary" onclick="loadSimScenario('tobe')">Cargar TO-BE (Meta Lograda)</button>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:24px;">
        <!-- CONTROLES DESLIZANTES (SLIDERS) -->
        <div>
          <div class="slider-group">
            <div class="slider-hdr">
              <span>EDM: Evaluar, Dirigir y Supervisar (Gobernanza Estratégica)</span>
              <span id="valSimEdm" style="color:var(--primary); font-size:16px;">1.0</span>
            </div>
            <input type="range" id="rngEdm" min="0" max="5" step="0.5" value="1.0" oninput="onSimSliderChange()">
          </div>

          <div class="slider-group">
            <div class="slider-hdr">
              <span>APO: Alinear, Planear y Organizar (Gestión de Arquitectura y Riesgos)</span>
              <span id="valSimApo" style="color:var(--primary); font-size:16px;">2.0</span>
            </div>
            <input type="range" id="rngApo" min="0" max="5" step="0.5" value="2.0" oninput="onSimSliderChange()">
          </div>

          <div class="slider-group">
            <div class="slider-hdr">
              <span>BAI: Construir, Adquirir e Implementar (Calidad QA y Software)</span>
              <span id="valSimBai" style="color:var(--primary); font-size:16px;">0.0</span>
            </div>
            <input type="range" id="rngBai" min="0" max="5" step="0.5" value="0.0" oninput="onSimSliderChange()">
          </div>

          <div class="slider-group">
            <div class="slider-hdr">
              <span>DSS: Entregar, Dar Servicio y Soporte (Mesa ITIL y Operaciones)</span>
              <span id="valSimDss" style="color:var(--primary); font-size:16px;">2.0</span>
            </div>
            <input type="range" id="rngDss" min="0" max="5" step="0.5" value="2.0" oninput="onSimSliderChange()">
          </div>

          <div class="slider-group">
            <div class="slider-hdr">
              <span>MEA: Supervisar, Evaluar y Valorar (Auditoría Continua y KPIs)</span>
              <span id="valSimMea" style="color:var(--primary); font-size:16px;">0.0</span>
            </div>
            <input type="range" id="rngMea" min="0" max="5" step="0.5" value="0.0" oninput="onSimSliderChange()">
          </div>
        </div>

        <!-- RESULTADOS PROYECTADOS EN VIVO -->
        <div>
          <div style="background:var(--bg-page); border:1px solid var(--border-color); border-radius:10px; padding:20px;">
            <h4 style="font-size:14px; font-weight:800; color:var(--text-subtle); text-transform:uppercase;">Diagnóstico Proyectado en Tiempo Real</h4>
            <div style="display:flex; align-items:baseline; gap:12px; margin:14px 0;">
              <span id="simAvgCap" style="font-size:48px; font-weight:900; color:var(--primary);">1.00</span>
              <span style="font-size:16px; font-weight:700; color:var(--text-muted);">/ 5.00 Nivel de Capacidad Promedio</span>
            </div>
            <div style="font-size:14px; font-weight:700; margin-bottom:12px;" id="simMaturityLevelBadge">
              Madurez EIS: <span class="badge badge-amber">Nivel 1: Inicial / Intuitivo</span>
            </div>

            <div class="kpi-outcome-grid">
              <div class="kpi-outcome">
                <div class="num" id="simChurnVal" style="color:var(--rose);">20.0%</div>
                <div class="lbl">Deserción Escolar (Churn)</div>
              </div>
              <div class="kpi-outcome">
                <div class="num" id="simReworkVal" style="color:var(--amber);">80.0%</div>
                <div class="lbl">Tiempo en Reprocesos</div>
              </div>
              <div class="kpi-outcome">
                <div class="num" id="simSlaVal" style="color:var(--emerald);">62.0%</div>
                <div class="lbl">Cumplimiento SLA ITIL</div>
              </div>
              <div class="kpi-outcome">
                <div class="num" id="simRoiVal" style="color:var(--indigo);">1.00x</div>
                <div class="lbl">Retorno Beneficio / Costo</div>
              </div>
            </div>

            <div style="margin-top:16px; font-size:12.5px; color:var(--text-subtle); background:#fff; padding:12px; border-radius:6px; border:1px solid var(--border-light);" id="simInterpretationText">
              <b>Interpretación Senior de Gobierno:</b> En la Línea Base (AS-IS), la empresa sufre por ausencia de controles formales de calidad (BAI Nivel 0) y auditoría (MEA Nivel 0), lo que dispara los reprocesos al 80% y la deserción de colegios al 20%. Mueva los controles hacia la derecha para proyectar las mejoras del PETI.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</main>

<!-- ======================================================================= -->
<!-- MODAL 1: FICHA DE AUDITORÍA Y ANÁLISIS DE CAUSA RAÍZ (RCA)             -->
<!-- ======================================================================= -->
<div id="auditModal" class="modal-overlay">
  <div class="modal-box">
    <div class="modal-hdr">
      <div>
        <span class="badge badge-indigo" id="mCode">TECNIF-DSS02-01</span>
        <h3 id="mTitle" style="margin-top:4px;">Título de la Incidencia</h3>
      </div>
      <button class="modal-close" onclick="closeAuditModal()">✕</button>
    </div>
    <div class="modal-body">
      <div class="detail-grid">
        <div class="detail-item"><div class="lbl">Aplicación / Producto</div><div class="val" id="mApp">ERP Modular Apolo</div></div>
        <div class="detail-item"><div class="lbl">Infraestructura / Alojamiento</div><div class="val" id="mHosting">Centro de Datos / Local</div></div>
        <div class="detail-item"><div class="lbl">Dominio y Proceso COBIT 2019</div><div class="val" id="mProcess">DSS06 / APO14</div></div>
        <div class="detail-item"><div class="lbl">Perspectiva Balanced Scorecard</div><div class="val" id="mBsc">Financiera / Procesos</div></div>
        <div class="detail-item"><div class="lbl">Prioridad y Severidad</div><div class="val" id="mPriority">P1 - Crítico</div></div>
        <div class="detail-item"><div class="lbl">Estado de Cumplimiento SLA</div><div class="val" id="mStatus">Completado en SLA (98.2%)</div></div>
        <div class="detail-item"><div class="lbl">Responsable Asignado</div><div class="val" id="mAssignee">Martín Murillo (QA)</div></div>
        <div class="detail-item"><div class="lbl">Evolución de Capacidad ISO 33000</div><div class="val" id="mCap">Nivel 0 → Nivel 3</div></div>
      </div>

      <div class="detail-block">
        <div class="lbl">🔍 Análisis de Causa Raíz (RCA — Metodología de los 5 Porqués)</div>
        <div id="mRca" style="font-size:13px; line-height:1.5;"></div>
      </div>

      <div class="detail-block">
        <div class="lbl">🛠️ Acción Correctiva y Control de Gobierno de TI Implementado</div>
        <div id="mAction" style="font-size:13px; line-height:1.5;"></div>
      </div>

      <div class="detail-block">
        <div class="lbl">📄 Evidencia Auditable Verificada</div>
        <div id="mEvidence" style="font-size:12.5px; font-family:monospace; color:var(--text-subtle);"></div>
      </div>
    </div>
    <div class="modal-ftr">
      <button class="btn btn-outline" onclick="copyAuditSummary()">📋 Copiar Ficha de Auditoría</button>
      <button class="btn btn-primary" onclick="closeAuditModal()">Cerrar</button>
    </div>
  </div>
</div>

<!-- ======================================================================= -->
<!-- MODAL 2: CREAR NUEVO CONTROL / INCIDENCIA                               -->
<!-- ======================================================================= -->
<div id="createModal" class="modal-overlay">
  <div class="modal-box">
    <div class="modal-hdr">
      <h3>+ Registrar Nuevo Control o Incidente de Gobierno de TI</h3>
      <button class="modal-close" onclick="closeCreateModal()">✕</button>
    </div>
    <div class="modal-body">
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-bottom:12px;">
        <div>
          <label style="font-size:12px; font-weight:700;">Código del Ticket</label>
          <input type="text" id="newCode" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;" value="TECNIF-DSS02-15">
        </div>
        <div>
          <label style="font-size:12px; font-weight:700;">Aplicación / Plataforma</label>
          <select id="newApp" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;">
            <option value="ERP Modular Apolo">ERP Modular Apolo</option>
            <option value="Apolo Académico SaaS" selected>Apolo Académico SaaS</option>
            <option value="Apolo II Mobile">Apolo II Mobile</option>
            <option value="Portal Web & Hosting VPS">Portal Web & Hosting VPS</option>
            <option value="AulaCloud & Wiki">AulaCloud & Wiki</option>
            <option value="CRM Open Source">CRM Open Source</option>
          </select>
        </div>
      </div>

      <div style="margin-bottom:12px;">
        <label style="font-size:12px; font-weight:700;">Título Descriptivo</label>
        <input type="text" id="newTitle" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;" placeholder="Ej. Bloqueo en emisión de boletines...">
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:12px; margin-bottom:12px;">
        <div>
          <label style="font-size:12px; font-weight:700;">Dominio COBIT</label>
          <select id="newDomain" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;">
            <option value="DSS" selected>DSS (Servicio y Soporte)</option>
            <option value="BAI">BAI (Construir e Implementar)</option>
            <option value="APO">APO (Alinear y Planear)</option>
            <option value="EDM">EDM (Gobernanza)</option>
            <option value="MEA">MEA (Supervisar y Evaluar)</option>
          </select>
        </div>
        <div>
          <label style="font-size:12px; font-weight:700;">Prioridad</label>
          <select id="newPriority" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;">
            <option value="P1 - Crítico">P1 - Crítico</option>
            <option value="P2 - Alto" selected>P2 - Alto</option>
            <option value="P3 - Medio">P3 - Medio</option>
            <option value="P4 - Bajo">P4 - Bajo</option>
          </select>
        </div>
        <div>
          <label style="font-size:12px; font-weight:700;">Estado</label>
          <select id="newStatus" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;">
            <option value="Completado en SLA" selected>Completado en SLA</option>
            <option value="En Curso">En Curso</option>
            <option value="Por Hacer">Por Hacer</option>
          </select>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-bottom:12px;">
        <div>
          <label style="font-size:12px; font-weight:700;">Responsable Asignado</label>
          <select id="newAssignee" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;">
            <option value="Martín Murillo (QA)">Martín Murillo (Líder QA)</option>
            <option value="Santiago Balanta (DevOps)">Santiago Balanta (DevOps)</option>
            <option value="Diego Vélez (Líder PETI)">Diego Vélez (Líder PETI)</option>
            <option value="Andrés Sarria (Comercial)">Andrés Sarria (Comercial)</option>
            <option value="Brayan Noguera (Riesgos)">Brayan Noguera (Riesgos)</option>
          </select>
        </div>
        <div>
          <label style="font-size:12px; font-weight:700;">Infraestructura</label>
          <select id="newHosting" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:13px;">
            <option value="Nube (Cloud VPS SaaS)" selected>Nube (Cloud VPS SaaS)</option>
            <option value="Servidor Dedicado / VPS">Servidor Dedicado / VPS</option>
            <option value="Centro de Datos / Local">Centro de Datos / Local</option>
          </select>
        </div>
      </div>

      <div style="margin-bottom:12px;">
        <label style="font-size:12px; font-weight:700;">Análisis de Causa Raíz (RCA)</label>
        <textarea id="newRca" rows="2" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:12.5px;" placeholder="Explique la causa fundamental de la falla o requerimiento..."></textarea>
      </div>

      <div>
        <label style="font-size:12px; font-weight:700;">Acción Correctiva de Gobierno de TI</label>
        <textarea id="newAction" rows="2" style="width:100%; padding:7px; border:1px solid var(--border-color); border-radius:6px; font-size:12.5px;" placeholder="Control implementado según COBIT 2019..."></textarea>
      </div>
    </div>
    <div class="modal-ftr">
      <button class="btn btn-outline" onclick="closeCreateModal()">Cancelar</button>
      <button class="btn btn-primary" onclick="saveNewTicket()">Guardar en Base de Datos</button>
    </div>
  </div>
</div>

<!-- ======================================================================= -->
<!-- MOTOR DE JAVASCRIPT: LÓGICA Y REACTIVIDAD 100% FUNCIONAL               -->
<!-- ======================================================================= -->
<script>
// DATASETS PRINCIPALES INYECTADOS DESDE PYTHON
let ALL_TICKETS = {tickets_json};
const MONTHLY_DATA = {monthly_json};
const COBIT_MATRIX = {matrix_json};

// ESTADO GLOBAL DE FILTROS
let currentFilter = {{
  domain: 'ALL',
  app: 'ALL',
  status: 'ALL',
  priority: 'ALL',
  assignee: 'ALL',
  hosting: 'ALL',
  reqType: 'ALL',
  search: '',
  timeRange: '12M'
}};

// VISIBILIDAD DE SERIES EN LA LÍNEA DE TIEMPO
let seriesVisibility = {{
  resolved: true,
  rework: true,
  bugs: true,
  sla: true
}};

// PAGINACIÓN Y ORDENAMIENTO EN TABLA
let tableState = {{
  page: 1,
  pageSize: 10,
  sortField: 'code',
  sortAsc: true,
  search: ''
}};

// INICIALIZACIÓN
document.addEventListener('DOMContentLoaded', () => {{
  renderAll();
  initMatrix();
  updateSimulation();
}});

function toggleDarkMode() {{
  document.body.classList.toggle('dark-mode');
  showToast(document.body.classList.contains('dark-mode') ? "Modo Oscuro activado" : "Modo Claro activado");
}}

function switchTab(tabId) {{
  document.querySelectorAll('.view-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById(tabId).classList.add('active');
  event.currentTarget.classList.add('active');
}}

function showToast(msg) {{
  const b = document.getElementById('toastBox');
  document.getElementById('toastMsg').textContent = msg;
  b.style.display = 'flex';
  setTimeout(() => {{ b.style.display = 'none'; }}, 3200);
}}

// =========================================================================
// FILTRADO DINÁMICO REACTIVO
// =========================================================================
function applyFilters() {{
  currentFilter.domain = document.getElementById('selDomain').value;
  currentFilter.app = document.getElementById('selApp').value;
  currentFilter.status = document.getElementById('selStatus').value;
  currentFilter.priority = document.getElementById('selPriority').value;
  currentFilter.assignee = document.getElementById('selAssignee').value;
  currentFilter.search = (document.getElementById('searchInput').value || '').toLowerCase().trim();

  renderAll();
}}

function setPreset(type) {{
  resetFilterInputs();
  if (type === 'criticos') {{
    currentFilter.priority = 'P1 - Crítico';
    document.getElementById('selPriority').value = 'P1 - Crítico';
  }} else if (type === 'itil') {{
    currentFilter.domain = 'DSS';
    document.getElementById('selDomain').value = 'DSS';
  }} else if (type === 'qa') {{
    currentFilter.domain = 'BAI';
    document.getElementById('selDomain').value = 'BAI';
  }} else if (type === 'erp') {{
    currentFilter.app = 'ERP Modular Apolo';
    document.getElementById('selApp').value = 'ERP Modular Apolo';
  }}
  renderAll();
}}

function filterByApp(app) {{
  currentFilter.app = app;
  document.getElementById('selApp').value = app;
  renderAll();
}}

function filterByHosting(h) {{
  currentFilter.hosting = (currentFilter.hosting === h) ? 'ALL' : h;
  renderAll();
}}

function filterByStatus(st) {{
  currentFilter.status = (currentFilter.status === st) ? 'ALL' : st;
  document.getElementById('selStatus').value = currentFilter.status;
  renderAll();
}}

function resetFilters() {{
  resetFilterInputs();
  currentFilter = {{
    domain: 'ALL', app: 'ALL', status: 'ALL', priority: 'ALL', assignee: 'ALL',
    hosting: 'ALL', reqType: 'ALL', search: '', timeRange: '12M'
  }};
  renderAll();
}}

function resetFilterInputs() {{
  document.getElementById('selDomain').value = 'ALL';
  document.getElementById('selApp').value = 'ALL';
  document.getElementById('selStatus').value = 'ALL';
  document.getElementById('selPriority').value = 'ALL';
  document.getElementById('selAssignee').value = 'ALL';
  document.getElementById('searchInput').value = '';
}}

function getFilteredTickets() {{
  return ALL_TICKETS.filter(t => {{
    if (currentFilter.domain !== 'ALL' && t.domain !== currentFilter.domain) return false;
    if (currentFilter.app !== 'ALL' && t.app !== currentFilter.app) return false;
    if (currentFilter.status !== 'ALL' && t.status !== currentFilter.status) return false;
    if (currentFilter.priority !== 'ALL' && t.priority !== currentFilter.priority) return false;
    if (currentFilter.assignee !== 'ALL' && !t.assignee.includes(currentFilter.assignee)) return false;
    if (currentFilter.hosting !== 'ALL' && t.hosting !== currentFilter.hosting) return false;
    if (currentFilter.reqType !== 'ALL' && t.req_type !== currentFilter.reqType) return false;
    if (currentFilter.search !== '') {{
      const q = currentFilter.search;
      const textMatch = (
        t.code.toLowerCase().includes(q) ||
        t.title.toLowerCase().includes(q) ||
        t.app.toLowerCase().includes(q) ||
        t.process.toLowerCase().includes(q) ||
        t.assignee.toLowerCase().includes(q) ||
        t.rca.toLowerCase().includes(q) ||
        t.action.toLowerCase().includes(q)
      );
      if (!textMatch) return false;
    }}
    return true;
  }});
}}

function toggleJqlPreview() {{
  const b = document.getElementById('jqlBox');
  b.style.display = (b.style.display === 'none') ? 'block' : 'none';
}}

// =========================================================================
// RENDERIZADO GLOBAL DE TODOS LOS COMPONENTES
// =========================================================================
function renderAll() {{
  const filtered = getFilteredTickets();
  const count = filtered.length;

  document.getElementById('filterFoundText').textContent = `● ${{count}} controles e incidentes encontrados`;
  document.getElementById('tabCount').textContent = count;

  // Actualizar consulta JQL
  let jql = 'project = "TECNIFICATE-PETI" AND framework = "COBIT-2019"';
  if (currentFilter.domain !== 'ALL') jql += ` AND domain = "${{currentFilter.domain}}"`;
  if (currentFilter.app !== 'ALL') jql += ` AND app = "${{currentFilter.app}}"`;
  if (currentFilter.status !== 'ALL') jql += ` AND status = "${{currentFilter.status}}"`;
  if (currentFilter.priority !== 'ALL') jql += ` AND priority = "${{currentFilter.priority}}"`;
  if (currentFilter.hosting !== 'ALL') jql += ` AND hosting = "${{currentFilter.hosting}}"`;
  if (currentFilter.search !== '') jql += ` AND text ~ "${{currentFilter.search}}"`;
  document.getElementById('jqlBox').textContent = jql;

  renderTimeline();
  renderAppBars(filtered);
  renderHostingCards(filtered);
  renderStatusDonut(filtered);
  renderRequestTypes(filtered);
  renderTable(filtered);
}}

// -------------------------------------------------------------------------
// WIDGET 2: LÍNEA DE TIEMPO INTERACTIVA SVG
// -------------------------------------------------------------------------
function setTimeRange(r) {{
  currentFilter.timeRange = r;
  renderTimeline();
}}

function toggleSeries(s) {{
  seriesVisibility[s] = !seriesVisibility[s];
  renderTimeline();
}}

function renderTimeline() {{
  let data = [...MONTHLY_DATA];
  if (currentFilter.timeRange === 'H1') data = data.slice(0, 6);
  if (currentFilter.timeRange === 'H2') data = data.slice(6);

  const wrap = document.getElementById('timelineSvgWrap');
  const W = 520, H = 260;
  const padL = 40, padR = 20, padT = 20, padB = 30;
  const plotW = W - padL - padR;
  const plotH = H - padT - padB;
  const n = data.length;

  let svg = `<svg viewBox="0 0 ${{W}} ${{H}}" style="width:100%; height:auto;">`;

  // Ejes y líneas de cuadrícula
  for (let val = 0; val <= 100; val += 25) {{
    const y = padT + plotH - (val / 100) * plotH;
    svg += `<line x1="${{padL}}" y1="${{y}}" x2="${{W - padR}}" y2="${{y}}" stroke="var(--border-light)" stroke-width="1"/>`;
    svg += `<text x="${{padL - 6}}" y="${{y + 4}}" font-size="10" fill="var(--text-muted)" text-anchor="end">${{val}}</text>`;
  }}
  svg += `<line x1="${{padL}}" y1="${{padT + plotH}}" x2="${{W - padR}}" y2="${{padT + plotH}}" stroke="var(--border-color)" stroke-width="1.5"/>`;

  const getX = (i) => padL + (i / (n - 1)) * plotW;
  const getY = (val, max = 100) => padT + plotH - (val / max) * plotH;

  // Serie 1: Resueltos en SLA (Escala 0..60 normalizada a 100)
  if (seriesVisibility.resolved) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.resolved, 60)}}`).join(' ');
    svg += `<polyline fill="none" stroke="#10b981" stroke-width="3" points="${{pts}}"/>`;
  }}
  // Serie 2: Reprocesos (Escala 0..100)
  if (seriesVisibility.rework) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.rework, 100)}}`).join(' ');
    svg += `<polyline fill="none" stroke="#f59e0b" stroke-width="3" points="${{pts}}"/>`;
  }}
  // Serie 3: Bugs en Producción (Escala 0..20 normalizada a 100)
  if (seriesVisibility.bugs) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.bugs, 20)}}`).join(' ');
    svg += `<polyline fill="none" stroke="#4f46e5" stroke-width="3" points="${{pts}}"/>`;
  }}
  // Serie 4: SLA Cumplimiento (Escala 0..100)
  if (seriesVisibility.sla) {{
    let pts = data.map((d, i) => `${{getX(i)}},${{getY(d.sla, 100)}}`).join(' ');
    svg += `<polyline fill="none" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4 3" points="${{pts}}"/>`;
  }}

  // Puntos interactivos y etiquetas X
  data.forEach((d, i) => {{
    const cx = getX(i);
    // Etiqueta mes
    svg += `<text x="${{cx}}" y="${{H - 8}}" font-size="9.5" fill="var(--text-muted)" text-anchor="middle">${{d.month.split(' ')[0]}}</text>`;

    if (seriesVisibility.resolved) {{
      const cy = getY(d.resolved, 60);
      svg += `<circle cx="${{cx}}" cy="${{cy}}" r="4" fill="#10b981" stroke="#fff" stroke-width="2" style="cursor:pointer;" onmouseenter="showTimelineTip(event, '${{d.month}}', '${{d.resolved}}', '${{d.rework}}', '${{d.bugs}}', '${{d.sla}}', '${{d.stage}}')" onmouseleave="hideTip()"/>`;
    }}
  }});

  svg += `</svg>`;
  wrap.innerHTML = svg;
}}

function showTimelineTip(e, month, res, rew, bugs, sla, stage) {{
  const t = document.getElementById('globalTooltip');
  t.innerHTML = `
    <div style="font-weight:800; font-size:13px; color:#38bdf8; margin-bottom:4px;">${{month}} — ${{stage}}</div>
    <div><b>✓ Resueltos en SLA:</b> ${{res}} controles / mes</div>
    <div><b>⚠ Reprocesos Manuales:</b> ${{rew}}% del tiempo</div>
    <div><b>🐞 Bugs en Producción:</b> ${{bugs}} errores / release</div>
    <div><b>⏱ Cumplimiento SLA:</b> ${{sla}}% en Mesa ITIL</div>
  `;
  t.style.left = (e.clientX + 14) + 'px';
  t.style.top = (e.clientY - 40) + 'px';
  t.style.display = 'block';
}}

// -------------------------------------------------------------------------
// WIDGET 3: BARRAS APILADAS POR APLICACIÓN
// -------------------------------------------------------------------------
function renderAppBars(filtered) {{
  const wrap = document.getElementById('appBarsWrap');
  const appNames = [
    ["ERP Modular Apolo", "ERP Apolo"],
    ["Apolo Académico SaaS", "Apolo SaaS"],
    ["Apolo II Mobile", "Apolo Mobile"],
    ["Portal Web & Hosting VPS", "Hosting VPS"],
    ["AulaCloud & Wiki", "AulaCloud"],
    ["CRM Open Source", "CRM Open"]
  ];

  const appCounts = appNames.map(([full, short]) => {{
    const items = filtered.filter(t => t.app === full);
    const done = items.filter(t => t.status === 'Completado en SLA').length;
    const prog = items.filter(t => t.status === 'En Curso').length;
    const todo = items.filter(t => t.status === 'Por Hacer').length;
    const crit = items.filter(t => t.priority === 'P1 - Crítico').length;
    return {{ full, short, total: items.length, done, prog, todo, crit }};
  }});

  const maxTotal = Math.max(...appCounts.map(a => a.total), 1);
  const W = 520, H = 220;
  const padL = 40, padR = 20, padB = 30;
  const barW = 42;
  const colSpacing = (W - padL - padR) / appNames.length;

  let svg = `<svg viewBox="0 0 ${{W}} ${{H}}" style="width:100%; height:auto;">`;
  svg += `<line x1="${{padL}}" y1="${{H - padB}}" x2="${{W - padR}}" y2="${{H - padB}}" stroke="var(--border-color)" stroke-width="1.5"/>`;

  appCounts.forEach((a, idx) => {{
    const x = padL + idx * colSpacing + (colSpacing - barW) / 2;
    let cy = H - padB;
    const scale = (H - padB - 25) / maxTotal;

    const hDone = a.done * scale;
    const hProg = a.prog * scale;
    const hTodo = a.todo * scale;

    // Segmento Done
    if (hDone > 0) {{
      svg += `<rect x="${{x}}" y="${{cy - hDone}}" width="${{barW}}" height="${{hDone}}" fill="#10b981" rx="2" style="cursor:pointer;" onclick="filterByApp('${{a.full}}')" onmouseenter="showAppTip(event, '${{a.full}}', ${{a.total}}, ${{a.done}}, ${{a.prog}}, ${{a.todo}})" onmouseleave="hideTip()"/>`;
      cy -= hDone;
    }}
    // Segmento In Progress
    if (hProg > 0) {{
      svg += `<rect x="${{x}}" y="${{cy - hProg}}" width="${{barW}}" height="${{hProg}}" fill="#f59e0b" rx="2" style="cursor:pointer;" onclick="filterByApp('${{a.full}}')" onmouseenter="showAppTip(event, '${{a.full}}', ${{a.total}}, ${{a.done}}, ${{a.prog}}, ${{a.todo}})" onmouseleave="hideTip()"/>`;
      cy -= hProg;
    }}
    // Segmento To Do
    if (hTodo > 0) {{
      svg += `<rect x="${{x}}" y="${{cy - hTodo}}" width="${{barW}}" height="${{hTodo}}" fill="#4f46e5" rx="2" style="cursor:pointer;" onclick="filterByApp('${{a.full}}')" onmouseenter="showAppTip(event, '${{a.full}}', ${{a.total}}, ${{a.done}}, ${{a.prog}}, ${{a.todo}})" onmouseleave="hideTip()"/>`;
      cy -= hTodo;
    }}

    // Total sobre la barra
    svg += `<text x="${{x + barW / 2}}" y="${{cy - 5}}" font-size="11" font-weight="800" fill="var(--text-main)" text-anchor="middle">${{a.total}}</text>`;
    // Nombre X
    svg += `<text x="${{x + barW / 2}}" y="${{H - 10}}" font-size="10" font-weight="700" fill="var(--text-muted)" text-anchor="middle">${{a.short}}</text>`;
  }});

  svg += `</svg>`;
  wrap.innerHTML = svg;
}}

function showAppTip(e, name, tot, done, prog, todo) {{
  const t = document.getElementById('globalTooltip');
  t.innerHTML = `
    <div style="font-weight:800; color:#38bdf8; font-size:13px; margin-bottom:4px;">${{name}}</div>
    <div><b>Total Controles:</b> ${{tot}}</div>
    <div><b>✓ Completados en SLA:</b> ${{done}}</div>
    <div><b>⚡ En Curso:</b> ${{prog}}</div>
    <div><b>⏳ Por Hacer:</b> ${{todo}}</div>
    <div style="margin-top:4px; font-size:10.5px; color:#cbd5e1;">(Clic para filtrar solo esta aplicación)</div>
  `;
  t.style.left = (e.clientX + 14) + 'px';
  t.style.top = (e.clientY - 40) + 'px';
  t.style.display = 'block';
}}

// -------------------------------------------------------------------------
// WIDGET 4: APP HOSTING CARDS
// -------------------------------------------------------------------------
function renderHostingCards(filtered) {{
  const cCloud = filtered.filter(t => t.hosting === 'Nube (Cloud VPS SaaS)').length;
  const cServer = filtered.filter(t => t.hosting === 'Servidor Dedicado / VPS').length;
  const cLocal = filtered.filter(t => t.hosting === 'Centro de Datos / Local').length;
  const total = filtered.length || 1;

  // Escalado proporcional a 342 para coincidir con la arquitectura del PETI
  const scale = 342 / ALL_TICKETS.length;
  const nCloud = Math.round(cCloud * scale);
  const nServer = Math.round(cServer * scale);
  const nLocal = Math.max(0, 342 - nCloud - nServer);

  document.getElementById('hCloudVal').textContent = nCloud;
  document.getElementById('hCloudPct').textContent = `${{((cCloud / total) * 100).toFixed(1)}}% (Apolo SaaS)`;

  document.getElementById('hServerVal').textContent = nServer;
  document.getElementById('hServerPct').textContent = `${{((cServer / total) * 100).toFixed(1)}}% (Hosting)`;

  document.getElementById('hLocalVal').textContent = nLocal;
  document.getElementById('hLocalPct').textContent = `${{((cLocal / total) * 100).toFixed(1)}}% (PyMEs)`;

  document.getElementById('hTotalVal').textContent = 342;

  // Clases active
  document.getElementById('cardCloud').classList.toggle('active', currentFilter.hosting === 'Nube (Cloud VPS SaaS)');
  document.getElementById('cardServer').classList.toggle('active', currentFilter.hosting === 'Servidor Dedicado / VPS');
  document.getElementById('cardLocal').classList.toggle('active', currentFilter.hosting === 'Centro de Datos / Local');
}}

// -------------------------------------------------------------------------
// WIDGET 5: GRÁFICO DE DONA DE ESTADO
// -------------------------------------------------------------------------
function renderStatusDonut(filtered) {{
  const done = filtered.filter(t => t.status === 'Completado en SLA').length;
  const prog = filtered.filter(t => t.status === 'En Curso').length;
  const todo = filtered.filter(t => t.status === 'Por Hacer').length;
  const total = filtered.length || 1;

  const pctDone = ((done / total) * 100).toFixed(1);
  const pctProg = ((prog / total) * 100).toFixed(1);
  const pctTodo = ((todo / total) * 100).toFixed(1);

  const C = 2 * Math.PI * 50; // radio 50
  const dDone = (done / total) * C;
  const dProg = (prog / total) * C;
  const dTodo = (todo / total) * C;

  let svg = `
    <svg viewBox="0 0 140 140" style="width:130px; height:130px; margin:0 auto;">
      <circle cx="70" cy="70" r="50" fill="none" stroke="#e2e8f0" stroke-width="20"/>
      <!-- Done (Verde) -->
      <circle cx="70" cy="70" r="50" fill="none" stroke="#10b981" stroke-width="20"
        stroke-dasharray="${{dDone}} ${{C}}" stroke-dashoffset="0" style="cursor:pointer;" onclick="filterByStatus('Completado en SLA')"/>
      <!-- In Progress (Ámbar) -->
      <circle cx="70" cy="70" r="50" fill="none" stroke="#f59e0b" stroke-width="20"
        stroke-dasharray="${{dProg}} ${{C}}" stroke-dashoffset="${{-dDone}}" style="cursor:pointer;" onclick="filterByStatus('En Curso')"/>
      <!-- To Do (Púrpura) -->
      <circle cx="70" cy="70" r="50" fill="none" stroke="#4f46e5" stroke-width="20"
        stroke-dasharray="${{dTodo}} ${{C}}" stroke-dashoffset="${{-(dDone + dProg)}}" style="cursor:pointer;" onclick="filterByStatus('Por Hacer')"/>
      <text x="70" y="68" text-anchor="middle" font-size="20" font-weight="900" fill="var(--text-main)">${{filtered.length}}</text>
      <text x="70" y="84" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--text-muted)">Controles</text>
    </svg>
  `;
  document.getElementById('donutWrap').innerHTML = svg;

  const tbody = document.getElementById('statusTableBody');
  tbody.innerHTML = `
    <tr onclick="filterByStatus('Completado en SLA')">
      <td><span class="dot" style="background:#10b981;"></span>Completado</td>
      <td><b>${{done}}</b></td>
      <td>${{pctDone}}%</td>
    </tr>
    <tr onclick="filterByStatus('En Curso')">
      <td><span class="dot" style="background:#f59e0b;"></span>En Curso</td>
      <td><b>${{prog}}</b></td>
      <td>${{pctProg}}%</td>
    </tr>
    <tr onclick="filterByStatus('Por Hacer')">
      <td><span class="dot" style="background:#4f46e5;"></span>Por Hacer</td>
      <td><b>${{todo}}</b></td>
      <td>${{pctTodo}}%</td>
    </tr>
  `;
}}

// -------------------------------------------------------------------------
// WIDGET 6: TIPO DE SOLICITUD (BARRAS HORIZONTALES)
// -------------------------------------------------------------------------
function renderRequestTypes(filtered) {{
  const types = [
    ["Soporte Técnico ITIL", "#10b981", "DSS02 / APO09"],
    ["Control de Calidad QA", "#06b6d4", "BAI07 / APO10"],
    ["Automatización BPM & ERP", "#4f46e5", "DSS06 / APO14"],
    ["Gestión Comercial CRM", "#f59e0b", "APO08 / APO10"],
    ["Gobierno y Seguridad", "#ef4444", "EDM / DSS05 / MEA"]
  ];

  const total = filtered.length || 1;
  let html = '<div style="display:flex; flex-direction:column; gap:10px;">';

  types.forEach(([name, color, cov]) => {{
    const cnt = filtered.filter(t => t.req_type.includes(name.split(' ')[0])).length;
    const pct = ((cnt / total) * 100).toFixed(1);
    html += `
      <div style="cursor:pointer;" onclick="filterByReqType('${{name}}')">
        <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:700; margin-bottom:3px;">
          <span>${{name}} <span style="font-size:10px; color:var(--text-muted);">(${{cov}})</span></span>
          <span><b>${{cnt}}</b> (${{pct}}%)</span>
        </div>
        <div style="width:100%; height:12px; background:var(--border-light); border-radius:6px; overflow:hidden;">
          <div style="width:${{pct}}%; height:100%; background:${{color}}; border-radius:6px; transition:width 0.3s;"></div>
        </div>
      </div>
    `;
  }});
  html += '</div>';
  document.getElementById('reqTypesWrap').innerHTML = html;
}}

function filterByReqType(t) {{
  currentFilter.reqType = (currentFilter.reqType === t) ? 'ALL' : t;
  renderAll();
}}

// =========================================================================
// TABLA Y EXPLORADOR DE CONTROLES (VISTA 2)
// =========================================================================
function onTableSearch() {{
  tableState.search = (document.getElementById('tableSearchInput').value || '').toLowerCase().trim();
  tableState.page = 1;
  renderTable(getFilteredTickets());
}}

function onPageSizeChange() {{
  tableState.pageSize = parseInt(document.getElementById('tablePageSize').value);
  tableState.page = 1;
  renderTable(getFilteredTickets());
}}

function sortTable(field) {{
  if (tableState.sortField === field) {{
    tableState.sortAsc = !tableState.sortAsc;
  }} else {{
    tableState.sortField = field;
    tableState.sortAsc = true;
  }}
  renderTable(getFilteredTickets());
}}

function renderTable(tickets) {{
  let list = [...tickets];
  if (tableState.search !== '') {{
    const q = tableState.search;
    list = list.filter(t =>
      t.code.toLowerCase().includes(q) ||
      t.title.toLowerCase().includes(q) ||
      t.app.toLowerCase().includes(q) ||
      t.assignee.toLowerCase().includes(q)
    );
  }}

  // Ordenamiento
  list.sort((a, b) => {{
    let vA = a[tableState.sortField];
    let vB = b[tableState.sortField];
    if (typeof vA === 'string') vA = vA.toLowerCase();
    if (typeof vB === 'string') vB = vB.toLowerCase();
    if (vA < vB) return tableState.sortAsc ? -1 : 1;
    if (vA > vB) return tableState.sortAsc ? 1 : -1;
    return 0;
  }});

  // Paginación
  const total = list.length;
  const start = (tableState.page - 1) * tableState.pageSize;
  const paged = list.slice(start, start + tableState.pageSize);

  const tbody = document.getElementById('ticketsTableBody');
  tbody.innerHTML = '';

  if (paged.length === 0) {{
    tbody.innerHTML = '<tr><td colspan="9" style="text-align:center; padding:20px; color:var(--text-muted);">No se encontraron controles con los criterios especificados.</td></tr>';
  }} else {{
    paged.forEach(t => {{
      const pColor = t.priority.includes('P1') ? 'badge-red' : (t.priority.includes('P2') ? 'badge-amber' : 'badge-blue');
      const sColor = t.status === 'Completado en SLA' ? 'badge-green' : (t.status === 'En Curso' ? 'badge-amber' : 'badge-indigo');

      const tr = document.createElement('tr');
      tr.style.cursor = 'pointer';
      tr.onclick = (e) => {{
        if (e.target.tagName !== 'BUTTON') openAuditModal(t.code);
      }};
      tr.innerHTML = `
        <td><b style="color:var(--primary);">${{t.code}}</b></td>
        <td><b>${{t.title}}</b></td>
        <td>${{t.app}}</td>
        <td><span class="badge badge-indigo">${{t.domain}}</span></td>
        <td><span class="badge ${{pColor}}">${{t.priority}}</span></td>
        <td><span class="badge ${{sColor}}">${{t.status}}</span></td>
        <td><b>${{t.sla}}%</b></td>
        <td>${{t.assignee.split('(')[0]}}</td>
        <td><button class="btn btn-outline" style="padding:4px 8px; font-size:11px;" onclick="openAuditModal('${{t.code}}')">Ficha RCA</button></td>
      `;
      tbody.appendChild(tr);
    }});
  }}

  // Info y botones paginación
  const end = Math.min(start + tableState.pageSize, total);
  document.getElementById('tablePaginationInfo').textContent = `Mostrando ${{total > 0 ? start + 1 : 0}} a ${{end}} de ${{total}} registros`;

  const totalPages = Math.ceil(total / tableState.pageSize) || 1;
  let pBtns = '';
  pBtns += `<button class="btn btn-outline" style="padding:3px 8px; font-size:11px;" ${{tableState.page === 1 ? 'disabled' : ''}} onclick="changePage(${{tableState.page - 1}})">« Anterior</button>`;
  for (let p = 1; p <= totalPages; p++) {{
    pBtns += `<button class="btn ${{p === tableState.page ? 'btn-primary' : 'btn-outline'}}" style="padding:3px 8px; font-size:11px;" onclick="changePage(${{p}})">${{p}}</button>`;
  }}
  pBtns += `<button class="btn btn-outline" style="padding:3px 8px; font-size:11px;" ${{tableState.page === totalPages ? 'disabled' : ''}} onclick="changePage(${{tableState.page + 1}})">Siguiente »</button>`;
  document.getElementById('paginationBtns').innerHTML = pBtns;
}}

function changePage(p) {{
  tableState.page = p;
  renderTable(getFilteredTickets());
}}

// =========================================================================
// MATRIZ DE CASCADA DE METAS (VISTA 3)
// =========================================================================
function initMatrix() {{
  const tbody = document.getElementById('matrixTableBody');
  tbody.innerHTML = '';
  COBIT_MATRIX.forEach(m => {{
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><b style="color:var(--primary);">${{m.code}}</b></td>
      <td><b>${{m.domain}}</b></td>
      <td>${{m.eg}}</td>
      <td>${{m.ag}}</td>
      <td><span class="badge badge-indigo">${{m.bsc}}</span></td>
      <td>${{m.metric}}</td>
      <td style="color:var(--rose);"><b>${{m.as_is}}</b></td>
      <td style="color:var(--emerald);"><b>${{m.to_be}}</b></td>
      <td><span class="badge badge-green">${{m.cap}}</span></td>
      <td>${{m.resp}}</td>
    `;
    tbody.appendChild(tr);
  }});
}}

// =========================================================================
// SIMULADOR DE CAPACIDAD ISO 33000 (VISTA 4)
// =========================================================================
function onSimSliderChange() {{
  updateSimulation();
}}

function loadSimScenario(sc) {{
  if (sc === 'asis') {{
    document.getElementById('rngEdm').value = 1.0;
    document.getElementById('rngApo').value = 2.0;
    document.getElementById('rngBai').value = 0.0;
    document.getElementById('rngDss').value = 2.0;
    document.getElementById('rngMea').value = 0.0;
  }} else if (sc === 'mid') {{
    document.getElementById('rngEdm').value = 2.0;
    document.getElementById('rngApo').value = 3.0;
    document.getElementById('rngBai').value = 2.0;
    document.getElementById('rngDss').value = 3.0;
    document.getElementById('rngMea').value = 2.0;
  }} else if (sc === 'tobe') {{
    document.getElementById('rngEdm').value = 4.0;
    document.getElementById('rngApo').value = 4.0;
    document.getElementById('rngBai').value = 3.0;
    document.getElementById('rngDss').value = 4.0;
    document.getElementById('rngMea').value = 4.0;
  }}
  updateSimulation();
  showToast(`Escenario ${{sc.toUpperCase()}} cargado`);
}}

function updateSimulation() {{
  const edm = parseFloat(document.getElementById('rngEdm').value);
  const apo = parseFloat(document.getElementById('rngApo').value);
  const bai = parseFloat(document.getElementById('rngBai').value);
  const dss = parseFloat(document.getElementById('rngDss').value);
  const mea = parseFloat(document.getElementById('rngMea').value);

  document.getElementById('valSimEdm').textContent = edm.toFixed(1);
  document.getElementById('valSimApo').textContent = apo.toFixed(1);
  document.getElementById('valSimBai').textContent = bai.toFixed(1);
  document.getElementById('valSimDss').textContent = dss.toFixed(1);
  document.getElementById('valSimMea').textContent = mea.toFixed(1);

  const avg = (edm + apo + bai + dss + mea) / 5.0;
  document.getElementById('simAvgCap').textContent = avg.toFixed(2);

  // Proyecciones paramétricas basadas en modelo PETI
  const churn = Math.max(5.0, 24.0 - avg * 3.8).toFixed(1);
  const rework = Math.max(25.0, 92.0 - avg * 13.5).toFixed(1);
  const sla = Math.min(99.0, 52.0 + avg * 10.8).toFixed(1);
  const roi = (1.0 + (avg - 1.0) * 0.12).toFixed(2);

  document.getElementById('simChurnVal').textContent = churn + '%';
  document.getElementById('simReworkVal').textContent = rework + '%';
  document.getElementById('simSlaVal').textContent = sla + '%';
  document.getElementById('simRoiVal').textContent = roi + 'x';

  // Nivel de madurez EIS
  let badgeHtml = '';
  if (avg < 1.0) badgeHtml = 'Madurez EIS: <span class="badge badge-red">Nivel 0: Incompleto</span>';
  else if (avg < 2.0) badgeHtml = 'Madurez EIS: <span class="badge badge-amber">Nivel 1: Inicial / Intuitivo</span>';
  else if (avg < 3.0) badgeHtml = 'Madurez EIS: <span class="badge badge-amber">Nivel 2: Administrado</span>';
  else if (avg < 4.0) badgeHtml = 'Madurez EIS: <span class="badge badge-green">Nivel 3: Definido y Estandarizado</span>';
  else badgeHtml = 'Madurez EIS: <span class="badge badge-green">Nivel 4: Cuantitativo / Orientado a Datos</span>';
  document.getElementById('simMaturityLevelBadge').innerHTML = badgeHtml;
}}

// =========================================================================
// MODAL DE DETALLE DE AUDITORÍA Y CAUSA RAÍZ (RCA)
// =========================================================================
let currentSelectedTicket = null;

function openAuditModal(code) {{
  const t = ALL_TICKETS.find(x => x.code === code) || ALL_TICKETS[0];
  currentSelectedTicket = t;

  document.getElementById('mCode').textContent = t.code;
  document.getElementById('mTitle').textContent = t.title;
  document.getElementById('mApp').textContent = t.app;
  document.getElementById('mHosting').textContent = t.hosting;
  document.getElementById('mProcess').textContent = `${{t.domain}} — ${{t.process}} (${{t.req_type}})`;
  document.getElementById('mBsc').textContent = t.bsc;
  document.getElementById('mPriority').textContent = t.priority;
  document.getElementById('mStatus').textContent = `${{t.status}} (SLA: ${{t.sla}}%)`;
  document.getElementById('mAssignee').textContent = t.assignee;
  document.getElementById('mCap').textContent = `${{t.cap_before}} → ${{t.cap_after}}`;
  document.getElementById('mRca').textContent = t.rca;
  document.getElementById('mAction').textContent = t.action;
  document.getElementById('mEvidence').textContent = t.evidence;

  document.getElementById('auditModal').classList.add('active');
}}

function closeAuditModal() {{
  document.getElementById('auditModal').classList.remove('active');
}}

function copyAuditSummary() {{
  if (!currentSelectedTicket) return;
  const t = currentSelectedTicket;
  const text = `=== FICHA DE AUDITORÍA DE GOBIERNO TI — TECNIFICATE S.A.S. ===\\n` +
    `Código: ${{t.code}}\\nTítulo: ${{t.title}}\\nAplicación: ${{t.app}}\\nDominio: ${{t.domain}} / ${{t.process}}\\n` +
    `Prioridad: ${{t.priority}} | Estado: ${{t.status}} (SLA: ${{t.sla}}%)\\nResponsable: ${{t.assignee}}\\n` +
    `Causa Raíz (RCA): ${{t.rca}}\\nAcción Implementada: ${{t.action}}\\nCapacidad: ${{t.cap_before}} → ${{t.cap_after}}\\nEvidencia: ${{t.evidence}}`;

  navigator.clipboard.writeText(text).then(() => {{
    showToast("Ficha de auditoría copiada al portapapeles");
  }});
}}

// =========================================================================
// MODAL DE CREACIÓN DE NUEVO CONTROL / TICKET
// =========================================================================
function openCreateModal() {{
  document.getElementById('newCode').value = `TECNIF-DSS02-${{ALL_TICKETS.length + 1}}`;
  document.getElementById('newTitle').value = '';
  document.getElementById('newRca').value = '';
  document.getElementById('newAction').value = '';
  document.getElementById('createModal').classList.add('active');
}}

function closeCreateModal() {{
  document.getElementById('createModal').classList.remove('active');
}}

function saveNewTicket() {{
  const code = document.getElementById('newCode').value.trim();
  const title = document.getElementById('newTitle').value.trim();
  if (!code || !title) {{
    alert("Por favor ingrese el código y el título del ticket.");
    return;
  }}

  const newT = {{
    code: code,
    title: title,
    app: document.getElementById('newApp').value,
    domain: document.getElementById('newDomain').value,
    process: `${{document.getElementById('newDomain').value}}02`,
    req_type: "Soporte Técnico ITIL",
    priority: document.getElementById('newPriority').value,
    status: document.getElementById('newStatus').value,
    assignee: document.getElementById('newAssignee').value,
    hosting: document.getElementById('newHosting').value,
    sla: 94.0,
    bsc: "Procesos Internos",
    rca: document.getElementById('newRca').value || "Falta de procedimiento estandarizado en el manejo de incidencias operativas.",
    action: document.getElementById('newAction').value || "Implementación de control de gobierno de TI y capacitación del personal.",
    cap_before: "Nivel 1 (Inicial)",
    cap_after: "Nivel 3 (Establecido)",
    evidence: "Registrado en el sistema de gestión de tickets COBIT 2019."
  }};

  ALL_TICKETS.unshift(newT);
  closeCreateModal();
  renderAll();
  showToast(`Ticket ${{code}} registrado exitosamente`);
}}

// =========================================================================
// EXPORTACIÓN A CSV CON UTF-8 BOM
// =========================================================================
function exportCsv() {{
  const list = getFilteredTickets();
  const headers = [
    "Codigo", "Titulo", "Aplicacion", "Dominio_COBIT", "Proceso_COBIT",
    "Tipo_Solicitud", "Prioridad", "Estado", "Responsable", "Alojamiento",
    "SLA_Porcentaje", "Perspectiva_BSC", "Causa_Raiz_RCA", "Accion_Correctiva",
    "Capacidad_Antes", "Capacidad_Despues", "Evidencia"
  ];

  let csvContent = "\\uFEFF" + headers.join(";") + "\\n";
  list.forEach(t => {{
    const row = [
      t.code, `"${{t.title.replace(/"/g, '""')}}"`, `"${{t.app}}"`, t.domain, t.process,
      `"${{t.req_type}}"`, `"${{t.priority}}"`, `"${{t.status}}"`, `"${{t.assignee}}"`,
      `"${{t.hosting}}"`, t.sla, `"${{t.bsc}}"`, `"${{t.rca.replace(/"/g, '""')}}"`,
      `"${{t.action.replace(/"/g, '""')}}"`, `"${{t.cap_before}}"`, `"${{t.cap_after}}"`,
      `"${{t.evidence.replace(/"/g, '""')}}"`
    ];
    csvContent += row.join(";") + "\\n";
  }});

  const blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `TECNIFICATE_Controles_COBIT2019_${{new Date().toISOString().slice(0,10)}}.csv`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  showToast("Archivo CSV exportado con éxito");
}}

function hideTip() {{
  document.getElementById('globalTooltip').style.display = 'none';
}}
</script>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML Dashboard successfully written to: {HTML_PATH}")
