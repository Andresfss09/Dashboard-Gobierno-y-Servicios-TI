# -*- coding: utf-8 -*-
import os
import csv
import json
import math
import zipfile
from xml.sax.saxutils import escape
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\andre\.gemini\antigravity\scratch\Gobierno_TI_Tecnificate\Entregable_Actividad5_Dashboard_Estrategico_Metricas_COBIT2019"
IMG_DIR = os.path.join(BASE_DIR, "graficos_dashboard")
os.makedirs(IMG_DIR, exist_ok=True)

# 1. DATOS DE EVOLUCIÓN MENSUAL (12 MESES: DIC 2025 A NOV 2026)
months_12 = [
    ("Dic 2025", 18, 38, 16, 80.0, 61.0),
    ("Ene 2026", 22, 36, 15, 78.0, 63.5),
    ("Feb 2026", 26, 35, 14, 75.0, 66.0),
    ("Mar 2026", 29, 32, 13, 72.0, 70.0),
    ("Abr 2026", 34, 30, 11, 68.0, 73.5),
    ("May 2026", 38, 27, 10, 64.0, 77.0),
    ("Jun 2026", 42, 25, 8,  60.0, 81.0),
    ("Jul 2026", 45, 22, 7,  55.0, 84.5),
    ("Ago 2026", 48, 19, 6,  50.0, 87.0),
    ("Sep 2026", 51, 17, 5,  46.0, 89.5),
    ("Oct 2026", 54, 15, 4,  43.0, 91.0),
    ("Nov 2026", 58, 12, 4,  40.0, 92.5)
]

# 2. DATOS POR APLICACIÓN DE TECNIFICATE S.A.S. (Open & Managed Governance Tickets - App Name)
app_tickets = [
    ("ERP Apolo", "ERP Modular Apolo (In-House / PyMEs)", 138, 82, 32, 16, 8, "APO14 / DSS06 / BAI03"),
    ("Apolo SaaS", "Apolo Académico v2.1 (SaaS Web)", 84, 54, 18, 8, 4, "DSS02 / BAI04 / APO09"),
    ("Apolo Mobile", "Apolo II Mobile (App Android)", 44, 28, 10, 4, 2, "BAI03 / BAI07 / APO10"),
    ("VPS & Web", "Portal tecnificate.net, Hosting & SSL", 34, 24, 6, 3, 1, "DSS01 / DSS05 / APO13"),
    ("AulaCloud", "AulaCloud & Wiki Videotutoriales", 24, 17, 5, 2, 0, "BAI08 / APO07"),
    ("CRM & Part.", "CRM Open Source & Canal Partners", 18, 13, 3, 2, 0, "APO08 / APO10 / EDM02")
]

# 3. DATOS POR CATEGORÍA DE ESTADO (Status Category: Total = 342)
status_cats = [
    ("To Do (Por Ejecutar)", 34, 9.9, "#4f46e5"),
    ("In Progress (En Curso)", 62, 18.1, "#f59e0b"),
    ("Done (Completado en SLA)", 246, 72.0, "#10b981")
]

# 4. DATOS DE APP HOSTING (Total = 342 instancias/servicios gobernados)
hosting_cats = [
    ("Cloud (VPS PaaS/IaaS)", 220, 64.3, "#0ea5e9", "Apolo Académico SaaS, ERP Cloud y AulaCloud"),
    ("Server (Web Hosting & SSL)", 84, 24.6, "#f59e0b", "Dominios, Correos Corporativos y Portal Web"),
    ("Data Center / On-Premise", 38, 11.1, "#4f46e5", "Desarrollos a la medida PyMEs/Estado y Git QA")
]

# 5. DATOS POR TIPO DE REQUERIMIENTO COBIT 2019 (All Governance Issues - Request Type: Total = 342)
request_types = [
    ("Soporte & Mesa de Ayuda ITIL (DSS02/APO09)", 142, 41.5, "#10b981"),
    ("Control de Calidad QA & Releases (APO10/BAI07)", 78, 22.8, "#0ea5e9"),
    ("Automatización BPM & ERP Apolo (DSS06/APO14)", 54, 15.8, "#4f46e5"),
    ("Gestión Comercial CRM & Partners (APO08/APO10)", 41, 12.0, "#f59e0b"),
    ("Gobierno, Riesgos, Seguridad & Wiki (EDM/BAI08/MEA)", 27, 7.9, "#ef4444")
]

# 6. MATRIZ ESTRATÉGICA DE MÉTRICAS COBIT 2019 (CASCADA DE METAS)
cobit_metrics_matrix = [
    ("EDM01 / EDM02", "Gobernanza (EDM)", "EG01: Portafolio competitivo / Valor financiero", "AG01: Cumplimiento y soporte de TI a metas del negocio",
     "Relación Beneficio / Costo real del PETI (Lag) y % de sesiones de Comité de Gobierno ejecutadas (Lead)",
     "Sin medir (1,00x)", "1,29x (US$4.267,69 / US$3.300)", "Nivel 1 → Nivel 4", "Gerente General / D. Vélez"),
    ("APO02 / APO03 / APO05", "Alinear, Planear y Organizar (APO)", "EG08: Optimización de la funcionalidad interna de procesos", "AG03: Obtención de beneficios de inversiones habilitadas por TI",
     "% de proyectos del PETI ejecutados según priorización Cassidy (258, 214, 132 pts) y % procesos con SIPOC",
     "0 % formalizado", "100 % caracterizado (4 fases PETI)", "Nivel 2 → Nivel 4", "Arquitecto TI (S. Balanta)"),
    ("APO08 / APO10", "Alinear, Planear y Organizar (APO)", "EG02: Continuidad y disponibilidad del servicio al cliente", "AG05: Prestación de servicios de TI de acuerdo con requerimientos",
     "Tasa anual de deserción de clientes (Churn) y % de conversión de plan Free a Premium en CRM",
     "20,0 % deserción", "10,0 % deserción / 6,8 % conv.", "Nivel 1 → Nivel 3", "Líder Comercial / A. Sarria"),
    ("APO10(11) / BAI03 / BAI07", "Construir, Adquirir e Implementar (BAI)", "EG06: Cultura de servicio orientada al cliente y calidad", "AG08: Habilitación y soporte de procesos de negocio integrando aplicaciones",
     "% de reducción de errores (bugs) en producción por versión liberada y cobertura de pruebas QA pre-release",
     "14 bugs / versión", "4 bugs (-71,4 % errores; meta -60 %)", "Nivel 0 → Nivel 3", "Analista QA (M. Murillo)"),
    ("BAI08 / APO07", "Construir, Adquirir e Implementar (BAI)", "EG12: Personas motivadas y calificadas", "AG13: Conocimiento, experiencia e iniciativas para la innovación",
     "% de sobrecosto en proyectos por fuga de conocimiento y horas anuales de capacitación técnica por persona",
     "25,0 % sobrecosto", "10,0 % sobrecosto / 40 h/año", "Nivel 0 → Nivel 3", "Gestión Conocimiento / RR.HH."),
    ("DSS01 / DSS02 / DSS03", "Entregar, Dar Servicio y Soporte (DSS)", "EG02: Continuidad y atención oportuna al cliente", "AG07: Seguridad de la información, infraestructura y aplicaciones",
     "% de cumplimiento de SLA en tickets de Mesa de Ayuda ITIL y Tiempo Medio de Resolución (MTTR)",
     "62,0 % (18,5 h)", "92,5 % SLA cumplido (3,8 h MTTR)", "Nivel 2 → Nivel 4", "Líder Soporte Técnico"),
    ("DSS06 / APO14", "Entregar, Dar Servicio y Soporte (DSS)", "EG08: Eficiencia operativa y reducción de costos", "AG08: Integración de datos y flujos de trabajo entre áreas",
     "% del tiempo operativo consumido en reprocesos manuales y N.º de áreas integradas en el ERP Apolo",
     "80,0 % (0/4 áreas)", "40,0 % reprocesos (4/4 áreas ERP)", "Nivel 0 → Nivel 3", "Líder Operaciones / ERP"),
    ("MEA01 / MEA02 / MEA03", "Supervisar, Evaluar y Valorar (MEA)", "EG04: Calidad de la información financiera y de gestión", "AG02: Riesgo de TI gestionado y cumplimiento normativo",
     "% de objetivos estratégicos con KPI activo en Dashboard BI y % de controles COBIT auditados semanalmente",
     "0 % (Sin KPIs)", "100 % KPIs activos (Audited = Yes)", "Nivel 0 → Nivel 4", "Comité Gobierno / B. Noguera")
]

# Exportar CSV consolidado
csv_path = os.path.join(BASE_DIR, "Metricas_Estrategicas_COBIT2019_12Meses.csv")
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["Codigo_COBIT", "Dominio_COBIT_2019", "Meta_Empresarial_EG", "Meta_Alineamiento_AG", "Metrica_Estrategica_y_Operativa", "Linea_Base_AS_IS", "Resultado_Actual_TO_BE", "Evolucion_Capacidad_ISO33000", "Responsable_Accountable"])
    for r in cobit_metrics_matrix:
        w.writerow(r)

# Generar libro Excel .xlsx multi-hoja
def create_act5_xlsx(filename):
    sheets = [
        ("1_Cascada_Metricas_COBIT", [["Codigo_COBIT", "Dominio_COBIT_2019", "Meta_Empresarial_EG", "Meta_Alineamiento_AG", "Metrica_Estrategica_KPI", "Linea_Base_AS_IS", "Meta_Alcanzada_TO_BE", "Capacidad_ISO33000", "Responsable"]] + [list(r) for r in cobit_metrics_matrix]),
        ("2_Serie_12Meses_Tickets", [["Mes", "Tickets_Resueltos_en_SLA_DSS02", "Solicitudes_Cambio_y_Reproceso_DSS06", "Bugs_Produccion_BAI07", "Porcentaje_Tiempo_Reprocesos", "Porcentaje_Cumplimiento_SLA"]] + [list(r) for r in months_12]),
        ("3_Metricas_por_Aplicacion", [["App_Code", "Nombre_Aplicacion_Tecnificate", "Total_Items_Gobernados", "Resueltos_Done", "En_Curso_InProgress", "Pendientes_ToDo", "Criticos_P1", "Objetivos_COBIT_Asociados"]] + [list(r) for r in app_tickets]),
        ("4_Distribucion_Hosting_y_Tipo", [["Categoria", "Subcategoria_o_Dominio", "Cantidad_Items", "Porcentaje", "Detalle"]] +
         [["Status Category", r[0], r[1], r[2], "Estado de ejecución"] for r in status_cats] +
         [["App Hosting", r[0], r[1], r[2], r[4]] for r in hosting_cats] +
         [["Request Type", r[0], r[1], r[2], "Distribución por proceso COBIT 2019"] for r in request_types])
    ]
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        overrides = "".join([f'<Override PartName="/xl/worksheets/sheet{i+1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(len(sheets))])
        zf.writestr('[Content_Types].xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>{overrides}</Types>')
        zf.writestr('_rels/.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        stags = "".join([f'<sheet name="{escape(n)}" sheetId="{i+1}" r:id="rId{i+1}"/>' for i, (n, _) in enumerate(sheets)])
        zf.writestr('xl/workbook.xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>{stags}</sheets></workbook>')
        wrels = "".join([f'<Relationship Id="rId{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i+1}.xml"/>' for i in range(len(sheets))]) + f'<Relationship Id="rId{len(sheets)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
        zf.writestr('xl/_rels/workbook.xml.rels', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{wrels}</Relationships>')
        zf.writestr('xl/styles.xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><fonts count="2"><font><sz val="10"/><name val="Calibri"/></font><font><b/><sz val="10"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font></fonts><fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF1B365D"/></patternFill></fill></fills><borders count="2"><border><left/><right/><top/><bottom/><diagonal/></border><border><left style="thin"><color rgb="FFCBD5E1"/></left><right style="thin"><color rgb="FFCBD5E1"/></right><top style="thin"><color rgb="FFCBD5E1"/></top><bottom style="thin"><color rgb="FFCBD5E1"/></bottom><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1"/><xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/></cellXfs></styleSheet>')
        for idx, (_, rows) in enumerate(sheets):
            rxml = []
            for ri, row in enumerate(rows, start=1):
                cxml = []
                s = "1" if ri == 1 else "0"
                for ci, val in enumerate(row, start=1):
                    ref = f"{chr(64+ci)}{ri}"
                    if isinstance(val, (int, float)) and ri > 1:
                        cxml.append(f'<c r="{ref}" s="0"><v>{val}</v></c>')
                    else:
                        cxml.append(f'<c r="{ref}" t="inlineStr" s="{s}"><is><t>{escape(str(val))}</t></is></c>')
                rxml.append(f'<row r="{ri}">{"".join(cxml)}</row>')
            zf.writestr(f'xl/worksheets/sheet{idx+1}.xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>{"".join(rxml)}</sheetData></worksheet>')

create_act5_xlsx(os.path.join(BASE_DIR, "Tecnificate_Dataset_Dashboard_Metricas_COBIT2019.xlsx"))

# ==============================================================================
# RENDERIZAR FIGURA 1: CAPTURA DE ALTA RESOLUCIÓN (300 DPI) DEL DASHBOARD CUSTOM CHARTS
# ==============================================================================
def get_font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def draw_fig1_dashboard():
    W, H = 1920, 1120
    BG = (241, 245, 249)
    WHITE = (255, 255, 255)
    NAVY = (15, 23, 42)
    BLUE = (2, 132, 199)
    INDIGO = (79, 70, 229)
    GREEN = (16, 185, 129)
    AMBER = (245, 158, 11)
    RED = (239, 68, 68)
    GRAY_D = (51, 65, 85)
    GRAY_M = (100, 116, 139)
    BORDER = (203, 213, 225)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Top Navigation Bar (estilo Jira Custom Charts / Old Street Tracker adaptado a TECNIFICATE)
    d.rectangle([0, 0, W, 64], fill=WHITE)
    d.line([(0, 64), (W, 64)], fill=BORDER, width=2)
    d.rounded_rectangle([24, 14, 60, 50], radius=8, fill=INDIGO)
    d.text((34, 18), "T", fill=WHITE, font=get_font(22, True))
    d.text((74, 20), "TECNIFICATE Governance Tracker", fill=NAVY, font=get_font(19, True))

    nav_items = ["Your work", "Projects v", "Filters v", "Dashboards v", "COBIT 2019 v", "BSC Metrics v"]
    nx = 385
    for ni in nav_items:
        is_act = "Dashboards" in ni
        d.text((nx, 22), ni, fill=BLUE if is_act else GRAY_D, font=get_font(16, is_act))
        if is_act:
            d.line([(nx, 62), (nx + 95, 62)], fill=BLUE, width=4)
        nx += 118

    d.rounded_rectangle([1115, 15, 1205, 49], radius=6, fill=BLUE)
    d.text((1134, 22), "Create", fill=WHITE, font=get_font(16, True))
    d.rounded_rectangle([1230, 15, 1560, 49], radius=6, fill=BG, outline=BORDER)
    d.text((1245, 22), "Search COBIT 2019 / PETI metrics...", fill=GRAY_M, font=get_font(15, False))
    d.text((1590, 22), "Sesión: auditor.gobiernoti@usc.edu.co", fill=INDIGO, font=get_font(15, True))

    # Layout de 3 columnas como en la imagen de referencia del docente
    # Columna 1: x=24..624 (w=600) -> Panel 1 (Simple Search) arriba + Panel 2 (Created - Past 12 Months) abajo
    # Columna 2: x=644..1264 (w=620) -> Panel 3 (Open Tickets - App Name) arriba + Panel 4 (App Hosting) abajo
    # Columna 3: x=1284..1896 (w=612) -> Panel 5 (Status Category Donut) arriba + Panel 6 (All Issues - Request Type Funnel) abajo

    # ------------------------------------------------------------------
    # PANEL 1: Custom Charts Simple Search (Col 1 Top)
    # ------------------------------------------------------------------
    p1 = [24, 82, 624, 305]
    d.rounded_rectangle(p1, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p1[0], p1[1], p1[2], p1[1]], fill=RED, width=4)
    d.text((42, 96), "▾ Custom Charts Simple Search — COBIT 2019 Filter", fill=GRAY_D, font=get_font(15, True))

    pills = [("Project: TECNIFICATE (PETI)", INDIGO, 42), ("Domain: All (EDM/APO/BAI/DSS/MEA)", BG, 250), ("Assignee: All", BG, 505)]
    for p_txt, p_bg, px in pills:
        fg = WHITE if p_bg == INDIGO else GRAY_D
        w_p = int(d.textlength(p_txt, font=get_font(13, True))) + 20
        d.rounded_rectangle([px, 132, px + w_p, 162], radius=5, fill=p_bg, outline=BORDER)
        d.text((px + 10, 138), p_txt, fill=fg, font=get_font(13, True))

    d.rounded_rectangle([42, 176, 485, 212], radius=5, fill=WHITE, outline=BORDER)
    d.text((54, 185), "framework = COBIT2019 AND sla >= 90%", fill=GRAY_M, font=get_font(14, False))
    d.rounded_rectangle([500, 176, 598, 212], radius=5, fill=BLUE)
    d.text((525, 185), "Search", fill=WHITE, font=get_font(14, True))

    d.text((42, 232), "● 342 governance controls & service issues found", fill=GREEN, font=get_font(14, True))
    d.text((520, 232), "Show JQL", fill=BLUE, font=get_font(14, True))
    d.text((42, 262), "Línea Base AS-IS: 38,3% BSC (Nivel 1) → Actual TO-BE: 78,0% BSC (Nivel 4 ISO 33000)", fill=GRAY_M, font=get_font(13, False))

    # ------------------------------------------------------------------
    # PANEL 2: Created & Resolved - Past 12 Months (Col 1 Bottom)
    # ------------------------------------------------------------------
    p2 = [24, 322, 624, 1095]
    d.rounded_rectangle(p2, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p2[0], p2[1], p2[2], p2[1]], fill=GREEN, width=4)
    d.text((42, 336), "▾ Custom Charts", fill=GRAY_M, font=get_font(14, True))
    d.text((155, 372), "Created & Resolved - Past 12 Months (COBIT 2019)", fill=NAVY, font=get_font(18, True))

    gx0, gy0, gw, gh = 78, 435, 515, 430
    for y_val in [0, 20, 40, 60, 80]:
        yy = gy0 + gh - int((y_val / 85.0) * gh)
        d.line([(gx0, yy), (gx0 + gw, yy)], fill=(226, 232, 240), width=1)
        d.text((44, yy - 8), str(y_val), fill=GRAY_M, font=get_font(13, False))

    # Series: Verde = SLA Cumplido (61 a 92.5 -> escalado a tickets 18..58), Amarillo = Reprocesos/Cambios (38..12), Morado = Bugs por Release (16..4)
    s_green = [r[1] for r in months_12]
    s_amber = [r[2] for r in months_12]
    s_purp = [r[3] for r in months_12]
    m_names = [r[0][:3] + " " + r[0][-2:] for r in months_12]

    def plot_series(vals, col):
        pts = []
        for idx, v in enumerate(vals):
            px = gx0 + int(idx * (gw / 11.0))
            py = gy0 + gh - int((v / 70.0) * gh)
            pts.append((px, py))
        d.line(pts, fill=col, width=4)
        for idx, (px, py) in enumerate(pts):
            d.ellipse([px-5, py-5, px+5, py+5], fill=WHITE, outline=col, width=3)
            d.text((px - 8, py - 22), str(vals[idx]), fill=col, font=get_font(12, True))

    plot_series(s_green, GREEN)
    plot_series(s_amber, AMBER)
    plot_series(s_purp, INDIGO)

    for idx, mn in enumerate(m_names):
        px = gx0 + int(idx * (gw / 11.0))
        d.text((px - 18, gy0 + gh + 12), mn, fill=GRAY_M, font=get_font(11, False))

    # Caja descriptiva inferior en Panel 2
    d.rounded_rectangle([42, 925, 606, 1075], radius=6, fill=BG, outline=BORDER)
    d.text((54, 938), "Evolución Estratégica de Métricas COBIT 2019 (12 Meses):", fill=NAVY, font=get_font(14, True))
    d.text((54, 966), "• Serie Verde (DSS02/MEA01): Controles y tickets en SLA >= 90% (18 a 58/mes).", fill=GREEN, font=get_font(12, True))
    d.text((54, 992), "• Serie Ámbar (DSS06/F1): Reprocesos manuales (cae de 38 a 12/mes: 80% → 40%).", fill=AMBER, font=get_font(12, True))
    d.text((54, 1018), "• Serie Morada (APO10/BAI07): Bugs en producción (cae de 16 a 4 bugs: -71,4%).", fill=INDIGO, font=get_font(12, True))
    d.text((54, 1044), "Resultado: Transición verificada desde Nivel 1 (Inicial) hacia Nivel 4 (ISO 33000).", fill=GRAY_D, font=get_font(12, False))

    # ------------------------------------------------------------------
    # PANEL 3: Open & Managed Support/Governance Tickets - App Name (Col 2 Top)
    # ------------------------------------------------------------------
    p3 = [644, 82, 1264, 765]
    d.rounded_rectangle(p3, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p3[0], p3[1], p3[2], p3[1]], fill=AMBER, width=4)
    d.text((662, 96), "▾ Custom Charts", fill=GRAY_M, font=get_font(14, True))
    d.text((765, 132), "Governance & Support Tickets - App Name", fill=NAVY, font=get_font(18, True))

    bx0, by0, bw, bh = 705, 195, 525, 460
    for y_v in [0, 50, 100, 150]:
        yy = by0 + bh - int((y_v / 155.0) * bh)
        d.line([(bx0, yy), (bx0 + bw, yy)], fill=(226, 232, 240), width=1)
        d.text((665, yy - 8), str(y_v), fill=GRAY_M, font=get_font(13, False))

    for idx, (short_n, full_n, tot, c_done, c_prog, c_todo, c_crit, cob_c) in enumerate(app_tickets):
        cx = bx0 + 22 + idx * 85
        col_w = 52
        # Apilar segmentos: Done (Ámbar/Azul estilo ref), InProgress, ToDo, Crit
        segs = [(c_done, AMBER), (c_prog, INDIGO), (c_todo, GREEN), (c_crit, BLUE)]
        curr_y = by0 + bh
        for sv, scol in segs:
            sh = int((sv / 155.0) * bh)
            if sh > 0:
                d.rectangle([cx, curr_y - sh, cx + col_w, curr_y], fill=scol)
                curr_y -= sh
        d.text((cx + 10, curr_y - 24), str(tot), fill=NAVY, font=get_font(14, True))
        d.text((cx - 2, by0 + bh + 12), short_n, fill=GRAY_D, font=get_font(13, True))
        d.text((cx - 2, by0 + bh + 32), cob_c[:5], fill=GRAY_M, font=get_font(11, False))

    d.text((895, by0 + bh + 62), "APP NAME (PORTAFOLIO TECNIFICATE S.A.S.)", fill=GRAY_M, font=get_font(13, True))

    # ------------------------------------------------------------------
    # PANEL 4: App Hosting (Col 2 Bottom)
    # ------------------------------------------------------------------
    p4 = [644, 782, 1264, 1095]
    d.rounded_rectangle(p4, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p4[0], p4[1], p4[2], p4[1]], fill=BLUE, width=4)
    d.text((662, 796), "▾ Custom Charts", fill=GRAY_M, font=get_font(14, True))
    d.text((895, 826), "App Hosting (COBIT APO03 / BAI04)", fill=NAVY, font=get_font(18, True))

    cards_h = [
        ("Cloud (VPS SaaS)", "220", "64,3%", BLUE, 666),
        ("Server / Web SSL", "84", "24,6%", AMBER, 868),
        ("Data Center / Local", "38", "11,1%", INDIGO, 1070)
    ]
    for h_title, h_num, h_pct, h_col, hx in cards_h:
        d.rounded_rectangle([hx, 872, hx + 178, 1025], radius=14, fill=WHITE, outline=h_col, width=4)
        tw_t = d.textlength(h_title, font=get_font(15, True))
        d.text((hx + (178 - tw_t)/2, 888), h_title, fill=GRAY_D, font=get_font(15, True))
        tw_n = d.textlength(h_num, font=get_font(36, True))
        d.text((hx + (178 - tw_n)/2, 922), h_num, fill=BLUE if h_col != INDIGO else INDIGO, font=get_font(36, True))
        tw_p = d.textlength(h_pct, font=get_font(15, True))
        d.text((hx + (178 - tw_p)/2, 982), h_pct, fill=GRAY_M, font=get_font(15, True))

    d.text((765, 1048), "Chart By: App Hosting    Count: Controles/Servicios    Total: 342", fill=NAVY, font=get_font(14, True))

    # ------------------------------------------------------------------
    # PANEL 5: Support & Governance Project - Status Category Donut (Col 3 Top)
    # ------------------------------------------------------------------
    p5 = [1284, 82, 1896, 560]
    d.rounded_rectangle(p5, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p5[0], p5[1], p5[2], p5[1]], fill=BLUE, width=4)
    d.text((1302, 96), "▾ Custom Charts", fill=GRAY_M, font=get_font(14, True))
    d.text((1430, 132), "Governance Project - Status Category", fill=NAVY, font=get_font(18, True))

    # Donut Chart a la izquierda del Panel 5
    dcx, dcy, dr_out, dr_in = 1435, 340, 125, 74
    bbox_out = [dcx - dr_out, dcy - dr_out, dcx + dr_out, dcy + dr_out]
    # Angulos: To Do = 9.9% (35.6 deg), In Progress = 18.1% (65.2 deg), Done = 72.0% (259.2 deg)
    d.pieslice(bbox_out, start=-90, end=-54, fill=INDIGO)
    d.pieslice(bbox_out, start=-54, end=11, fill=AMBER)
    d.pieslice(bbox_out, start=11, end=270, fill=GREEN)
    d.ellipse([dcx - dr_in, dcy - dr_in, dcx + dr_in, dcy + dr_in], fill=WHITE)
    d.text((dcx - 32, dcy - 22), "342", fill=NAVY, font=get_font(28, True))
    d.text((dcx - 42, dcy + 12), "Controles", fill=GRAY_M, font=get_font(14, False))

    # Tabla lateral en Panel 5
    tx5, ty5 = 1585, 235
    d.text((tx5, ty5), "Status Category", fill=GRAY_M, font=get_font(13, True))
    d.text((tx5 + 150, ty5), "Issues", fill=GRAY_M, font=get_font(13, True))
    d.text((tx5 + 215, ty5), "%", fill=GRAY_M, font=get_font(13, True))
    d.line([(tx5, ty5 + 24), (1875, ty5 + 24)], fill=BORDER, width=1)

    st_rows = [
        ("To Do (Fase 3-4)", "34", "9,9%", INDIGO),
        ("In Progress", "62", "18,1%", AMBER),
        ("Done (En SLA)", "246", "72,0%", GREEN),
    ]
    for idx, (s_lbl, s_cnt, s_pct, s_col) in enumerate(st_rows):
        ry = ty5 + 38 + idx * 42
        d.ellipse([tx5, ry + 2, tx5 + 16, ry + 18], fill=s_col)
        d.text((tx5 + 24, ry), s_lbl, fill=GRAY_D, font=get_font(14, False))
        d.text((tx5 + 155, ry), s_cnt, fill=BLUE, font=get_font(14, True))
        d.text((tx5 + 210, ry), s_pct, fill=BLUE, font=get_font(14, True))
        d.line([(tx5, ry + 28), (1875, ry + 28)], fill=BG, width=1)

    d.text((tx5, ty5 + 175), "Total", fill=NAVY, font=get_font(14, True))
    d.text((tx5 + 150, ty5 + 175), "342", fill=NAVY, font=get_font(14, True))
    d.text((tx5 + 210, ty5 + 175), "100%", fill=NAVY, font=get_font(14, True))

    # ------------------------------------------------------------------
    # PANEL 6: All Governance & Support Issues - Request Type (Col 3 Bottom)
    # ------------------------------------------------------------------
    p6 = [1284, 578, 1896, 1095]
    d.rounded_rectangle(p6, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p6[0], p6[1], p6[2], p6[1]], fill=BLUE, width=4)
    d.text((1302, 592), "▾ Custom Charts", fill=GRAY_M, font=get_font(14, True))
    d.text((1405, 628), "All Governance Issues - COBIT Request Type", fill=NAVY, font=get_font(18, True))

    # Embudo simétrico a la izquierda de Panel 6
    fcx = 1415
    funnel_bars = [
        (180, 38, GREEN),
        (135, 38, BLUE),
        (105, 38, INDIGO),
        (82, 38, AMBER),
        (56, 38, RED)
    ]
    fy = 705
    d.line([(fcx, fy), (fcx, fy + 260)], fill=AMBER, width=2)
    for fw_b, fh_b, f_col in funnel_bars:
        d.rounded_rectangle([fcx - fw_b//2, fy, fcx + fw_b//2, fy + fh_b], radius=6, fill=f_col)
        fy += fh_b + 14

    # Tabla derecha en Panel 6
    tx6, ty6 = 1530, 685
    d.text((tx6, ty6), "Request Type (COBIT)", fill=GRAY_M, font=get_font(13, True))
    d.text((tx6 + 215, ty6), "Issues", fill=GRAY_M, font=get_font(13, True))
    d.text((tx6 + 275, ty6), "%", fill=GRAY_M, font=get_font(13, True))
    d.line([(tx6, ty6 + 24), (1880, ty6 + 24)], fill=BORDER, width=1)

    req_short = [
        ("Soporte ITIL (DSS02)", "142", "41,5%", GREEN),
        ("Calidad QA (APO10/BAI07)", "78", "22,8%", BLUE),
        ("BPM & ERP (DSS06/APO14)", "54", "15,8%", INDIGO),
        ("CRM & Ventas (APO08)", "41", "12,0%", AMBER),
        ("Gobierno & Wiki (EDM/MEA)", "27", "7,9%", RED),
    ]
    for idx, (r_lbl, r_cnt, r_pct, r_col) in enumerate(req_short):
        ry = ty6 + 36 + idx * 46
        d.ellipse([tx6, ry + 2, tx6 + 16, ry + 18], fill=r_col)
        d.text((tx6 + 22, ry), r_lbl, fill=GRAY_D, font=get_font(13, False))
        d.text((tx6 + 220, ry), r_cnt, fill=BLUE, font=get_font(13, True))
        d.text((tx6 + 272, ry), r_pct, fill=BLUE, font=get_font(13, True))
        d.line([(tx6, ry + 30), (1880, ry + 30)], fill=BG, width=1)

    d.text((tx6, ty6 + 275), "Total", fill=NAVY, font=get_font(14, True))
    d.text((tx6 + 218, ty6 + 275), "342", fill=NAVY, font=get_font(14, True))
    d.text((tx6 + 270, ty6 + 275), "100%", fill=NAVY, font=get_font(14, True))

    img.save(os.path.join(IMG_DIR, "fig1_dashboard_custom_charts_cobit2019.png"), dpi=(300, 300))

# ==============================================================================
# RENDERIZAR FIGURA 2: CASCADA DE METAS Y MÉTRICAS COBIT 2019 EN TECNIFICATE
# ==============================================================================
def draw_fig2_cascade():
    W, H = 1800, 760
    WHITE = (255, 255, 255)
    NAVY = (27, 54, 93)
    BLUE = (43, 92, 143)
    TEAL = (20, 143, 119)
    GRAY_D = (38, 43, 51)
    GRAY_M = (100, 110, 125)
    BORDER = (203, 213, 224)

    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    d.text((60, 28), "Arquitectura en Cascada de Metas y Métricas de Gobierno de TI (COBIT 2019)", fill=NAVY, font=get_font(30, True))
    d.text((60, 70), "Alineación trazable desde las Necesidades de las Partes Interesadas de TECNIFICATE S.A.S. hasta las Métricas del Dashboard", fill=GRAY_M, font=get_font(20, False))

    stages = [
        ("1. Necesidades de Partes Interesadas\n(Accionistas, PyMEs, Colegios, Equipo)",
         ["• Detener pérdida del 20% anual de clientes (A1)",
          "• Eliminar el 80% de tiempo en reprocesos (D6)",
          "• Evitar el 25% de sobrecosto por rotación (A3)",
          "• Asegurar retorno financiero del PETI (B/C >= 1,29)"],
         NAVY),
        ("2. Metas Empresariales (EG)\n(Perspectivas del BSC Corporativo)",
         ["• EG01: Portafolio de productos SaaS competitivo",
          "• EG02: Continuidad y disponibilidad de servicios",
          "• EG08: Optimización de procesos internos",
          "• EG12: Talento técnico motivado y retenido"],
         BLUE),
        ("3. Metas de Alineamiento (AG)\n(Puente TI – Negocio)",
         ["• AG03: Beneficios realizados de inversiones TI",
          "• AG05: Entrega de servicios acorde a SLA >= 90%",
          "• AG08: Aplicaciones y datos integrados (ERP/CRM)",
          "• AG13: Conocimiento documentado e innovación"],
         TEAL),
        ("4. Métricas de Objetivos COBIT 2019\n(Monitoreadas en Dashboard BI)",
         ["• EDM02 / F2: Relación B/C = 1,29x (PETI)",
          "• DSS02 / P2: SLA ITIL = 92,5% (MTTR = 3,8 h)",
          "• APO10 / BAI07 / P1: -71,4% bugs en prod.",
          "• DSS06 / APO14 / F1: Reprocesos 80% a 40%"],
         (16, 120, 96))
    ]

    sx = 55
    sw = 395
    for idx, (st_title, bullets, col) in enumerate(stages):
        y = 140
        d.rounded_rectangle([sx, y, sx + sw, y + 510], radius=12, fill=(248, 250, 252), outline=BORDER, width=2)
        d.rounded_rectangle([sx, y, sx + sw, y + 84], radius=12, fill=col)
        d.multiline_text((sx + 18, y + 16), st_title, fill=WHITE, font=get_font(19, True), spacing=4)

        by = y + 115
        for b_txt in bullets:
            d.rounded_rectangle([sx + 16, by, sx + sw - 16, by + 82], radius=8, fill=WHITE, outline=BORDER)
            d.multiline_text((sx + 28, by + 18), b_txt, fill=GRAY_D, font=get_font(16, False), spacing=4)
            by += 95

        if idx < 3:
            ax = sx + sw + 4
            ay = y + 255
            d.polygon([(ax, ay - 10), (ax + 24, ay), (ax, ay + 10)], fill=col)

        sx += sw + 34

    d.rounded_rectangle([55, 678, 1745, 735], radius=8, fill=(235, 248, 255), outline=BLUE)
    d.text((80, 695), "Principio COBIT 2019 Aplicado: Cada métrica visualizada en el Dashboard responde a una Meta de Alineamiento (AG) y a una Meta Empresarial (EG).", fill=NAVY, font=get_font(19, True))

    img.save(os.path.join(IMG_DIR, "fig2_cascada_metas_metricas_cobit2019.png"), dpi=(300, 300))

draw_fig1_dashboard()
draw_fig2_cascade()

# ==============================================================================
# GENERAR EL DASHBOARD WEB INTERACTIVO (Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html)
# ==============================================================================
html_dash = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TECNIFICATE Governance Tracker — Dashboard Estratégico de Métricas COBIT 2019</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #f1f5f9; color: #0f172a; min-height: 100vh;
}}
/* Topbar estilo Jira / Custom Charts */
.topbar {{
  background: #ffffff; border-bottom: 1px solid #cbd5e1; padding: 0 24px; height: 60px;
  display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 100;
}}
.nav-left {{ display: flex; align-items: center; gap: 22px; height: 100%; }}
.brand-logo {{
  display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 16.5px; color: #0f172a;
}}
.brand-logo .icon {{
  width: 34px; height: 34px; border-radius: 8px; background: #4f46e5; color: #fff;
  display: flex; align-items: center; justify-content: center; font-weight: 900;
}}
.nav-links {{ display: flex; gap: 18px; height: 100%; align-items: center; font-size: 14px; font-weight: 600; color: #475569; }}
.nav-links span {{ cursor: pointer; height: 100%; display: flex; align-items: center; border-bottom: 3px solid transparent; }}
.nav-links span.active {{ color: #0284c7; border-bottom-color: #0284c7; }}
.btn-create {{
  background: #0284c7; color: #fff; border: none; padding: 7px 14px; border-radius: 6px;
  font-weight: 700; font-size: 13.5px; cursor: pointer;
}}
.nav-right {{ display: flex; align-items: center; gap: 12px; }}
.user-pill {{
  background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8; padding: 5px 12px;
  border-radius: 999px; font-size: 12.5px; font-weight: 700;
}}

/* Grid de 3 columnas estilo Custom Charts */
.dashboard-grid {{
  max-width: 1680px; margin: 18px auto; padding: 0 18px;
  display: grid; grid-template-columns: 1fr 1.05fr 1fr; gap: 16px; align-items: start;
}}
@media (max-width: 1200px) {{ .dashboard-grid {{ grid-template-columns: 1fr; }} }}
.col-stack {{ display: flex; flex-direction: column; gap: 16px; }}

.widget {{
  background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04); overflow: hidden;
}}
.widget.top-red {{ border-top: 4px solid #ef4444; }}
.widget.top-green {{ border-top: 4px solid #10b981; }}
.widget.top-amber {{ border-top: 4px solid #f59e0b; }}
.widget.top-blue {{ border-top: 4px solid #0284c7; }}

.w-hdr {{
  padding: 10px 16px; display: flex; justify-content: space-between; align-items: center;
  font-size: 12.5px; font-weight: 700; color: #64748b; border-bottom: 1px solid #f1f5f9;
}}
.w-body {{ padding: 16px; }}
.w-title {{ text-align: center; font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 14px; }}

/* Simple Search Controls */
.filter-pills {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; }}
.filter-pills select {{
  padding: 6px 10px; border-radius: 6px; border: 1px solid #cbd5e1;
  font-size: 12.5px; font-weight: 600; background: #f8fafc; color: #1e293b; cursor: pointer;
}}
.filter-pills select.primary {{ background: #4f46e5; color: #fff; border-color: #4f46e5; }}
.search-row {{ display: flex; gap: 8px; margin-bottom: 10px; }}
.search-row input {{
  flex: 1; padding: 7px 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 13px;
}}
.search-row button {{
  background: #0284c7; color: #fff; border: none; padding: 7px 16px; border-radius: 6px; font-weight: 700; cursor: pointer;
}}
.jql-meta {{ display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 700; }}

/* Hosting Cards */
.hosting-row {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 10px 0 14px; }}
.h-card {{
  border: 3px solid #0ea5e9; border-radius: 12px; padding: 12px 8px; text-align: center;
}}
.h-card.amber {{ border-color: #f59e0b; }}
.h-card.indigo {{ border-color: #4f46e5; }}
.h-card .lbl {{ font-size: 13px; font-weight: 700; color: #334155; }}
.h-card .num {{ font-size: 28px; font-weight: 800; color: #0284c7; margin: 4px 0; }}
.h-card .pct {{ font-size: 12px; color: #64748b; font-weight: 600; }}

/* Tables inside widgets */
.mini-table {{ width: 100%; border-collapse: collapse; font-size: 12.5px; }}
.mini-table th {{ text-align: left; color: #64748b; padding: 6px; border-bottom: 1px solid #e2e8f0; }}
.mini-table td {{ padding: 7px 6px; border-bottom: 1px solid #f1f5f9; }}
.dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 6px; }}

/* Bottom Full-Width Cascade Table */
.full-section {{ max-width: 1680px; margin: 0 auto 36px; padding: 0 18px; }}
.matrix-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
.matrix-table th {{ background: #1e293b; color: #fff; padding: 10px 12px; text-align: left; }}
.matrix-table td {{ padding: 10px 12px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }}
.matrix-table tr:nth-child(even) td {{ background: #f8fafc; }}
.badge-lvl {{ background: #dcfce7; color: #15803d; padding: 3px 8px; border-radius: 6px; font-weight: 700; font-size: 11.5px; }}
</style>
</head>
<body>

<div class="topbar">
  <div class="nav-left">
    <div class="brand-logo"><div class="icon">T</div> TECNIFICATE Governance Tracker</div>
    <div class="nav-links">
      <span>Your work</span>
      <span>Projects ▾</span>
      <span>Filters ▾</span>
      <span class="active">Dashboards ▾</span>
      <span>COBIT 2019 ▾</span>
      <span>BSC Metrics ▾</span>
    </div>
    <button class="btn-create" onclick="exportCsv()">⬇ Exportar CSV COBIT</button>
  </div>
  <div class="nav-right">
    <span class="user-pill">👤 auditor.gobiernoti@usc.edu.co | Clave: TecnificateBSC2026*</span>
    <button class="btn-create" style="background:#0f172a;" onclick="window.print()">🖨 Imprimir PDF</button>
  </div>
</div>

<div class="dashboard-grid">
  <!-- COLUMNA 1: SIMPLE SEARCH + CREATED PAST 12 MONTHS -->
  <div class="col-stack">
    <div class="widget top-red">
      <div class="w-hdr"><span>▾ Custom Charts Simple Search</span><span>⤢ ⚙</span></div>
      <div class="w-body">
        <div class="filter-pills">
          <select id="selDomain" class="primary" onchange="applyFilters()">
            <option value="ALL">Dominio COBIT: Todos (EDM/APO/BAI/DSS/MEA)</option>
            <option value="EDM">Gobernanza EDM (Evaluar, Dirigir, Supervisar)</option>
            <option value="APO">Gestión APO (Alinear, Planear, Organizar)</option>
            <option value="BAI">Gestión BAI (Construir, Adquirir, Implementar)</option>
            <option value="DSS">Gestión DSS (Entregar, Servicio y Soporte)</option>
            <option value="MEA">Gestión MEA (Monitorear, Evaluar, Valorar)</option>
          </select>
          <select id="selApp" onchange="applyFilters()">
            <option value="ALL">App: Todas (6 Plataformas)</option>
            <option value="ERP Apolo">ERP Modular Apolo</option>
            <option value="Apolo SaaS">Apolo Académico v2.1 SaaS</option>
            <option value="Apolo Mobile">Apolo II Mobile</option>
            <option value="VPS & Web">Portal Web & Hosting VPS</option>
            <option value="AulaCloud">AulaCloud & Wiki</option>
            <option value="CRM & Part.">CRM Open Source</option>
          </select>
        </div>
        <div class="search-row">
          <input type="text" id="jqlInput" value='project = "TECNIFICATE-PETI" AND framework = "COBIT-2019"' oninput="applyFilters()">
          <button onclick="applyFilters()">Search</button>
        </div>
        <div class="jql-meta">
          <span style="color:#10b981;" id="foundCount">● 342 governance controls & service issues found</span>
          <span style="color:#0284c7; cursor:pointer;" onclick="resetFilters()">Reset Filters (JQL)</span>
        </div>
      </div>
    </div>

    <div class="widget top-green">
      <div class="w-hdr"><span>▾ Custom Charts</span><span>⤢ ⚙</span></div>
      <div class="w-body">
        <div class="w-title">Created & Resolved - Past 12 Months (COBIT 2019)</div>
        <svg viewBox="0 0 520 300" style="width:100%; height:auto;">
          <!-- Grid lines -->
          <line x1="40" y1="30" x2="500" y2="30" stroke="#e2e8f0"/>
          <line x1="40" y1="90" x2="500" y2="90" stroke="#e2e8f0"/>
          <line x1="40" y1="150" x2="500" y2="150" stroke="#e2e8f0"/>
          <line x1="40" y1="210" x2="500" y2="210" stroke="#e2e8f0"/>
          <line x1="40" y1="250" x2="500" y2="250" stroke="#cbd5e1"/>
          <text x="12" y="34" font-size="11" fill="#64748b">60</text>
          <text x="12" y="94" font-size="11" fill="#64748b">45</text>
          <text x="12" y="154" font-size="11" fill="#64748b">30</text>
          <text x="12" y="214" font-size="11" fill="#64748b">15</text>
          <text x="18" y="254" font-size="11" fill="#64748b">0</text>
          <!-- Green Line: SLA Resolved -->
          <polyline fill="none" stroke="#10b981" stroke-width="3" points="45,184 86,169 127,155 168,144 209,125 250,111 291,96 332,85 373,74 414,63 455,52 496,37"/>
          <!-- Amber Line: Rework/Changes -->
          <polyline fill="none" stroke="#f59e0b" stroke-width="3" points="45,111 86,118 127,122 168,133 209,140 250,151 291,158 332,169 373,180 414,188 455,195 496,206"/>
          <!-- Indigo Line: Bugs per Release -->
          <polyline fill="none" stroke="#4f46e5" stroke-width="3" points="45,191 86,195 127,199 168,202 209,210 250,213 291,221 332,224 373,228 414,232 455,235 496,235"/>
          <text x="35" y="272" font-size="10" fill="#64748b">Dic 25</text>
          <text x="117" y="272" font-size="10" fill="#64748b">Feb 26</text>
          <text x="199" y="272" font-size="10" fill="#64748b">Abr 26</text>
          <text x="281" y="272" font-size="10" fill="#64748b">Jun 26</text>
          <text x="363" y="272" font-size="10" fill="#64748b">Ago 26</text>
          <text x="465" y="272" font-size="10" fill="#64748b">Nov 26</text>
        </svg>
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px; font-size:12px; margin-top:8px;">
          <div><b style="color:#10b981;">● Serie Verde (DSS02 / MEA01):</b> Controles y tickets resueltos en SLA ≥ 90% (sube de 18 a 58/mes).</div>
          <div><b style="color:#f59e0b;">● Serie Ámbar (DSS06 / F1):</b> Incidencias por reprocesos manuales (cae de 38 a 12/mes: 80% → 40%).</div>
          <div><b style="color:#4f46e5;">● Serie Morada (APO10 / BAI07):</b> Bugs en producción por versión (cae de 16 a 4 bugs: −71,4%).</div>
        </div>
      </div>
    </div>
  </div>

  <!-- COLUMNA 2: OPEN SUPPORT TICKETS BY APP NAME + APP HOSTING -->
  <div class="col-stack">
    <div class="widget top-amber">
      <div class="w-hdr"><span>▾ Custom Charts</span><span>⤢ ⚙</span></div>
      <div class="w-body">
        <div class="w-title">Open & Managed Governance Tickets - App Name</div>
        <div id="appBarsSvgWrap"></div>
      </div>
    </div>

    <div class="widget top-blue">
      <div class="w-hdr"><span>▾ Custom Charts</span><span>⤢ ⚙</span></div>
      <div class="w-body">
        <div class="w-title">App Hosting (COBIT APO03 / BAI04)</div>
        <div class="hosting-row">
          <div class="h-card">
            <div class="lbl">Cloud (VPS SaaS)</div>
            <div class="num" id="hCloudNum">220</div>
            <div class="pct">64,3% (Apolo SaaS)</div>
          </div>
          <div class="h-card amber">
            <div class="lbl">Server (Web/SSL)</div>
            <div class="num" id="hSrvNum">84</div>
            <div class="pct">24,6% (Hosting)</div>
          </div>
          <div class="h-card indigo">
            <div class="lbl">Data Center / Local</div>
            <div class="num" id="hDcNum">38</div>
            <div class="pct">11,1% (In-House)</div>
          </div>
        </div>
        <div style="text-align:center; font-size:12.5px; color:#475569; font-weight:700;">
          Chart By: App Hosting &nbsp;|&nbsp; Count: Issues/Controles &nbsp;|&nbsp; Total: <span style="color:#0284c7;" id="hTotNum">342</span>
        </div>
      </div>
    </div>
  </div>

  <!-- COLUMNA 3: STATUS CATEGORY DONUT + ALL SUPPORT ISSUES REQUEST TYPE -->
  <div class="col-stack">
    <div class="widget top-blue">
      <div class="w-hdr"><span>▾ Custom Charts</span><span>⤢ ⚙</span></div>
      <div class="w-body">
        <div class="w-title">Governance & Support Project - Status Category</div>
        <div style="display:grid; grid-template-columns: 160px 1fr; gap:14px; align-items:center;">
          <svg viewBox="0 0 160 160" style="width:150px; height:150px; margin:0 auto;">
            <circle cx="80" cy="80" r="56" fill="none" stroke="#10b981" stroke-width="24" stroke-dasharray="253 352" stroke-dashoffset="0"/>
            <circle cx="80" cy="80" r="56" fill="none" stroke="#f59e0b" stroke-width="24" stroke-dasharray="64 352" stroke-dashoffset="-253"/>
            <circle cx="80" cy="80" r="56" fill="none" stroke="#4f46e5" stroke-width="24" stroke-dasharray="35 352" stroke-dashoffset="-317"/>
            <text x="80" y="78" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a" id="donutTotTxt">342</text>
            <text x="80" y="95" text-anchor="middle" font-size="10" fill="#64748b">Controles</text>
          </svg>
          <table class="mini-table">
            <thead><tr><th>Status Category</th><th>Issues</th><th>%</th></tr></thead>
            <tbody id="statusTableBody"></tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="widget top-blue">
      <div class="w-hdr"><span>▾ Custom Charts</span><span>⤢ ⚙</span></div>
      <div class="w-body">
        <div class="w-title">All Governance Issues - Request Type (COBIT 2019)</div>
        <div style="display:grid; grid-template-columns: 135px 1fr; gap:12px; align-items:center;">
          <div style="display:flex; flex-direction:column; align-items:center; gap:8px;">
            <div style="width:120px; height:24px; background:#10b981; border-radius:5px;"></div>
            <div style="width:96px; height:24px; background:#0ea5e9; border-radius:5px;"></div>
            <div style="width:76px; height:24px; background:#4f46e5; border-radius:5px;"></div>
            <div style="width:58px; height:24px; background:#f59e0b; border-radius:5px;"></div>
            <div style="width:42px; height:24px; background:#ef4444; border-radius:5px;"></div>
          </div>
          <table class="mini-table">
            <thead><tr><th>Request Type (COBIT)</th><th>Issues</th><th>%</th></tr></thead>
            <tbody id="reqTableBody"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- TABLA INFERIOR DE CASCADA DE METAS Y MÉTRICAS COBIT 2019 -->
<div class="full-section">
  <div class="widget top-blue">
    <div class="w-hdr"><span>▾ Matriz Estratégica de Cascada de Metas y Métricas de Gobierno de TI (COBIT 2019 & BSC)</span><span>TECNIFICATE S.A.S.</span></div>
    <div class="w-body" style="overflow-x:auto;">
      <table class="matrix-table">
        <thead>
          <tr>
            <th>Objetivos COBIT</th>
            <th>Dominio COBIT 2019</th>
            <th>Meta Empresarial (EG)</th>
            <th>Meta de Alineamiento (AG)</th>
            <th>Métrica Estratégica (Lag) e Inductor (Lead)</th>
            <th>Línea Base (AS-IS)</th>
            <th>Resultado Actual (TO-BE)</th>
            <th>Capacidad ISO 33000</th>
            <th>Responsable</th>
          </tr>
        </thead>
        <tbody id="matrixBody"></tbody>
      </table>
    </div>
  </div>
</div>

<script>
const APPS = {json.dumps(app_tickets, ensure_ascii=False)};
const MATRIX = {json.dumps(cobit_metrics_matrix, ensure_ascii=False)};

function applyFilters() {{
  const dom = document.getElementById('selDomain').value;
  const app = document.getElementById('selApp').value;
  const q = (document.getElementById('jqlInput').value || '').toLowerCase();

  const filteredApps = APPS.filter(a => {{
    if (app !== 'ALL' && a[0] !== app) return false;
    if (dom !== 'ALL' && !a[7].includes(dom)) return false;
    return true;
  }});

  const tot = filteredApps.reduce((acc, r) => acc + r[2], 0) || 342;
  document.getElementById('foundCount').textContent = `● ${{tot}} governance controls & service issues found`;
  document.getElementById('donutTotTxt').textContent = tot;
  document.getElementById('hTotNum').textContent = tot;
  document.getElementById('hCloudNum').textContent = Math.round(tot * 0.643);
  document.getElementById('hSrvNum').textContent = Math.round(tot * 0.246);
  document.getElementById('hDcNum').textContent = tot - Math.round(tot * 0.643) - Math.round(tot * 0.246);

  // Renderizar barras apiladas por aplicación
  let barsHtml = '<svg viewBox="0 0 520 265" style="width:100%; height:auto;">';
  barsHtml += '<line x1="40" y1="220" x2="500" y2="220" stroke="#cbd5e1"/>';
  filteredApps.forEach((a, idx) => {{
    const x = 58 + idx * 74;
    const hDone = Math.round((a[3] / 150) * 180);
    const hProg = Math.round((a[4] / 150) * 180);
    const hTodo = Math.round((a[5] / 150) * 180);
    const hCrit = Math.round((a[6] / 150) * 180);
    let cy = 220;
    barsHtml += `<rect x="${{x}}" y="${{cy - hDone}}" width="42" height="${{hDone}}" fill="#f59e0b"/>`; cy -= hDone;
    barsHtml += `<rect x="${{x}}" y="${{cy - hProg}}" width="42" height="${{hProg}}" fill="#4f46e5"/>`; cy -= hProg;
    barsHtml += `<rect x="${{x}}" y="${{cy - hTodo}}" width="42" height="${{hTodo}}" fill="#10b981"/>`; cy -= hTodo;
    barsHtml += `<rect x="${{x}}" y="${{cy - hCrit}}" width="42" height="${{hCrit}}" fill="#0ea5e9"/>`; cy -= hCrit;
    barsHtml += `<text x="${{x + 21}}" y="${{cy - 6}}" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">${{a[2]}}</text>`;
    barsHtml += `<text x="${{x + 21}}" y="238" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">${{a[0]}}</text>`;
    barsHtml += `<text x="${{x + 21}}" y="252" text-anchor="middle" font-size="9.5" fill="#64748b">${{a[7].split('/')[0]}}</text>`;
  }});
  barsHtml += '</svg>';
  document.getElementById('appBarsSvgWrap').innerHTML = barsHtml;

  const todoCnt = Math.round(tot * 0.099);
  const progCnt = Math.round(tot * 0.181);
  const doneCnt = tot - todoCnt - progCnt;
  document.getElementById('statusTableBody').innerHTML = `
    <tr><td><span class="dot" style="background:#4f46e5;"></span>To Do (Fase 3-4)</td><td><b>${{todoCnt}}</b></td><td>9,9%</td></tr>
    <tr><td><span class="dot" style="background:#f59e0b;"></span>In Progress</td><td><b>${{progCnt}}</b></td><td>18,1%</td></tr>
    <tr><td><span class="dot" style="background:#10b981;"></span>Done (En SLA)</td><td><b>${{doneCnt}}</b></td><td>72,0%</td></tr>
    <tr><td><b>Total</b></td><td><b>${{tot}}</b></td><td><b>100%</b></td></tr>
  `;

  document.getElementById('reqTableBody').innerHTML = `
    <tr><td><span class="dot" style="background:#10b981;"></span>Soporte ITIL (DSS02)</td><td><b>${{Math.round(tot*0.415)}}</b></td><td>41,5%</td></tr>
    <tr><td><span class="dot" style="background:#0ea5e9;"></span>Calidad QA (APO10/BAI07)</td><td><b>${{Math.round(tot*0.228)}}</b></td><td>22,8%</td></tr>
    <tr><td><span class="dot" style="background:#4f46e5;"></span>BPM & ERP (DSS06/APO14)</td><td><b>${{Math.round(tot*0.158)}}</b></td><td>15,8%</td></tr>
    <tr><td><span class="dot" style="background:#f59e0b;"></span>CRM & Ventas (APO08)</td><td><b>${{Math.round(tot*0.120)}}</b></td><td>12,0%</td></tr>
    <tr><td><span class="dot" style="background:#ef4444;"></span>Gobierno & Wiki (EDM/MEA)</td><td><b>${{Math.round(tot*0.079)}}</b></td><td>7,9%</td></tr>
    <tr><td><b>Total</b></td><td><b>${{tot}}</b></td><td><b>100%</b></td></tr>
  `;

  const filtMatrix = MATRIX.filter(m => dom === 'ALL' || m[0].includes(dom) || m[1].includes(dom));
  document.getElementById('matrixBody').innerHTML = filtMatrix.map(m => `
    <tr>
      <td><b style="color:#0284c7;">${{m[0]}}</b></td>
      <td><b>${{m[1]}}</b></td>
      <td>${{m[2]}}</td>
      <td>${{m[3]}}</td>
      <td><b>${{m[4]}}</b></td>
      <td style="color:#dc2626; font-weight:700;">${{m[5]}}</td>
      <td style="color:#16a34a; font-weight:700;">${{m[6]}}</td>
      <td><span class="badge-lvl">${{m[7]}}</span></td>
      <td>${{m[8]}}</td>
    </tr>
  `).join('');
}}

function resetFilters() {{
  document.getElementById('selDomain').value = 'ALL';
  document.getElementById('selApp').value = 'ALL';
  document.getElementById('jqlInput').value = 'project = "TECNIFICATE-PETI" AND framework = "COBIT-2019"';
  applyFilters();
}}

function exportCsv() {{
  const headers = ['Codigo_COBIT','Dominio_COBIT_2019','Meta_Empresarial_EG','Meta_Alineamiento_AG','Metrica_Estrategica_y_Operativa','Linea_Base_AS_IS','Resultado_Actual_TO_BE','Evolucion_Capacidad_ISO33000','Responsable'];
  const lines = [headers.join(','), ...MATRIX.map(r => r.map(c => '"' + String(c).replace(/"/g, '""') + '"').join(','))];
  const blob = new Blob(['\\uFEFF' + lines.join('\\n')], {{ type: 'text/csv;charset=utf-8;' }});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'Tecnificate_Metricas_Estrategicas_COBIT2019.csv';
  a.click();
}}

applyFilters();
</script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "Dashboard_Estrategico_Metricas_COBIT2019_Tecnificate.html"), "w", encoding="utf-8") as f:
    f.write(html_dash)

print("Generated Activity 5 HTML Dashboard, Excel, CSV and 2 high-DPI charts successfully.")
