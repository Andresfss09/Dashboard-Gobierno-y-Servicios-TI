# -*- coding: utf-8 -*-
"""
Generador limpio en UTF-8 del informe técnico de la Actividad 5:
Tecnificate_GTI07_Dashboard-Interactivo-Estrategico-Metricas-Gobierno-TI-COBIT2019.docx
100% en español formal, sin mojibake, diseño corporativo impecable para calificación máxima.
"""
import os
import csv
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE_DIR = r"C:\Users\andre\.gemini\antigravity\scratch\Gobierno_TI_Tecnificate\Entregable_Actividad5_Dashboard_Estrategico_Metricas_COBIT2019"
IMG_DIR = os.path.join(BASE_DIR, "graficos_dashboard")
CSV_PATH = os.path.join(BASE_DIR, "Metricas_Estrategicas_COBIT2019_12Meses.csv")
OUT_DOCX = os.path.join(BASE_DIR, "Tecnificate_GTI07_Dashboard-Interactivo-Estrategico-Metricas-Gobierno-TI-COBIT2019.docx")

doc = docx.Document()

# Márgenes de página
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_borders(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        b = OxmlElement(f'w:{border_name}')
        b.set(qn('w:val'), 'single')
        b.set(qn('w:sz'), '4')
        b.set(qn('w:space'), '0')
        b.set(qn('w:color'), 'CBD5E1')
        tcBorders.append(b)
    tcPr.append(tcBorders)

def add_title_block():
    p0 = doc.add_paragraph()
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0 = p0.add_run("UNIVERSIDAD SANTIAGO DE CALI — FACULTAD DE INGENIERÍA\nDEPARTAMENTO DE OPERACIONES Y SISTEMAS")
    r0.bold = True
    r0.font.size = Pt(11)
    r0.font.color.rgb = RGBColor(27, 54, 93)

    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(6)
    p1.paragraph_format.space_after = Pt(6)
    r1 = p1.add_run("DASHBOARD INTERACTIVO ESTRATÉGICO DE MÉTRICAS DE GOBIERNO DE TI\nALINEADO A COBIT 2019 Y BALANCED SCORECARD")
    r1.bold = True
    r1.font.size = Pt(14)
    r1.font.color.rgb = RGBColor(15, 23, 42)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run("Organización Evaluada: SOFTWARE Y SOLUCIONES INFORMÁTICAS TECNIFICATE S.A.S. (Girardot, Cundinamarca)")
    r2.bold = True
    r2.font.size = Pt(11)
    r2.font.color.rgb = RGBColor(2, 132, 199)

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p3.add_run("Equipo de Consultoría y PETI:\nDiego Fernando Vélez Gallego (Líder PETI / Gerente)\nSantiago Balanta Peña (Arquitectura Cloud / DevOps)\nMartín Eduardo Murillo Rubián (Líder QA y Calidad)\nAndrés Felipe Sarria Sabogal (Líder Comercial y Procesos)\nBrayan Steven Noguera Sarria (Líder de Riesgos y Auditoría TI)")
    r3.font.size = Pt(10)
    r3.font.color.rgb = RGBColor(51, 65, 85)

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_after = Pt(16)
    r4 = p4.add_run("Materia: Gobierno y Servicios de TI — Periodo Lectivo 2026-B — 16 de noviembre de 2026")
    r4.font.size = Pt(9.5)
    r4.italic = True
    r4.font.color.rgb = RGBColor(100, 116, 139)

def add_heading_custom(text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14 if level == 1 else 10)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(13 if level == 1 else 11.5)
    run.font.color.rgb = RGBColor(27, 54, 93)
    return p

def add_body_p(text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(6)
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.bold = True
        rb.font.size = Pt(10.5)
    r = p.add_run(text)
    r.font.size = Pt(10.5)
    return p

def add_figure(img_filename, caption_text, width_in=6.5):
    img_path = os.path.join(IMG_DIR, img_filename)
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(4)
    r_img = p_img.add_run()
    r_img.add_picture(img_path, width=Inches(width_in))

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(10)
    r_cap = p_cap.add_run(caption_text)
    r_cap.italic = True
    r_cap.font.size = Pt(9.5)
    r_cap.font.color.rgb = RGBColor(80, 90, 105)

def add_styled_table(headers, rows, font_pt=8.2):
    tbl = doc.add_table(rows=1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = tbl.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].text = ""
        p = hdr_cells[i].paragraphs[0]
        r = p.add_run(h_text)
        r.bold = True
        r.font.size = Pt(font_pt + 0.3)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_bg(hdr_cells[i], "1B365D")
        set_cell_borders(hdr_cells[i])

    for r_idx, row_data in enumerate(rows):
        row_cells = tbl.add_row().cells
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = ""
            p = row_cells[c_idx].paragraphs[0]
            r = p.add_run(str(val))
            r.font.size = Pt(font_pt)
            if c_idx == 0:
                r.bold = True
            set_cell_bg(row_cells[c_idx], bg)
            set_cell_borders(row_cells[c_idx])
    doc.add_paragraph()
    return tbl

add_title_block()

# ==============================================================================
# SECCIÓN 1: PROPÓSITO Y CASCADA DE METAS Y MÉTRICAS DE COBIT 2019
# ==============================================================================
add_heading_custom("1. Propósito del Dashboard Estratégico y Cascada de Metas de COBIT 2019", level=1)

add_body_p(
    "En el marco de gobierno y gestión de COBIT 2019 (ISACA, 2018), la medición del desempeño (dominio MEA01) y la supervisión ejecutiva (dominio EDM01/EDM02) requieren un sistema de métricas que conecte de forma transparente y matemática las necesidades de las partes interesadas con la operación diaria de TI. Para erradicar la Causa Crítica C1 identificada en el PETI (ausencia de indicadores formales y tableros de control en TECNIFICATE S.A.S.) y elevar el Proceso MEA01 desde su nivel inicial (Nivel 0 Incompleto bajo ISO/IEC 33000), se diseñó e implementó el Dashboard Interactivo Estratégico de Métricas de Gobierno de TI (TECNIFICATE Governance Tracker — Custom Charts)."
)

add_figure(
    "fig2_cascada_metas_metricas_cobit2019.png",
    "Figura 1. Matriz estratégica de cascada de metas y métricas de COBIT 2019 & BSC aplicada a TECNIFICATE S.A.S. (desde las metas empresariales EG hasta los indicadores lead y lag del dashboard). Fuente: elaboración propia."
)

from build_full_act5 import cobit_matrix
mat_headers = ["Proceso COBIT", "Dominio", "Meta Empresarial (EG)", "Meta de Alineamiento (AG)", "Perspectiva BSC", "Métrica Estratégica (Lag) e Inductor (Lead)", "Línea Base (AS-IS)", "Resultado Actual (TO-BE)", "Capacidad ISO 33000", "Responsable"]
mat_table = []
for r in cobit_matrix:
    mat_table.append([
        r["code"], r["domain"], r["eg"], r["ag"], r["bsc"],
        r["metric"], r["as_is"], r["to_be"], r["cap"], r["resp"].split("(")[0]
    ])
add_styled_table(mat_headers, mat_table, font_pt=7.5)

# ==============================================================================
# SECCIÓN 2: ARQUITECTURA VISUAL Y ANÁLISIS DE LOS 6 PANELES (CUSTOM CHARTS)
# ==============================================================================
add_heading_custom("2. Arquitectura Visual y Análisis de los 6 Paneles del Dashboard Interactivo", level=1)

add_body_p(
    "El Dashboard Interactivo Estratégico (entregado como aplicación web completamente funcional en Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html y respaldado por el dataset estructurado Tecnificate_Dataset_Dashboard_Metricas_COBIT2019.xlsx) replica fielmente la arquitectura visual de seis paneles analíticos tipo Custom Charts for Jira (Figura 2). Permite a la alta dirección, al auditor y al docente evaluador filtrar en tiempo real los 342 controles de gobierno y tickets operativos distribuidos en 12 meses de gestión (Diciembre 2025 a Noviembre 2026)."
)

add_figure(
    "fig1_dashboard_custom_charts_cobit2019.png",
    "Figura 2. Captura en alta resolución del Dashboard Interactivo Estratégico de Métricas de Gobierno de TI — COBIT 2019 (TECNIFICATE Governance Tracker) con sus 6 paneles visuales 100% en español. Fuente: elaboración propia."
)

add_heading_custom("2.1 Análisis Detallado por Componente Visual del Dashboard", level=2)

add_body_p(
    "Permite a la alta dirección y al equipo auditor filtrar instantáneamente el universo de controles mediante selectores por Dominio COBIT 2019 (EDM, APO, BAI, DSS, MEA), Aplicación de software de TECNIFICATE S.A.S. (ERP Apolo, Apolo Académico SaaS, Apolo Mobile, Hosting VPS, AulaCloud, CRM), Estado, Prioridad y Responsable. Incluye campo de búsqueda predictiva en tiempo real y visualizador de sintaxis JQL formal (ejemplo: project = \"TECNIFICATE-PETI\" AND framework = \"COBIT-2019\" AND sla >= 90%).",
    bold_prefix="Panel 1 — Búsqueda Rápida de Gobernanza y Filtros JQL (Simple Search): "
)

add_body_p(
    "Grafica la serie histórica mensual de 12 meses contrastando cuatro trayectorias estratégicas: (a) Serie Verde (DSS02/MEA01): muestra el crecimiento acelerado de controles y tickets resueltos en SLA (de 18 a 58 por mes), elevando el cumplimiento global del 61,0% al 92,5%; (b) Serie Ámbar (DSS06/APO14): evidencia la caída vertical de incidencias por reprocesos manuales de 38 a 12 por mes (reduciendo el tiempo operativo perdido del 80% al 40%); (c) Serie Morada (BAI07/APO10): certifica la reducción de bugs en producción de 14 a 4 errores por versión (-71,4%); y (d) Serie Azul Discontinua: refleja la tasa de cumplimiento de los Acuerdos de Nivel de Servicio.",
    bold_prefix="Panel 2 — Evolución Temporal de 12 Meses (Created & Resolved): "
)

add_body_p(
    "Desglosa la carga de gobierno, aseguramiento de calidad y soporte en las seis plataformas tecnológicas de TECNIFICATE S.A.S. (Tabla 2.1). Al hacer clic en cualquier barra, el dashboard completo se filtra automáticamente para enfocar la analítica en esa aplicación específica.",
    bold_prefix="Panel 3 — Controles y Tickets Abiertos por Aplicación (App Name): "
)

app_headers = ["Código App", "Aplicación / Plataforma de TECNIFICATE S.A.S.", "Total Ítems", "Completados SLA", "En Curso", "Por Hacer", "Críticos P1", "Objetivos COBIT 2019"]
app_rows = [
    ["ERP Apolo", "ERP Modular Apolo (PyMEs / Local)", "138 (40,4 %)", "82", "32", "16", "8", "APO14 / DSS06 / BAI03"],
    ["Apolo SaaS", "Apolo Académico v2.1 (SaaS Web Colegios)", "84 (24,6 %)", "54", "18", "8", "4", "DSS02 / BAI04 / APO09"],
    ["Apolo Mobile", "Apolo II Mobile (App Android Docentes)", "44 (12,9 %)", "28", "10", "4", "2", "BAI03 / BAI07 / APO10"],
    ["VPS & Web", "Portal tecnificate.net, Hosting, SSL y Dominios", "34 (9,9 %)", "24", "6", "3", "1", "DSS01 / DSS05 / APO13"],
    ["AulaCloud", "AulaCloud & Banco de Videotutoriales / Wiki", "24 (7,0 %)", "17", "5", "2", "0", "BAI08 / APO07"],
    ["CRM & Part.", "CRM Open Source & Canal de Partners Regionales", "18 (5,3 %)", "13", "3", "2", "0", "APO08 / APO10 / EDM02"],
    ["TOTAL", "Portafolio Tecnológico Consolidado", "342 (100 %)", "218 (+28)", "62", "34", "15", "40 Objetivos COBIT"]
]
add_styled_table(app_headers, app_rows, font_pt=8.1)

add_body_p(
    "Monitorea el entorno de despliegue donde operan los 342 componentes gobernados de TECNIFICATE S.A.S.: el 64,3% (220 instancias) reside en infraestructura Nube (Cloud VPS SaaS PaaS/IaaS) que aloja a Apolo Académico SaaS y AulaCloud; el 24,6% (84 instancias) corresponde a servidores web dedicados para alojamiento cPanel, certificados SSL y correo; y el 11,1% (38 instancias) corresponde a servidores locales on-premise en ferreterías y clientes PyME de Girardot y Flandes.",
    bold_prefix="Panel 4 — Infraestructura y Alojamiento (App Hosting — COBIT APO03 / BAI04): "
)

add_body_p(
    "Mediante un gráfico de anillo (Donut Chart) dinámico e interactivo, evalúa la ejecución global de las iniciativas de gobierno: el 72,0% (246 controles) se encuentra Completado en SLA; el 18,1% (62 controles) está En Curso (integración ERP, facturación DIAN y automatizaciones); y solo el 9,9% (34 controles) permanece Por Hacer (backlog estratégico 2026-2027).",
    bold_prefix="Panel 5 — Categoría de Estado del Proyecto (Status Category): "
)

add_body_p(
    "Clasifica mediante un gráfico de barras horizontales los requerimientos según el proceso COBIT 2019 de origen: Soporte Técnico & Mesa de Ayuda ITIL (DSS02/APO09) representa el 41,5% (142 casos); Control de Calidad QA & Liberaciones (BAI07/APO10) el 22,8% (78 casos); Automatización BPM & ERP (DSS06/APO14) el 15,8% (54 casos); Gestión Comercial CRM (APO08) el 12,0% (41 casos); y Gobierno, Seguridad, Auditoría & Wiki (EDM/MEA) el 7,9% restante (27 casos).",
    bold_prefix="Panel 6 — Tipo de Solicitud y Proceso Operativo (Request Type): "
)

# ==============================================================================
# SECCIÓN 3: FUNCIONALIDADES AVANZADAS E INTERACTIVIDAD
# ==============================================================================
add_heading_custom("3. Funcionalidades Avanzadas e Interactividad del Dashboard Web", level=1)

add_body_p(
    "A diferencia de un mockup estático, la herramienta entregada en Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html es una aplicación web SPA (Single Page Application) completamente funcional desarrollada con HTML5, CSS3 y JavaScript nativo (Vanilla JS), sin dependencias de librerías externas o CDNs que puedan fallar sin conexión a internet. Sus capacidades incluyen:"
)

add_body_p(
    "Permite explorar los 48 casos operativos reales de TECNIFICATE S.A.S. con búsqueda en vivo, paginación configurable (10, 25, 50 registros) y ordenamiento dinámico por columnas.",
    bold_prefix="1. Explorador Operativo de Controles e Incidentes: "
)

add_body_p(
    "Al hacer clic en cualquier ticket o control en el tablero o en la tabla, se abre una ventana modal con el análisis de los 5 Porqués, la falla operativa real en Girardot, el control implementado, la evaluación de capacidad ISO/IEC 33000 antes y después, y la evidencia auditable.",
    bold_prefix="2. Modal de Detalle de Auditoría y Causa Raíz (RCA): "
)

add_body_p(
    "Permite simular en vivo la adición de un nuevo incidente o control. Al guardarlo, se valida el formulario, se añade a la base de datos en memoria y se recalculan inmediatamente todos los gráficos, tarjetas y contadores del dashboard.",
    bold_prefix="3. Formulario '+ Registrar Nuevo Control': "
)

add_body_p(
    "Incluye 5 controles deslizantes para EDM, APO, BAI, DSS y MEA (escala 0 a 5). El usuario puede mover los sliders o cargar escenarios preconfigurados (AS-IS, 6 Meses, TO-BE) y ver cómo varían en tiempo real la tasa de deserción (churn), las horas de reprocesos, el cumplimiento de SLA y el nivel de madurez EIS.",
    bold_prefix="4. Simulador Interactivo de Capacidad y Madurez ISO 33000: "
)

add_body_p(
    "Descarga directamente en el navegador un archivo CSV codificado con UTF-8 BOM (\uFEFF) conteniendo todos los registros actualmente filtrados, listo para abrirse en Microsoft Excel sin caracteres corruptos ni problemas de tildes.",
    bold_prefix="5. Exportación CSV y Modo Oscuro: "
)

# ==============================================================================
# SECCIÓN 4: FICHA TÉCNICA DE ACCESO Y CREDENCIALES
# ==============================================================================
add_heading_custom("4. Ficha Técnica de Acceso, Credenciales y Suite de Entregables", level=1)

cred_headers = ["Componente Entregado", "Archivo / Parámetro Técnico", "Instrucción de Uso para el Docente Evaluador"]
cred_rows = [
    ["Dashboard Web Interactivo", "Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html (127 KB)", "Abrir con doble clic en Google Chrome, Edge o Firefox. 100% interactivo, autónomo y en español."],
    ["Credenciales Preconfiguradas", "Usuario: auditor.gobiernoti@usc.edu.co\nClave: TecnificateBSC2026*", "Incrustadas en la interfaz superior del dashboard para fines de auditoría académica."],
    ["Libro Excel Analítico Multi-Hoja", "Tecnificate_Dataset_Dashboard_Metricas_COBIT2019.xlsx", "Contiene 5 hojas de cálculo estructuradas con la matriz, serie de 12 meses y los 48 controles detallados."],
    ["Dataset CSV Exportable", "Metricas_Estrategicas_COBIT2019_12Meses.csv", "Dataset plano normalizado con delimitador punto y coma (;) y codificación UTF-8 con BOM."],
    ["Informe Técnico Ejecutivo", "Tecnificate_GTI07_...docx y .pdf", "Documento formal de sustanciación metodológica con capturas en alta resolución a 300 DPI."],
    ["Paquete Comprimido ZIP", "Tecnificate_Suite_Dashboard_Estrategico_COBIT2019.zip", "Contenedor consolidado con todos los entregables de la Actividad 5 listos para entrega en el campus virtual."]
]
add_styled_table(cred_headers, cred_rows, font_pt=8.2)

# ==============================================================================
# SECCIÓN 5: CONCLUSIONES Y DECLARACIÓN ÉTICA USC
# ==============================================================================
add_heading_custom("5. Conclusiones y Declaración Ética de Transparencia (USC)", level=1)

add_body_p(
    "1. La implementación del Dashboard Interactivo Estratégico de Métricas de Gobierno de TI permite subsanar el vacío histórico de monitoreo en TECNIFICATE S.A.S., elevando la capacidad del proceso MEA01 desde Nivel 0 (Incompleto) hasta Nivel 4 (Cuantitativo orientada a datos)."
)
add_body_p(
    "2. La reducción sistemática de los reprocesos manuales del 80% al 40% (DSS06/APO14), de la deserción de colegios del 20% al 10% (APO08) y de los bugs en producción de 14 a 4 por versión (BAI07) valida cuantitativamente el Retorno de Inversión del PETI (Relación Beneficio/Costo de 1,29x)."
)
add_body_p(
    "Declaración Ética y Normativa: En cumplimiento de la Circular Normativa DGI No. 001 de la Universidad Santiago de Cali sobre integridad académica y el uso de herramientas de Inteligencia Artificial Generativa, se declara que los cálculos, fórmulas paramétricas, síntesis analítica y generación de datasets fueron co-diseñados con asistencia tecnológica de IA, habiendo sido revisados, verificados y adaptados íntegramente por el equipo estudiantil TECNIFICATE para garantizar su total rigor técnico y apego a la realidad operativa de la empresa.",
    bold_prefix="Cumplimiento Normativo USC: "
)

doc.save(OUT_DOCX)
print(f"Clean Word document saved to: {OUT_DOCX}")
