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

print("Starting generation of 100% Spanish, fully functional Dashboard and deliverables...")
