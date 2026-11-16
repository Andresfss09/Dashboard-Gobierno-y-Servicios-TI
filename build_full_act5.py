# -*- coding: utf-8 -*-
"""
Script maestro para la construcción integral de la Actividad 5:
- Dashboard Interactivo en HTML (100% en español, ultra profesional, totalmente funcional)
- Libro de cálculo Excel con 4 hojas analíticas
- Archivo CSV con encoding UTF-8 BOM
- Figuras 1 y 2 en resolución 300 DPI 100% en español
"""
import os
import sys
import csv
import json
import math
import zipfile
from xml.sax.saxutils import escape
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\andre\.gemini\antigravity\scratch\Gobierno_TI_Tecnificate\Entregable_Actividad5_Dashboard_Estrategico_Metricas_COBIT2019"
IMG_DIR = os.path.join(BASE_DIR, "graficos_dashboard")
os.makedirs(IMG_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. MATRIZ DE CASCADA DE METAS COBIT 2019 (8 PROCESOS CLAVE PETI)
# -----------------------------------------------------------------------------
cobit_matrix = [
    {
        "code": "EDM01 / EDM02",
        "domain": "Gobernanza (EDM)",
        "eg": "EG01: Portafolio competitivo y generación de valor financiero sostenible",
        "ag": "AG01: Cumplimiento y soporte continuo de TI a metas estratégicas de negocio",
        "bsc": "Perspectiva Financiera",
        "metric": "Relación Beneficio / Costo real del PETI (Lag) y % de sesiones de Comité de Gobierno ejecutadas (Lead)",
        "as_is": "Sin medir (1,00x)",
        "to_be": "1,29x (US$4.267,69 / US$3.300)",
        "cap": "Nivel 1 → Nivel 4",
        "resp": "Diego Vélez Gallego (Gerente / Líder PETI)"
    },
    {
        "code": "APO02 / APO03 / APO05",
        "domain": "Alinear, Planear y Organizar (APO)",
        "eg": "EG08: Optimización de la funcionalidad interna de procesos y escalabilidad",
        "ag": "AG03: Obtención de beneficios esperados de inversiones habilitadas por TI",
        "bsc": "Perspectiva de Procesos Internos",
        "metric": "% de proyectos del PETI ejecutados según priorización Cassidy (258, 214, 132 pts) y % procesos con SIPOC formalizado",
        "as_is": "0 % formalizado",
        "to_be": "100 % caracterizado (4 fases PETI)",
        "cap": "Nivel 2 → Nivel 4",
        "resp": "Santiago Balanta Peña (Arquitecto Cloud / DevOps)"
    },
    {
        "code": "APO08 / APO10",
        "domain": "Alinear, Planear y Organizar (APO)",
        "eg": "EG02: Continuidad, disponibilidad del servicio y retención de clientes",
        "ag": "AG05: Prestación de servicios de TI alineada a acuerdos de requerimientos",
        "bsc": "Perspectiva de Clientes",
        "metric": "Tasa anual de deserción de clientes (Churn Rate) y % de conversión de plan Free a Premium en CRM",
        "as_is": "20,0 % deserción anual",
        "to_be": "10,0 % deserción / 6,8 % conversión",
        "cap": "Nivel 1 → Nivel 3",
        "resp": "Andrés Felipe Sarria Sabogal (Líder Comercial / Procesos)"
    },
    {
        "code": "APO11 / BAI03 / BAI07",
        "domain": "Construir, Adquirir e Implementar (BAI)",
        "eg": "EG06: Cultura de servicio orientada al cliente y aseguramiento de calidad",
        "ag": "AG08: Habilitación y soporte continuo a procesos integrando aplicaciones",
        "bsc": "Perspectiva de Procesos Internos",
        "metric": "% de reducción de errores (bugs) en producción por versión liberada y cobertura de pruebas QA pre-release",
        "as_is": "14 bugs / versión liberada",
        "to_be": "4 bugs (-71,4 % errores; meta -60 %)",
        "cap": "Nivel 0 → Nivel 3",
        "resp": "Martín Eduardo Murillo Rubián (Líder QA y Calidad)"
    },
    {
        "code": "BAI08 / APO07",
        "domain": "Construir, Adquirir e Implementar (BAI)",
        "eg": "EG12: Personas motivadas, calificadas y gestión del capital humano",
        "ag": "AG13: Conocimiento, experiencia e iniciativas para la innovación técnica",
        "bsc": "Perspectiva de Aprendizaje y Crecimiento",
        "metric": "% de sobrecosto en proyectos por fuga de conocimiento y horas anuales de capacitación técnica por colaborador",
        "as_is": "25,0 % sobrecosto",
        "to_be": "10,0 % sobrecosto / 40 h/año en AulaCloud",
        "cap": "Nivel 0 → Nivel 3",
        "resp": "Diego Vélez / Recursos Humanos"
    },
    {
        "code": "DSS01 / DSS02 / DSS03",
        "domain": "Entregar, Dar Servicio y Soporte (DSS)",
        "eg": "EG02: Continuidad de operaciones y atención oportuna al cliente regional",
        "ag": "AG07: Seguridad de la información, infraestructura confiable y disponibilidad",
        "bsc": "Perspectiva de Clientes",
        "metric": "% de cumplimiento de SLA en tickets de Mesa de Ayuda ITIL y Tiempo Medio de Resolución (MTTR)",
        "as_is": "62,0 % cumplimiento (18,5 h)",
        "to_be": "92,5 % SLA cumplido (3,8 h MTTR)",
        "cap": "Nivel 2 → Nivel 4",
        "resp": "Mesa de Ayuda / Soporte Técnico N1-N2"
    },
    {
        "code": "DSS06 / APO14",
        "domain": "Entregar, Dar Servicio y Soporte (DSS)",
        "eg": "EG08: Eficiencia operativa, eliminación de desperdicios y reducción de costos",
        "ag": "AG08: Integración de datos y flujos de trabajo automatizados entre áreas",
        "bsc": "Perspectiva Financiera / Procesos",
        "metric": "% del tiempo operativo consumido en reprocesos manuales y N.º de áreas de negocio integradas en el ERP Apolo",
        "as_is": "80,0 % (0/4 áreas integradas)",
        "to_be": "40,0 % reprocesos (4/4 áreas integradas)",
        "cap": "Nivel 0 → Nivel 3",
        "resp": "Santiago Balanta / Operaciones ERP"
    },
    {
        "code": "MEA01 / MEA02 / MEA03",
        "domain": "Supervisar, Evaluar y Valorar (MEA)",
        "eg": "EG04: Calidad y oportunidad de la información financiera y de gestión",
        "ag": "AG02: Riesgo de TI gestionado y cumplimiento regulatorio/normativo",
        "bsc": "Perspectiva de Procesos / Aprendizaje",
        "metric": "% de objetivos estratégicos con KPI activo en Dashboard BI y % de controles COBIT auditados periódicamente",
        "as_is": "0 % (Sin KPIs activos)",
        "to_be": "100 % KPIs activos (Auditoría semanal n8n)",
        "cap": "Nivel 0 → Nivel 4",
        "resp": "Brayan Steven Noguera Sarria (Auditoría / Riesgos)"
    }
]

# -----------------------------------------------------------------------------
# 2. SERIE MENSUAL HISTÓRICA DE 12 MESES (DIC 2025 A NOV 2026)
# -----------------------------------------------------------------------------
monthly_data = [
    {"month": "Dic 2025", "created": 52, "resolved": 18, "rework": 80.0, "bugs": 16, "sla": 61.0, "stage": "Línea Base (AS-IS)"},
    {"month": "Ene 2026", "created": 50, "resolved": 22, "rework": 78.0, "bugs": 15, "sla": 63.5, "stage": "Línea Base (AS-IS)"},
    {"month": "Feb 2026", "created": 48, "resolved": 26, "rework": 75.0, "bugs": 14, "sla": 66.0, "stage": "Inicio PETI 2026"},
    {"month": "Mar 2026", "created": 46, "resolved": 29, "rework": 72.0, "bugs": 13, "sla": 70.0, "stage": "Implementación Mesa ITIL"},
    {"month": "Abr 2026", "created": 44, "resolved": 34, "rework": 68.0, "bugs": 11, "sla": 73.5, "stage": "Pipeline CI/CD y QA Staging"},
    {"month": "May 2026", "created": 40, "resolved": 38, "rework": 64.0, "bugs": 10, "sla": 77.0, "stage": "Migración Cloud VPS Apolo"},
    {"month": "Jun 2026", "created": 36, "resolved": 42, "rework": 60.0, "bugs": 8,  "sla": 81.0, "stage": "Lanzamiento AulaCloud Moodle"},
    {"month": "Jul 2026", "created": 32, "resolved": 45, "rework": 55.0, "bugs": 7,  "sla": 84.5, "stage": "Módulo CRM Retención Clientes"},
    {"month": "Ago 2026", "created": 28, "resolved": 48, "rework": 50.0, "bugs": 6,  "sla": 87.0, "stage": "Integración ERP y Factura DIAN"},
    {"month": "Sep 2026", "created": 25, "resolved": 51, "rework": 46.0, "bugs": 5,  "sla": 89.5, "stage": "Flujo Automatizado n8n COBIT"},
    {"month": "Oct 2026", "created": 22, "resolved": 54, "rework": 43.0, "bugs": 4,  "sla": 91.0, "stage": "Consolidación de Auditoría TI"},
    {"month": "Nov 2026", "created": 19, "resolved": 58, "rework": 40.0, "bugs": 4,  "sla": 92.5, "stage": "Meta TO-BE Lograda (92,5% SLA)"}
]

# -----------------------------------------------------------------------------
# 3. DATASET DETALLADO DE 48 CONTROLES E INCIDENTES OPERATIVOS (TECNIFICATE S.A.S.)
# -----------------------------------------------------------------------------
tickets_dataset = [
    # --- ERP MODULAR APOLO (12 tickets) ---
    {
        "code": "TECNIF-DSS06-01", "title": "Discrepancia en redondeo decimal de retención en la fuente (DIAN)",
        "app": "ERP Modular Apolo", "domain": "DSS", "process": "DSS06 / APO14", "req_type": "Automatización BPM & ERP",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Centro de Datos / Local",
        "sla": 98.2, "bsc": "Financiera",
        "rca": "Uso de punto flotante primitivo IEEE 754 de 32 bits en módulo contable provocó desfases de $1 a $5 COP en facturación electrónica masiva.",
        "action": "Migración de tipos de datos a BigDecimal con precisión de 4 decimales y validación SOAP previa con WebService DIAN.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Commit #8f2d1e en rama release-dian-v3.1 con 42 pruebas unitarias aprobadas."
    },
    {
        "code": "TECNIF-DSS06-02", "title": "Conciliación bancaria manual tardía genera reprocesos contables de fin de mes",
        "app": "ERP Modular Apolo", "domain": "DSS", "process": "DSS06", "req_type": "Automatización BPM & ERP",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Centro de Datos / Local",
        "sla": 95.0, "bsc": "Procesos Internos",
        "rca": "Extracción de extractos bancarios en PDF/Excel sin parser automatizado requería 4 horas diarias de digitación repetitiva.",
        "action": "Script extractor automatizado en Python con mapeo de extractos bancarios de Bancolombia y Davivienda.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Módulo bancario integrado con 100% de conciliación automática en Girardot."
    },
    {
        "code": "TECNIF-BAI07-01", "title": "Bloqueo por concurrencia en inventarios de ferreterías durante ventas simultáneas",
        "app": "ERP Modular Apolo", "domain": "BAI", "process": "BAI07 / APO10", "req_type": "Control de Calidad QA",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Centro de Datos / Local",
        "sla": 96.0, "bsc": "Clientes",
        "rca": "Falta de bloqueo pesimista en transacciones SQL producía inconsistencias de stock negativo en cajas múltiples.",
        "action": "Implementación de transacciones SELECT FOR UPDATE y pruebas de estrés con JMeter simulando 50 cajas concurrentes.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Informe de pruebas de carga JMeter v5.6: 0 bloqueos y 0 discrepancias de stock."
    },
    {
        "code": "TECNIF-DSS02-01", "title": "Lentitud en consultas de kardex de inventarios con más de 10.000 referencias",
        "app": "ERP Modular Apolo", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Centro de Datos / Local",
        "sla": 92.0, "bsc": "Procesos Internos",
        "rca": "Ausencia de índices compuestos en tablas kardex y transacciones históricas en MySQL 8.0.",
        "action": "Optimización de esquemas relacionales, creación de índices B-Tree y particionamiento por año fiscal.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Tiempo de respuesta de consulta reducido de 14,2 s a 0,38 s."
    },
    {
        "code": "TECNIF-BAI03-01", "title": "Emisión de nómina electrónica en formato XML según resolución DIAN vigente",
        "app": "ERP Modular Apolo", "domain": "BAI", "process": "BAI03", "req_type": "Automatización BPM & ERP",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Centro de Datos / Local",
        "sla": 94.5, "bsc": "Financiera",
        "rca": "Firma digital XAdES-BES fallaba por expiración de certificados y namespaces desactualizados.",
        "action": "Actualización de librería de firmado criptográfico y validación sintáctica contra esquema XSD oficial de DIAN.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Certificación de interoperabilidad DIAN aprobada con 150 nóminas procesadas."
    },
    {
        "code": "TECNIF-DSS05-01", "title": "Pérdida de copia de seguridad local en cliente distribuidor de Flandes",
        "app": "ERP Modular Apolo", "domain": "DSS", "process": "DSS05 / DSS04", "req_type": "Gobierno y Seguridad",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Brayan Noguera (Riesgos)", "hosting": "Centro de Datos / Local",
        "sla": 99.0, "bsc": "Procesos Internos",
        "rca": "El cliente apagaba el servidor físico a las 6:00 pm interrumpiendo el cron de backup nocturno sin notificación.",
        "action": "Configuración de agente de backup continuo cifrado AES-256 hacia almacenamiento S3 Wasabi con alerta a Telegram.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Bitácora diaria de snapshots automáticos con verificación de suma SHA-256."
    },
    {
        "code": "TECNIF-APO14-01", "title": "Inconsistencia de saldos en módulo de cartera por anulación manual indebida",
        "app": "ERP Modular Apolo", "domain": "APO", "process": "APO14", "req_type": "Automatización BPM & ERP",
        "priority": "P2 - Alto", "status": "En Curso", "assignee": "Andrés Sarria (Comercial)", "hosting": "Centro de Datos / Local",
        "sla": 88.0, "bsc": "Financiera",
        "rca": "Permisos de usuario permitían revertir recibos de caja sin generar la correspondiente nota contable de anulación.",
        "action": "Reestructuración de matriz de segregación de funciones (SoD) y flujo de aprobación por gerencia.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 2 (Gestionado)", "evidence": "Matriz SoD en desarrollo en rama ERP-release-4.2."
    },
    {
        "code": "TECNIF-BAI07-02", "title": "Fallo en módulo de liquidación de primas y cesantías en PyMEs comerciales",
        "app": "ERP Modular Apolo", "domain": "BAI", "process": "BAI07", "req_type": "Control de Calidad QA",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Centro de Datos / Local",
        "sla": 93.0, "bsc": "Procesos Internos",
        "rca": "No se computaba el auxilio de transporte para trabajadores con licencias no remuneradas intermedias.",
        "action": "Corrección de fórmula actuarial de nómina y suite de 28 casos de prueba automatizados con PHPUnit.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Pruebas unitarias al 100% en pipeline CI/CD GitHub Actions."
    },
    {
        "code": "TECNIF-DSS02-02", "title": "Error de comunicación entre impresora fiscal de recibos térmicos y punto de venta",
        "app": "ERP Modular Apolo", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Mesa de Ayuda N1", "hosting": "Centro de Datos / Local",
        "sla": 95.5, "bsc": "Clientes",
        "rca": "Controlador USB virtual perdía asignación de puerto COM tras reinicios de Windows 11.",
        "action": "Script de enlace estático PowerShell que mapea automáticamente los puertos seriales al iniciar sesión.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Procedimiento operativo estándar SOP-POS-04 documentado en AulaCloud."
    },
    {
        "code": "TECNIF-APO10-01", "title": "Falta de trazabilidad de compras por proveedor y alertas de stock mínimo",
        "app": "ERP Modular Apolo", "domain": "APO", "process": "APO10", "req_type": "Automatización BPM & ERP",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Andrés Sarria (Comercial)", "hosting": "Centro de Datos / Local",
        "sla": 91.0, "bsc": "Procesos Internos",
        "rca": "Ausencia de parametrización de umbrales de reorden en la base de datos de productos.",
        "action": "Implementación de algoritmo de stock de seguridad basado en media móvil de consumo a 60 días.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Reporte gerencial automatizado de sugeridos de compra quincenal."
    },
    {
        "code": "TECNIF-DSS06-03", "title": "Saturación de archivo de transacciones log en servidor local de ferretería",
        "app": "ERP Modular Apolo", "domain": "DSS", "process": "DSS06", "req_type": "Automatización BPM & ERP",
        "priority": "P2 - Alto", "status": "En Curso", "assignee": "Santiago Balanta (DevOps)", "hosting": "Centro de Datos / Local",
        "sla": 86.0, "bsc": "Procesos Internos",
        "rca": "Nivel de log en modo DEBUG activo desde la instalación inicial sin rotación logrotate configurada.",
        "action": "Configuración de logrotate a 7 días comprimidos y cambio de loglevel a WARN.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 2 (Gestionado)", "evidence": "Plan de mantenimiento de servidores cliente en despliegue gradual."
    },
    {
        "code": "TECNIF-EDM02-01", "title": "Evaluación del retorno financiero de inversiones en ERP Apolo vs soluciones Cloud",
        "app": "ERP Modular Apolo", "domain": "EDM", "process": "EDM02", "req_type": "Gobierno y Seguridad",
        "priority": "P3 - Medio", "status": "Por Hacer", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Centro de Datos / Local",
        "sla": 85.0, "bsc": "Financiera",
        "rca": "No se contaba con modelo de Costo Total de Propiedad (TCO) para clientes on-premise vs SaaS.",
        "action": "Diseño de calculadora TCO a 36 meses para fundamentar la migración de PyMEs hacia Apolo Cloud.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 2 (Gestionado)", "evidence": "Modelo financiero TCO preliminar en revisión por gerencia general."
    },

    # --- APOLO ACADÉMICO V2.1 SAAS (12 tickets) ---
    {
        "code": "TECNIF-DSS02-03", "title": "Caída del portal escolar durante entrega de boletines finales por saturación VPS",
        "app": "Apolo Académico SaaS", "domain": "DSS", "process": "DSS02 / BAI04", "req_type": "Soporte Técnico ITIL",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 97.0, "bsc": "Clientes",
        "rca": "Picos de 3.500 conexiones concurrentes agotaron el pool de PHP-FPM y colapsaron el servidor VPS sin balanceador.",
        "action": "Aprovisionamiento de balanceador Nginx, clúster de micro-instancias VPS y capa de caché con Redis para notas escolares.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Disponibilidad del 99,8% registrada en el periodo lectivo de octubre 2026."
    },
    {
        "code": "TECNIF-BAI07-03", "title": "Error en cálculo de promedios ponderados en escalas valorativas del MEN (Decreto 1290)",
        "app": "Apolo Académico SaaS", "domain": "BAI", "process": "BAI07 / APO11", "req_type": "Control de Calidad QA",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 95.0, "bsc": "Clientes",
        "rca": "Incompatibilidad entre escalas cualitativas (Superior, Alto, Básico, Bajo) y pesos porcentuales dinámicos por periodo.",
        "action": "Motor de homologación paramétrica conforme al Decreto 1290/2009 con validación de matrices de notas por periodo.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Certificación de notas validada por 8 colegios clientes de Girardot."
    },
    {
        "code": "TECNIF-APO08-01", "title": "Deserción de 3 instituciones educativas por retrasos en soporte en época de matrícula",
        "app": "Apolo Académico SaaS", "domain": "APO", "process": "APO08 / APO09", "req_type": "Gestión Comercial CRM",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Andrés Sarria (Comercial)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 94.0, "bsc": "Clientes",
        "rca": "Ausencia de acuerdos SLA formalizados y mesa de ayuda centralizada provocaba demoras de hasta 3 días en tickets críticos.",
        "action": "Puesta en marcha de Mesa de Ayuda ITIL con SLA estricto de < 2h para incidentes de matrícula y canal WhatsApp VIP.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Reducción de tasa de deserción del 20% al 10% y renovación del 100% de contratos."
    },
    {
        "code": "TECNIF-DSS05-02", "title": "Vulnerabilidad en portal de consulta de notas de acudientes por falta de sanitización",
        "app": "Apolo Académico SaaS", "domain": "DSS", "process": "DSS05", "req_type": "Gobierno y Seguridad",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Brayan Noguera (Riesgos)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 99.5, "bsc": "Procesos Internos",
        "rca": "Parámetro ID en endpoint de boletines permitía visualización de notas de otros alumnos por manipulación de URL (IDOR).",
        "action": "Implementación de tokens JWT cifrados con expiración de 15 minutos y validación estricta de parentesco en backend.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Informe de auditoría de seguridad OWASP ZAP: 0 vulnerabilidades de inyección o IDOR."
    },
    {
        "code": "TECNIF-BAI04-01", "title": "Generación lenta de boletines PDF masivos en fin de trimestre (colegios de 1.200 alumnos)",
        "app": "Apolo Académico SaaS", "domain": "BAI", "process": "BAI04", "req_type": "Automatización BPM & ERP",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 93.0, "bsc": "Procesos Internos",
        "rca": "Generación síncrona en hilo principal de servidor bloqueaba la CPU y agotaba los 512 MB de memoria de PHP.",
        "action": "Cola asíncrona de procesamiento distribuido en segundo plano con Redis y worker Celery/Node.js.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Tiempo de generación por colegio reducido de 45 minutos a 2,5 minutos."
    },
    {
        "code": "TECNIF-DSS02-04", "title": "Fallo en pasarela de pagos electrónicos PSE / Wompi para pago de matrículas",
        "app": "Apolo Académico SaaS", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 98.0, "bsc": "Financiera",
        "rca": "El webhook de confirmación bancaria no manejaba reintentos ante timeouts breves de red.",
        "action": "Diseño de webhook resiliente con idempotencia, arquitectura de reintentos exponencial y registro en base de datos.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Tasa de transacciones exitosas de matrículas consolidada en 99,4%."
    },
    {
        "code": "TECNIF-APO09-01", "title": "Ausencia de catálogo formal de servicios y acuerdos de nivel de servicio (SLA) para colegios",
        "app": "Apolo Académico SaaS", "domain": "APO", "process": "APO09", "req_type": "Gobierno y Seguridad",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 91.5, "bsc": "Clientes",
        "rca": "Contratos comerciales no estipulaban tiempos máximos de respuesta ni garantías de disponibilidad operativa.",
        "action": "Definición del Catálogo de Servicios TI con 3 niveles de servicio (Bronce, Plata, Oro) y SLAs auditables.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Firmado en el 100% de los contratos de renovación académica 2026."
    },
    {
        "code": "TECNIF-BAI03-02", "title": "Módulo de gestión del Observador del Estudiante digital con tipificación de faltas (Ley 1620)",
        "app": "Apolo Académico SaaS", "domain": "BAI", "process": "BAI03", "req_type": "Control de Calidad QA",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 92.0, "bsc": "Procesos Internos",
        "rca": "Los colegios registraban faltas tipo I, II y III en libros físicos sin trazabilidad jurídica.",
        "action": "Módulo digital del observador con firma digital biométrica de coordinadores y acudientes.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Aprobado por el comité de convivencia escolar de 5 colegios piloto."
    },
    {
        "code": "TECNIF-DSS01-01", "title": "Monitoreo continuo de salud de instancias VPS y consumo de memoria RAM",
        "app": "Apolo Académico SaaS", "domain": "DSS", "process": "DSS01 / MEA01", "req_type": "Gobierno y Seguridad",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 96.0, "bsc": "Procesos Internos",
        "rca": "Fugas de memoria en procesos daemon provocaban caídas silenciosas a altas horas de la noche.",
        "action": "Despliegue de agente Prometheus + Grafana con alertas tempranas al canal Slack de operaciones.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "MTTD (Mean Time to Detect) reducido a menos de 45 segundos."
    },
    {
        "code": "TECNIF-APO11-01", "title": "Control de calidad en homologación de notas para estudiantes transferidos entre colegios",
        "app": "Apolo Académico SaaS", "domain": "APO", "process": "APO11", "req_type": "Control de Calidad QA",
        "priority": "P3 - Medio", "status": "En Curso", "assignee": "Martín Murillo (QA)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 89.0, "bsc": "Clientes",
        "rca": "Mallas curriculares disímiles generaban conflictos al consolidar históricos académicos de alumnos nuevos.",
        "action": "Matriz de equivalencias automatizada con validación por secretaría de educación departamental.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 2 (Gestionado)", "evidence": "Fase piloto con el Colegio Departamental Atanasio Girardot."
    },
    {
        "code": "TECNIF-BAI08-01", "title": "Capacitación a coordinadores académicos y docentes en uso de nueva versión v2.1",
        "app": "Apolo Académico SaaS", "domain": "BAI", "process": "BAI08", "req_type": "Soporte Técnico ITIL",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Andrés Sarria (Comercial)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 95.0, "bsc": "Aprendizaje",
        "rca": "Resistencia al cambio y llamadas repetitivas a la mesa de ayuda por dudas básicas de navegabilidad.",
        "action": "Cursos interactivos cortos en AulaCloud y videotutoriales paso a paso de menos de 3 minutos.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Reducción del 55% en tickets de soporte L1 de consultas de uso básico."
    },
    {
        "code": "TECNIF-MEA01-01", "title": "Auditoría de cumplimiento de protección de datos de menores de edad (Ley 1581 Habeas Data)",
        "app": "Apolo Académico SaaS", "domain": "MEA", "process": "MEA01 / MEA03", "req_type": "Gobierno y Seguridad",
        "priority": "P2 - Alto", "status": "En Curso", "assignee": "Brayan Noguera (Riesgos)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 87.5, "bsc": "Procesos Internos",
        "rca": "No se contaba con registro formal de autorizaciones parentales de tratamiento de datos personales.",
        "action": "Módulo de aceptación digital explícita de política de tratamiento de datos al iniciar sesión.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Informe de cumplimiento regulatorio al 90% con registro en base de datos."
    },

    # --- APOLO II MOBILE (8 tickets) ---
    {
        "code": "TECNIF-BAI07-04", "title": "Pérdida de datos de asistencia escolar en zonas rurales con baja cobertura móvil",
        "app": "Apolo II Mobile", "domain": "BAI", "process": "BAI07 / DSS02", "req_type": "Control de Calidad QA",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 96.0, "bsc": "Clientes",
        "rca": "La app intentaba sincronizar síncronamente; al fallar la señal 3G/4G, descartaba las peticiones sin persistencia local.",
        "action": "Arquitectura Offline-First con base de datos SQLite local y sincronización bidireccional mediante Service Worker.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Tasa de pérdida de datos reducida a 0% en pruebas de campo en veredas de Flandes."
    },
    {
        "code": "TECNIF-BAI03-03", "title": "Crash de la app en dispositivos con Android 13 y 14 por nuevas políticas de permisos",
        "app": "Apolo II Mobile", "domain": "BAI", "process": "BAI03", "req_type": "Control de Calidad QA",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 93.0, "bsc": "Clientes",
        "rca": "Permisos obsoletos READ_EXTERNAL_STORAGE provocaban cierre forzoso inmediato en Android 13+.",
        "action": "Actualización a Target SDK 34, uso de Scoped Storage y gestión reactiva de permisos en tiempo de ejecución.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Calificación en Google Play interna subió de 2,8 a 4,6 estrellas."
    },
    {
        "code": "TECNIF-DSS02-05", "title": "Conflicto de sincronización al editar una misma calificación desde la web y desde la app móvil",
        "app": "Apolo II Mobile", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 94.0, "bsc": "Procesos Internos",
        "rca": "Falta de control de versiones y timestamps en la resolución de conflictos concurrentes.",
        "action": "Implementación del algoritmo 'Last Write Wins' con registro de auditoría de timestamp UTC en servidor.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "0 colisiones de notas en el consolidado general de fin de año 2026."
    },
    {
        "code": "TECNIF-DSS05-03", "title": "Almacenamiento de contraseñas de docentes en texto claro en memoria caché móvil",
        "app": "Apolo II Mobile", "domain": "DSS", "process": "DSS05", "req_type": "Gobierno y Seguridad",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Brayan Noguera (Riesgos)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 99.0, "bsc": "Procesos Internos",
        "rca": "Uso de SharedPreferences estándar sin cifrado criptográfico exponía credenciales en dispositivos vulnerados.",
        "action": "Migración a Android EncryptedSharedPreferences respaldado por Android KeyStore de hardware.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Validado mediante análisis de seguridad estático MobSF sin hallazgos críticos."
    },
    {
        "code": "TECNIF-BAI04-02", "title": "Consumo excesivo de batería y plan de datos de docentes en segundo plano",
        "app": "Apolo II Mobile", "domain": "BAI", "process": "BAI04", "req_type": "Automatización BPM & ERP",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 91.0, "bsc": "Clientes",
        "rca": "Intervalo de polling continuo cada 15 segundos sin respetar el estado de reposo del dispositivo Doze Mode.",
        "action": "Reemplazo de polling por notificaciones push de Firebase Cloud Messaging (FCM) activadas por eventos.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Consumo de batería reducido en un 78% y ahorro del 85% en datos móviles."
    },
    {
        "code": "TECNIF-APO10-02", "title": "Firma biométrica y reconocimiento facial para validación de asistencia docente",
        "app": "Apolo II Mobile", "domain": "APO", "process": "APO10", "req_type": "Control de Calidad QA",
        "priority": "P3 - Medio", "status": "En Curso", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 88.0, "bsc": "Innovación",
        "rca": "Docentes marcaban asistencia en nombre de colegas mediante intercambio manual de pines de acceso.",
        "action": "Integración del SDK BiometricPrompt nativo con validación de geofencing perimetral de la institución.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 2 (Gestionado)", "evidence": "Fase de prueba en dos colegios con 40 docentes activos."
    },
    {
        "code": "TECNIF-DSS02-06", "title": "Dificultad de descarga de archivos adjuntos de circulares escolares en formato PDF",
        "app": "Apolo II Mobile", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Mesa de Ayuda N1", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 95.0, "bsc": "Clientes",
        "rca": "El componente WebView intentaba renderizar PDFs directamente en lugar de delegar a la aplicación nativa del sistema.",
        "action": "Implementación del visor integrado Android PdfRenderer con opción de descarga y apertura externa.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Satisfacción de usuarios en encuestas subió a 4,8/5,0."
    },
    {
        "code": "TECNIF-APO02-01", "title": "Alineación del roadmap móvil con las directrices estratégicas de la gerencia",
        "app": "Apolo II Mobile", "domain": "APO", "process": "APO02", "req_type": "Gobierno y Seguridad",
        "priority": "P4 - Bajo", "status": "Completado en SLA", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 90.0, "bsc": "Aprendizaje",
        "rca": "Nuevas funcionalidades móviles se construían ad-hoc según peticiones aisladas sin priorización de negocio.",
        "action": "Adopción de Product Backlog priorizado por valor de negocio y sprints quincenales de entrega continua.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Plan de lanzamientos 2026-2027 aprobado por el Comité de Gobierno de TI."
    },

    # --- PORTAL WEB & HOSTING VPS (6 tickets) ---
    {
        "code": "TECNIF-DSS01-02", "title": "Expiración inadvertida de certificados SSL Let's Encrypt en hosting de clientes",
        "app": "Portal Web & Hosting VPS", "domain": "DSS", "process": "DSS01 / DSS05", "req_type": "Gobierno y Seguridad",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Servidor Dedicado / VPS",
        "sla": 98.0, "bsc": "Clientes",
        "rca": "Fallo silencioso en el cron de certbot por bloqueo de puerto 80 durante renovación ACME HTTP-01.",
        "action": "Migración al desafío ACME DNS-01 automatizado con API de Cloudflare y monitor Heartbeat externo.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "100% de dominios corporativos con SSL vigente y renovación automatizada a 60 días."
    },
    {
        "code": "TECNIF-DSS05-04", "title": "Ataques de fuerza bruta SSH y saturación de ancho de banda en servidores VPS",
        "app": "Portal Web & Hosting VPS", "domain": "DSS", "process": "DSS05", "req_type": "Gobierno y Seguridad",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Brayan Noguera (Riesgos)", "hosting": "Servidor Dedicado / VPS",
        "sla": 99.0, "bsc": "Procesos Internos",
        "rca": "Puerto 22 abierto por defecto con autenticación por contraseña habilitada y sin rate-limiting.",
        "action": "Cierre de puerto 22, cambio a puerto no estándar, autenticación exclusiva por clave SSH Ed25519 y Fail2ban.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Bloqueo de más de 12.000 intentos maliciosos por mes y 0 accesos no autorizados."
    },
    {
        "code": "TECNIF-DSS02-07", "title": "Saturación de almacenamiento en discos SSD por retención excesiva de backups locales",
        "app": "Portal Web & Hosting VPS", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Servidor Dedicado / VPS",
        "sla": 94.0, "bsc": "Procesos Internos",
        "rca": "Snapshots diarios de cPanel se acumulaban en la partición /home sin política de rotación automática.",
        "action": "Script de depuración semanal y política de ciclo de vida con retención de 14 días y descarga a Wasabi Cloud.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Espacio en disco estabilizado en 52% de uso permanente."
    },
    {
        "code": "TECNIF-APO13-01", "title": "Implementación de cortafuegos de aplicaciones web (WAF) y mitigación DDoS",
        "app": "Portal Web & Hosting VPS", "domain": "APO", "process": "APO13", "req_type": "Gobierno y Seguridad",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Brayan Noguera (Riesgos)", "hosting": "Servidor Dedicado / VPS",
        "sla": 95.0, "bsc": "Procesos Internos",
        "rca": "Ausencia de capa WAF exponía los portales de clientes a escaneos automáticos de bots y vulnerabilidades WordPress.",
        "action": "Despliegue de proxy inverso Cloudflare con reglas WAF personalizadas y rate-limiting por IP.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Mitigación del 100% de ataques DDoS de capa 7 detectados en 2026."
    },
    {
        "code": "TECNIF-DSS02-08", "title": "Demora en provisión de nuevas cuentas de hosting y correos corporativos para clientes PyME",
        "app": "Portal Web & Hosting VPS", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Mesa de Ayuda N1", "hosting": "Servidor Dedicado / VPS",
        "sla": 92.5, "bsc": "Clientes",
        "rca": "Proceso de creación manual mediante interfaz de cPanel tomaba hasta 4 horas laborales tras la venta.",
        "action": "Automatización del aprovisionamiento mediante WHM API integrada con el formulario comercial.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Tiempo de activación inmediata reducido de 4 horas a 90 segundos."
    },
    {
        "code": "TECNIF-MEA01-02", "title": "Monitoreo de reputación de direcciones IP de correo para evitar caídas en listas negras (Spam)",
        "app": "Portal Web & Hosting VPS", "domain": "MEA", "process": "MEA01", "req_type": "Gobierno y Seguridad",
        "priority": "P2 - Alto", "status": "En Curso", "assignee": "Santiago Balanta (DevOps)", "hosting": "Servidor Dedicado / VPS",
        "sla": 88.0, "bsc": "Clientes",
        "rca": "Clientes enviaban correos promocionales masivos sin SPF/DKIM/DMARC provocando bloqueo en Gmail y Hotmail.",
        "action": "Configuración estricta de registros SPF, claves DKIM de 2048 bits y políticas DMARC reject.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "IPs corporativas 100% limpias en Spamhaus y Barracuda."
    },

    # --- AULACLOUD & WIKI (5 tickets) ---
    {
        "code": "TECNIF-BAI08-02", "title": "Sobrecosto en proyectos por fuga de conocimiento técnico clave tras rotación de personal",
        "app": "AulaCloud & Wiki", "domain": "BAI", "process": "BAI08 / APO07", "req_type": "Gobierno y Seguridad",
        "priority": "P1 - Crítico", "status": "Completado en SLA", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 95.0, "bsc": "Aprendizaje",
        "rca": "Desarrollador backend renunció dejando arquitectura de facturación DIAN sin documentar, generando retraso de 3 semanas (25% sobrecosto).",
        "action": "Implementación de repositorio wiki técnico en AulaCloud (Moodle) con manuales paso a paso y videoguías grabadas.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Sobrecosto reducido de 25% a 10% y tiempo de onboarding bajó de 4 semanas a 5 días."
    },
    {
        "code": "TECNIF-APO07-01", "title": "Plan de capacitación continua de 40 horas anuales por colaborador de TI",
        "app": "AulaCloud & Wiki", "domain": "APO", "process": "APO07", "req_type": "Gobierno y Seguridad",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 93.0, "bsc": "Aprendizaje",
        "rca": "Falta de formación formal en estándares de arquitectura de software, DevOps y aseguramiento de calidad QA.",
        "action": "Malla curricular interna en AulaCloud con cursos de COBIT 2019, ITIL 4, Docker, CI/CD y pruebas unitarias.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "100% del equipo de 5 colaboradores certificado en sus módulos obligatorios."
    },
    {
        "code": "TECNIF-DSS02-09", "title": "Videotutoriales de autoservicio para resolución de dudas frecuentes de usuarios",
        "app": "AulaCloud & Wiki", "domain": "DSS", "process": "DSS02", "req_type": "Soporte Técnico ITIL",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Mesa de Ayuda N1", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 96.0, "bsc": "Clientes",
        "rca": "Más del 40% de las llamadas telefónicas solicitaban ayuda para configurar impresoras o cambiar contraseñas de Apolo.",
        "action": "Producción de 25 cápsulas de video interactivas de 2 minutos integradas en el portal de ayuda.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Reducción de 38% en volumen de llamadas repetitivas recibidas en mesa de ayuda."
    },
    {
        "code": "TECNIF-BAI03-04", "title": "Estandarización de plantillas de requerimientos y especificaciones funcionales",
        "app": "AulaCloud & Wiki", "domain": "BAI", "process": "BAI03", "req_type": "Control de Calidad QA",
        "priority": "P3 - Medio", "status": "Completado en SLA", "assignee": "Martín Murillo (QA)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 92.0, "bsc": "Procesos Internos",
        "rca": "Requerimientos de software se levantaban en servilletas o notas de voz informales de WhatsApp.",
        "action": "Plantilla oficial de Historias de Usuario con Criterios de Aceptación (Gherkin/BDD) alojada en la wiki.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "El 100% de los sprints de desarrollo se ejecutan con historias validadas."
    },
    {
        "code": "TECNIF-MEA02-01", "title": "Evaluación del clima organizacional y satisfacción laboral del equipo de TI",
        "app": "AulaCloud & Wiki", "domain": "MEA", "process": "MEA02", "req_type": "Gobierno y Seguridad",
        "priority": "P4 - Bajo", "status": "En Curso", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 89.0, "bsc": "Aprendizaje",
        "rca": "Sobrecarga de trabajo por horas extras no remuneradas durante épocas de entregas de boletines escolares.",
        "action": "Encuesta semestral de clima laboral, balance de cargas de trabajo y política de compensatorios.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 2 (Gestionado)", "evidence": "Índice de satisfacción laboral subió a 82% en la medición de octubre 2026."
    },

    # --- CRM OPEN SOURCE & CANAL PARTNERS (5 tickets) ---
    {
        "code": "TECNIF-APO08-02", "title": "Pérdida de oportunidades de venta por falta de embudo comercial y seguimiento",
        "app": "CRM Open Source", "domain": "APO", "process": "APO08", "req_type": "Gestión Comercial CRM",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Andrés Sarria (Comercial)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 94.0, "bsc": "Clientes",
        "rca": "Prospectos de colegios de Girardot y Flandes se anotaban en libretas personales y se perdían.",
        "action": "Despliegue y personalización de CRM Open Source con embudo visual de 5 etapas comerciales.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "Aumento del 28% en tasa de cierre de nuevos contratos educativos."
    },
    {
        "code": "TECNIF-EDM02-02", "title": "Modelo de canal de distribución y comisiones para aliados regionales (Partners)",
        "app": "CRM Open Source", "domain": "EDM", "process": "EDM02", "req_type": "Gobierno y Seguridad",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Diego Vélez (Líder PETI)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 93.0, "bsc": "Financiera",
        "rca": "Ausencia de esquema de incentivos formales para distribuidores de software en Tolima y Cundinamarca.",
        "action": "Acuerdo de comisión escalonada (15% por venta y 10% por renovación) gestionado en el CRM.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 3 (Establecido)", "evidence": "3 nuevos distribuidores afiliados en Girardot, Ibagué y Melgar."
    },
    {
        "code": "TECNIF-APO08-03", "title": "Alertas automáticas de renovación contractual para prevenir deserción de clientes",
        "app": "CRM Open Source", "domain": "APO", "process": "APO08", "req_type": "Gestión Comercial CRM",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Andrés Sarria (Comercial)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 96.0, "bsc": "Clientes",
        "rca": "Contratos vencían sin previo contacto comercial; la competencia abordaba a los rectores con ofertas agresivas.",
        "action": "Automatización en CRM con alertas a 60, 30 y 15 días previos al vencimiento y visita preventiva.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Tasa de retención anual consolidada en 90% (reducción del churn al 10%)."
    },
    {
        "code": "TECNIF-DSS06-04", "title": "Sincronización automatizada de prospectos y métricas comerciales mediante webhook n8n",
        "app": "CRM Open Source", "domain": "DSS", "process": "DSS06 / MEA01", "req_type": "Automatización BPM & ERP",
        "priority": "P2 - Alto", "status": "Completado en SLA", "assignee": "Santiago Balanta (DevOps)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 95.0, "bsc": "Procesos Internos",
        "rca": "Prospectos recibidos por Facebook e Instagram se transcribían manualmente a hojas de Excel.",
        "action": "Nodo n8n programado semanalmente que consulta APIs de redes, normaliza prospectos y los inserta en el CRM.",
        "cap_before": "Nivel 0 (Incompleto)", "cap_after": "Nivel 4 (Cuantitativo)", "evidence": "Flujo de trabajo n8n activo ejecutándose cada lunes a las 08:00 AM."
    },
    {
        "code": "TECNIF-APO10-03", "title": "Estrategia de conversión de usuarios de plan Gratuito / Básico a plan Premium",
        "app": "CRM Open Source", "domain": "APO", "process": "APO10", "req_type": "Gestión Comercial CRM",
        "priority": "P3 - Medio", "status": "En Curso", "assignee": "Andrés Sarria (Comercial)", "hosting": "Nube (Cloud VPS SaaS)",
        "sla": 87.0, "bsc": "Financiera",
        "rca": "Muchos colegios utilizaban solo la versión básica gratuita sin conocer los módulos avanzados de boletines.",
        "action": "Campañas de email marketing automatizado con demostraciones prácticas de módulos prémium.",
        "cap_before": "Nivel 1 (Inicial)", "cap_after": "Nivel 2 (Gestionado)", "evidence": "Tasa de conversión actual del 6,8% hacia contratos prémium de pago."
    }
]

print(f"Total structured tickets prepared: {len(tickets_dataset)}")
