# -*- coding: utf-8 -*-
"""
Script para actualizar:
1. Tecnificate_Dataset_Dashboard_Metricas_COBIT2019.xlsx (5 hojas en español)
2. Metricas_Estrategicas_COBIT2019_12Meses.csv (con UTF-8 BOM)
3. fig1_dashboard_custom_charts_cobit2019.png (100% en español, alta resolución)
4. fig2_cascada_metas_metricas_cobit2019.png (100% en español)
"""
import os
import csv
import zipfile
from xml.sax.saxutils import escape
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\andre\.gemini\antigravity\scratch\Gobierno_TI_Tecnificate\Entregable_Actividad5_Dashboard_Estrategico_Metricas_COBIT2019"
IMG_DIR = os.path.join(BASE_DIR, "graficos_dashboard")
os.makedirs(IMG_DIR, exist_ok=True)

from build_full_act5 import tickets_dataset, monthly_data, cobit_matrix

# -----------------------------------------------------------------------------
# 1. EXPORTAR CSV CON UTF-8 BOM
# -----------------------------------------------------------------------------
csv_path = os.path.join(BASE_DIR, "Metricas_Estrategicas_COBIT2019_12Meses.csv")
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow([
        "Codigo_COBIT", "Dominio_COBIT_2019", "Meta_Empresarial_EG",
        "Meta_Alineamiento_AG", "Perspectiva_BSC", "Metrica_Estrategica_y_Operativa",
        "Linea_Base_AS_IS", "Resultado_Actual_TO_BE", "Evolucion_Capacidad_ISO33000",
        "Responsable_Accountable"
    ])
    for r in cobit_matrix:
        w.writerow([
            r["code"], r["domain"], r["eg"], r["ag"], r["bsc"],
            r["metric"], r["as_is"], r["to_be"], r["cap"], r["resp"]
        ])
print(f"CSV updated: {csv_path}")

# -----------------------------------------------------------------------------
# 2. GENERAR LIBRO EXCEL .XLSX MULTI-HOJA EN ESPAÑOL
# -----------------------------------------------------------------------------
def create_excel_file(filename):
    # Hoja 1: Cascada
    h1 = [["Codigo_COBIT", "Dominio_COBIT_2019", "Meta_Empresarial_EG", "Meta_Alineamiento_AG", "Perspectiva_BSC", "Metrica_Estrategica_KPI", "Linea_Base_AS_IS", "Meta_Alcanzada_TO_BE", "Capacidad_ISO33000", "Responsable"]]
    for r in cobit_matrix:
        h1.append([r["code"], r["domain"], r["eg"], r["ag"], r["bsc"], r["metric"], r["as_is"], r["to_be"], r["cap"], r["resp"]])

    # Hoja 2: Serie 12 Meses
    h2 = [["Mes", "Tickets_Resueltos_en_SLA_DSS02", "Tasa_Reprocesos_Manuales_DSS06", "Bugs_Produccion_BAI07", "Porcentaje_Cumplimiento_SLA", "Etapa_PETI_2026"]]
    for m in monthly_data:
        h2.append([m["month"], m["resolved"], m["rework"], m["bugs"], m["sla"], m["stage"]])

    # Hoja 3: Métricas por Aplicación
    h3 = [
        ["App_Code", "Nombre_Aplicacion_Tecnificate", "Total_Items_Gobernados", "Resueltos_SLA", "En_Curso", "Por_Hacer", "Criticos_P1", "Objetivos_COBIT_Asociados"],
        ["ERP Apolo", "ERP Modular Apolo (PyMEs / Local)", 138, 82, 32, 16, 8, "APO14 / DSS06 / BAI03"],
        ["Apolo SaaS", "Apolo Académico v2.1 (SaaS Web)", 84, 54, 18, 8, 4, "DSS02 / BAI04 / APO09"],
        ["Apolo Mobile", "Apolo II Mobile (App Android)", 44, 28, 10, 4, 2, "BAI03 / BAI07 / APO10"],
        ["VPS & Web", "Portal tecnificate.net, Hosting & SSL", 34, 24, 6, 3, 1, "DSS01 / DSS05 / APO13"],
        ["AulaCloud", "AulaCloud & Wiki Videotutoriales", 24, 17, 5, 2, 0, "BAI08 / APO07"],
        ["CRM & Part.", "CRM Open Source & Canal Partners", 18, 13, 3, 2, 0, "APO08 / APO10 / EDM02"]
    ]

    # Hoja 4: Distribución Infraestructura y Solicitudes
    h4 = [
        ["Categoria_General", "Subcategoria_o_Ambiente", "Cantidad_Items", "Porcentaje", "Detalle_Operativo"],
        ["Estado del Control", "Completado en SLA (Resuelto)", 246, 72.0, "Controles implementados y validados"],
        ["Estado del Control", "En Curso (En Ejecución)", 62, 18.1, "En desarrollo por equipo PETI"],
        ["Estado del Control", "Por Hacer (Pendiente)", 34, 9.9, "Backlog priorizado 2026-2027"],
        ["Alojamiento (Hosting)", "Nube (Cloud VPS SaaS)", 220, 64.3, "Apolo Académico SaaS y AulaCloud"],
        ["Alojamiento (Hosting)", "Servidor Dedicado / VPS", 84, 24.6, "Hosting cPanel, SSL y Portal Web"],
        ["Alojamiento (Hosting)", "Centro de Datos / Local", 38, 11.1, "ERP Apolo on-premise en ferreterías"],
        ["Tipo de Solicitud", "Soporte Técnico ITIL (DSS02/APO09)", 142, 41.5, "Mesa de Ayuda, atención colegios"],
        ["Tipo de Solicitud", "Control de Calidad QA (APO10/BAI07)", 78, 22.8, "Pruebas unitarias, homologación notas"],
        ["Tipo de Solicitud", "Automatización ERP & BPM (DSS06/APO14)", 54, 15.8, "DIAN, conciliación, optimización"],
        ["Tipo de Solicitud", "Gestión Comercial CRM (APO08/APO10)", 41, 12.0, "Embudo ventas, prevención de churn"],
        ["Tipo de Solicitud", "Gobierno, Seguridad & Wiki (EDM/MEA)", 27, 7.9, "Auditoría n8n, ISO 33000, comités"]
    ]

    # Hoja 5: 48 Controles con RCA
    h5 = [["Codigo", "Titulo", "Aplicacion", "Dominio_COBIT", "Prioridad", "Estado", "Responsable", "Alojamiento", "SLA_Pct", "Causa_Raiz_RCA", "Accion_Correctiva_Gobierno", "Capacidad_Antes", "Capacidad_Despues", "Evidencia"]]
    for t in tickets_dataset:
        h5.append([
            t["code"], t["title"], t["app"], t["domain"], t["priority"],
            t["status"], t["assignee"], t["hosting"], t["sla"],
            t["rca"], t["action"], t["cap_before"], t["cap_after"], t["evidence"]
        ])

    sheets = [
        ("1_Cascada_Metas_COBIT", h1),
        ("2_Serie_12Meses_Gobernanza", h2),
        ("3_Metricas_por_Aplicacion", h3),
        ("4_Infraestructura_Hosting", h4),
        ("5_Detalle_48_Controles_RCA", h5)
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
                    col_let = ""
                    cnum = ci
                    while cnum > 0:
                        cnum, rem = divmod(cnum - 1, 26)
                        col_let = chr(65 + rem) + col_let
                    ref = f"{col_let}{ri}"
                    if isinstance(val, (int, float)) and ri > 1:
                        cxml.append(f'<c r="{ref}" s="0"><v>{val}</v></c>')
                    else:
                        cxml.append(f'<c r="{ref}" t="inlineStr" s="{s}"><is><t>{escape(str(val))}</t></is></c>')
                rxml.append(f'<row r="{ri}">{"".join(cxml)}</row>')
            zf.writestr(f'xl/worksheets/sheet{idx+1}.xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>{"".join(rxml)}</sheetData></worksheet>')

xlsx_path = os.path.join(BASE_DIR, "Tecnificate_Dataset_Dashboard_Metricas_COBIT2019.xlsx")
create_excel_file(xlsx_path)
print(f"Excel workbook updated: {xlsx_path}")

# -----------------------------------------------------------------------------
# 3. RENDERIZAR FIGURAS 1 Y 2 EN ALTA RESOLUCIÓN (100% EN ESPAÑOL)
# -----------------------------------------------------------------------------
def get_font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def draw_fig1_spanish():
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

    # Top Navigation Bar en Español
    d.rectangle([0, 0, W, 64], fill=WHITE)
    d.line([(0, 64), (W, 64)], fill=BORDER, width=2)
    d.rounded_rectangle([24, 14, 60, 50], radius=8, fill=INDIGO)
    d.text((34, 18), "T", fill=WHITE, font=get_font(22, True))
    d.text((74, 20), "TECNIFICATE S.A.S. — Sistema de Gobernanza TI", fill=NAVY, font=get_font(19, True))

    nav_items = ["Mi Trabajo", "Proyectos v", "Filtros v", "Tableros v", "Gobierno COBIT v", "Métricas BSC v"]
    nx = 440
    for ni in nav_items:
        is_act = "Tableros" in ni
        d.text((nx, 22), ni, fill=BLUE if is_act else GRAY_D, font=get_font(16, is_act))
        if is_act:
            d.line([(nx, 62), (nx + 80, 62)], fill=BLUE, width=4)
        nx += 124

    d.rounded_rectangle([1200, 15, 1320, 49], radius=6, fill=BLUE)
    d.text((1218, 22), "+ Crear Ticket", fill=WHITE, font=get_font(15, True))
    d.rounded_rectangle([1335, 15, 1620, 49], radius=6, fill=BG, outline=BORDER)
    d.text((1350, 22), "Buscar métricas COBIT / PETI...", fill=GRAY_M, font=get_font(14, False))
    d.text((1640, 22), "👤 Diego Vélez | auditor.gobiernoti@usc.edu.co", fill=INDIGO, font=get_font(14, True))

    # ------------------------------------------------------------------
    # PANEL 1: Búsqueda Rápida de Gobernanza (Col 1 Top)
    # ------------------------------------------------------------------
    p1 = [24, 82, 624, 305]
    d.rounded_rectangle(p1, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p1[0], p1[1], p1[2], p1[1]], fill=RED, width=4)
    d.text((42, 96), "▾ Búsqueda Rápida de Gobernanza (Simple Search) — COBIT 2019", fill=GRAY_D, font=get_font(15, True))

    pills = [("Proyecto: TECNIFICATE (PETI)", INDIGO, 42), ("Dominio: Todos (EDM/APO/BAI/DSS/MEA)", BG, 260), ("Responsable: Todo el Equipo", BG, 460)]
    for p_txt, p_bg, px in pills:
        fg = WHITE if p_bg == INDIGO else GRAY_D
        w_p = int(d.textlength(p_txt, font=get_font(13, True))) + 20
        d.rounded_rectangle([px, 132, min(px + w_p, 610), 162], radius=5, fill=p_bg, outline=BORDER)
        d.text((px + 10, 138), p_txt, fill=fg, font=get_font(12, True))

    d.rounded_rectangle([42, 176, 485, 212], radius=5, fill=WHITE, outline=BORDER)
    d.text((54, 185), 'proyecto = "TECNIFICATE-PETI" Y sla >= 90%', fill=GRAY_M, font=get_font(14, False))
    d.rounded_rectangle([500, 176, 598, 212], radius=5, fill=BLUE)
    d.text((525, 185), "Buscar", fill=WHITE, font=get_font(14, True))

    d.text((42, 230), "● 342 controles de gobierno e incidencias operativas encontrados", fill=GREEN, font=get_font(13, True))
    d.text((42, 255), "Filtro activo: 6 aplicaciones de software | Líder: Diego Vélez Gallego", fill=GRAY_M, font=get_font(12, False))
    d.text((450, 275), "Ver Consulta JQL", fill=BLUE, font=get_font(12, True))

    # ------------------------------------------------------------------
    # PANEL 2: Línea de Tiempo 12 Meses (Col 1 Bottom)
    # ------------------------------------------------------------------
    p2 = [24, 325, 624, 765]
    d.rounded_rectangle(p2, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p2[0], p2[1], p2[2], p2[1]], fill=GREEN, width=4)
    d.text((42, 338), "▾ Evolución Temporal — Creados y Resueltos en SLA (12 Meses)", fill=GRAY_D, font=get_font(15, True))
    d.text((120, 372), "Controles Creados y Resueltos en SLA — COBIT 2019", fill=NAVY, font=get_font(16, True))

    # Ejes
    ax_x0, ax_y0, ax_x1, ax_y1 = 80, 420, 580, 630
    d.line([(ax_x0, ax_y1), (ax_x1, ax_y1)], fill=BORDER, width=2)
    for y_v, lbl in [(420, "60"), (472, "45"), (525, "30"), (578, "15"), (630, "0")]:
        d.line([(ax_x0, y_v), (ax_x1, y_v)], fill=BG, width=1)
        d.text((ax_x0 - 30, y_v - 7), lbl, fill=GRAY_M, font=get_font(12, False))

    # Curvas
    pts_green = [(95, 590), (135, 560), (175, 530), (215, 500), (255, 465), (295, 435), (335, 410), (375, 385), (415, 365), (455, 345), (495, 330), (535, 310)]
    pts_amber = [(95, 450), (135, 465), (175, 480), (215, 500), (255, 520), (295, 545), (335, 565), (375, 585), (415, 600), (455, 615), (495, 620), (535, 625)]
    pts_purple = [(95, 530), (135, 540), (175, 550), (215, 560), (255, 575), (295, 585), (335, 595), (375, 605), (415, 615), (455, 620), (495, 620), (535, 625)]

    d.line(pts_green, fill=GREEN, width=4)
    d.line(pts_amber, fill=AMBER, width=4)
    d.line(pts_purple, fill=INDIGO, width=3)

    for pt in pts_green: d.ellipse([pt[0]-4, pt[1]-4, pt[0]+4, pt[1]+4], fill=GREEN, outline=WHITE, width=2)
    for pt in pts_amber: d.ellipse([pt[0]-4, pt[1]-4, pt[0]+4, pt[1]+4], fill=AMBER, outline=WHITE, width=2)
    for pt in pts_purple: d.ellipse([pt[0]-3, pt[1]-3, pt[0]+3, pt[1]+3], fill=INDIGO, outline=WHITE, width=1)

    meses_lbl = ["Dic 25", "Feb 26", "Abr 26", "Jun 26", "Ago 26", "Oct 26", "Nov 26"]
    for i, ml in enumerate(meses_lbl):
        d.text((95 + i * 72, ax_y1 + 10), ml, fill=GRAY_M, font=get_font(11, False))

    d.rounded_rectangle([42, 665, 605, 748], radius=6, fill=BG, outline=BORDER)
    d.text((54, 674), "● Serie Verde (DSS02/MEA01): Resueltos en SLA sube de 18 a 58/mes (Cumplimiento 92,5%)", fill=GREEN, font=get_font(12, True))
    d.text((54, 698), "● Serie Ámbar (DSS06/APO14): Reprocesos manuales se reducen del 80% al 40%", fill=AMBER, font=get_font(12, True))
    d.text((54, 722), "● Serie Morada (BAI07/APO10): Bugs en producción caen de 14 a 4 (-71,4%)", fill=INDIGO, font=get_font(12, True))

    # ------------------------------------------------------------------
    # PANEL 3: Barras Apiladas por Aplicación (Col 2 Top)
    # ------------------------------------------------------------------
    p3 = [644, 82, 1264, 520]
    d.rounded_rectangle(p3, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p3[0], p3[1], p3[2], p3[1]], fill=AMBER, width=4)
    d.text((662, 96), "▾ Tickets y Controles Abiertos por Aplicación", fill=GRAY_D, font=get_font(15, True))
    d.text((710, 130), "Controles Gestionados por Aplicación (TECNIFICATE S.A.S.)", fill=NAVY, font=get_font(16, True))

    apps_draw = [
        ("ERP Apolo", 138, 82, 32, 16, 8),
        ("Apolo SaaS", 84, 54, 18, 8, 4),
        ("Apolo Mobile", 44, 28, 10, 4, 2),
        ("Hosting VPS", 34, 24, 6, 3, 1),
        ("AulaCloud", 24, 17, 5, 2, 0),
        ("CRM Open", 18, 13, 3, 2, 0)
    ]

    bx0, by_base = 690, 440
    d.line([(bx0, by_base), (1230, by_base)], fill=BORDER, width=2)

    for i, (an, tot, done, prog, todo, crit) in enumerate(apps_draw):
        x = bx0 + i * 88 + 15
        bw = 48
        cy = by_base

        h_done = int((done / 150) * 250)
        h_prog = int((prog / 150) * 250)
        h_todo = int((todo / 150) * 250)
        h_crit = int((crit / 150) * 250)

        # Draw stacked bars
        d.rectangle([x, cy - h_done, x + bw, cy], fill=GREEN)
        cy -= h_done
        d.rectangle([x, cy - h_prog, x + bw, cy], fill=AMBER)
        cy -= h_prog
        d.rectangle([x, cy - h_todo, x + bw, cy], fill=INDIGO)
        cy -= h_todo
        if h_crit > 0:
            d.rectangle([x, cy - h_crit, x + bw, cy], fill=RED)
            cy -= h_crit

        d.text((x + 12, cy - 20), str(tot), fill=NAVY, font=get_font(14, True))
        d.text((x - 2, by_base + 8), an, fill=GRAY_D, font=get_font(12, True))

    d.text((720, 485), "Leyenda:  ■ Completado en SLA   ■ En Curso   ■ Por Hacer   ■ Crítico P1", fill=GRAY_D, font=get_font(12, True))

    # ------------------------------------------------------------------
    # PANEL 4: App Hosting (Col 2 Bottom)
    # ------------------------------------------------------------------
    p4 = [644, 540, 1264, 765]
    d.rounded_rectangle(p4, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p4[0], p4[1], p4[2], p4[1]], fill=BLUE, width=4)
    d.text((662, 554), "▾ Infraestructura y Alojamiento de Aplicaciones", fill=GRAY_D, font=get_font(15, True))
    d.text((735, 580), "Alojamiento de Aplicaciones (COBIT APO03 / BAI04)", fill=NAVY, font=get_font(16, True))

    cards_h = [
        ("Nube (Cloud VPS SaaS)", "220", "64,3% (Apolo SaaS)", BLUE, 665),
        ("Servidor Web / SSL", "84", "24,6% (Hosting)", AMBER, 860),
        ("Centro de Datos Local", "38", "11,1% (PyMEs)", INDIGO, 1055)
    ]
    for c_lbl, c_val, c_sub, c_col, cx in cards_h:
        d.rounded_rectangle([cx, 615, cx + 180, 715], radius=10, fill=WHITE, outline=c_col, width=3)
        d.text((cx + 18, 626), c_lbl, fill=GRAY_D, font=get_font(12, True))
        d.text((cx + 52, 646), c_val, fill=c_col, font=get_font(32, True))
        d.text((cx + 25, 688), c_sub, fill=GRAY_M, font=get_font(11, False))

    d.text((720, 735), "Total Gobernado: 342 componentes  |  Líder Cloud: Santiago Balanta (DevOps)", fill=GRAY_D, font=get_font(12, True))

    # ------------------------------------------------------------------
    # PANEL 5: Gráfico de Dona de Estado (Col 3 Top)
    # ------------------------------------------------------------------
    p5 = [1284, 82, 1896, 420]
    d.rounded_rectangle(p5, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p5[0], p5[1], p5[2], p5[1]], fill=BLUE, width=4)
    d.text((1302, 96), "▾ Categoría de Estado de Gobernanza", fill=GRAY_D, font=get_font(15, True))
    d.text((1360, 125), "Estado del Proyecto de Gobernanza (COBIT 2019)", fill=NAVY, font=get_font(16, True))

    # Draw Donut Chart
    cx_d, cy_d, r_ext, r_int = 1430, 260, 95, 55
    d.pieslice([cx_d - r_ext, cy_d - r_ext, cx_d + r_ext, cy_d + r_ext], 0, 259, fill=GREEN)
    d.pieslice([cx_d - r_ext, cy_d - r_ext, cx_d + r_ext, cy_d + r_ext], 259, 324, fill=AMBER)
    d.pieslice([cx_d - r_ext, cy_d - r_ext, cx_d + r_ext, cy_d + r_ext], 324, 360, fill=INDIGO)
    d.ellipse([cx_d - r_int, cy_d - r_int, cx_d + r_int, cy_d + r_int], fill=WHITE)
    d.text((cx_d - 24, cy_d - 18), "342", fill=NAVY, font=get_font(26, True))
    d.text((cx_d - 28, cy_d + 12), "Controles", fill=GRAY_M, font=get_font(11, True))

    # Tabla de estados a la derecha de la dona
    tx, ty = 1570, 195
    d.text((tx, ty), "Estado", fill=GRAY_M, font=get_font(12, True))
    d.text((tx + 180, ty), "Items", fill=GRAY_M, font=get_font(12, True))
    d.text((tx + 240, ty), "%", fill=GRAY_M, font=get_font(12, True))
    d.line([(tx, ty + 18), (tx + 270, ty + 18)], fill=BORDER, width=1)

    rows_donut = [
        ("● Completado en SLA", "246", "72,0%", GREEN),
        ("● En Curso", "62", "18,1%", AMBER),
        ("● Por Hacer", "34", "9,9%", INDIGO),
        ("Total Gobernado", "342", "100%", NAVY)
    ]
    for idx, (st_lbl, st_num, st_pct, st_col) in enumerate(rows_donut):
        y_r = ty + 28 + idx * 28
        d.text((tx, y_r), st_lbl, fill=st_col, font=get_font(13, True))
        d.text((tx + 185, y_r), st_num, fill=NAVY, font=get_font(13, True))
        d.text((tx + 240, y_r), st_pct, fill=GRAY_D, font=get_font(13, False))

    # ------------------------------------------------------------------
    # PANEL 6: Tipo de Solicitud (Col 3 Bottom)
    # ------------------------------------------------------------------
    p6 = [1284, 440, 1896, 765]
    d.rounded_rectangle(p6, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p6[0], p6[1], p6[2], p6[1]], fill=INDIGO, width=4)
    d.text((1302, 454), "▾ Clasificación por Tipo de Solicitud (COBIT 2019)", fill=GRAY_D, font=get_font(15, True))
    d.text((1360, 482), "Solicitudes por Dominio Operativo (Request Type)", fill=NAVY, font=get_font(16, True))

    reqs_draw = [
        ("Soporte Técnico ITIL (DSS02/APO09)", 142, "41,5%", GREEN),
        ("Control de Calidad QA & Releases (BAI07)", 78, "22,8%", (6, 182, 212)),
        ("Automatización BPM & ERP Apolo (DSS06)", 54, "15,8%", INDIGO),
        ("Gestión Comercial CRM (APO08)", 41, "12,0%", AMBER),
        ("Gobierno, Seguridad & Wiki (EDM/MEA)", 27, "7,9%", RED)
    ]

    for idx, (r_name, r_cnt, r_pct, r_col) in enumerate(reqs_draw):
        y_pos = 530 + idx * 42
        d.text((1315, y_pos), r_name, fill=GRAY_D, font=get_font(13, True))
        d.text((1780, y_pos), f"{r_cnt} ({r_pct})", fill=NAVY, font=get_font(13, True))

        bw_pct = int((r_cnt / 142) * 450)
        d.rounded_rectangle([1315, y_pos + 18, 1315 + bw_pct, y_pos + 28], radius=4, fill=r_col)

    # ------------------------------------------------------------------
    # PANEL INFERIOR: BANNER RESUMEN PETI & ISO 33000
    # ------------------------------------------------------------------
    p_bot = [24, 785, 1896, 1095]
    d.rounded_rectangle(p_bot, radius=8, fill=WHITE, outline=BORDER, width=2)
    d.line([p_bot[0], p_bot[1], p_bot[2], p_bot[1]], fill=NAVY, width=4)
    d.text((42, 802), "▾ Matriz Resumen de Cascada de Metas y Madurez de Gobernanza — TECNIFICATE S.A.S. (Girardot, Cundinamarca)", fill=NAVY, font=get_font(16, True))

    bot_cols = [
        ("OBJETIVO DEL PETI 2026", "Alinear la estrategia de TI al crecimiento regional del 35% y resolver el cuello de botella del 80% en reprocesos manuales.", BLUE),
        ("MATEMÁTICA CONVERGENTE", "Línea Base: BSC 38,25% | EIS 38,71% (Nivel 1) | MinTIC 46,25% | COBIT 1,08/5,00. Meta TO-BE: Capacidad 3,24/5,00 (Nivel 4).", GREEN),
        ("RETORNO FINANCIERO", "Inversión PETI: US$3.300 | Beneficios Esperados: US$4.267,69 | Relación Beneficio/Costo: 1,29x | Payback: 9,2 meses.", AMBER),
        ("AUDITORÍA CONTINUA", "Flujo semanal n8n con 4 endpoints GET automatizados, bitácora en Google Sheets y alertas de desviación a gerencia.", INDIGO)
    ]
    for i, (b_title, b_desc, b_col) in enumerate(bot_cols):
        bx = 42 + i * 465
        d.rounded_rectangle([bx, 840, bx + 445, 1070], radius=8, fill=BG, outline=BORDER)
        d.rectangle([bx, 840, bx + 445, 875], fill=b_col)
        d.text((bx + 14, 850), b_title, fill=WHITE, font=get_font(13, True))

        # Texto multilínea
        words = b_desc.split(" ")
        lines, cur = [], ""
        for w in words:
            if len(cur + " " + w) < 42:
                cur = cur + " " + w if cur else w
            else:
                lines.append(cur)
                cur = w
        if cur: lines.append(cur)

        for li, line in enumerate(lines):
            d.text((bx + 16, 895 + li * 24), line, fill=GRAY_D, font=get_font(13, False))

    out_p = os.path.join(IMG_DIR, "fig1_dashboard_custom_charts_cobit2019.png")
    img.save(out_p, dpi=(300, 300))
    print(f"Figura 1 en español guardada en: {out_p}")

def draw_fig2_spanish():
    W, H = 1800, 950
    BG = (241, 245, 249)
    WHITE = (255, 255, 255)
    NAVY = (15, 23, 42)
    BLUE = (2, 132, 199)
    GREEN = (16, 185, 129)
    AMBER = (245, 158, 11)
    BORDER = (203, 213, 225)
    GRAY_D = (51, 65, 85)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 70], fill=NAVY)
    d.text((36, 22), "TECNIFICATE S.A.S. — Matriz Estratégica de Cascada de Metas y Métricas de Gobierno de TI (COBIT 2019 & BSC)", fill=WHITE, font=get_font(18, True))

    headers = ["Proceso COBIT", "Dominio", "Meta Empresarial (EG)", "Meta Alineamiento (AG)", "Perspectiva BSC", "Métrica Estratégica", "Línea Base (AS-IS)", "Meta (TO-BE)", "Capacidad ISO 33000"]
    widths = [140, 180, 250, 240, 160, 330, 160, 160, 140]

    y = 85
    x = 30
    d.rectangle([x, y, x + sum(widths), y + 40], fill=BLUE)
    cx = x
    for i, h in enumerate(headers):
        d.text((cx + 8, y + 10), h, fill=WHITE, font=get_font(12, True))
        cx += widths[i]

    y += 40
    for idx, r in enumerate(cobit_matrix):
        row_bg = WHITE if idx % 2 == 0 else (248, 250, 252)
        d.rectangle([x, y, x + sum(widths), y + 95], fill=row_bg, outline=BORDER)

        row_vals = [
            r["code"], r["domain"].split("(")[0], r["eg"][:45] + "...", r["ag"][:45] + "...",
            r["bsc"], r["metric"][:55] + "...", r["as_is"], r["to_be"], r["cap"]
        ]

        cx = x
        for i, val in enumerate(row_vals):
            is_asis = (i == 6)
            is_tobe = (i == 7)
            col_txt = (239, 68, 68) if is_asis else (GREEN if is_tobe else GRAY_D)
            d.text((cx + 8, y + 36), str(val), fill=col_txt, font=get_font(11, is_tobe or is_asis or i == 0))
            cx += widths[i]
        y += 95

    out_p = os.path.join(IMG_DIR, "fig2_cascada_metas_metricas_cobit2019.png")
    img.save(out_p, dpi=(300, 300))
    print(f"Figura 2 en español guardada en: {out_p}")

draw_fig1_spanish()
draw_fig2_spanish()
