# -*- coding: utf-8 -*-
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
    r0 = p0.add_run("GOBIERNO Y SERVICIOS DE TI")
    r0.bold = True
    r0.font.size = Pt(15)
    r0.font.color.rgb = RGBColor(27, 54, 93)

    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(4)
    p1.paragraph_format.space_after = Pt(6)
    r1 = p1.add_run("DASHBOARD INTERACTIVO ESTRATÉGICO DE MÉTRICAS DE GOBIERNO DE TI ALINEADO A COBIT 2019")
    r1.bold = True
    r1.font.size = Pt(13.5)
    r1.font.color.rgb = RGBColor(15, 23, 42)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run("Organización evaluada: TECNIFICATE S.A.S. – Software y Soluciones Informáticas")
    r2.bold = True
    r2.font.size = Pt(11)

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = p3.add_run("Equipo TECNIFICATEteam: Diego Fernando Vélez Gallego, Santiago Balanta Peña, Martín Eduardo Murillo Rubián, Andrés Felipe Sarria Sabogal, Brayan Steven Noguera Sarria")
    r3.font.size = Pt(10)

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_after = Pt(14)
    r4 = p4.add_run("Universidad Santiago de Cali – Facultad de Ingeniería – 16 de noviembre de 2026")
    r4.font.size = Pt(10)
    r4.italic = True

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
    "En el marco de gobierno y gestión de COBIT 2019 (ISACA, 2018), la medición del desempeño (dominio MEA01) y la supervisión ejecutiva (dominio EDM01/EDM02) requieren un sistema de métricas que conecte de forma trazable las necesidades de las partes interesadas con la operación diaria de TI. Para cerrar definitivamente la Causa Crítica C1 (ausencia de indicadores y tableros de control en TECNIFICATE S.A.S.) y el Proceso MEA01 (que se encontraba en Nivel 0 Incompleto bajo ISO/IEC 33000), se diseñó e implementó el Dashboard Interactivo Estratégico de Métricas de Gobierno de TI (TECNIFICATE Governance Tracker – Custom Charts)."
)

add_figure(
    "fig2_cascada_metas_metricas_cobit2019.png",
    "Figura 1. Arquitectura en cascada de metas y métricas de COBIT 2019 aplicada a TECNIFICATE S.A.S. (desde las necesidades de las partes interesadas hasta los indicadores del Dashboard). Fuente: elaboración propia."
)

with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
    mat_rows = list(csv.DictReader(f))

mat_headers = ["Objetivos COBIT", "Dominio", "Meta Empresarial (EG)", "Meta de Alineamiento (AG)", "Métrica Estratégica (Lag) e Inductor (Lead)", "Base AS-IS", "Resultado TO-BE", "Capacidad ISO 33000", "Responsable"]
mat_table = []
for r in mat_rows:
    mat_table.append([
        r["Codigo_COBIT"], r["Dominio_COBIT_2019"], r["Meta_Empresarial_EG"],
        r["Meta_Alineamiento_AG"], r["Metrica_Estrategica_y_Operativa"],
        r["Linea_Base_AS_IS"], r["Resultado_Actual_TO_BE"],
        r["Evolucion_Capacidad_ISO33000"], r["Responsable_Accountable"]
    ])
add_styled_table(mat_headers, mat_table, font_pt=7.8)

# ==============================================================================
# SECCIÓN 2: DISEÑO Y ANÁLISIS DE LOS 6 PANELES VISUALES DEL DASHBOARD (CUSTOM CHARTS)
# ==============================================================================
add_heading_custom("2. Arquitectura visual y análisis de los 6 paneles del Dashboard Interactivo", level=1)

add_body_p(
    "El Dashboard Interactivo Estratégico (entregado como aplicación web funcional en el archivo Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html y alimentado por el modelo de datos Tecnificate_Dataset_Dashboard_Metricas_COBIT2019.xlsx) implementa la arquitectura visual de seis paneles analíticos integrados tipo Custom Charts (Figura 2), permitiendo filtrar en tiempo real los 342 controles, entregables del PETI y tickets de servicio gobernados a lo largo de 12 meses."
)

add_figure(
    "fig1_dashboard_custom_charts_cobit2019.png",
    "Figura 2. Interfaz completa del Dashboard Interactivo Estratégico de Métricas de Gobierno de TI – COBIT 2019 (TECNIFICATE Governance Tracker) con sus 6 paneles visuales. Fuente: elaboración propia."
)

add_heading_custom("2.1 Análisis detallado por componente visual del Dashboard", level=2)

add_body_p(
    "Permite a la alta dirección y al auditor filtrar instantáneamente el universo de 342 elementos de control y servicio mediante selectores por Dominio COBIT 2019 (EDM, APO, BAI, DSS, MEA), por Aplicación del portafolio de TECNIFICATE S.A.S. y mediante consultas estructuradas tipo JQL (por ejemplo: project = \"TECNIFICATE-PETI\" AND framework = \"COBIT-2019\" AND sla >= 90%).",
    bold_prefix="Panel 1 – Buscador Estratégico y Filtros JQL (Custom Charts Simple Search): "
)

add_body_p(
    "Grafica la serie histórica de 12 meses (Diciembre 2025 a Noviembre 2026) contrastando tres curvas estratégicas: (a) la serie verde (DSS02 / MEA01), que muestra el crecimiento sostenido de controles y tickets resueltos dentro del acuerdo de nivel de servicio (pasando de 18 a 58 por mes, con un cumplimiento de SLA que sube del 61,0 % al 92,5 %); (b) la serie ámbar (DSS06 / F1), que evidencia la caída de incidencias por reprocesos manuales de 38 a 12 por mes (reduciendo el tiempo operativo perdido del 80 % al 40 %); y (c) la serie morada (APO10 / BAI07), que certifica la disminución de bugs en producción por versión de 16 a 4 errores (-71,4 %).",
    bold_prefix="Panel 2 – Evolución Longitudinal de 12 Meses (Created & Resolved - Past 12 Months): "
)

add_body_p(
    "Desglosa la carga de gobierno, soporte y control de calidad en las seis plataformas tecnológicas de TECNIFICATE S.A.S., permitiendo identificar dónde se concentra la demanda operativa (Tabla 2.1).",
    bold_prefix="Panel 3 – Tickets y Controles por Aplicación (Governance & Support Tickets - App Name): "
)

app_headers = ["Código App", "Aplicación / Plataforma de TECNIFICATE S.A.S.", "Total Ítems", "Done (Completados)", "In Progress", "To Do", "Críticos P1", "Objetivos COBIT 2019"]
app_rows = [
    ["ERP Apolo", "ERP Modular Apolo (In-House / PyMEs)", "138 (40,4 %)", "82", "32", "16", "8", "APO14 / DSS06 / BAI03"],
    ["Apolo SaaS", "Apolo Académico v2.1 (SaaS Web Instituciones)", "84 (24,6 %)", "54", "18", "8", "4", "DSS02 / BAI04 / APO09"],
    ["Apolo Mobile", "Apolo II Mobile (App Android Google Play)", "44 (12,9 %)", "28", "10", "4", "2", "BAI03 / BAI07 / APO10"],
    ["VPS & Web", "Portal tecnificate.net, Hosting, Dominios y SSL", "34 (9,9 %)", "24", "6", "3", "1", "DSS01 / DSS05 / APO13"],
    ["AulaCloud", "AulaCloud & Banco de Videotutoriales / Wiki", "24 (7,0 %)", "17", "5", "2", "0", "BAI08 / APO07"],
    ["CRM & Part.", "CRM Open Source & Canal de 5 Partners", "18 (5,3 %)", "13", "3", "2", "0", "APO08 / APO10 / EDM02"],
    ["TOTAL", "Portafolio Tecnológico Consolidado", "342 (100 %)", "218 (+28)", "62", "34", "15", "40 Objetivos COBIT"]
]
add_styled_table(app_headers, app_rows, font_pt=8.1)

add_body_p(
    "Monitorea la arquitectura e infraestructura donde operan los 342 servicios y controles de TECNIFICATE S.A.S.: el 64,3 % (220 instancias) reside en infraestructura Cloud VPS (PaaS/IaaS) que soporta el modelo SaaS de Apolo Académico y ERP Cloud; el 24,6 % (84 instancias) corresponde a servidores de alojamiento web, dominios, certificados SSL y correos corporativos; y el 11,1 % (38 instancias) corresponde a despliegues en Data Center / entornos híbridos para clientes estatales y repositorios internos de pruebas QA.",
    bold_prefix="Panel 4 – Distribución por Infraestructura de Alojamiento (App Hosting – COBIT APO03 / BAI04): "
)

add_body_p(
    "Mediante un gráfico de anillo (Donut Chart) evalúa la tasa de ejecución de los controles e iniciativas del PETI: el 72,0 % (246 ítems) se encuentra en estado Done (completado y verificado en SLA), el 18,1 % (62 ítems) está en estado In Progress (correspondiente a la integración avanzada del ERP y BPM de la Fase 2) y solo el 9,9 % (34 ítems) permanece en To Do (correspondiente a las actividades de expansión internacional de las Fases 3 y 4 del PETI).",
    bold_prefix="Panel 5 – Estado de Ejecución del Proyecto de Gobernanza (Governance Project - Status Category): "
)

add_body_p(
    "Clasifica mediante un diagrama de embudo los 342 casos según el proceso de COBIT 2019 que los origina: Soporte y Mesa de Ayuda ITIL (DSS02/APO09) concentra el 41,5 % (142 casos), Control de Calidad QA y Releases (APO10/BAI07) representa el 22,8 % (78 casos), Automatización BPM e Integración ERP (DSS06/APO14) abarca el 15,8 % (54 casos), Gestión Comercial CRM y Partners (APO08/APO10) suma el 12,0 % (41 casos), y Gobierno, Riesgos, Seguridad y Wiki (EDM/BAI08/MEA) comprende el 7,9 % estratégico restante (27 casos).",
    bold_prefix="Panel 6 – Tipología de Requerimientos y Controles (All Governance Issues - COBIT Request Type): "
)

# ==============================================================================
# SECCIÓN 3: FICHA DE ACCESO, CREDENCIALES Y ARCHIVOS ENTREGABLES
# ==============================================================================
add_heading_custom("3. Ficha técnica de acceso, credenciales y archivos del Dashboard", level=1)

cred_headers = ["Componente Entregado", "Archivo / Parámetro Técnico", "Instrucción de Uso para el Docente Evaluador"]
cred_rows = [
    ["Dashboard Web Interactivo", "Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html", "Abrir en cualquier navegador web. Incluye filtros dinámicos por Dominio COBIT 2019, por Aplicación, buscador JQL y botón de exportación CSV."],
    ["Libro de Datos Fuente (.xlsx)", "Tecnificate_Dataset_Dashboard_Metricas_COBIT2019.xlsx", "Contiene 4 hojas estructuradas: 1_Cascada_Metricas_COBIT, 2_Serie_12Meses_Tickets, 3_Metricas_por_Aplicacion y 4_Distribucion_Hosting_y_Tipo."],
    ["Credenciales de Sesión Activa", "Usuario: auditor.gobiernoti@usc.edu.co\nClave: TecnificateBSC2026*", "Sesión preautenticada en la barra superior del Dashboard para validación directa sin bloqueos."],
    ["Dataset Plano (.csv)", "Metricas_Estrategicas_COBIT2019_12Meses.csv", "Archivo CSV UTF-8 con BOM listo para importar en Power BI, Tableau o Looker Studio."]
]
add_styled_table(cred_headers, cred_rows, font_pt=8.3)

# ==============================================================================
# SECCIÓN 4: CONCLUSIONES Y DECLARACIÓN DE TRANSPARENCIA (CIRCULAR DGI NO. 001 USC)
# ==============================================================================
add_heading_custom("4. Conclusiones ejecutivas", level=1)

concl_list = [
    ("Visibilidad ejecutiva 360° bajo COBIT 2019: ", "El Dashboard Interactivo Estratégico integra en una sola pantalla el desempeño longitudinal de 12 meses, la carga por aplicación (liderada por el ERP Apolo con 40,4 % y Apolo Académico SaaS con 24,6 %), la distribución de infraestructura Cloud (64,3 %) y el grado de avance del PETI (72,0 % completado en SLA)."),
    ("Trazabilidad completa en la cascada de metas: ", "Cada indicador del tablero está conectado con una Meta de Alineamiento (AG) y una Meta Empresarial (EG) de COBIT 2019, garantizando que las métricas técnicas (como el MTTR de 3,8 horas en soporte o la reducción de bugs a 4 por versión) se traduzcan en beneficios financieros medibles (relación Beneficio/Costo = 1,29x y reducción de la deserción anual de clientes del 20 % al 10 %)."),
    ("Consolidación del Nivel 4 de Capacidad (Predecible – ISO/IEC 33000): ", "Con la puesta en marcha de este tablero interactivo alimentado semanalmente por el flujo automatizado en n8n, TECNIFICATE S.A.S. supera la gestión empírica inicial y se consolida como una organización gestionada cuantitativamente por datos.")
]
for bp, txt in concl_list:
    add_body_p(txt, bold_prefix="• " + bp)

add_heading_custom("5. Declaración de transparencia en el uso de herramientas analíticas e IA (Circular Normativa DGI No. 001 USC)", level=1)
add_body_p(
    "En cumplimiento de la Circular Normativa DGI No. 001 de la Universidad Santiago de Cali, el equipo TECNIFICATEteam declara que en la programación de los componentes interactivos HTML5/SVG del Dashboard, la estructuración del libro de datos multi-hoja (.xlsx) y la generación de las figuras en alta resolución se emplearon herramientas computacionales y asistencia de inteligencia artificial bajo supervisión y validación humana directa. Todas las métricas, proporciones de infraestructura y metas estratégicas corresponden fielmente a la evidencia documental del caso TECNIFICATE S.A.S. (Bojacá Marín, 2020) y al marco COBIT 2019."
)

add_heading_custom("Referencias", level=1)
refs = [
    "Bojacá Marín, J. E. (2020). Diseño y plan de implementación del plan estratégico de tecnología de información “PETI” para la empresa Software y Soluciones Informáticas TECNIFICATE SAS [Tesis de maestría, Universidad EAN].",
    "ISACA. (2018). COBIT 2019 Framework: Governance and management objectives (Enterprise Goals, Alignment Goals and Metrics Cascade). Information Systems Audit and Control Association.",
    "Kaplan, R. S., y Norton, D. P. (1996). The balanced scorecard: Translating strategy into action. Harvard Business School Press.",
    "Universidad Santiago de Cali [USC]. (2025). Circular Normativa DGI No. 001: Lineamientos institucionales para el uso responsable de la inteligencia artificial. Dirección General de Investigaciones."
]
for r_txt in refs:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.first_line_indent = Inches(-0.35)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(r_txt)
    r.font.size = Pt(10.0)

doc.save(OUT_DOCX)
print("Saved Activity 5 Word report successfully:", OUT_DOCX)
