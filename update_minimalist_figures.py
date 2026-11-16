# -*- coding: utf-8 -*-
"""
Generador de figuras de alta resolución (300 DPI) completamente minimalistas,
sin emojis, con diseño senior de ingeniería de sistemas y paleta neutral/enterprise.
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

def get_font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def draw_minimalist_fig1():
    W, H = 1920, 1120
    BG = (248, 250, 252) # #f8fafc
    WHITE = (255, 255, 255)
    DARK = (15, 23, 42) # #0f172a
    BRAND = (2, 132, 199) # #0284c7
    GREEN = (5, 150, 105) # #059669
    AMBER = (217, 119, 6) # #d97706
    PURPLE = (79, 70, 229) # #4f46e5
    RED = (220, 38, 38) # #dc2626
    BORDER = (226, 232, 240) # #e2e8f0
    BORDER_STR = (203, 213, 225)
    MUTED = (100, 116, 139) # #64748b
    SECONDARY = (51, 65, 85) # #334155

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # 1. TOP NAVIGATION BAR (Minimalist Enterprise)
    d.rectangle([0, 0, W, 56], fill=WHITE)
    d.line([(0, 56), (W, 56)], fill=BORDER, width=1)

    # Brand mark
    d.rounded_rectangle([24, 12, 54, 42], radius=4, fill=DARK)
    d.text((33, 17), "T", fill=WHITE, font=get_font(18, True))
    d.text((66, 15), "TECNIFICATE S.A.S.", fill=DARK, font=get_font(15, True))
    d.text((66, 32), "Sistema de Gobierno de TI — COBIT 2019", fill=MUTED, font=get_font(11, False))

    # Navigation items
    navs = ["Tablero de Control", "Registro de Controles (48)", "Cascada de Metas", "Simulador ISO 33000"]
    nx = 380
    for ni in navs:
        is_act = "Tablero" in ni
        col_txt = BRAND if is_act else MUTED
        d.text((nx, 20), ni, fill=col_txt, font=get_font(13.5, is_act))
        if is_act:
            d.line([(nx, 54), (nx + 130, 54)], fill=BRAND, width=3)
        nx += 165

    # Top right actions
    d.rounded_rectangle([1320, 13, 1450, 43], radius=4, fill=BRAND)
    d.text((1334, 19), "+ Registrar Control", fill=WHITE, font=get_font(12, True))

    d.rounded_rectangle([1460, 13, 1565, 43], radius=4, fill=WHITE, outline=BORDER_STR)
    d.text((1474, 19), "Exportar CSV", fill=SECONDARY, font=get_font(12, True))

    d.rounded_rectangle([1575, 13, 1896, 43], radius=4, fill=(241, 245, 249), outline=BORDER)
    d.text((1590, 20), "Auditor: auditor.gobiernoti@usc.edu.co", fill=SECONDARY, font=get_font(11.5, True))

    # 2. PANEL 1: Simple Search (Col 1 Top)
    p1 = [24, 72, 624, 290]
    d.rounded_rectangle(p1, radius=6, fill=WHITE, outline=BORDER, width=1)
    d.text((38, 84), "Filtros de Búsqueda de Gobernanza", fill=SECONDARY, font=get_font(13, True))
    d.text((540, 85), "Restablecer", fill=BRAND, font=get_font(11, True))
    d.line([(24, 106), (624, 106)], fill=BORDER, width=1)

    chips = [("Proyecto: TECNIFICATE (PETI)", BRAND, 38), ("Dominio: Todos", (241, 245, 249), 235), ("Responsable: Todos", (241, 245, 249), 410)]
    for c_txt, c_bg, cx in chips:
        c_fg = WHITE if c_bg == BRAND else SECONDARY
        tw = int(d.textlength(c_txt, font=get_font(11, True))) + 16
        d.rounded_rectangle([cx, 118, cx + tw, 144], radius=4, fill=c_bg, outline=BORDER_STR)
        d.text((cx + 8, 124), c_txt, fill=c_fg, font=get_font(11, True))

    d.rounded_rectangle([38, 156, 610, 188], radius=4, fill=WHITE, outline=BORDER_STR)
    d.text((50, 163), 'Buscar por código, DIAN, colegios, SLA, Girardot...', fill=MUTED, font=get_font(12, False))

    presets = [("Críticos P1", 38), ("Mesa ITIL (DSS02)", 135), ("Calidad QA (BAI07)", 270), ("Reprocesos ERP (DSS06)", 420)]
    for pr_txt, pr_x in presets:
        pr_w = int(d.textlength(pr_txt, font=get_font(10.5, True))) + 14
        d.rounded_rectangle([pr_x, 198, pr_x + pr_w, 222], radius=4, fill=(241, 245, 249), outline=BORDER)
        d.text((pr_x + 7, 204), pr_txt, fill=SECONDARY, font=get_font(10.5, True))

    d.text((38, 238), "● 48 controles identificados según criterios", fill=GREEN, font=get_font(11.5, True))
    d.text((545, 238), "Ver JQL", fill=BRAND, font=get_font(11, True))

    d.rounded_rectangle([38, 258, 610, 280], radius=4, fill=(241, 245, 249), outline=BORDER)
    d.text((46, 263), 'project = "TECNIFICATE-PETI" AND framework = "COBIT-2019"', fill=MUTED, font=get_font(10.5, False))

    # 3. PANEL 2: Línea de Tiempo 12 Meses (Col 1 Bottom)
    p2 = [24, 305, 624, 765]
    d.rounded_rectangle(p2, radius=6, fill=WHITE, outline=BORDER, width=1)
    d.text((38, 318), "Evolución Temporal de Gobernanza (12 Meses)", fill=SECONDARY, font=get_font(13, True))
    d.text((520, 319), "12M  |  H1  |  H2", fill=MUTED, font=get_font(11, True))
    d.line([(24, 340), (624, 340)], fill=BORDER, width=1)

    d.text((115, 355), "Controles Creados vs Resueltos en SLA (COBIT 2019)", fill=DARK, font=get_font(14, True))

    # Ejes
    ax0, ay0, ax1, ay1 = 70, 400, 590, 620
    d.line([(ax0, ay1), (ax1, ay1)], fill=BORDER_STR, width=1)
    for y_val, y_lbl in [(400, "100"), (455, "75"), (510, "50"), (565, "25"), (620, "0")]:
        d.line([(ax0, y_val), (ax1, y_val)], fill=(241, 245, 249), width=1)
        d.text((ax0 - 28, y_val - 6), y_lbl, fill=MUTED, font=get_font(10, False))

    pts_grn = [(85, 580), (130, 555), (175, 530), (220, 500), (265, 465), (310, 435), (355, 410), (400, 385), (445, 365), (490, 345), (535, 330), (575, 310)]
    pts_amb = [(85, 440), (130, 460), (175, 480), (220, 500), (265, 520), (310, 545), (355, 565), (400, 585), (445, 600), (490, 610), (535, 615), (575, 620)]
    pts_pur = [(85, 530), (130, 540), (175, 550), (220, 560), (265, 575), (310, 585), (355, 595), (400, 605), (445, 615), (490, 618), (535, 620), (575, 620)]

    d.line(pts_grn, fill=GREEN, width=3)
    d.line(pts_amb, fill=AMBER, width=3)
    d.line(pts_pur, fill=PURPLE, width=2)

    for pt in pts_grn: d.ellipse([pt[0]-3, pt[1]-3, pt[0]+3, pt[1]+3], fill=GREEN, outline=WHITE, width=1)

    meses = ["Dic", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov"]
    for i, m_name in enumerate(meses):
        d.text((80 + i * 44, ay1 + 8), m_name, fill=MUTED, font=get_font(10, False))

    d.rounded_rectangle([38, 660, 610, 745], radius=4, fill=(248, 250, 252), outline=BORDER)
    d.text((50, 672), "● Resueltos en SLA (DSS02): Crecimiento de 18 a 58 por mes (92,5% SLA)", fill=GREEN, font=get_font(11.5, True))
    d.text((50, 696), "● Reprocesos manuales (DSS06): Reducción sostenida del 80% al 40%", fill=AMBER, font=get_font(11.5, True))
    d.text((50, 720), "● Bugs en producción (BAI07): Caída de 14 a 4 errores por release (-71,4%)", fill=PURPLE, font=get_font(11.5, True))

    # 4. PANEL 3: Barras por Aplicación (Col 2 Top)
    p3 = [644, 72, 1264, 490]
    d.rounded_rectangle(p3, radius=6, fill=WHITE, outline=BORDER, width=1)
    d.text((658, 84), "Controles y Tickets por Aplicación", fill=SECONDARY, font=get_font(13, True))
    d.text((1200, 85), "Ver Todas", fill=BRAND, font=get_font(11, True))
    d.line([(644, 106), (1264, 106)], fill=BORDER, width=1)

    d.text((720, 125), "Distribución de Gobernanza por Plataforma de Software", fill=DARK, font=get_font(14, True))

    apps_data = [
        ("ERP Apolo", 138, 82, 32, 16),
        ("Apolo SaaS", 84, 54, 18, 8),
        ("Apolo Mobile", 44, 28, 10, 4),
        ("Hosting VPS", 34, 24, 6, 3),
        ("AulaCloud", 24, 17, 5, 2),
        ("CRM Open", 18, 13, 3, 2)
    ]

    bx0, by_base = 690, 420
    d.line([(bx0, by_base), (1230, by_base)], fill=BORDER_STR, width=1)

    for i, (an, tot, done, prog, todo) in enumerate(apps_data):
        x = bx0 + i * 88 + 15
        bw = 44
        cy = by_base

        h_done = int((done / 150) * 240)
        h_prog = int((prog / 150) * 240)
        h_todo = int((todo / 150) * 240)

        d.rectangle([x, cy - h_done, x + bw, cy], fill=GREEN)
        cy -= h_done
        d.rectangle([x, cy - h_prog, x + bw, cy], fill=AMBER)
        cy -= h_prog
        d.rectangle([x, cy - h_todo, x + bw, cy], fill=PURPLE)
        cy -= h_todo

        d.text((x + 10, cy - 18), str(tot), fill=DARK, font=get_font(13, True))
        d.text((x - 2, by_base + 8), an, fill=SECONDARY, font=get_font(11, True))

    d.text((750, 460), "Leyenda:  ■ Completado en SLA   ■ En Curso   ■ Por Hacer", fill=MUTED, font=get_font(11.5, True))

    # 5. PANEL 4: App Hosting (Col 2 Bottom)
    p4 = [644, 510, 1264, 765]
    d.rounded_rectangle(p4, radius=6, fill=WHITE, outline=BORDER, width=1)
    d.text((658, 524), "Infraestructura y Alojamiento", fill=SECONDARY, font=get_font(13, True))
    d.text((1150, 525), "COBIT APO03 / BAI04", fill=MUTED, font=get_font(11, False))
    d.line([(644, 545), (1264, 545)], fill=BORDER, width=1)

    d.text((770, 565), "Entornos de Despliegue (App Hosting)", fill=DARK, font=get_font(14, True))

    hosts = [
        ("Nube (Cloud VPS SaaS)", "220", "64,3% (Apolo SaaS)", BRAND, 665),
        ("Servidor Web / SSL", "84", "24,6% (Hosting)", AMBER, 860),
        ("Centro de Datos Local", "38", "11,1% (PyMEs)", PURPLE, 1055)
    ]
    for h_lbl, h_val, h_sub, h_col, hx in hosts:
        d.rounded_rectangle([hx, 600, hx + 180, 705], radius=4, fill=WHITE, outline=BORDER_STR, width=1)
        d.text((hx + 18, 612), h_lbl, fill=MUTED, font=get_font(11, True))
        d.text((hx + 56, 632), h_val, fill=DARK, font=get_font(30, True))
        d.text((hx + 28, 678), h_sub, fill=MUTED, font=get_font(10.5, False))

    d.text((740, 730), "Total Gobernado: 342 componentes auditados  |  Líder Cloud: Santiago Balanta", fill=MUTED, font=get_font(11.5, True))

    # 6. PANEL 5: Gráfico de Dona (Col 3 Top)
    p5 = [1284, 72, 1896, 420]
    d.rounded_rectangle(p5, radius=6, fill=WHITE, outline=BORDER, width=1)
    d.text((1298, 84), "Estado del Proyecto de Gobernanza", fill=SECONDARY, font=get_font(13, True))
    d.text((1800, 85), "COBIT MEA01", fill=MUTED, font=get_font(11, False))
    d.line([(1284, 106), (1896, 106)], fill=BORDER, width=1)

    d.text((1380, 125), "Categoría de Estado (Status Category)", fill=DARK, font=get_font(14, True))

    cxd, cyd, r_out, r_in = 1430, 260, 90, 55
    d.pieslice([cxd - r_out, cyd - r_out, cxd + r_out, cyd + r_out], 0, 259, fill=GREEN)
    d.pieslice([cxd - r_out, cyd - r_out, cxd + r_out, cyd + r_out], 259, 324, fill=AMBER)
    d.pieslice([cxd - r_out, cyd - r_out, cxd + r_out, cyd + r_out], 324, 360, fill=PURPLE)
    d.ellipse([cxd - r_in, cyd - r_in, cxd + r_in, cyd + r_in], fill=WHITE)
    d.text((cxd - 24, cyd - 16), "342", fill=DARK, font=get_font(24, True))
    d.text((cxd - 28, cyd + 12), "Controles", fill=MUTED, font=get_font(10.5, True))

    tx, ty = 1570, 195
    d.text((tx, ty), "Estado", fill=MUTED, font=get_font(11.5, True))
    d.text((tx + 175, ty), "Items", fill=MUTED, font=get_font(11.5, True))
    d.text((tx + 235, ty), "%", fill=MUTED, font=get_font(11.5, True))
    d.line([(tx, ty + 16), (tx + 270, ty + 16)], fill=BORDER, width=1)

    donut_rows = [
        ("● Completado en SLA", "246", "72,0%", GREEN),
        ("● En Curso", "62", "18,1%", AMBER),
        ("● Por Hacer", "34", "9,9%", PURPLE),
        ("Total Gobernado", "342", "100%", DARK)
    ]
    for idx, (st_lbl, st_num, st_pct, st_col) in enumerate(donut_rows):
        yr = ty + 28 + idx * 28
        d.text((tx, yr), st_lbl, fill=st_col, font=get_font(12, True))
        d.text((tx + 180, yr), st_num, fill=DARK, font=get_font(12, True))
        d.text((tx + 235, yr), st_pct, fill=MUTED, font=get_font(12, False))

    # 7. PANEL 6: Tipo de Solicitud (Col 3 Bottom)
    p6 = [1284, 440, 1896, 765]
    d.rounded_rectangle(p6, radius=6, fill=WHITE, outline=BORDER, width=1)
    d.text((1298, 454), "Clasificación por Proceso Operativo", fill=SECONDARY, font=get_font(13, True))
    d.text((1800, 455), "COBIT 2019", fill=MUTED, font=get_font(11, False))
    d.line([(1284, 475), (1896, 475)], fill=BORDER, width=1)

    d.text((1380, 495), "Solicitudes por Tipo (Request Type)", fill=DARK, font=get_font(14, True))

    reqs = [
        ("Soporte Técnico ITIL (DSS02/APO09)", 142, "41,5%", GREEN),
        ("Control Calidad QA (BAI07/APO10)", 78, "22,8%", BRAND),
        ("Automatización BPM & ERP (DSS06)", 54, "15,8%", PURPLE),
        ("Gestión Comercial CRM (APO08)", 41, "12,0%", AMBER),
        ("Gobierno y Seguridad (EDM/MEA)", 27, "7,9%", RED)
    ]
    for idx, (r_name, r_cnt, r_pct, r_col) in enumerate(reqs):
        yp = 540 + idx * 40
        d.text((1315, yp), r_name, fill=SECONDARY, font=get_font(12, True))
        d.text((1780, yp), f"{r_cnt} ({r_pct})", fill=DARK, font=get_font(12, True))

        bar_len = int((r_cnt / 142) * 450)
        d.rounded_rectangle([1315, yp + 16, 1315 + bar_len, yp + 24], radius=2, fill=r_col)

    # 8. PANEL INFERIOR: RESUMEN ESTRATÉGICO
    p_bot = [24, 785, 1896, 1095]
    d.rounded_rectangle(p_bot, radius=6, fill=WHITE, outline=BORDER, width=1)
    d.text((38, 800), "Alineación Estratégica PETI & Capacidad ISO/IEC 33000 — TECNIFICATE S.A.S.", fill=DARK, font=get_font(14, True))
    d.line([(24, 822), (1896, 822)], fill=BORDER, width=1)

    blocks = [
        ("OBJETIVO DEL PETI 2026", "Alinear la estrategia de TI al crecimiento regional y resolver el cuello de botella del 80% en reprocesos manuales.", BRAND),
        ("MATEMÁTICA CONVERGENTE", "Línea Base: BSC 38,25% | EIS 38,71% (Nivel 1) | MinTIC 46,25% | COBIT 1,08/5. Meta TO-BE: Capacidad 3,24/5 (Nivel 4).", GREEN),
        ("RETORNO FINANCIERO", "Inversión PETI: US$3.300 | Beneficios Esperados: US$4.267,69 | Relación Beneficio/Costo: 1,29x | Payback: 9,2 meses.", AMBER),
        ("AUDITORÍA CONTINUA", "Flujo semanal n8n con 4 endpoints GET automatizados, bitácora en Google Sheets y alertas de desviación.", PURPLE)
    ]
    for i, (b_tit, b_txt, b_col) in enumerate(blocks):
        bx = 38 + i * 465
        d.rounded_rectangle([bx, 840, bx + 445, 1070], radius=4, fill=(248, 250, 252), outline=BORDER)
        d.rounded_rectangle([bx, 840, bx + 445, 870], radius=4, fill=b_col)
        d.text((bx + 12, 848), b_tit, fill=WHITE, font=get_font(12, True))

        words = b_txt.split(" ")
        lines, cur = [], ""
        for w in words:
            if len(cur + " " + w) < 42:
                cur = cur + " " + w if cur else w
            else:
                lines.append(cur)
                cur = w
        if cur: lines.append(cur)

        for li, line in enumerate(lines):
            d.text((bx + 14, 890 + li * 24), line, fill=SECONDARY, font=get_font(12, False))

    out_p = os.path.join(IMG_DIR, "fig1_dashboard_custom_charts_cobit2019.png")
    img.save(out_p, dpi=(300, 300))
    print(f"Minimalist Fig 1 saved: {out_p}")

def draw_minimalist_fig2():
    W, H = 1800, 950
    BG = (248, 250, 252)
    WHITE = (255, 255, 255)
    DARK = (15, 23, 42)
    BRAND = (2, 132, 199)
    GREEN = (5, 150, 105)
    RED = (220, 38, 38)
    BORDER = (226, 232, 240)
    SECONDARY = (51, 65, 85)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, W, 56], fill=DARK)
    d.text((36, 18), "TECNIFICATE S.A.S. — Matriz de Cascada de Metas y Métricas de Gobierno de TI (COBIT 2019 & BSC)", fill=WHITE, font=get_font(16, True))

    headers = ["Proceso COBIT", "Dominio", "Meta Empresarial (EG)", "Meta Alineamiento (AG)", "Perspectiva BSC", "Métrica Estratégica", "Línea Base (AS-IS)", "Meta (TO-BE)", "Capacidad ISO 33000"]
    widths = [140, 180, 250, 240, 160, 330, 160, 160, 140]

    y = 75
    x = 30
    d.rectangle([x, y, x + sum(widths), y + 36], fill=BRAND)
    cx = x
    for i, h in enumerate(headers):
        d.text((cx + 8, y + 10), h, fill=WHITE, font=get_font(11.5, True))
        cx += widths[i]

    y += 36
    for idx, r in enumerate(cobit_matrix):
        row_bg = WHITE if idx % 2 == 0 else (241, 245, 249)
        d.rectangle([x, y, x + sum(widths), y + 90], fill=row_bg, outline=BORDER)

        row_vals = [
            r["code"], r["domain"].split("(")[0], r["eg"][:45] + "...", r["ag"][:45] + "...",
            r["bsc"], r["metric"][:55] + "...", r["as_is"], r["to_be"], r["cap"]
        ]

        cx = x
        for i, val in enumerate(row_vals):
            is_asis = (i == 6)
            is_tobe = (i == 7)
            col_txt = RED if is_asis else (GREEN if is_tobe else SECONDARY)
            d.text((cx + 8, y + 34), str(val), fill=col_txt, font=get_font(11, is_tobe or is_asis or i == 0))
            cx += widths[i]
        y += 90

    out_p = os.path.join(IMG_DIR, "fig2_cascada_metas_metricas_cobit2019.png")
    img.save(out_p, dpi=(300, 300))
    print(f"Minimalist Fig 2 saved: {out_p}")

draw_minimalist_fig1()
draw_minimalist_fig2()
