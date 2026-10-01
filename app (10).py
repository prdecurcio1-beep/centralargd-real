import urllib.parse
import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)

# ============================================================
# DROGARIA TOTAL ITUVERAVA - Delivery e Ofertas
# Pedidos: WhatsApp (16) 99106-7477
# ============================================================

ZAP_PEDIDOS = "5516991067477"
ZAP_LOJA = "5516999982256"
CDN_IMG = "https://cdn-cosmos.bluesoft.com.br/products/"
VIDEO_ID = "OheBqPHgUr8"

BASE = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.join(BASE, "estaticas")

# Artes servidas da pasta estaticas
LOGO = "/estaticas/logo.png"
A_CARRO = "/estaticas/arte-carro.jpg"
A_BEMME = "/estaticas/arte-bemme.jpg"
A_PART = "/estaticas/arte-participar.jpg"

@app.route("/estaticas/<path:nome>")
def estaticas(nome):
    return send_from_directory(PASTA, nome)

BEMME = [
    {"n": "WAFER PROTEIN COOKIES CREAM ZERO 25G BEMME", "f": "Bemme", "de": 12.9, "pc": 12.9, "e": 13, "c": "Bemme - 5x Chances", "ean": "7898775460583", "campanha":1},
    {"n": "BARRA BANANA C/ AMENDOIM ZERO 25G BEMME", "f": "Bemme", "de": 5.99, "pc": 5.99, "e": 11, "c": "Bemme - 5x Chances", "ean": "7898775460538", "campanha":1},
    {"n": "BARRA NUTS CRANBERRY ZERO 25G BEMME", "f": "Bemme", "de": 6.99, "pc": 6.99, "e": 11, "c": "Bemme - 5x Chances", "ean": "7898775460576", "campanha":1},
    {"n": "COND.BEMME RECONSTRUCAO 300ML", "f": "Bemme", "de": 31.9, "pc": 28.7, "e": 11, "c": "Bemme - 5x Chances", "ean": "7897799835318", "campanha":1},
    {"n": "MASC.BEMME NUTRICAO 250ML", "f": "Bemme", "de": 33.3, "pc": 29.9, "e": 11, "c": "Bemme - 5x Chances", "ean": "7897799835400", "campanha":1},
    {"n": "SH.BEMME NUTRICAO 300ML", "f": "Bemme", "de": 31.5, "pc": 28.3, "e": 11, "c": "Bemme - 5x Chances", "ean": "7897799835387", "campanha":1},
    {"n": "SH.BEMME RECONSTRUCAO 300ML", "f": "Bemme", "de": 31.5, "pc": 28.3, "e": 11, "c": "Bemme - 5x Chances", "ean": "7897799835301", "campanha":1},
    {"n": "BARRA COCADA C/CHOCOLATE ZERO 25G BEMME", "f": "Bemme", "de": 6.99, "pc": 6.99, "e": 10, "c": "Bemme - 5x Chances", "ean": "7898775460552", "campanha":1},
    {"n": "BEMME GUMMIES SENIOR 50+ C/60 GOMAS SABOR MELANCIA", "f": "Bemme", "de": 100.2, "pc": 89.9, "e": 7, "c": "Bemme - 5x Chances", "ean": "7896321041746", "campanha":1},
    {"n": "Bemme Perfume IV 15ml", "f": "Bemme", "de": 44.8, "pc": 39.9, "e": 57, "c": "Bemme - 5x Chances", "vs": [{"v": "VIP ROSE", "ean": "7899918942006", "pc": 39.9, "e": 7}, {"v": "OLIMPYC", "ean": "7899918942020", "pc": 39.9, "e": 6}, {"v": "PASSION", "ean": "7899918942013", "pc": 39.9, "e": 6}, {"v": "CREEDY AVENTUS", "ean": "7899918942044", "pc": 39.9, "e": 5}, {"v": "ESTY BELLA", "ean": "7899918941948", "pc": 39.9, "e": 5}, {"v": "GYRL BLUSH", "ean": "7899918941955", "pc": 39.9, "e": 5}, {"v": "GYRL", "ean": "7899918942174", "pc": 39.9, "e": 5}, {"v": "INVYCTUS", "ean": "7899918942037", "pc": 39.9, "e": 5}, {"v": "SAVAGE", "ean": "7899918942181", "pc": 39.9, "e": 5}, {"v": "MAN NY", "ean": "7899918941979", "pc": 39.9, "e": 4}, {"v": "MILION", "ean": "7899918941986", "pc": 39.9, "e": 4}]},
    {"n": "BARRA COCADA C/ABACAXI ZERO 25G BEMME", "f": "Bemme", "de": 5.99, "pc": 5.99, "e": 6, "c": "Bemme - 5x Chances", "ean": "7898775460590", "campanha":1},
    {"n": "COND.BEMME CACHOS 300ML", "f": "Bemme", "de": 31.9, "pc": 28.7, "e": 5, "c": "Bemme - 5x Chances", "ean": "7897799835356", "campanha":1},
    {"n": "LEAVE IN BEMME CACHOS 250ML", "f": "Bemme", "de": 33.3, "pc": 29.9, "e": 5, "c": "Bemme - 5x Chances", "ean": "7897799835363", "campanha":1},
    {"n": "Bemme Body Splash 220ml", "f": "Bemme", "de": 57.4, "pc": 51.4, "e": 14, "c": "Bemme - 5x Chances", "vs": [{"v": "ESTY BELLA", "ean": "7899918943232", "pc": 51.4, "e": 4}, {"v": "LOVY SPELL", "ean": "7899918943256", "pc": 51.4, "e": 3}, {"v": "AMALFY SUNSET", "ean": "7899918943263", "pc": 51.4, "e": 2}, {"v": "IV GIRL", "ean": "7899918943225", "pc": 51.4, "e": 2}, {"v": "BARY VANILLA", "ean": "7899918943270", "pc": 51.4, "e": 1}, {"v": "PASSION", "ean": "7899918943249", "pc": 51.4, "e": 1}, {"v": "URBANY BEAT", "ean": "7899918943287", "pc": 51.4, "e": 1}]},
    {"n": "KIT ENX.BUCAL ZERO ALCOOL MENTA 500ML+250ML BEMME", "f": "Bemme", "de": 28.8, "pc": 23.95, "e": 4, "c": "Bemme - 5x Chances", "ean": "7908324802511", "campanha":1},
    {"n": "MASC.BEMME CACHOS 250ML", "f": "Bemme", "de": 33.3, "pc": 29.9, "e": 3, "c": "Bemme - 5x Chances", "ean": "7897799835370", "campanha":1},
    {"n": "BODY SPLASH MAN NY IVENCY 220ML BEMME", "f": "Bemme", "de": 57.4, "pc": 44.9, "e": 2, "c": "Bemme - 5x Chances", "ean": "7898976443432", "campanha":1},
    {"n": "COND.BEMME ANTICASPA 300ML", "f": "Bemme", "de": 29.9, "pc": 29.9, "e": 2, "c": "Bemme - 5x Chances", "ean": "7897799835448", "campanha":1},
    {"n": "COND.BEMME NUTRICAO 300ML", "f": "Bemme", "de": 31.9, "pc": 28.7, "e": 2, "c": "Bemme - 5x Chances", "ean": "7897799835394", "campanha":1},
    {"n": "KIT BEMME PERFUME INVENCY + BODY SPLASH", "f": "Bemme", "de": 109.9, "pc": 94.9, "e": 2, "c": "Bemme - 5x Chances", "ean": "7898976443470", "campanha":1},
    {"n": "LEAVE IN BEMME RECONSTRUCAO 250ML", "f": "Bemme", "de": 33.3, "pc": 29.9, "e": 2, "c": "Bemme - 5x Chances", "ean": "7897799835325", "campanha":1},
    {"n": "MASC.BEMME RECONSTRUCAO 250ML", "f": "Bemme", "de": 33.3, "pc": 29.9, "e": 2, "c": "Bemme - 5x Chances", "ean": "7897799835332", "campanha":1},
    {"n": "SH.BEMME ANTICASPA 300ML", "f": "Bemme", "de": 29.9, "pc": 29.9, "e": 2, "c": "Bemme - 5x Chances", "ean": "7897799835431", "campanha":1},
    {"n": "SH.BEMME ANTIQUEDA 300ML", "f": "Bemme", "de": 31.5, "pc": 28.3, "e": 2, "c": "Bemme - 5x Chances", "ean": "7897799835455", "campanha":1},
    {"n": "SH.BEMME CACHOS 300ML", "f": "Bemme", "de": 31.5, "pc": 28.3, "e": 2, "c": "Bemme - 5x Chances", "ean": "7897799835349", "campanha":1},
    {"n": "BODY SPLASH SAVAGE IVENCY 220ML BEMME", "f": "Bemme", "de": 57.4, "pc": 51.4, "e": 1, "c": "Bemme - 5x Chances", "ean": "7898976443449", "campanha":1}
]

ESSENCE = [
    {"n": "TOALHA UMED.ESSENCE ALL BABY C/140UN", "f": "Essence All", "de": 10.99, "pc": 7.99, "e": 224, "c": "Linha Essence All", "ean": "7898197416628", "comissao":1},
    {"n": "Essence All C/60 CPS", "f": "Essence All", "de": 105.9, "pc": 69.9, "e": 166, "c": "Linha Essence All", "vs": [{"v": "VITAMINA B12", "ean": "0040141781529", "pc": 69.9, "e": 17}, {"v": "MAG5", "ean": "0040141781413", "pc": 69.9, "e": 16}, {"v": "HOMEM", "ean": "0040141781475", "pc": 69.9, "e": 15}, {"v": "SENIOR", "ean": "0040141781420", "pc": 69.9, "e": 13}, {"v": "6 MAGNESIOS", "ean": "0631430486395", "pc": 69.9, "e": 12}, {"v": "CABELO PELE E UNHA", "ean": "0042882082231", "pc": 69.9, "e": 12}, {"v": "MULHER", "ean": "0040141781505", "pc": 69.9, "e": 12}, {"v": "COLAGENO CURCUMA  A.H", "ean": "0040141781451", "pc": 69.9, "e": 11}, {"v": "COLAGENO TIPO 2", "ean": "0042882082217", "pc": 69.9, "e": 11}, {"v": "CALCIO MDK", "ean": "0042882082224", "pc": 69.9, "e": 9}, {"v": "AZ", "ean": "0040141781437", "pc": 69.9, "e": 7}, {"v": "CURCUMA LONGA", "ean": "0040141779045", "pc": 69.9, "e": 5}, {"v": "MULTI KIDS", "ean": "0042882082200", "pc": 69.9, "e": 4}, {"v": "THERMO ALL", "ean": "0040141778987", "pc": 69.9, "e": 4}, {"v": "BIOTINA", "ean": "0040141779007", "pc": 69.9, "e": 3}, {"v": "TESTO ENERGY", "ean": "0040141781512", "pc": 69.9, "e": 3}, {"v": "VITAMINA B12", "ean": "0040141779069", "pc": 69.9, "e": 3}, {"v": "CAFEINA", "ean": "0040141781444", "pc": 69.9, "e": 2}, {"v": "CLORETO MAGNESIO P.A.", "ean": "0040141779052", "pc": 69.9, "e": 2}, {"v": "NAC", "ean": "0631430486371", "pc": 69.9, "e": 2}, {"v": "PICOLINATO DE CROMO", "ean": "0040141778994", "pc": 69.9, "e": 2}, {"v": "CARBONATO DE CALCIO", "ean": "0631430486401", "pc": 69.9, "e": 1}]},
    {"n": "Essence All C/100 CPS", "f": "Essence All", "de": 105.9, "pc": 69.9, "e": 15, "c": "Linha Essence All", "vs": [{"v": "COMPLEXO B", "ean": "0040141779038", "pc": 69.9, "e": 11}, {"v": "MELATONINA SL", "ean": "0040141781499", "pc": 69.9, "e": 4}]},
    {"n": "ESSENCE ALL OMEGA 3  C/120 CPS", "f": "Essence All", "de": 105.9, "pc": 69.9, "e": 11, "c": "Linha Essence All", "ean": "0040141779014", "comissao":1},
    {"n": "ESSENCE ALL SENIOR 50+ CHOCOLATE 800G", "f": "Essence All", "de": 124.9, "pc": 109.9, "e": 6, "c": "Linha Essence All", "ean": "0631430487125", "comissao":1},
    {"n": "ESSENCE ALL SENIOR 50+ SEM SABOR 800G", "f": "Essence All", "de": 124.9, "pc": 109.9, "e": 3, "c": "Linha Essence All", "ean": "0631430487132", "comissao":1},
    {"n": "ESSENCE ALL MAGNESIO INOSITOL 180G", "f": "Essence All", "de": 84.9, "pc": 69.9, "e": 2, "c": "Linha Essence All", "ean": "0631430486388", "comissao":1}
]

JORNAL = [
    {"n": "TOALHA UMED BEBE FOFINHO PREMIUM 120UN (CX 12UN) RB JORNAL", "f": "20", "de": 15.99, "pc": 11.99, "e": 12, "c": "Bebe & Infantil", "ean": "7897622318568",
    {"n": "TOALHA UMED BEBE FOFINHO PLUS 140UN (CX 12UN) RB JORNAL", "f": "20", "de": 10, "pc": 7.99, "e": 143, "c": "Bebe & Infantil", "ean": "7897622318605",
    {"n": "Fralda BEBE FOFINHO PLUS TAMANHO", "f": "20", "de": 58.9, "pc": 47.9, "e": 30, "c": "Fraldas", "vs": [{"v": "P", "ean": "7898972620165", "pc": 47.9, "e": 3}, {"v": "M", "ean": "7898972620172", "pc": 47.9, "e": 5}, {"v": "G", "ean": "7898972620189", "pc": 47.9, "e": 6}, {"v": "XG", "ean": "7898972620196", "pc": 47.9, "e": 8}, {"v": "XXG", "ean": "7898972620202", "pc": 47.9, "e": 8}]},
    {"n": "Fralda BEBE FOFINHO PREMIUM JUMBO", "f": "20", "de": 68.4, "pc": 54.9, "e": 19, "c": "Fraldas", "vs": [{"v": "XG", "ean": "7899693238905", "pc": 54.9, "e": 7}, {"v": "M", "ean": "7899693238882", "pc": 54.9, "e": 4}, {"v": "XXG", "ean": "7899693238912", "pc": 54.9, "e": 4}, {"v": "G", "ean": "7899693238899", "pc": 54.9, "e": 4}]},
    {"n": "Fralda HIPOPO BABY HIPER PROMO", "f": "JOHNSON & JOHNSON", "de": 64.99, "pc": 49.9, "e": 18, "c": "Fraldas", "vs": [{"v": "XG", "ean": "7899700802594", "pc": 49.9, "e": 11}, {"v": "XXG", "ean": "7899700802600", "pc": 49.9, "e": 7}]},
    {"n": "FRALDA HUGGIES MAXIMA PROTECAO HIPERZINHA M (3X66UN) JORNAL RB", "f": "LIMA  PERGHER", "de": 99, "pc": 79.9, "e": 5, "c": "Fraldas", "ean": "7896007552788",
    {"n": "FRALDA HUGGIES MAXIMA PROTECAO HIPERZINHA G (3X58UN) JORNAL RB", "f": "KIMBERLY -CLARK BRASIL INDUSTRIA E COMER", "de": 99, "pc": 79.9, "e": 6, "c": "Fraldas", "ean": "7896007552801",
    {"n": "FRALDA HUGGIES MAXIMA PROTECAO HIPERZINHA XXG (3X54UN) JORNAL RB", "f": "KIMBERLY -CLARK BRASIL INDUSTRIA E COMER", "de": 99, "pc": 79.9, "e": 8, "c": "Fraldas", "ean": "7896007552849",
    {"n": "FRALDA HUGGIES LITTLE SWIMMERS G/XG (8X10UN) RB", "f": "KIMBERLY CLARK", "de": 54, "pc": 40.99, "e": 5, "c": "Fraldas", "ean": "7896007552214",
    {"n": "Fralda MILI BABY GIGA", "f": "MILI S.A", "de": 75.88, "pc": 64.9, "e": 35, "c": "Fraldas", "vs": [{"v": "G", "ean": "7896104992159", "pc": 64.9, "e": 9}, {"v": "M", "ean": "7896104992166", "pc": 64.9, "e": 2}, {"v": "XG", "ean": "7896104992142", "pc": 64.9, "e": 9}, {"v": "XXG", "ean": "7896104992135", "pc": 64.9, "e": 15}]},
    {"n": "Creme Facial Nivea 100g", "f": "NIVEA", "de": 30, "pc": 29.9, "e": 18, "c": "Dermocosmeticos", "vs": [{"v": "ANTISSINAIS", "ean": "42360414", "pc": 29.9, "e": 6}, {"v": "CUIDADO NUTRITIVO", "ean": "42360407", "pc": 29.9, "e": 8}, {"v": "CONTROLE DE OLEOSIDADE 7EM1", "ean": "42495727", "pc": 29.9, "e": 3}, {"v": "7EM1 VITAMINA C", "ean": "42513827", "pc": 29.9, "e": 1}]},
    {"n": "Desodorante Rexona Aerosol 150ml", "f": "UNILEVER", "de": 19.7, "pc": 13.99, "e": 54, "c": "Perfumes & Desodorantes", "vs": [{"v": "ANTIBACTERI/INVISIB", "ean": "7506306244177", "pc": 13.99, "e": 7}, {"v": "FEM ERVA DOCE", "ean": "7891150054653", "pc": 13.99, "e": 6}, {"v": "FEM FRUT VERM", "ean": "7891150064737", "pc": 13.99, "e": 5}, {"v": "FEM INVISIBLE", "ean": "7791293032481", "pc": 13.99, "e": 4}, {"v": "FEM SEM PERFUME", "ean": "7791293032368", "pc": 13.99, "e": 4}, {"v": "MEN ACTIVE DRY", "ean": "7791293022598", "pc": 13.99, "e": 6}, {"v": "MEN ANTIBAC/INVISIB", "ean": "7506306244184", "pc": 13.99, "e": 4}, {"v": "MEN ANTIBACT PROTEC", "ean": "7791293025537", "pc": 13.99, "e": 2}, {"v": "MEN IMPACTO", "ean": "7891150054646", "pc": 13.99, "e": 6}, {"v": "MEN INVISIBLE", "ean": "7791293022635", "pc": 13.99, "e": 1}, {"v": "MEN SEM PERFUME", "ean": "7891150055872", "pc": 13.99, "e": 3}, {"v": "MEN XTRACOOL", "ean": "7791293022581", "pc": 13.99, "e": 6}]},
    {"n": "DES DOVE AER ORIGINAL 150ML RB JORNAL", "f": "UNILEVER", "de": 20, "pc": 15.89, "e": 181, "c": "Perfumes & Desodorantes", "ean": "7506306241183",
    {"n": "Absorvente Intimus INT MEDIO LV16 PG15", "f": "JOHNSON OTC", "de": 23.7, "pc": 17.49, "e": 1, "c": "Higiene Intima", "ean": "7896007542864",
    {"n": "Absorvente Intimus TD PROTEGIDA NOT SECA C/ABAS 30UN", "f": "KIMBERLY CLARK", "de": 35.75, "pc": 23.9, "e": 4, "c": "Higiene Intima", "ean": "7896007550906",
    {"n": "Absorvente Intimus TD PROTEGIDA NOT SUAVE C/ABAS 30UN", "f": "KIMBERLY CLARK", "de": 35.75, "pc": 23.9, "e": 14, "c": "Higiene Intima", "ean": "7896007550890",
    {"n": "ABS MILI PROT TOTAL SUAVE C/ABAS 8UN", "f": "MILI S.A", "de": 4.8, "pc": 2.49, "e": 4, "c": "Higiene Intima", "ean": "7896104993941",
    {"n": "Sabonete Lux 85g", "f": "20", "de": 3.99, "pc": 2.39, "e": 5, "c": "Higiene & Banho", "vs": [{"v": "BUQUE DE JASMIN", "ean": "7891150059849", "pc": 2.39, "e": 2}, {"v": "BUQUE DE LAVANDA", "ean": "7891150059887", "pc": 2.39, "e": 1}, {"v": "BUQUE DE ORQUIDEA", "ean": "7891150059900", "pc": 2.39, "e": 2}]},
    {"n": "Roupa Intima Plenitud", "f": "KIMBERLY CLARK", "de": 98.25, "pc": 64.9, "e": 9, "c": "Fraldas", "vs": [{"v": "PLUS FIT G/XG (2X16UN)", "ean": "7896007547210", "pc": 64.9, "e": 7}, {"v": "PLUS FIT P/M (2X16UN)", "ean": "7896007547203", "pc": 64.9, "e": 2}]},
    {"n": "Locao Hidratante Nivea 400ml", "f": "NIVEA", "de": 32, "pc": 24.9, "e": 15, "c": "Dermocosmeticos", "vs": [{"v": "SOFT MILK", "ean": "4005900004956", "pc": 24.9, "e": 7}, {"v": "MILK HID PROFUNDA", "ean": "4005808315697", "pc": 24.9, "e": 8}]},
    {"n": "PRESERV LUB JONTEX SENSITIVE L8P7 RB", "f": "JOHNSON OTC", "de": 37.99, "pc": 22.9, "e": 3, "c": "Preservativos & Barbear", "ean": "7896222721068",
    {"n": "AP BARB PRESTOBARBA 3 EXTRA SUAVE MASCULINO 2UN", "f": "JOHNSON OTC", "de": 26.5, "pc": 19.49, "e": 2, "c": "Preservativos & Barbear", "ean": "7702018874729",
    {"n": "Kit Seda Shampoo 300ml + Cond. 190ml", "f": "UNILEVER", "de": 19.99, "pc": 17.99, "e": 5, "c": "Cabelos", "vs": [{"v": "LUMINOUS GLYCOL+VITAM C COMPLEX", "ean": "7891150099982", "pc": 17.99, "e": 1}, {"v": "TOQUE DE SEDA", "ean": "7891150101630", "pc": 17.99, "e": 4}]},
    {"n": "OLEO E SERUM DOVE BIFASICO BOND REPAIR+PEPTIDEO 110ML RB", "f": "UNILEVER", "de": 33.2, "pc": 29.9, "e": 4, "c": "Cabelos", "ean": "7891150095540",
    {"n": "OLEO E SERUM DOVE UV REPAIR & GLOW+FERULICO SPRAY 110ML RB", "f": "UNILEVER", "de": 47.1, "pc": 29.9, "e": 3, "c": "Cabelos", "ean": "7891150102798",
    {"n": "CR DENT SORRISO TRIPLA LIMPEZA 70G RB", "f": "JOHNSON OTC", "de": 5.2, "pc": 2.99, "e": 1, "c": "Higiene Bucal", "ean": "7891528029498",
    {"n": "LEAVE-IN SERUM SEDA TOQUE DE SEDA 100ML RB", "f": "20", "de": 25, "pc": 15.99, "e": 2, "c": "Dermocosmeticos", "ean": "7891150101760",
    {"n": "PROT SOL SUNDOWN TRIPLA PROTECAO FPS50 100ML RB JORNAL", "f": "JOHNSON OTC", "de": 49.7, "pc": 38.9, "e": 1, "c": "Dermocosmeticos", "ean": "7891010258139",
    {"n": "PROT SOL NIVEA PROTECT E HIDRATA FPS50 200ML RB", "f": "NIVEA", "de": 69.2, "pc": 49.89, "e": 2, "c": "Dermocosmeticos", "ean": "4005808555345",
    {"n": "PROT FACE NIVEA FPS70 40ML RB", "f": "NIVEA", "de": 49.5, "pc": 39.99, "e": 4, "c": "Dermocosmeticos", "ean": "4005900980397",
    {"n": "CREATINA HARDCORE 300G JORNAL RB", "f": "INTEGRAL MEDICA", "de": 89.9, "pc": 54.9, "e": 1, "c": "Vitaminas & Nutricao", "ean": "7896311708314",
    {"n": "MAG PLUS 5 550MG 60CAPS RB", "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "de": 55.99, "pc": 39.5, "e": 5, "c": "Vitaminas & Nutricao", "ean": "7908699000024"
]

ESSENCE = [
    {"n": "TOALHA UMED.ESSENCE ALL BABY C/140UN", "f": "Essence All", "de": 10.99, "pc": 7.99, "e": 224, "c": "Linha Essence All", "ean": "7898197416628", "comissao":1},
    {"n": "Essence All C/60 CPS", "f": "Essence All", "de": 105.9, "pc": 69.9, "e": 166, "c": "Linha Essence All", "vs": [{"v": "VITAMINA B12", "ean": "0040141781529", "pc": 69.9, "e": 17}, {"v": "MAG5", "ean": "0040141781413", "pc": 69.9, "e": 16}, {"v": "HOMEM", "ean": "0040141781475", "pc": 69.9, "e": 15}, {"v": "SENIOR", "ean": "0040141781420", "pc": 69.9, "e": 13}, {"v": "6 MAGNESIOS", "ean": "0631430486395", "pc": 69.9, "e": 12}, {"v": "CABELO PELE E UNHA", "ean": "0042882082231", "pc": 69.9, "e": 12}, {"v": "MULHER", "ean": "0040141781505", "pc": 69.9, "e": 12}, {"v": "COLAGENO CURCUMA  A.H", "ean": "0040141781451", "pc": 69.9, "e": 11}, {"v": "COLAGENO TIPO 2", "ean": "0042882082217", "pc": 69.9, "e": 11}, {"v": "CALCIO MDK", "ean": "0042882082224", "pc": 69.9, "e": 9}, {"v": "AZ", "ean": "0040141781437", "pc": 69.9, "e": 7}, {"v": "CURCUMA LONGA", "ean": "0040141779045", "pc": 69.9, "e": 5}, {"v": "MULTI KIDS", "ean": "0042882082200", "pc": 69.9, "e": 4}, {"v": "THERMO ALL", "ean": "0040141778987", "pc": 69.9, "e": 4}, {"v": "BIOTINA", "ean": "0040141779007", "pc": 69.9, "e": 3}, {"v": "TESTO ENERGY", "ean": "0040141781512", "pc": 69.9, "e": 3}, {"v": "VITAMINA B12", "ean": "0040141779069", "pc": 69.9, "e": 3}, {"v": "CAFEINA", "ean": "0040141781444", "pc": 69.9, "e": 2}, {"v": "CLORETO MAGNESIO P.A.", "ean": "0040141779052", "pc": 69.9, "e": 2}, {"v": "NAC", "ean": "0631430486371", "pc": 69.9, "e": 2}, {"v": "PICOLINATO DE CROMO", "ean": "0040141778994", "pc": 69.9, "e": 2}, {"v": "CARBONATO DE CALCIO", "ean": "0631430486401", "pc": 69.9, "e": 1}]},
    {"n": "Essence All C/100 CPS", "f": "Essence All", "de": 105.9, "pc": 69.9, "e": 15, "c": "Linha Essence All", "vs": [{"v": "COMPLEXO B", "ean": "0040141779038", "pc": 69.9, "e": 11}, {"v": "MELATONINA SL", "ean": "0040141781499", "pc": 69.9, "e": 4}]},
    {"n": "ESSENCE ALL OMEGA 3  C/120 CPS", "f": "Essence All", "de": 105.9, "pc": 69.9, "e": 11, "c": "Linha Essence All", "ean": "0040141779014", "comissao":1},
    {"n": "ESSENCE ALL SENIOR 50+ CHOCOLATE 800G", "f": "Essence All", "de": 124.9, "pc": 109.9, "e": 6, "c": "Linha Essence All", "ean": "0631430487125", "comissao":1},
    {"n": "ESSENCE ALL SENIOR 50+ SEM SABOR 800G", "f": "Essence All", "de": 124.9, "pc": 109.9, "e": 3, "c": "Linha Essence All", "ean": "0631430487132", "comissao":1},
    {"n": "ESSENCE ALL MAGNESIO INOSITOL 180G", "f": "Essence All", "de": 84.9, "pc": 69.9, "e": 2, "c": "Linha Essence All", "ean": "0631430486388", "comissao":1}
]

JORNAL = [
    {"n": "Kit Seda Shampoo 300ml + Cond. 190ml", "f": "UNILEVER", "de": 19.99, "pc": 17.99, "e": 5, "c": "Cabelos", "vs": [{"v": "LUMINOUS GLYCOL+VITAM C COMPLEX", "ean": "7891150099982", "pc": 17.99, "e": 1}, {"v": "TOQUE DE SEDA", "ean": "7891150101630", "pc": 17.99, "e": 4}]},
    {"n": "DES DOVE AER ORIGINAL 150ML RB JORNAL", "f": "UNILEVER", "de": 20, "pc": 15.89, "e": 181, "c": "Perfumes & Desodorantes", "ean": "7506306241183", "jornal":1},
    {"n": "DES DOVE ROLL ON ORIGINAL 50ML RB", "f": "UNILEVER", "de": 15.9, "pc": 11.29, "e": 9, "c": "Perfumes & Desodorantes", "ean": "78924468", "jornal":1},
    {"n": "Sabonete Rexona Antibacterial 84g", "f": "UNILEVER", "de": 4.5, "pc": 2.49, "e": 29, "c": "Higiene & Banho", "vs": [{"v": "FRESH", "ean": "7891150034952", "pc": 2.49, "e": 3}, {"v": "LIMP PROFUNDA", "ean": "7891150066908", "pc": 2.49, "e": 3}, {"v": "BAMBOO & ALOE", "ean": "7891150024816", "pc": 2.49, "e": 5}, {"v": "MULTIVITAMINAS", "ean": "7891150083288", "pc": 2.49, "e": 4}, {"v": "FRUTAS VERMELHAS", "ean": "7891150083271", "pc": 2.49, "e": 1}, {"v": "ERVA DOCE", "ean": "7891150083264", "pc": 2.49, "e": 13}]},
    {"n": "SAB LIQ DOVE OLEO DE BANHO GLICERINADO 240ML RB JORNAL", "f": "UNILEVER", "de": 39.1, "pc": 29.99, "e": 3, "c": "Higiene & Banho", "ean": "7891150098442", "jornal":1},
    {"n": "SH PANTENE BAMBU 400ML RB", "f": "P&G", "de": 41.8, "pc": 24.8, "e": 2, "c": "Cabelos", "ean": "7500435154239", "jornal":1},
    {"n": "CR HID NIVEA LATA 56G RB", "f": "NIVEA", "de": 26.55, "pc": 21.59, "e": 20, "c": "Dermocosmeticos", "ean": "78906617", "jornal":1},
    {"n": "FIO DENTAL J&J ESSENCIAL MENTA 100MT RB", "f": "JOHNSON & JOHNSON LT", "de": 23.8, "pc": 16.99, "e": 5, "c": "Higiene Bucal", "ean": "7891010501105", "jornal":1},
    {"n": "ENX BUC LISTERINE COOL MINT SUAVE S/AL 500ML RB", "f": "JOHNSON & JOHNSON", "de": 31.25, "pc": 20.49, "e": 6, "c": "Higiene Bucal", "ean": "7891010974312", "jornal":1},
    {"n": "ENX BUC LISTERINE MELANCIA E HORTELA ZERO 500ML RB", "f": "JOHNSON OTC", "de": 28.99, "pc": 20.49, "e": 3, "c": "Higiene Bucal", "ean": "7891010256050", "jornal":1},
    {"n": "ESC DENT COLG CLASSIC CLEAN 3UN RB", "f": "COLGATE", "de": 17.8, "pc": 11.49, "e": 3, "c": "Higiene Bucal", "ean": "7891024026434", "jornal":1},
    {"n": "CR DENT COLG T12 ADVANCED FRESH 90G RB", "f": "JOHNSON OTC", "de": 18.3, "pc": 11.99, "e": 1, "c": "Higiene Bucal", "ean": "7891024135310", "jornal":1},
    {"n": "ABS INTIMUS TD PROTEGIDA TRI PROT SUA C/ABAS 32UN RB", "f": "UNILEVER", "de": 21.1, "pc": 14.99, "e": 8, "c": "Higiene Intima", "ean": "7896007544042", "jornal":1},
    {"n": "ABS INTIMUS TD PROTEGIDA TRI PROT SEC C/ABAS 32UN RB", "f": "JOHNSON OTC", "de": 21.1, "pc": 14.99, "e": 8, "c": "Higiene Intima", "ean": "7896007544059", "jornal":1},
    {"n": "DES NIVEA STICK MEN CLINICAL DERMA PROTECT 54G RB", "f": "NIVEA", "de": 33.5, "pc": 24.89, "e": 1, "c": "Perfumes & Desodorantes", "ean": "4006000045504", "jornal":1},
    {"n": "ROUPA INTIMA PLENITUD PLUS FIT G/XG (2X16UN) RB JORNAL", "f": "KIMBERLY CLARK", "de": 98.25, "pc": 64.9, "e": 7, "c": "Fraldas", "ean": "7896007547210", "jornal":1},
    {"n": "ROUPA INTIMA PLENITUD PLUS FIT P/M (2X16UN) RB JORNAL", "f": "KIMBERLY CLARK", "de": 98.25, "pc": 64.9, "e": 2, "c": "Fraldas", "ean": "7896007547203", "jornal":1},
    {"n": "Desodorante Monange Aerosol 150ml", "f": "20", "de": 11.2, "pc": 9.49, "e": 57, "c": "Perfumes & Desodorantes", "vs": [{"v": "HIDR INT EXT OLIVA", "ean": "7891350034646", "pc": 9.49, "e": 19}, {"v": "INVISIBLE", "ean": "7898919411900", "pc": 9.49, "e": 12}, {"v": "SENSIVEL S/PERF", "ean": "7891350034615", "pc": 9.49, "e": 7}, {"v": "ANTITRANSP DETOX", "ean": "7896235353904", "pc": 9.49, "e": 7}, {"v": "PROTECAO SECA", "ean": "7896235353911", "pc": 9.49, "e": 10}, {"v": "ESPORTE", "ean": "7896235354208", "pc": 9.49, "e": 2}]},
    {"n": "Desodorante Bozzano Aerosol 150ml", "f": "BOZZANO", "de": 11.2, "pc": 9.49, "e": 61, "c": "Perfumes & Desodorantes", "vs": [{"v": "EXTREME", "ean": "7891350032857", "pc": 9.49, "e": 12}, {"v": "FRESH", "ean": "7891350032741", "pc": 9.49, "e": 4}, {"v": "S/PERF", "ean": "7891350032406", "pc": 9.49, "e": 11}, {"v": "INVISIBLE", "ean": "7891350032970", "pc": 9.49, "e": 22}, {"v": "ANTI CARVAO", "ean": "7891350037807", "pc": 9.49, "e": 5}, {"v": "DRY", "ean": "7891350037791", "pc": 9.49, "e": 7}]},
    {"n": "Oleo de Amendoas Paixao 100ml", "f": "JOHNSON & JOHNSON", "de": 16, "pc": 10.99, "e": 7, "c": "Perfumes & Desodorantes", "vs": [{"v": "TENTADORA", "ean": "7898919411931", "pc": 10.99, "e": 1}, {"v": "FLOR BAUNILHA", "ean": "7896235354048", "pc": 10.99, "e": 1}, {"v": "INSP ROSAS BRANCAS", "ean": "7896235354017", "pc": 10.99, "e": 1}, {"v": "IRRES FLOR DE LIS", "ean": "7896235354024", "pc": 10.99, "e": 4}]},
    {"n": "PROT SOL SUNDOWN TRIPLA PROTECAO FPS50 100ML RB", "f": "JOHNSON OTC", "de": 49.7, "pc": 41.99, "e": 1, "c": "Dermocosmeticos", "ean": "7891010258139", "jornal":1},
    {"n": "PROT FACIAL NEUTROGENA SUN FRESH DERM CARE FPS70 40G RB", "f": "JOHNSON & JOHNSON", "de": 96.2, "pc": 66.99, "e": 2, "c": "Dermocosmeticos", "ean": "7891010253196", "jornal":1},
    {"n": "PROT FACIAL NEUTROGENA SUN FRESH DERM CARE MORENA FPS70 40G RB", "f": "JOHNSON & JOHNSON", "de": 79.5, "pc": 66.99, "e": 1, "c": "Dermocosmeticos", "ean": "7891010253219", "jornal":1},
    {"n": "TOALHA UMED BEBE FOFINHO PREMIUM 120UN (CX 12UN) RB JORNAL", "f": "20", "de": 15.99, "pc": 11.99, "e": 12, "c": "Bebe & Infantil", "ean": "7897622318568", "jornal":1},
    {"n": "TOALHA UMED BEBE FOFINHO PLUS 140UN (CX 12UN) RB JORNAL", "f": "20", "de": 10, "pc": 7.99, "e": 143, "c": "Bebe & Infantil", "ean": "7897622318605", "jornal":1},
    {"n": "Fralda Bebe Fofinho Plus", "f": "20", "de": 58.9, "pc": 47.9, "e": 30, "c": "Fraldas", "vs": [{"v": "P", "ean": "7898972620165", "pc": 47.9, "e": 3}, {"v": "M", "ean": "7898972620172", "pc": 47.9, "e": 5}, {"v": "G", "ean": "7898972620189", "pc": 47.9, "e": 6}, {"v": "XG", "ean": "7898972620196", "pc": 47.9, "e": 8}, {"v": "XXG", "ean": "7898972620202", "pc": 47.9, "e": 8}]},
    {"n": "Fralda Bebe Fofinho Premium Jumbo", "f": "20", "de": 68.4, "pc": 54.9, "e": 19, "c": "Fraldas", "vs": [{"v": "XG", "ean": "7899693238905", "pc": 54.9, "e": 7}, {"v": "M", "ean": "7899693238882", "pc": 54.9, "e": 4}, {"v": "XXG", "ean": "7899693238912", "pc": 54.9, "e": 4}, {"v": "G", "ean": "7899693238899", "pc": 54.9, "e": 4}]},
    {"n": "Fralda Huggies Maxima Protecao Hiperzinha", "f": "KIMBERLY -CLARK BRASIL INDUSTRIA E COMER", "de": 99, "pc": 79.9, "e": 19, "c": "Fraldas", "vs": [{"v": "XXG", "ean": "7896007552849", "pc": 79.9, "e": 8}, {"v": "M", "ean": "7896007552788", "pc": 79.9, "e": 5}, {"v": "G", "ean": "7896007552801", "pc": 79.9, "e": 6}]},
    {"n": "Fralda Mili Baby Giga", "f": "MILI S.A", "de": 75.88, "pc": 64.9, "e": 35, "c": "Fraldas", "vs": [{"v": "G", "ean": "7896104992159", "pc": 64.9, "e": 9}, {"v": "M", "ean": "7896104992166", "pc": 64.9, "e": 2}, {"v": "XG", "ean": "7896104992142", "pc": 64.9, "e": 9}, {"v": "XXG", "ean": "7896104992135", "pc": 64.9, "e": 15}]},
    {"n": "SAB LIQ GRANADO BEBE TRADICIONAL 250ML RB", "f": "GRANADO", "de": 33.8, "pc": 24.99, "e": 6, "c": "Higiene & Banho", "ean": "7896512904621", "jornal":1},
    {"n": "CREATINA HARDCORE 300G JORNAL RB", "f": "INTEGRAL MEDICA", "de": 89.9, "pc": 54.9, "e": 1, "c": "Vitaminas & Nutricao", "ean": "7896311708314", "jornal":1},
    {"n": "MAG PLUS 6 60CAPS RB", "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "de": 59.95, "pc": 50.89, "e": 2, "c": "Vitaminas & Nutricao", "ean": "7898303264594", "jornal":1},
    {"n": "COBALAMAX SB FRUTAS VERMELHAS 60CPR MAST RB", "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "de": 44.99, "pc": 35.9, "e": 1, "c": "Vitaminas & Nutricao", "ean": "7898303265225", "jornal":1}
]


FOTOS_LOCAIS = {
 "22002": "/estaticas/produto-22002.png",
 "42360414": "/estaticas/produto-42360414.png",
 "75076818": "/estaticas/produto-75076818.png",
 "75076825": "/estaticas/produto-75076825.png",
 "75076870": "/estaticas/produto-75076870.png",
 "70330734425": "/estaticas/produto-70330734425.png",
 "79400526359": "/estaticas/produto-79400526359.png",
 "70341368879": "/estaticas/produto-70341368879.png",
 "76660008625": "/estaticas/produto-76660008625.png",
 "40141779038": "/estaticas/produto-40141779038.jpg",
 "40141781529": "/estaticas/produto-40141781529.jpg",
 "40141779014": "/estaticas/produto-40141779014.jpg"
}

CATALOGO = [
 {
  "n": "ABS P/SEIOS AMAMENTE C/12 UNID",
  "f": "",
  "de": 16.99,
  "pc": 15.29,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7897211100130"
 },
 {
  "n": "ASPIRADOR NASAL DE SUCCAO C/ESTOJO BUBA",
  "f": "",
  "de": 42.35,
  "pc": 38.1,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7908103718590"
 },
 {
  "n": "BICO MAM.LILLO SUPER RED.LATEX C/1 REF.9497",
  "f": "",
  "de": 35.33,
  "pc": 31.8,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7896033294973"
 },
 {
  "n": "BUBA BOWL EM SILICONE 350ML",
  "f": "",
  "de": 61.2,
  "pc": 54.9,
  "e": 6,
  "c": "Bebe & Infantil",
  "ean": "7908103756349"
 },
 {
  "n": "BUBA KIT ESCOVA MAMADEIRA E BICO AZUL",
  "f": "",
  "de": 30.4,
  "pc": 0,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7899525654149"
 },
 {
  "n": "BUBA KIT TALHER EM SILICONE E BAMBU",
  "f": "",
  "de": 54.4,
  "pc": 48.9,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7908103758275"
 },
 {
  "n": "BUBA PRATINHO EM SILICONE",
  "f": "",
  "de": 61.2,
  "pc": 54.9,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7908103756318"
 },
 {
  "n": "CHUP.AVENT SOOTHIE 4 A 6 MESES AZUL C/2 (AVENT)",
  "f": "",
  "de": 121.45,
  "pc": 109.3,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "8710103962342"
 },
 {
  "n": "ENSURE BAUNILHA 850G",
  "f": "",
  "de": 271.7,
  "pc": 239.9,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7891158105203"
 },
 {
  "n": "KIT BANHO BABY MURIEL ROSA MENINA",
  "f": "",
  "de": 39.99,
  "pc": 35.99,
  "e": 6,
  "c": "Bebe & Infantil",
  "ean": "7896279113502"
 },
 {
  "n": "KIT ESCOVA PARA MAMADEIRA BRANCO E ROSA",
  "f": "",
  "de": 25.5,
  "pc": 0,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7899525654156"
 },
 {
  "n": "LEITE APTANUTRI SOJA  3 800G",
  "f": "",
  "de": 151.85,
  "pc": 128.4,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7795323776116"
 },
 {
  "n": "LEITE NAN COMFOR 1 800G",
  "f": "",
  "de": 91.79,
  "pc": 80.9,
  "e": 5,
  "c": "Bebe & Infantil",
  "ean": "7891000071625"
 },
 {
  "n": "LEITE NAN S/LACTOSE 400G",
  "f": "",
  "de": 112.25,
  "pc": 93.1,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7613034909480"
 },
 {
  "n": "LEITE NAN SENSITIVE 800G",
  "f": "",
  "de": 165,
  "pc": 147.49,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7613036671927"
 },
 {
  "n": "LEITE NAN SUPREME 1 800G",
  "f": "",
  "de": 156.69,
  "pc": 128.9,
  "e": 2,
  "c": "Bebe & Infantil",
  "ean": "7613034968364"
 },
 {
  "n": "LEITE NANLAC COMFOR 1A3 800G",
  "f": "",
  "de": 93.99,
  "pc": 81.5,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7891000097649"
 },
 {
  "n": "LEITE NESTOGENO 1 800G",
  "f": "",
  "de": 72.8,
  "pc": 65.5,
  "e": 2,
  "c": "Bebe & Infantil",
  "ean": "7891000062722"
 },
 {
  "n": "LEITE NESTOGENO 2 800G",
  "f": "",
  "de": 77,
  "pc": 67.8,
  "e": 6,
  "c": "Bebe & Infantil",
  "ean": "7891000062760"
 },
 {
  "n": "LEITE NESTONUTRI 1 A 3.800G",
  "f": "",
  "de": 72.6,
  "pc": 62.5,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7891000255544"
 },
 {
  "n": "LEITE NINHO FASES CRES PREBIO 3+800G LT.",
  "f": "",
  "de": 62.5,
  "pc": 55.8,
  "e": 13,
  "c": "Bebe & Infantil",
  "ean": "7891000282809"
 },
 {
  "n": "LEITE NINHO ZERO LACTOSE 380GR",
  "f": "",
  "de": 28.29,
  "pc": 24.3,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7891000109908"
 },
 {
  "n": "LENCO UMED.BEPANTOL BABY 96UN L96P80",
  "f": "",
  "de": 39,
  "pc": 34.9,
  "e": 6,
  "c": "Bebe & Infantil",
  "ean": "7891106915182"
 },
 {
  "n": "MALVATRIKIDS INFANTIL 4-7 ANOS 70G",
  "f": "",
  "de": 30.1,
  "pc": 26.99,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7896026170390"
 },
 {
  "n": "MAM.AVENT PETALA BICO RITMO INDIVIDUAL 125ML",
  "f": "",
  "de": 121.45,
  "pc": 109.3,
  "e": 2,
  "c": "Bebe & Infantil",
  "ean": "8720689007344"
 },
 {
  "n": "NUTREN SENIOR PO BAUNILHA 370G",
  "f": "",
  "de": 112.8,
  "pc": 79.95,
  "e": 2,
  "c": "Bebe & Infantil",
  "ean": "7891000241547"
 },
 {
  "n": "NUTREN SENIOR PO CAFE C/LEITE 740G",
  "f": "",
  "de": 187.3,
  "pc": 168.5,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7891000287699"
 },
 {
  "n": "NUTREN SENIOR PO S/SABOR 740G",
  "f": "",
  "de": 187.3,
  "pc": 168.5,
  "e": 2,
  "c": "Bebe & Infantil",
  "ean": "7891000103487"
 },
 {
  "n": "SAB.LIQ.GRANADO BEBE GLICERINA 250ML JORNAL",
  "f": "",
  "de": 33.8,
  "pc": 24.99,
  "e": 5,
  "c": "Bebe & Infantil",
  "ean": "7896512904621"
 },
 {
  "n": "SH.DOVE BABY 200ML",
  "f": "",
  "de": 25.15,
  "pc": 22.6,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7891150025929"
 },
 {
  "n": "SH.J&J BABY 2 EM 1 400ML",
  "f": "",
  "de": 45.1,
  "pc": 40.59,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7891010257101"
 },
 {
  "n": "SH.J&J BABY REGULAR 400ML",
  "f": "",
  "de": 40.9,
  "pc": 36.8,
  "e": 4,
  "c": "Bebe & Infantil",
  "ean": "7891010800048"
 },
 {
  "n": "SUSTAGEN KIDS BAUNILHA 380G",
  "f": "",
  "de": 41.9,
  "pc": 37.5,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7898941911058"
 },
 {
  "n": "SUSTAGEN KIDS MORANGO 380G",
  "f": "",
  "de": 41.9,
  "pc": 37.5,
  "e": 5,
  "c": "Bebe & Infantil",
  "ean": "7898941911072"
 },
 {
  "n": "TALCO INF.J&J BABY REG. 100G",
  "f": "",
  "de": 34.2,
  "pc": 30.5,
  "e": 3,
  "c": "Bebe & Infantil",
  "ean": "7702031244646"
 },
 {
  "n": "AP.BARB.BIC SOLEIL COLOR L4P3",
  "f": "",
  "de": 25.2,
  "pc": 22.6,
  "e": 3,
  "c": "Cabelos",
  "ean": "70330734425"
 },
 {
  "n": "COND.BEMME ANTICASPA 300ML",
  "f": "",
  "de": 29.9,
  "pc": 29.9,
  "e": 2,
  "c": "Cabelos",
  "ean": "7897799835448"
 },
 {
  "n": "COND.BEMME CACHOS 300ML",
  "f": "",
  "de": 31.9,
  "pc": 28.7,
  "e": 5,
  "c": "Cabelos",
  "ean": "7897799835356"
 },
 {
  "n": "COND.BEMME NUTRICAO 300ML",
  "f": "",
  "de": 31.9,
  "pc": 28.7,
  "e": 2,
  "c": "Cabelos",
  "ean": "7897799835394"
 },
 {
  "n": "COND.BEMME RECONSTRUCAO 300ML",
  "f": "",
  "de": 31.9,
  "pc": 28.7,
  "e": 11,
  "c": "Cabelos",
  "ean": "7897799835318"
 },
 {
  "n": "COND.ELSEVE CACHOS SELADOR 400ML",
  "f": "",
  "de": 47.95,
  "pc": 43,
  "e": 11,
  "c": "Cabelos",
  "ean": "7899706197588"
 },
 {
  "n": "COND.ELSEVE COLLAGEN LIFTER 400ML",
  "f": "",
  "de": 47.95,
  "pc": 43,
  "e": 5,
  "c": "Cabelos",
  "ean": "7908966527193"
 },
 {
  "n": "COND.ELSEVE LISO DOS SONHOS LIQUID HAIR 400ML",
  "f": "",
  "de": 47.95,
  "pc": 43,
  "e": 6,
  "c": "Cabelos",
  "ean": "7908785461609"
 },
 {
  "n": "COND.ELSEVE OL.EXTRAOR.NUTRICAO 400ML",
  "f": "",
  "de": 47.95,
  "pc": 43,
  "e": 5,
  "c": "Cabelos",
  "ean": "7898587774376"
 },
 {
  "n": "COND.MEU LISINHO KIDS S.LINE 300ML",
  "f": "",
  "de": 24.35,
  "pc": 21.9,
  "e": 4,
  "c": "Cabelos",
  "ean": "7898623956209"
 },
 {
  "n": "CR.NIELY GOLD QUERATINA 80G",
  "f": "",
  "de": 28.14,
  "pc": 25.33,
  "e": 3,
  "c": "Cabelos",
  "ean": "7908785464525"
 },
 {
  "n": "CR.TRAT.ELSEVE BOND REPAIR 200G",
  "f": "",
  "de": 79.5,
  "pc": 71.5,
  "e": 3,
  "c": "Cabelos",
  "ean": "7908615092959"
 },
 {
  "n": "CR.TRAT.ELSEVE COLLAGEN LIFTER 300G",
  "f": "",
  "de": 35,
  "pc": 31.5,
  "e": 7,
  "c": "Cabelos",
  "ean": "7908966528367"
 },
 {
  "n": "GIZ COLORIR CABELO IMPALA STITCH ANGEL AZUL 7,3G",
  "f": "",
  "de": 38.18,
  "pc": 34.35,
  "e": 4,
  "c": "Cabelos",
  "ean": "7896111903155"
 },
 {
  "n": "KIT SEDA SH+COND.LUMINOUS UV JORNAL",
  "f": "",
  "de": 24.9,
  "pc": 17.99,
  "e": 5,
  "c": "Cabelos",
  "ean": "7891150099982"
 },
 {
  "n": "KIT TIONACHO SH+COND. ANTIQU/ENGR 415ML+200ML",
  "f": "",
  "de": 65.1,
  "pc": 58.59,
  "e": 5,
  "c": "Cabelos",
  "ean": "7898636191581"
 },
 {
  "n": "KNUT SH.K-FORCE 250ML",
  "f": "",
  "de": 66.2,
  "pc": 59.9,
  "e": 6,
  "c": "Cabelos",
  "ean": "7898483150601"
 },
 {
  "n": "LEAVE IN BEMME CACHOS 250ML",
  "f": "",
  "de": 33.3,
  "pc": 29.9,
  "e": 5,
  "c": "Cabelos",
  "ean": "7897799835363"
 },
 {
  "n": "LEAVE IN BEMME RECONSTRUCAO 250ML",
  "f": "",
  "de": 33.3,
  "pc": 29.9,
  "e": 2,
  "c": "Cabelos",
  "ean": "7897799835325"
 },
 {
  "n": "MASC.BEMME CACHOS 250ML",
  "f": "",
  "de": 33.3,
  "pc": 29.9,
  "e": 3,
  "c": "Cabelos",
  "ean": "7897799835370"
 },
 {
  "n": "MASC.BEMME NUTRICAO 250ML",
  "f": "",
  "de": 33.3,
  "pc": 29.9,
  "e": 11,
  "c": "Cabelos",
  "ean": "7897799835400"
 },
 {
  "n": "MASC.BEMME RECONSTRUCAO 250ML",
  "f": "",
  "de": 33.3,
  "pc": 29.9,
  "e": 2,
  "c": "Cabelos",
  "ean": "7897799835332"
 },
 {
  "n": "OLEO ELSEVE EXTRAORDINARIO 100ML",
  "f": "",
  "de": 47,
  "pc": 42.3,
  "e": 29,
  "c": "Cabelos",
  "ean": "7899026478909"
 },
 {
  "n": "SERUM ELSEVE COLLAGEN LIFTER 100ML",
  "f": "",
  "de": 61,
  "pc": 54.9,
  "e": 4,
  "c": "Cabelos",
  "ean": "7908966529333"
 },
 {
  "n": "SERUM ELSEVE LISO DOS SONHOS 100ML",
  "f": "",
  "de": 45.79,
  "pc": 41.2,
  "e": 5,
  "c": "Cabelos",
  "ean": "7908785461555"
 },
 {
  "n": "SH.BEMME ANTICASPA 300ML",
  "f": "",
  "de": 29.9,
  "pc": 29.9,
  "e": 2,
  "c": "Cabelos",
  "ean": "7897799835431"
 },
 {
  "n": "SH.BEMME ANTIQUEDA 300ML",
  "f": "",
  "de": 31.5,
  "pc": 28.3,
  "e": 2,
  "c": "Cabelos",
  "ean": "7897799835455"
 },
 {
  "n": "SH.BEMME CACHOS 300ML",
  "f": "",
  "de": 31.5,
  "pc": 28.3,
  "e": 2,
  "c": "Cabelos",
  "ean": "7897799835349"
 },
 {
  "n": "SH.BEMME NUTRICAO 300ML",
  "f": "",
  "de": 31.5,
  "pc": 28.3,
  "e": 11,
  "c": "Cabelos",
  "ean": "7897799835387"
 },
 {
  "n": "SH.BEMME RECONSTRUCAO 300ML",
  "f": "",
  "de": 31.5,
  "pc": 28.3,
  "e": 11,
  "c": "Cabelos",
  "ean": "7897799835301"
 },
 {
  "n": "SH.PANTENE MOLECULAR 510ML",
  "f": "",
  "de": 54.2,
  "pc": 48.7,
  "e": 3,
  "c": "Cabelos",
  "ean": "7500435260312"
 },
 {
  "n": "SPRAY KARINA EXTRA FORTE 400ML",
  "f": "",
  "de": 41,
  "pc": 36.9,
  "e": 4,
  "c": "Cabelos",
  "ean": "7893300521169"
 },
 {
  "n": "SPRAY KARINA NORMAL 400ML",
  "f": "",
  "de": 41,
  "pc": 36.9,
  "e": 3,
  "c": "Cabelos",
  "ean": "7893300521084"
 },
 {
  "n": "TINT.IMEDIA 1 PRETO",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 3,
  "c": "Cabelos",
  "ean": "7896014140435"
 },
 {
  "n": "TINT.IMEDIA 3 CAST.ESC",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 16,
  "c": "Cabelos",
  "ean": "7896014140442"
 },
 {
  "n": "TINT.IMEDIA 4 CASTANHO NATURAL",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 7,
  "c": "Cabelos",
  "ean": "7896014140459"
 },
 {
  "n": "TINT.IMEDIA 5 CAST.CLARO",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 3,
  "c": "Cabelos",
  "ean": "7896014140480"
 },
 {
  "n": "TINT.IMEDIA 6 LOURO ESCURO",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 8,
  "c": "Cabelos",
  "ean": "7896014140527"
 },
 {
  "n": "TINT.IMEDIA 6.1 LOU.ESC.ACINZ",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 3,
  "c": "Cabelos",
  "ean": "7896014140534"
 },
 {
  "n": "TINT.IMEDIA 6.41 MARRON",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 3,
  "c": "Cabelos",
  "ean": "7896014140558"
 },
 {
  "n": "TINT.IMEDIA 8 LOURO",
  "f": "",
  "de": 43.6,
  "pc": 39.2,
  "e": 4,
  "c": "Cabelos",
  "ean": "7896014140633"
 },
 {
  "n": "ABELHA RAINHA OLEO ROSA MOSQUETA PURO 20ML",
  "f": "",
  "de": 46.4,
  "pc": 41.75,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7898728324996"
 },
 {
  "n": "ASEPXIA SAB.DETOX 80G",
  "f": "",
  "de": 22.09,
  "pc": 19.88,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7898636190874"
 },
 {
  "n": "CICAPLAST BAUME B5 40ML",
  "f": "",
  "de": 103,
  "pc": 91.9,
  "e": 5,
  "c": "Dermocosmeticos",
  "ean": "7908615000244"
 },
 {
  "n": "CR.HID.CERAVE 200G",
  "f": "",
  "de": 101.8,
  "pc": 91.6,
  "e": 4,
  "c": "Dermocosmeticos",
  "ean": "7899706159173"
 },
 {
  "n": "CR.HID.CERAVE 340G",
  "f": "",
  "de": 94.75,
  "pc": 85.2,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7908615086309"
 },
 {
  "n": "CR.HID.NIVEA 145G",
  "f": "",
  "de": 48,
  "pc": 42.9,
  "e": 5,
  "c": "Dermocosmeticos",
  "ean": "4005900408891"
 },
 {
  "n": "CR.HID.NIVEA FAC.ANTISSINAIS 100G",
  "f": "",
  "de": 30.9,
  "pc": 29.9,
  "e": 6,
  "c": "Dermocosmeticos",
  "ean": "42360414"
 },
 {
  "n": "CR.HID.NIVEA VISAGE Q10 PLUS NOT.50G.",
  "f": "",
  "de": 52.2,
  "pc": 46.9,
  "e": 2,
  "c": "Dermocosmeticos",
  "ean": "4005808812899"
 },
 {
  "n": "CR.NIVEA LUMINOUS FLUIDO FPS50 30ML",
  "f": "",
  "de": 117.9,
  "pc": 105.9,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "4005900813046"
 },
 {
  "n": "DEPIL.NEORLY CR.P/ CORPO SENSE DELICADA 120GR.",
  "f": "",
  "de": 39.4,
  "pc": 35.4,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7898302722507"
 },
 {
  "n": "DES.DOVE AERO ORIGINAL 150ML(JORNAL)",
  "f": "",
  "de": 20,
  "pc": 15.89,
  "e": 166,
  "c": "Dermocosmeticos",
  "ean": "7506306241183"
 },
 {
  "n": "DES.DOVE SERUM F.STICK TROPICAL HIBISCUS 45G",
  "f": "",
  "de": 38.8,
  "pc": 34.9,
  "e": 4,
  "c": "Dermocosmeticos",
  "ean": "79400526359"
 },
 {
  "n": "EPISOL COLOR  SMART FPS50 40ML",
  "f": "",
  "de": 93.6,
  "pc": 83.5,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7891142205735"
 },
 {
  "n": "EPISOL COLOR TOM2 CLARO FPS70 40ML",
  "f": "",
  "de": 94.85,
  "pc": 84.99,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7891142205643"
 },
 {
  "n": "EPISOL COLOR TOM3 MEDIO FPS70 40ML",
  "f": "",
  "de": 94.85,
  "pc": 84.99,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7891142205704"
 },
 {
  "n": "EPISOL INTENSE FPS60 200ML",
  "f": "",
  "de": 126.39,
  "pc": 108.9,
  "e": 6,
  "c": "Dermocosmeticos",
  "ean": "7891142205131"
 },
 {
  "n": "EPISOL SEC ACQUA FPS60 40ML",
  "f": "",
  "de": 107.45,
  "pc": 96.7,
  "e": 1,
  "c": "Dermocosmeticos",
  "ean": "7891142984203"
 },
 {
  "n": "EPISOL SEC OC FPS60 CLARO 60G",
  "f": "",
  "de": 103.79,
  "pc": 92.5,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7891142207166"
 },
 {
  "n": "FUTURA BIOTECH ANTIT.DERM ONE ROLLON 65ML",
  "f": "",
  "de": 58.99,
  "pc": 52.8,
  "e": 16,
  "c": "Dermocosmeticos",
  "ean": "7898901366621"
 },
 {
  "n": "LOC.HID.NIVEA BODY MILK 200Ml",
  "f": "",
  "de": 17.5,
  "pc": 15.75,
  "e": 25,
  "c": "Dermocosmeticos",
  "ean": "4005808309436"
 },
 {
  "n": "LOC.HID.NIVEA BODY Q10 FIRMADOR 200ML",
  "f": "",
  "de": 39.85,
  "pc": 35.8,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "4005808311286"
 },
 {
  "n": "LOC.HID.NIVEA BODY Q10 FIRMADOR 400ML",
  "f": "",
  "de": 57.4,
  "pc": 51.5,
  "e": 4,
  "c": "Dermocosmeticos",
  "ean": "4005900116192"
 },
 {
  "n": "LOC.HID.NIVEA BODY SOFT MILK 400ML",
  "f": "",
  "de": 32.2,
  "pc": 24.9,
  "e": 7,
  "c": "Dermocosmeticos",
  "ean": "4005900004956"
 },
 {
  "n": "LOC.HID.VASENOL GELEIA VASELINA 100ML",
  "f": "",
  "de": 36.7,
  "pc": 32.9,
  "e": 7,
  "c": "Dermocosmeticos",
  "ean": "7891150029323"
 },
 {
  "n": "MANITOL 20% 250ML",
  "f": "",
  "de": 22.3,
  "pc": 19.99,
  "e": 8,
  "c": "Dermocosmeticos",
  "ean": "7896137607730"
 },
 {
  "n": "NUTRIOL LOC.ANTICOCEIRA 390ML",
  "f": "",
  "de": 140.4,
  "pc": 125.9,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "3282770388497"
 },
 {
  "n": "OLEO E SERUM DOVE UV REPAIR E GLOW+FERULICO 110ML",
  "f": "",
  "de": 47.1,
  "pc": 29.9,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7891150102798"
 },
 {
  "n": "P.SOLAR ANASOL OIL FREE E TOQUE SECO FPS75 200G",
  "f": "",
  "de": 50.8,
  "pc": 45.7,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7897230305165"
 },
 {
  "n": "P.SOLAR EXP FAC.ANTIRRUGAS COR FPS60 40G",
  "f": "",
  "de": 60.5,
  "pc": 54.45,
  "e": 4,
  "c": "Dermocosmeticos",
  "ean": "7899706184960"
 },
 {
  "n": "P.SOLAR NIVEA  FACIAL FPS70 40ML",
  "f": "",
  "de": 49.5,
  "pc": 39.99,
  "e": 4,
  "c": "Dermocosmeticos",
  "ean": "4005900980397"
 },
 {
  "n": "P.SOLAR NIVEA SUN FPS30 200ML",
  "f": "",
  "de": 63,
  "pc": 56.7,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "4005808555307"
 },
 {
  "n": "PRINCIPIA 10% UREIA+5% GLICERINA+5% OL DE SEMENTE",
  "f": "",
  "de": 74.79,
  "pc": 67.3,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "70341368879"
 },
 {
  "n": "PRINCIPIA CREME CALMANTE MULTIREPARADOR 17,5%",
  "f": "",
  "de": 54.6,
  "pc": 49,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "0609963220670"
 },
 {
  "n": "PRINCIPIA GEL DE LIMPEZA 350G GL-01 JORNAL",
  "f": "",
  "de": 57.6,
  "pc": 54,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "0609963220564"
 },
 {
  "n": "REPEL.OFF ACTIVE SPRAY 170ML",
  "f": "",
  "de": 43.69,
  "pc": 39.3,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7894650009598"
 },
 {
  "n": "SAB.LIQ.DOVE ANTIBACTERIANO CUIDA PROTEGE 250ML",
  "f": "",
  "de": 23.4,
  "pc": 20.99,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7891150075405"
 },
 {
  "n": "SAB.LIQ.GRANADO GLICERINA TRADICIONAL 300ML",
  "f": "",
  "de": 33.65,
  "pc": 29.99,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7896512939593"
 },
 {
  "n": "SAB.LIQ.J&J BABY CABECA/PES GLICERINA 180ML REFIL",
  "f": "",
  "de": 23,
  "pc": 20.7,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7891010871031"
 },
 {
  "n": "SAB.LIQ.OLEO MURIEL ARABE 230ML",
  "f": "",
  "de": 20.4,
  "pc": 18.3,
  "e": 3,
  "c": "Dermocosmeticos",
  "ean": "7896279129299"
 },
 {
  "n": "SAB.LUX BUQUE DE JASMIN 85G",
  "f": "",
  "de": 3.99,
  "pc": 2.39,
  "e": 2,
  "c": "Dermocosmeticos",
  "ean": "7891150059849"
 },
 {
  "n": "ABS.BIGFRAL REGULAR 20UN",
  "f": "",
  "de": 27.7,
  "pc": 24.9,
  "e": 6,
  "c": "Fraldas",
  "ean": "7896012880531"
 },
 {
  "n": "FR.BEBE FOFINHO PLUS P C/96UN JORNAL",
  "f": "",
  "de": 58.9,
  "pc": 47.9,
  "e": 3,
  "c": "Fraldas",
  "ean": "7898972620165"
 },
 {
  "n": "FR.BEBE FOFINHO PREMIUM JUMBO XG C/56UN JORNAL",
  "f": "",
  "de": 68.4,
  "pc": 54.9,
  "e": 7,
  "c": "Fraldas",
  "ean": "7899693238905"
 },
 {
  "n": "FR.BIGFRAL DERMA PLUS SEVERA G C/16UN",
  "f": "",
  "de": 71,
  "pc": 63.9,
  "e": 9,
  "c": "Fraldas",
  "ean": "7896012880210"
 },
 {
  "n": "FR.HIPOPO BABY HIPER G C/74",
  "f": "",
  "de": 64.99,
  "pc": 49.9,
  "e": 18,
  "c": "Fraldas",
  "ean": "7899700800194"
 },
 {
  "n": "FR.HIPOPO BABY HIPER XG 64UN",
  "f": "",
  "de": 64.99,
  "pc": 49.9,
  "e": 11,
  "c": "Fraldas",
  "ean": "7899700802594"
 },
 {
  "n": "FR.HUGGIES SUP M HIPZINHA 3X66 JORNAL",
  "f": "",
  "de": 99,
  "pc": 79.9,
  "e": 5,
  "c": "Fraldas",
  "ean": "7896007552788"
 },
 {
  "n": "FR.HUGGIES SUPREME CARE G HIPZI 3X58 JORNAL",
  "f": "",
  "de": 99,
  "pc": 79.9,
  "e": 9,
  "c": "Fraldas",
  "ean": "7896007552801"
 },
 {
  "n": "FR.HUGGIES SUPREME CARE MEGA G C/32(VERMELHO)",
  "f": "",
  "de": 71,
  "pc": 60.69,
  "e": 4,
  "c": "Fraldas",
  "ean": "7896007548415"
 },
 {
  "n": "FR.HUGGIES SUPREME CARE XXG HIPZI 3X54 JORNAL",
  "f": "",
  "de": 99,
  "pc": 79.9,
  "e": 16,
  "c": "Fraldas",
  "ean": "7896007552849"
 },
 {
  "n": "FR.MAMYPOKO CALCA DIA&NOITE AMARELA G C/30",
  "f": "",
  "de": 84,
  "pc": 75.6,
  "e": 6,
  "c": "Fraldas",
  "ean": "7898656390216"
 },
 {
  "n": "FR.MILI BABY GIGA G C/72UN JORNAL",
  "f": "",
  "de": 75.88,
  "pc": 64.9,
  "e": 8,
  "c": "Fraldas",
  "ean": "7896104992159"
 },
 {
  "n": "FR.PAMPERS PANTS MEGA  AJUSTE TOTAL XXG 20UN",
  "f": "",
  "de": 81.9,
  "pc": 73.7,
  "e": 4,
  "c": "Fraldas",
  "ean": "7500435260838"
 },
 {
  "n": "FR.PAMPERS PREMIUM CARE MEGA M C/80UN",
  "f": "",
  "de": 188,
  "pc": 167.49,
  "e": 4,
  "c": "Fraldas",
  "ean": "7500435132435"
 },
 {
  "n": "FR.PAMPERS PREMIUM CARE RN C/36",
  "f": "",
  "de": 83.9,
  "pc": 75.5,
  "e": 4,
  "c": "Fraldas",
  "ean": "7500435132534"
 },
 {
  "n": "FR.PAMPERS SUPERSEQUINHA SUPER G 60UN",
  "f": "",
  "de": 109.99,
  "pc": 98.99,
  "e": 3,
  "c": "Fraldas",
  "ean": "7500435250207"
 },
 {
  "n": "FR.PAMPERS T.CONF. FORTEBAG G/60UN",
  "f": "",
  "de": 122,
  "pc": 108.9,
  "e": 6,
  "c": "Fraldas",
  "ean": "7500435106672"
 },
 {
  "n": "FR.PLENITUD ACTIVE PLUS UNISEX G/XG 16UND JORNAL",
  "f": "",
  "de": 98.25,
  "pc": 64.9,
  "e": 7,
  "c": "Fraldas",
  "ean": "7896007547210"
 },
 {
  "n": "FR.PLENITUD CLASSIC INTENSA UNISEX G/X 16UND",
  "f": "",
  "de": 72.19,
  "pc": 64.9,
  "e": 3,
  "c": "Fraldas",
  "ean": "7896007552986"
 },
 {
  "n": "FR.PLENITUD PLU P-M L24P22",
  "f": "",
  "de": 111.55,
  "pc": 99.9,
  "e": 3,
  "c": "Fraldas",
  "ean": "7896007549993"
 },
 {
  "n": "FR.POMPOM PROTEK HIPER G C/68",
  "f": "",
  "de": 83.8,
  "pc": 75.4,
  "e": 8,
  "c": "Fraldas",
  "ean": "7896012878491"
 },
 {
  "n": "FR.TENA PANTS DERMACARE G/EG C/24UN",
  "f": "",
  "de": 133.45,
  "pc": 110.49,
  "e": 2,
  "c": "Fraldas",
  "ean": "7896770981808"
 },
 {
  "n": "FR.TENA PANTS DERMACARE G/EG L16P14",
  "f": "",
  "de": 73.6,
  "pc": 65.9,
  "e": 7,
  "c": "Fraldas",
  "ean": "7896770982867"
 },
 {
  "n": "FR.TENA PANTS DERMACARE G/EG L24P21",
  "f": "",
  "de": 96,
  "pc": 85.9,
  "e": 3,
  "c": "Fraldas",
  "ean": "7896770983635"
 },
 {
  "n": "FR.TENA PANTS DERMACARE P/M L16P14",
  "f": "",
  "de": 73.6,
  "pc": 65.9,
  "e": 14,
  "c": "Fraldas",
  "ean": "7896770982850"
 },
 {
  "n": "FR.TENA PANTS MEN G/XG C/16",
  "f": "",
  "de": 79.6,
  "pc": 71.4,
  "e": 9,
  "c": "Fraldas",
  "ean": "7896770982201"
 },
 {
  "n": "FR.TENA PANTS NOTURNA G/EG L16P14",
  "f": "",
  "de": 81.79,
  "pc": 72.9,
  "e": 13,
  "c": "Fraldas",
  "ean": "7896770908867"
 },
 {
  "n": "FR.TENA SLIP NOTURNA  EG LV16PG14",
  "f": "",
  "de": 78,
  "pc": 69.9,
  "e": 5,
  "c": "Fraldas",
  "ean": "7896770983611"
 },
 {
  "n": "SAB.LIQ.DOVE OLEO DE BANHO GLICERINADO 240ML JORNAL",
  "f": "",
  "de": 39.1,
  "pc": 35.19,
  "e": 3,
  "c": "Higiene & Banho",
  "ean": "7891150098442"
 },
 {
  "n": "COREGA ULTRA CR.S/SABOR 40G",
  "f": "",
  "de": 86.3,
  "pc": 71.9,
  "e": 4,
  "c": "Higiene Bucal",
  "ean": "7896009490651"
 },
 {
  "n": "COREGA ULTRA CREME SEM SABOR 8,5G",
  "f": "",
  "de": 24.4,
  "pc": 19.9,
  "e": 3,
  "c": "Higiene Bucal",
  "ean": "7896015591007"
 },
 {
  "n": "COREGA ULTRA TRIPLA  ACAO 70G",
  "f": "",
  "de": 93.9,
  "pc": 84.3,
  "e": 3,
  "c": "Higiene Bucal",
  "ean": "7896009498787"
 },
 {
  "n": "CR.D.COLG.SENSITIVE PRO ALIVIO IMEDIATO 60G",
  "f": "",
  "de": 21.5,
  "pc": 19.35,
  "e": 5,
  "c": "Higiene Bucal",
  "ean": "7509546653396"
 },
 {
  "n": "CR.D.COLG.SENSITIVE PRO ALIVIO IMEDIATO ORIG 140G",
  "f": "",
  "de": 31,
  "pc": 27.9,
  "e": 3,
  "c": "Higiene Bucal",
  "ean": "7509546653402"
 },
 {
  "n": "CR.D.COLGATE TOTAL LIMPEZA PROFUNDA INTERDENTAL 90G",
  "f": "",
  "de": 19.6,
  "pc": 17.5,
  "e": 4,
  "c": "Higiene Bucal",
  "ean": "7509546704067"
 },
 {
  "n": "CR.D.SENSODYNE ORIGINAL 90G",
  "f": "",
  "de": 20.5,
  "pc": 18.45,
  "e": 6,
  "c": "Higiene Bucal",
  "ean": "7896009419324"
 },
 {
  "n": "FIO D.J&J ESSENCIAL 100MT JORNAL",
  "f": "",
  "de": 23.8,
  "pc": 21.4,
  "e": 17,
  "c": "Higiene Bucal",
  "ean": "7891010501105"
 },
 {
  "n": "FIO D.J&J EXP.PLUS 50MTS",
  "f": "",
  "de": 23.4,
  "pc": 20.99,
  "e": 5,
  "c": "Higiene Bucal",
  "ean": "7891010038892"
 },
 {
  "n": "FIXODENT ORIG.21G",
  "f": "",
  "de": 55.2,
  "pc": 41.9,
  "e": 5,
  "c": "Higiene Bucal",
  "ean": "76660008625"
 },
 {
  "n": "KIT ENX.BUCAL ZERO ALCOOL MENTA 500ML+250ML BEMME",
  "f": "",
  "de": 28.8,
  "pc": 23.95,
  "e": 4,
  "c": "Higiene Bucal",
  "ean": "7908324802511"
 },
 {
  "n": "LISTERINE MELANCIA E HORTELA 500ML JORNAL",
  "f": "",
  "de": 28.99,
  "pc": 25.9,
  "e": 3,
  "c": "Higiene Bucal",
  "ean": "7891010256050"
 },
 {
  "n": "LISTERINE PRO GENGIVA EXPERT 250ML",
  "f": "",
  "de": 44.5,
  "pc": 38.5,
  "e": 7,
  "c": "Higiene Bucal",
  "ean": "7891010256883"
 },
 {
  "n": "LISTERINE TARTAR CONTROL 500ML",
  "f": "",
  "de": 44.1,
  "pc": 39.6,
  "e": 4,
  "c": "Higiene Bucal",
  "ean": "7891010256791"
 },
 {
  "n": "PASTA D AGUA (PASTOL)100G",
  "f": "",
  "de": 21,
  "pc": 18.8,
  "e": 15,
  "c": "Higiene Bucal",
  "ean": "7897780209159"
 },
 {
  "n": "PERIODENT DENTRAT 250ML",
  "f": "",
  "de": 20,
  "pc": 17.9,
  "e": 3,
  "c": "Higiene Bucal",
  "ean": "7898395843370"
 },
 {
  "n": "PERIODENT DENTRAT ZERO 250ML",
  "f": "",
  "de": 22.3,
  "pc": 19.9,
  "e": 6,
  "c": "Higiene Bucal",
  "ean": "7898395843394"
 },
 {
  "n": "PERIOGARD 250ML COLG.S/ALCOOL",
  "f": "",
  "de": 41.7,
  "pc": 37.4,
  "e": 6,
  "c": "Higiene Bucal",
  "ean": "7891024179925"
 },
 {
  "n": "PERIOGARD ENX.BUC.S/ALC.EXTRA MINT 250ML",
  "f": "",
  "de": 41.7,
  "pc": 37.4,
  "e": 10,
  "c": "Higiene Bucal",
  "ean": "7891024033425"
 },
 {
  "n": "ABS.ALWAYS NOTURNO SECA C/ABAS XXG C/10",
  "f": "",
  "de": 45.45,
  "pc": 40.9,
  "e": 6,
  "c": "Higiene Intima",
  "ean": "7506309805498"
 },
 {
  "n": "ABS.BIOFRAL MAXI GERIATRIC C/20",
  "f": "",
  "de": 32.7,
  "pc": 29.4,
  "e": 5,
  "c": "Higiene Intima",
  "ean": "7896770900038"
 },
 {
  "n": "ABS.CAREFREE NEUTRALIZE S/PERF.C/40",
  "f": "",
  "de": 24.2,
  "pc": 21.7,
  "e": 2,
  "c": "Higiene Intima",
  "ean": "7891010875596"
 },
 {
  "n": "ABS.DRY MAN MASC. C/10",
  "f": "",
  "de": 26.3,
  "pc": 23.59,
  "e": 4,
  "c": "Higiene Intima",
  "ean": "7894513142066"
 },
 {
  "n": "ABS.INTIMUS DAYS S/PERF. L80P70",
  "f": "",
  "de": 23.61,
  "pc": 21.22,
  "e": 3,
  "c": "Higiene Intima",
  "ean": "7896007546039"
 },
 {
  "n": "ABS.INTIMUS DAYS S/PERF.L40P30",
  "f": "",
  "de": 18.2,
  "pc": 16.3,
  "e": 4,
  "c": "Higiene Intima",
  "ean": "7896007542482"
 },
 {
  "n": "ABS.INTIMUS NOT SECA C/ABAS 30UN",
  "f": "",
  "de": 35.75,
  "pc": 23.9,
  "e": 3,
  "c": "Higiene Intima",
  "ean": "7896007550906"
 },
 {
  "n": "ABS.INTIMUS NOT SUAVE C/ABAS 30UN",
  "f": "",
  "de": 35.75,
  "pc": 23.9,
  "e": 12,
  "c": "Higiene Intima",
  "ean": "7896007550890"
 },
 {
  "n": "ABS.INTIMUS NOT.SUAVE C/ABAS 16UN",
  "f": "",
  "de": 23,
  "pc": 20.7,
  "e": 6,
  "c": "Higiene Intima",
  "ean": "7896007550883"
 },
 {
  "n": "ABS.MILI NOTURNO SUAVE C/ABAS 32UN",
  "f": "",
  "de": 29.8,
  "pc": 26.8,
  "e": 154,
  "c": "Higiene Intima",
  "ean": "7896104992777"
 },
 {
  "n": "ABS.OB INTERNO COMFORT MEDIO C/16",
  "f": "",
  "de": 29.99,
  "pc": 26.99,
  "e": 4,
  "c": "Higiene Intima",
  "ean": "7891010245085"
 },
 {
  "n": "ABS.S.L.ADAPT.PLUS SUAVE C/AB C/16",
  "f": "",
  "de": 19.3,
  "pc": 17.3,
  "e": 2,
  "c": "Higiene Intima",
  "ean": "7891010579616"
 },
 {
  "n": "ABS.S.L.ADAPT.PLUS SUAVE C/AB C/32",
  "f": "",
  "de": 31.5,
  "pc": 28.35,
  "e": 4,
  "c": "Higiene Intima",
  "ean": "7891010704780"
 },
 {
  "n": "ABS.S.L.SUAVE NOT C/ABAS LV 32 PG24",
  "f": "",
  "de": 47.3,
  "pc": 42.5,
  "e": 3,
  "c": "Higiene Intima",
  "ean": "7891010518844"
 },
 {
  "n": "AGUA COLONIA POMPOM 100ML",
  "f": "",
  "de": 22.2,
  "pc": 19.9,
  "e": 4,
  "c": "Perfumes & Desodorantes",
  "ean": "7896012800867"
 },
 {
  "n": "BARRA BANANA C/ AMENDOIM ZERO 25G BEMME",
  "f": "",
  "de": 6.5,
  "pc": 6.5,
  "e": 35,
  "c": "Perfumes & Desodorantes",
  "ean": "7898775460538"
 },
 {
  "n": "BARRA COCADA C/ABACAXI ZERO 25G BEMME",
  "f": "",
  "de": 6.5,
  "pc": 6.5,
  "e": 30,
  "c": "Perfumes & Desodorantes",
  "ean": "7898775460590"
 },
 {
  "n": "BARRA COCADA C/CHOCOLATE ZERO 25G BEMME",
  "f": "",
  "de": 7.99,
  "pc": 7.99,
  "e": 34,
  "c": "Perfumes & Desodorantes",
  "ean": "7898775460552"
 },
 {
  "n": "BARRA NUTS CRANBERRY ZERO 25G BEMME",
  "f": "",
  "de": 7.99,
  "pc": 7.99,
  "e": 35,
  "c": "Perfumes & Desodorantes",
  "ean": "7898775460576"
 },
 {
  "n": "BEMME GUMMIES SENIOR 50+ C/60 GOMAS SABOR MELANCIA",
  "f": "",
  "de": 100.2,
  "pc": 89.9,
  "e": 7,
  "c": "Perfumes & Desodorantes",
  "ean": "7896321041746"
 },
 {
  "n": "BEMME PERFUME IV VIP ROSE WOMAN 15ML",
  "f": "",
  "de": 44.8,
  "pc": 39.9,
  "e": 7,
  "c": "Perfumes & Desodorantes",
  "ean": "7899918942006"
 },
 {
  "n": "BODY SPLASH ESTY BELLA INVENCY 220ML BEMME",
  "f": "",
  "de": 57.4,
  "pc": 49.9,
  "e": 4,
  "c": "Perfumes & Desodorantes",
  "ean": "7899918943232"
 },
 {
  "n": "BODY SPLASH MAN NY IVENCY 220ML BEMME",
  "f": "",
  "de": 57.4,
  "pc": 49.9,
  "e": 9,
  "c": "Perfumes & Desodorantes",
  "ean": "7898976443432"
 },
 {
  "n": "BODY SPLASH SAVAGE IVENCY 220ML BEMME",
  "f": "",
  "de": 57.4,
  "pc": 49.9,
  "e": 8,
  "c": "Perfumes & Desodorantes",
  "ean": "7898976443449"
 },
 {
  "n": "DES.ABOVE AERO ZERO MEN 150ML",
  "f": "",
  "de": 18,
  "pc": 15.99,
  "e": 12,
  "c": "Perfumes & Desodorantes",
  "ean": "7899674030559"
 },
 {
  "n": "DES.DOVE CR.F.PREVINE ESCURECIMENTO 50ML",
  "f": "",
  "de": 25.5,
  "pc": 22.9,
  "e": 6,
  "c": "Perfumes & Desodorantes",
  "ean": "7891150096783"
 },
 {
  "n": "DES.DOVE CR.F.PREVINE IRRITACAO 50ML",
  "f": "",
  "de": 25.5,
  "pc": 22.9,
  "e": 4,
  "c": "Perfumes & Desodorantes",
  "ean": "7891150096790"
 },
 {
  "n": "DES.DOVE CR.F.REPARACAO DIARIA 50ML",
  "f": "",
  "de": 25.5,
  "pc": 22.9,
  "e": 3,
  "c": "Perfumes & Desodorantes",
  "ean": "7891150094741"
 },
 {
  "n": "DES.GIOVANNA BABY AERO S/ALUMINIO CLASSIC 150ML",
  "f": "",
  "de": 25.99,
  "pc": 23.39,
  "e": 3,
  "c": "Perfumes & Desodorantes",
  "ean": "7896044998723"
 },
 {
  "n": "DES.PIERRE CREME 50G",
  "f": "",
  "de": 31.3,
  "pc": 27.9,
  "e": 47,
  "c": "Perfumes & Desodorantes",
  "ean": "22002"
 },
 {
  "n": "DES.REX AERO F.ANTBACT.INVISIBLE 150ML",
  "f": "",
  "de": 19.7,
  "pc": 13.99,
  "e": 7,
  "c": "Perfumes & Desodorantes",
  "ean": "7506306244177"
 },
 {
  "n": "DES.REX CLINICAL CLASSIC 58GR",
  "f": "",
  "de": 36,
  "pc": 32.4,
  "e": 7,
  "c": "Perfumes & Desodorantes",
  "ean": "75076818"
 },
 {
  "n": "DES.REX CLINICAL CLEAN 58G",
  "f": "",
  "de": 36,
  "pc": 32.4,
  "e": 10,
  "c": "Perfumes & Desodorantes",
  "ean": "75076825"
 },
 {
  "n": "DES.REX.AERO F.POWDER DRY 250ML.",
  "f": "",
  "de": 28.5,
  "pc": 25.65,
  "e": 10,
  "c": "Perfumes & Desodorantes",
  "ean": "7891150081253"
 },
 {
  "n": "DES.REXONA CLINICAL EXTRA DRY 58G",
  "f": "",
  "de": 36,
  "pc": 32.4,
  "e": 9,
  "c": "Perfumes & Desodorantes",
  "ean": "75076870"
 },
 {
  "n": "KIT BEMME PERFUME INVENCY + BODY SPLASH",
  "f": "",
  "de": 109.9,
  "pc": 94.9,
  "e": 2,
  "c": "Perfumes & Desodorantes",
  "ean": "7898976443470"
 },
 {
  "n": "WAFER PROTEIN COOKIES CREAM ZERO 25G BEMME",
  "f": "",
  "de": 11.9,
  "pc": 11.9,
  "e": 37,
  "c": "Perfumes & Desodorantes",
  "ean": "7898775460583"
 },
 {
  "n": "AP.BARB.BIC FLEX3 EXTRA SUAVE C/2UNID",
  "f": "",
  "de": 23.5,
  "pc": 0,
  "e": 4,
  "c": "Preservativos & Barbear",
  "ean": "7501843503350"
 },
 {
  "n": "AP.BARB.GILLETTE MACH 3 REGULAR C/1",
  "f": "",
  "de": 44,
  "pc": 39.6,
  "e": 8,
  "c": "Preservativos & Barbear",
  "ean": "7702018001071"
 },
 {
  "n": "AP.BARB.GILLETTE PREST.3 ICE C/2",
  "f": "",
  "de": 26.5,
  "pc": 19.49,
  "e": 6,
  "c": "Preservativos & Barbear",
  "ean": "7702018983872"
 },
 {
  "n": "AP.BARB.GILLETTE PREST.CARVAO ATIVADO C/2 UND",
  "f": "",
  "de": 24.5,
  "pc": 21.9,
  "e": 3,
  "c": "Preservativos & Barbear",
  "ean": "7500435245821"
 },
 {
  "n": "AP.BARB.GILLETTE VENUS FEM.SIMPLY L4P3",
  "f": "",
  "de": 37.2,
  "pc": 33.4,
  "e": 4,
  "c": "Preservativos & Barbear",
  "ean": "7500435004220"
 },
 {
  "n": "AP.GILLETTE CORPO C/2UN",
  "f": "",
  "de": 24.7,
  "pc": 22.2,
  "e": 3,
  "c": "Preservativos & Barbear",
  "ean": "7500435178594"
 },
 {
  "n": "AP.PREST MASC ULTRAGRIP 3 PBC/2",
  "f": "",
  "de": 21.95,
  "pc": 19.75,
  "e": 8,
  "c": "Preservativos & Barbear",
  "ean": "7500435011297"
 },
 {
  "n": "AP.PREST.PROBAK LEVE 7 PAGUE 5",
  "f": "",
  "de": 17.9,
  "pc": 15.9,
  "e": 5,
  "c": "Preservativos & Barbear",
  "ean": "7891051040403"
 },
 {
  "n": "AP.VENUS SIMPLY ROSA C/2",
  "f": "",
  "de": 25.8,
  "pc": 23.2,
  "e": 3,
  "c": "Preservativos & Barbear",
  "ean": "7702018072392"
 },
 {
  "n": "CARGA GILLETTE MACH3 C/2",
  "f": "",
  "de": 20.5,
  "pc": 18.45,
  "e": 11,
  "c": "Preservativos & Barbear",
  "ean": "7500435179829"
 },
 {
  "n": "PRES.JONTEX LUBRIFICADO LV8 PG7",
  "f": "",
  "de": 27.3,
  "pc": 24.5,
  "e": 4,
  "c": "Preservativos & Barbear",
  "ean": "7896222721075"
 },
 {
  "n": "PRES.JONTEX SENSITIVE C/3",
  "f": "",
  "de": 21.59,
  "pc": 19.3,
  "e": 7,
  "c": "Preservativos & Barbear",
  "ean": "7896222720009"
 },
 {
  "n": "PRES.OLLA LUB.BOL.LV8PG6",
  "f": "",
  "de": 23.1,
  "pc": 20.79,
  "e": 6,
  "c": "Preservativos & Barbear",
  "ean": "7896222717788"
 },
 {
  "n": "PRES.OLLA LUBRIF. C/6",
  "f": "",
  "de": 20.7,
  "pc": 18.6,
  "e": 5,
  "c": "Preservativos & Barbear",
  "ean": "7896222716262"
 },
 {
  "n": "PRES.OLLA MORANGO C/6",
  "f": "",
  "de": 21.7,
  "pc": 19.5,
  "e": 3,
  "c": "Preservativos & Barbear",
  "ean": "7896222718273"
 },
 {
  "n": "PRES.OLLA SENSITIVE C/3",
  "f": "",
  "de": 15.66,
  "pc": 0,
  "e": 5,
  "c": "Preservativos & Barbear",
  "ean": "7896222717948"
 },
 {
  "n": "PRES.OLLA SENSITIVE C/6",
  "f": "",
  "de": 20.35,
  "pc": 18.3,
  "e": 4,
  "c": "Preservativos & Barbear",
  "ean": "7896222717962"
 },
 {
  "n": "BAND-AID C/40",
  "f": "",
  "de": 24.99,
  "pc": 22.49,
  "e": 10,
  "c": "Primeiros Socorros",
  "ean": "7891010504755"
 },
 {
  "n": "BAND-AID VARIADOS C 30",
  "f": "",
  "de": 29.99,
  "pc": 26.99,
  "e": 3,
  "c": "Primeiros Socorros",
  "ean": "7891010247263"
 },
 {
  "n": "BITUFO LIMPADOR LINGUA DUPLA AÇAO",
  "f": "",
  "de": 26.7,
  "pc": 23.99,
  "e": 3,
  "c": "Primeiros Socorros",
  "ean": "7897144600370"
 },
 {
  "n": "COTONETE J&J C/150",
  "f": "",
  "de": 21,
  "pc": 18.9,
  "e": 6,
  "c": "Primeiros Socorros",
  "ean": "7891010560812"
 },
 {
  "n": "COTONETE J&J C/150 POTE",
  "f": "",
  "de": 24.5,
  "pc": 21.9,
  "e": 6,
  "c": "Primeiros Socorros",
  "ean": "7891010032937"
 },
 {
  "n": "COTONETE JEJ CX C/300 NEU",
  "f": "",
  "de": 34.85,
  "pc": 31.3,
  "e": 3,
  "c": "Primeiros Socorros",
  "ean": "7891010047764"
 },
 {
  "n": "CURATIVO CREMER A PROVA DAGUA C/15 - 372847",
  "f": "",
  "de": 23.99,
  "pc": 21.5,
  "e": 5,
  "c": "Primeiros Socorros",
  "ean": "7891800372847"
 },
 {
  "n": "CURATIVO CREMER EXTRA GRANDE XXG C/8 -",
  "f": "",
  "de": 21.5,
  "pc": 19.3,
  "e": 7,
  "c": "Primeiros Socorros",
  "ean": "7891800644470"
 },
 {
  "n": "ESP. SALVELOX BRANCO 10CMX3CM",
  "f": "",
  "de": 23.99,
  "pc": 21.5,
  "e": 5,
  "c": "Primeiros Socorros",
  "ean": "7891800670608"
 },
 {
  "n": "ESP.SALVELOX BRANCO 5.0X4.5",
  "f": "",
  "de": 17.6,
  "pc": 15.8,
  "e": 18,
  "c": "Primeiros Socorros",
  "ean": "7891800628432"
 },
 {
  "n": "FITA D.J&J EXP.PLUS 50MTS",
  "f": "",
  "de": 23.4,
  "pc": 20.99,
  "e": 4,
  "c": "Primeiros Socorros",
  "ean": "7891010038953"
 },
 {
  "n": "LENCO PAPEL ELITE C/150",
  "f": "",
  "de": 23.75,
  "pc": 21.3,
  "e": 5,
  "c": "Primeiros Socorros",
  "ean": "7896061953279"
 },
 {
  "n": "MASCARA CIRURGICA DESCARPACK MEDIX C/50 UND",
  "f": "",
  "de": 21.2,
  "pc": 18.99,
  "e": 3,
  "c": "Primeiros Socorros",
  "ean": "7898283813065"
 },
 {
  "n": "TALA CURTA BILATERAL PRETA M MERCUR",
  "f": "",
  "de": 70,
  "pc": 56.9,
  "e": 3,
  "c": "Primeiros Socorros",
  "ean": "7896342452187"
 },
 {
  "n": "TENYS PE JATO SECO CANFORADO 92G",
  "f": "",
  "de": 26.6,
  "pc": 23.9,
  "e": 3,
  "c": "Primeiros Socorros",
  "ean": "7896020160168"
 },
 {
  "n": "ADOC.STEVIA PLUS 80ML",
  "f": "",
  "de": 23.3,
  "pc": 20.9,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7896292000186"
 },
 {
  "n": "APIS FLORA EXT. PROPOLIS S/ALCOOL  30ML",
  "f": "",
  "de": 44.2,
  "pc": 39.6,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7896663301317"
 },
 {
  "n": "APIS FLORA EXTRATO DE PROPOLIS 30ML",
  "f": "",
  "de": 31.99,
  "pc": 28.79,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7896663300204"
 },
 {
  "n": "APIS FLORA EXTRATO DE PROPOLIS VERDE 30ML",
  "f": "",
  "de": 42.5,
  "pc": 38.25,
  "e": 9,
  "c": "Vitaminas & Nutricao",
  "ean": "7896663302550"
 },
 {
  "n": "APIS FLORA EXTRATO DE PROPOLIS VERDE 70ML",
  "f": "",
  "de": 60.9,
  "pc": 54.8,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7896663322473"
 },
 {
  "n": "BARRA NUTRATA CHARGE 45G",
  "f": "",
  "de": 18.9,
  "pc": 18.9,
  "e": 9,
  "c": "Vitaminas & Nutricao",
  "ean": "7900392000103"
 },
 {
  "n": "BIONATUS CRISTAIS GENGIBRE LIMAO SAL ARDRAK",
  "f": "",
  "de": 21.6,
  "pc": 19.2,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7896755400058"
 },
 {
  "n": "BIOTINA 45MCG 60CAPS",
  "f": "",
  "de": 28.56,
  "pc": 19.9,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7898303263870"
 },
 {
  "n": "CLORETO DE MAGNESIO P.A 500MG C/60 CPSHERBAMED",
  "f": "",
  "de": 28.82,
  "pc": 19.9,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7898303261050"
 },
 {
  "n": "COENZIMA Q10 100MG 60CAPS HERBAMED",
  "f": "",
  "de": 62.24,
  "pc": 52.9,
  "e": 2,
  "c": "Vitaminas & Nutricao",
  "ean": "7908699000239"
 },
 {
  "n": "ESSENCE ALL COMPLEXO B C/100 CPS",
  "f": "",
  "de": 105.9,
  "pc": 69.9,
  "e": 7,
  "c": "Vitaminas & Nutricao",
  "ean": "40141779038"
 },
 {
  "n": "ESSENCE ALL MAGNESIO INOSITOL 180G",
  "f": "",
  "de": 84.9,
  "pc": 69.9,
  "e": 2,
  "c": "Vitaminas & Nutricao",
  "ean": "0631430486388"
 },
 {
  "n": "ESSENCE ALL OMEGA 3  C/120 CPS",
  "f": "",
  "de": 105.9,
  "pc": 69.9,
  "e": 9,
  "c": "Vitaminas & Nutricao",
  "ean": "40141779014"
 },
 {
  "n": "ESSENCE ALL SENIOR 50+ CHOCOLATE 800G",
  "f": "",
  "de": 124.9,
  "pc": 109.9,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "0631430487125"
 },
 {
  "n": "ESSENCE ALL SENIOR 50+ SEM SABOR 800G",
  "f": "",
  "de": 124.9,
  "pc": 109.9,
  "e": 3,
  "c": "Vitaminas & Nutricao",
  "ean": "0631430487132"
 },
 {
  "n": "ESSENCE ALL VITAMINA B12 C/60 CPS MORANGO MASTI",
  "f": "",
  "de": 105.9,
  "pc": 69.9,
  "e": 14,
  "c": "Vitaminas & Nutricao",
  "ean": "40141781529"
 },
 {
  "n": "FLEXIGOLD 40MG C/30 + 30",
  "f": "",
  "de": 108.95,
  "pc": 49.9,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7898303263597"
 },
 {
  "n": "GUARANA PO 170G.CAXINAUA",
  "f": "",
  "de": 68.9,
  "pc": 61.9,
  "e": 3,
  "c": "Vitaminas & Nutricao",
  "ean": "7897554400027"
 },
 {
  "n": "HERBAMED CAFEINA 210MG C/60 CPS HERBAMED",
  "f": "",
  "de": 42.01,
  "pc": 35.9,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7898303261135"
 },
 {
  "n": "HERBAMED CRANBERRY 500MG C/60 CPS",
  "f": "",
  "de": 39.05,
  "pc": 31.7,
  "e": 3,
  "c": "Vitaminas & Nutricao",
  "ean": "7898303261180"
 },
 {
  "n": "MAG PLUS 5 550MG 60CAPS",
  "f": "",
  "de": 55.99,
  "pc": 39.5,
  "e": 5,
  "c": "Vitaminas & Nutricao",
  "ean": "7908699000024"
 },
 {
  "n": "MAGNESIO DIMALATO 400MG 60CAPS HERBAMED",
  "f": "",
  "de": 40.6,
  "pc": 33.9,
  "e": 3,
  "c": "Vitaminas & Nutricao",
  "ean": "7898303262699"
 },
 {
  "n": "OLEO DE GIRASSOL FARMAX 200ML",
  "f": "",
  "de": 28.99,
  "pc": 25.99,
  "e": 6,
  "c": "Vitaminas & Nutricao",
  "ean": "7896902210998"
 },
 {
  "n": "SIMFORT PLUS C/60 CAPS",
  "f": "",
  "de": 149.7,
  "pc": 126.95,
  "e": 3,
  "c": "Vitaminas & Nutricao",
  "ean": "7898665433256"
 },
 {
  "n": "TOALHA UMED.ESSENCE ALL BABY C/140UN",
  "f": "",
  "de": 10.99,
  "pc": 7.99,
  "e": 438,
  "c": "Vitaminas & Nutricao",
  "ean": "7898197416628"
 },
 {
  "n": "ZINCO QUELATO 60CAPS HERBAMED",
  "f": "",
  "de": 33.15,
  "pc": 28.7,
  "e": 4,
  "c": "Vitaminas & Nutricao",
  "ean": "7898303260954"
 }
]

ABAS = ["Fraldas", "Leites & Nutricao", "Dermocosmeticos", "Perfumes & Desodorantes", "Cabelos", "Higiene Intima", "Higiene Bucal", "Higiene & Banho", "Vitaminas & Nutricao", "Bebe & Infantil", "Preservativos & Barbear"]

def desconto(de, por):
    if de > por and de > 0:
        return int(round((1 - (por / de)) * 100))
    return 0

def brl(v):
    return ("%.2f" % v).replace(".", ",")

def card(p, idx):
    d = desconto(p["de"], p["pc"])
    tem_vs = "vs" in p and len(p.get("vs", [])) > 1
    badge = "<span class='bd'>-" + str(d) + "% OFF</span>" if d > 0 else ""
    de_html = "<div class='pde'>De R$ " + brl(p["de"]) + "</div>" if d > 0 else ""
    if p["e"] <= 2:
        est_html = "<div class='est crit'>ULTIMAS " + str(int(p["e"])) + " UNIDADES - confirme o estoque</div>"
    elif p["e"] <= 10:
        est_html = "<div class='est esc'>Apenas " + str(int(p["e"])) + " unid.</div>"
    else:
        est_html = "<div class='est'>Disponivel</div>"
    ean_pad = p.get("ean", "")
    nm_pad = p["n"].replace("'", "")
    opts = ""
    if tem_vs:
        ean_pad = p["vs"][0]["ean"]
        nm_pad = (p["n"] + " - " + p["vs"][0]["v"]).replace("'", "")
        for i, v in enumerate(p["vs"]):
            chk = "checked" if i == 0 else ""
            nmv = v["v"].replace("'", "")
            opts = opts + "<input type='radio' name='v" + str(idx) + "' id='q" + str(idx) + "_" + str(i) + "' value='" + v["ean"] + "' data-nm='" + nmv + "' data-pc='" + brl(v["pc"]) + "' " + chk + " onchange='mudaOp(" + str(idx) + ")'><label class='op' for='q" + str(idx) + "_" + str(i) + "'>" + v["v"] + "</label>"
    r1 = "<article class='card' data-i='" + str(idx) + "'>"
    r2 = "<div class='ctop'>" + badge + "</div>"
    _foto = FOTOS_LOCAIS.get(ean_pad, CDN_IMG + ean_pad)
    r3 = "<div class='imgb'><img class='fot' src='" + _foto + "' alt='" + nm_pad + "' loading='lazy'></div>"
    r4 = "<div class='cb'><h3 class='nm'>" + p["n"] + "</h3>"
    r5 = "<div class='fl'>" + p["f"] + "</div>"
    r6 = "<div class='pcs'>" + de_html + "<div class='pp'><span>R$</span> <span id='pc" + str(idx) + "'>" + brl(p["pc"]) + "</span></div>" + est_html + "</div>"
    r7 = ("<div class='sv'>Escolha:</div><div class='ops'>" + opts + "</div>") if tem_vs else ""
    r8 = "<input type='hidden' id='en" + str(idx) + "' value='" + ean_pad + "'>"
    r9 = "<input type='hidden' id='nn" + str(idx) + "' value='" + nm_pad + "'>"
    r10 = "<button class='btnadd' onclick='addSac(" + str(idx) + ")'>ADICIONAR A SACOLA</button></div></article>"
    return r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10

def render(lista):
    return "".join(card(p, i) for i, p in enumerate(lista))

def carrossel():
    s1 = "<img class='slide on' src='" + A_CARRO + "' alt='Sorte Real na Total - 4 carros 0km'>"
    s2 = "<img class='slide' src='" + A_BEMME + "' alt='Produtos Bemme valem 5x mais chances'>"
    s3 = "<img class='slide' src='" + A_PART + "' alt='Como participar do Sorte Real na Total'>"
    c1 = "<div class='carrossel'><div class='cpalco'>" + s1 + s2 + s3 + "</div>"
    c2 = "<div class='cdots'><span class='dpg at'></span><span class='dpg'></span><span class='dpg'></span></div></div>"
    return c1 + c2

def video_jornal():
    v = "<div class='vsec'><div class='stit'>Jornal de Ofertas - Edicao Outubro</div>"
    v = v + "<div class='ssub'>Assista as ofertas do mes</div>"
    v = v + "<div class='vbox'><iframe src='https://www.youtube.com/embed/" + VIDEO_ID + "?autoplay=1&mute=1&loop=1&playlist=" + VIDEO_ID + "&rel=0&playsinline=1&modestbranding=1' title='Jornal de Ofertas Drogaria Total' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe></div></div>"
    return v

def pills(at):
    p = "<a class='pl " + ("on" if not at else "") + "' href='/'>Inicio</a>"
    for a in ABAS:
        if not any(x["c"] == a for x in CATALOGO):
            continue
        p = p + "<a class='pl " + ("on" if at == a else "") + "' href='/?aba=" + urllib.parse.quote_plus(a) + "'>" + a + "</a>"
    return p

SELOS = """
<div class="selos">
<div class="selo"><span class="sic">&#128737;</span><span>Farmacia Autorizada<small>ANVISA - RDC 44/2009</small></span></div>
<div class="selo"><span class="sic">&#128176;</span><span>Pagamento na Entrega<small>Pix, cartao ou dinheiro</small></span></div>
<div class="selo"><span class="sic">&#128666;</span><span>Entrega Rapida<small>Ate 45 min em Ituverava</small></span></div>
<div class="selo"><span class="sic">&#128274;</span><span>Compra Protegida<small>Seus dados seguros - LGPD</small></span></div>
<div class="selo"><span class="sic">&#9989;</span><span>Servico Oficial<small>Da Drogaria Total Ituverava</small></span></div>
</div>
"""

DESTAQUE = """
<div class="vantagens">
  <div class="vant-tit">Por que pedir pelo site?</div>
  <div class="vant-lista">
    <div class="vant"><span class="vico">&#9200;</span><div><b>Sem fila</b><small>Peca de casa e receba em ate 45 min</small></div></div>
    <div class="vant"><span class="vico">&#128176;</span><div><b>Melhor preco</b><small>Ofertas do jornal, iguais as da loja</small></div></div>
    <div class="vant"><span class="vico">&#128666;</span><div><b>Entrega rapida</b><small>Direto na sua porta em Ituverava</small></div></div>
    <div class="vant"><span class="vico">&#127873;</span><div><b>Concorra a 4 carros</b><small>Informe o CPF e acumule numeros da sorte</small></div></div>
  </div>
</div>"""

def home():
    x1 = carrossel()
    x2 = DESTAQUE
    x3 = video_jornal()
    x4 = "<div class='stit'>Escolha uma categoria</div>"
    x5 = "<div class='cats'>"
    for a in ABAS:
        if not any(y["c"] == a for y in CATALOGO):
            continue
        x5 = x5 + "<a class='cat' href='/?aba=" + urllib.parse.quote_plus(a) + "'><span class='cn'>" + a + "</span></a>"
    x6 = "</div>"
    x7 = SELOS
    return PAGINA.replace("__PILLS__", pills("")).replace("__CONTEUDO__", x1 + x2 + x3 + x4 + x5 + x6 + x7).replace("__Q__", "").replace("__LOGO__", LOGO)

def pg_aba(titulo, lista):
    y1 = "<div class='cvolta'><a href='/'>&#8592; Voltar as categorias</a></div>"
    y2 = "<div class='stit'>" + titulo + "</div>"
    y3 = "<div class='mt'>" + str(len(lista)) + " produtos</div>"
    y4 = "<div class='grid'>" + render(lista) + "</div>"
    return PAGINA.replace("__PILLS__", pills(titulo)).replace("__CONTEUDO__", y1 + y2 + y3 + y4).replace("__Q__", "").replace("__LOGO__", LOGO)

@app.route("/")
def index():
    aba = request.args.get("aba", "").strip()
    q = request.args.get("q", "").strip().lower()
    if aba or q:
        lista = [p for p in CATALOGO if (not aba or p["c"] == aba)]
        if q:
            lista = [p for p in lista if q in p["n"].lower() or q in p["f"].lower()]
        return pg_aba(aba if aba else ("Busca: " + request.args.get("q", "")), lista)
    return home()

PAGINA = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Drogaria Total Ituverava - Delivery e Ofertas</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:Inter,Arial,sans-serif}
body{background:#f1f5f9;color:#0f172a}
.faixa{background:#0f172a;color:#fff;font-size:12.5px;padding:9px 14px;text-align:center;font-weight:600;display:flex;justify-content:center;gap:20px;flex-wrap:wrap}
.faixa b{color:#4ade80}
header{background:#fff;border-bottom:2px solid #fee2e2;padding:12px 18px;position:sticky;top:0;z-index:60;box-shadow:0 2px 12px rgba(0,0,0,.06)}
.hw{max-width:1240px;margin:auto;display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}
.lg{height:44px;display:block}
.busc{flex:1;min-width:200px;max-width:440px;display:flex;border:2px solid #cbd5e1;border-radius:12px;overflow:hidden}
.busc input{flex:1;padding:10px 14px;border:none;outline:none;font-size:14px}
.busc button{background:#c1121f;color:#fff;border:none;padding:0 18px;font-weight:800;cursor:pointer}
.sactx{background:#c1121f;color:#fff;border:none;padding:11px 15px;border-radius:12px;font-weight:900;font-size:13px;cursor:pointer;white-space:nowrap}
main{max-width:1240px;margin:18px auto;padding:0 16px}
.pills{display:flex;gap:7px;overflow-x:auto;padding-bottom:10px;margin-bottom:14px}
.pl{text-decoration:none;padding:8px 14px;background:#fff;border:1px solid #e2e8f0;border-radius:20px;font-size:12.5px;font-weight:700;color:#475569;white-space:nowrap}
.pl.on{background:#c1121f;color:#fff;border-color:#c1121f}
.carrossel{background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 12px 30px rgba(0,0,0,.16);margin-bottom:20px}
.cpalco{position:relative;background:#fff;min-height:180px}
.cpalco img{width:100%;height:auto;display:none}
.cpalco img.on{display:block}
.cdots{display:flex;justify-content:center;gap:8px;padding:12px}
.dpg{width:10px;height:10px;border-radius:50%;background:#cbd5e1}
.dpg.at{background:#c1121f;width:26px;border-radius:6px}
.vsec{margin-bottom:26px}
.vbox{position:relative;width:100%;padding-bottom:56.25%;height:0;background:#000;border-radius:16px;overflow:hidden;box-shadow:0 10px 28px rgba(0,0,0,.18)}
.vbox iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
.vantagens{background:linear-gradient(135deg,#16a34a,#15803d);border-radius:16px;padding:18px 20px;margin-bottom:22px;box-shadow:0 10px 26px rgba(22,163,74,.25)}
.vant-tit{color:#fff;font-size:15px;font-weight:900;margin-bottom:12px;text-align:center}
.vant-lista{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.vant{background:rgba(255,255,255,.14);border-radius:11px;padding:12px;display:flex;align-items:center;gap:10px;color:#fff}
.vant b{display:block;font-size:13px;font-weight:900}
.vant small{font-size:10.5px;font-weight:600;opacity:.9;line-height:1.3;display:block}
.vico{font-size:22px;flex-shrink:0}
.stit{font-size:19px;font-weight:900;margin-bottom:12px}
.ssub{font-size:12.5px;color:#64748b;font-weight:600;margin:-8px 0 12px}
.cats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:22px;max-width:920px}
.cat{text-decoration:none;background:#fff;border:1.5px solid #e2e8f0;border-radius:11px;padding:13px 12px}
.cat:hover{border-color:#c1121f}
.cn{font-size:13px;font-weight:700;color:#0f172a}
.cvolta{margin-bottom:14px}
.cvolta a{text-decoration:none;color:#c1121f;font-weight:800;font-size:13.5px}
.mt{font-weight:700;color:#475569;margin-bottom:14px;font-size:13.5px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:15px;align-items:start}
.card{background:#fff;border-radius:16px;border:1px solid #e2e8f0;box-shadow:0 4px 15px rgba(0,0,0,.04);display:flex;flex-direction:column;position:relative;overflow:hidden}
.ctop{position:absolute;top:9px;left:9px;z-index:2}
.bd{background:#dc2626;color:#fff;font-size:11px;font-weight:900;padding:4px 8px;border-radius:8px}
.imgb{height:165px;background:#fff;display:flex;align-items:center;justify-content:center;border-bottom:1px solid #e2e8f0;overflow:hidden}
.fot{max-width:100%;max-height:100%;object-fit:contain;padding:8px}
.cb{padding:12px;display:flex;flex-direction:column;flex:1;justify-content:space-between}
.nm{font-size:12.5px;font-weight:700;line-height:1.4;margin-bottom:3px;min-height:34px}
.fl{font-size:9.5px;color:#c1121f;font-weight:800;text-transform:uppercase;margin-bottom:8px}
.pcs{background:#f8fafc;padding:8px 10px;border-radius:9px;margin-bottom:9px}
.pde{font-size:11px;text-decoration:line-through;color:#94a3b8;font-weight:600}
.pp{font-size:20px;font-weight:900;color:#16a34a;line-height:1.1}
.pp span{font-size:13px}
.est{font-size:10.5px;font-weight:700;color:#059669;margin-top:2px}
.est.esc{color:#dc2626}
.sv{font-size:10px;font-weight:800;color:#475569;text-transform:uppercase;margin-bottom:6px}
.ops{display:flex;flex-wrap:wrap;gap:4px;margin-bottom:9px}
.ops input{display:none}
.op{display:inline-block;padding:5px 9px;border:1.5px solid #cbd5e1;border-radius:8px;font-size:10.5px;font-weight:700;color:#475569;cursor:pointer;background:#fff}
.ops input:checked + .op{background:#c1121f;border-color:#c1121f;color:#fff}
.btnadd{background:#c1121f;color:#fff;border:none;padding:11px;border-radius:10px;font-size:11.5px;font-weight:900;cursor:pointer;width:100%}
.selos{display:flex;gap:9px;flex-wrap:wrap;justify-content:center;margin:24px 0 6px}
.selo{background:#fff;border:1px solid #e2e8f0;border-radius:11px;padding:11px 14px;font-size:11.5px;font-weight:800;color:#0f172a;display:flex;align-items:center;gap:9px}
.selo small{display:block;font-size:10px;font-weight:600;color:#64748b}
.sic{font-size:19px}
.modal{position:fixed;inset:0;background:rgba(15,23,42,.65);z-index:100;display:none;align-items:center;justify-content:center;padding:16px}
.modal.on{display:flex}
.mbox{background:#fff;border-radius:18px;max-width:520px;width:100%;max-height:86vh;overflow-y:auto}
.mtop{background:#c1121f;color:#fff;padding:15px 18px;font-weight:900;display:flex;justify-content:space-between;align-items:center}
.mx{background:transparent;border:none;color:#fff;font-size:22px;cursor:pointer}
.mitem{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:12px 18px;border-bottom:1px solid #f1f5f9;font-size:13px}
.mitem b{display:block;font-weight:800}
.mitem small{color:#64748b;font-size:11px}
.mrm{background:#fee2e2;color:#b91c1c;border:none;width:28px;height:28px;border-radius:50%;cursor:pointer;font-weight:900;flex-shrink:0}
.mfoot{padding:16px 18px;position:sticky;bottom:0;background:#fff;border-top:2px solid #f1f5f9}
.mtot{display:flex;justify-content:space-between;font-size:17px;font-weight:900;margin-bottom:12px}
.mfin{background:#16a34a;color:#fff;border:none;width:100%;padding:14px;border-radius:11px;font-size:13.5px;font-weight:900;cursor:pointer}
.maviso{background:#fffbeb;border:1.5px dashed #f59e0b;border-radius:10px;padding:10px 12px;font-size:11px;color:#92400e;font-weight:600;margin-bottom:12px;line-height:1.5}
footer{background:#0f172a;color:#94a3b8;padding:40px 20px 20px;margin-top:44px;font-size:12.5px}
.fg{max-width:1240px;margin:auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:26px;padding-bottom:24px;border-bottom:1px solid #1e293b}
.fg h3{color:#fff;font-size:14.5px;margin-bottom:10px}
.fg p{line-height:1.6;margin-bottom:6px}
.legal{max-width:1240px;margin:20px auto 0;font-size:11px;text-align:center;color:#64748b;line-height:1.7}
.legal strong{color:#94a3b8}
@media (max-width:900px){.vant-lista{grid-template-columns:repeat(2,1fr)}}
@media (max-width:768px){.lg{height:34px}.cats{grid-template-columns:repeat(2,1fr);gap:8px;max-width:100%}.grid{grid-template-columns:repeat(2,1fr);gap:10px}.imgb{height:130px}.vant-lista{grid-template-columns:1fr;gap:8px}.faixa{font-size:10.5px;gap:11px}}
/* Alerta de estoque critico (1-2 unidades) */
.est.crit{background:#7f1d1d;color:#fff;padding:6px 9px;border-radius:7px;font-size:10.5px;font-weight:900;margin-top:5px;text-align:center;letter-spacing:.3px;animation:pulsa 1.6s infinite}
@keyframes pulsa{0%,100%{opacity:1}50%{opacity:.72}}
</style>
</head>
<body>
<div class="faixa">
<span>&#128666; Entrega em Ituverava - SP</span>
<span>&#9200; Ate <b>18h</b>: entrega no mesmo dia</span>
<span>&#127769; Apos 18h: dia seguinte as 8h</span>
<span>&#128172; <b>(16) 99106-7477</b></span>
</div>
<header><div class="hw">
<a href="/"><img class="lg" src="__LOGO__" alt="Drogaria Total"></a>
<form class="busc" method="GET" action="/"><input type="text" name="q" value="__Q__" placeholder="Buscar produto..."><button type="submit">Buscar</button></form>
<button class="sactx" onclick="abreSac()">&#128722; <span id="ctSac">0</span> itens</button>
</div></header>
<main>
<div class="pills">__PILLS__</div>
__CONTEUDO__
</main>
<div class="modal" id="modalSac">
<div class="mbox">
<div class="mtop"><span>Minha Sacola</span><button class="mx" onclick="fechaSac()">&times;</button></div>
<div id="listaSac"></div>
<div class="mfoot">
<div class="maviso">&#9203; Seu pedido sera enviado como <strong>AGUARDANDO CONFIRMACAO</strong>. A compra somente e garantida apos o atendente da Drogaria Total responder confirmando.</div>
<div class="mtot"><span>Total estimado:</span><span id="totSac">R$ 0,00</span></div>
<button class="mfin" onclick="finSac()">&#128172; FINALIZAR PEDIDO NO WHATSAPP</button>
</div></div></div>
<footer>
<div class="fg">
<div><h3>Drogaria Total Ituverava</h3>
<p>Servico oficial de delivery e ofertas da Drogaria Total Ituverava - SP.</p>
<p><strong>Pedidos e Delivery:</strong> (16) 99106-7477</p>
<p><strong>Atendimento na loja:</strong> (16) 99998-2256</p>
<p>Ituverava - SP &bull; CEP 14500-053</p></div>
<div><h3>Politica de Entrega</h3>
<p>Pedidos ate as 18h: entrega no <strong>mesmo dia</strong>, em ate 45 minutos.</p>
<p>Pedidos a partir das 18h: entrega no <strong>dia seguinte a partir das 8h</strong>.</p>
<p>Entregas por motoboy identificado da farmacia.</p></div>
<div><h3>Regulacao e Seguranca</h3>
<p>&bull; Dispensacao conforme <strong>RDC 44/2009 ANVISA</strong></p>
<p>&bull; Produtos de higiene, beleza e cuidados pessoais</p>
<p>&bull; Medicamentos <strong>nao</strong> sao vendidos pelo delivery</p></div>
<div><h3>Seus Direitos</h3>
<p>&bull; <strong>CDC</strong> - Lei 8.078/90: arrependimento em ate 7 dias</p>
<p>&bull; <strong>LGPD</strong> - Lei 13.709/18: dados tratados com sigilo</p>
<p>&bull; <strong>Marco Civil da Internet</strong> - Lei 12.965/14</p>
<p>&bull; <strong>Lei do E-commerce</strong> - Decreto 7.962/13</p></div>
<div><h3>Sorte Real na Total</h3>
<p>Campanha valida de 05/09/2026 a 31/12/2026.</p>
<p>Informe seu CPF no pedido para acumular numeros da sorte.</p>
<p>Produtos Bemme dao <strong>5 numeros extras</strong> por compra.</p></div>
</div>
<div class="legal">
<p><strong>AVISO LEGAL:</strong> Este e um canal oficial de atendimento da Drogaria Total Ituverava. Os precos, condicoes de frete e disponibilidade exibidos sao informativos e sujeitos a alteracao sem aviso previo. A venda somente e confirmada apos validacao pelo atendente da farmacia.</p>
<p style="margin-top:7px">Imagens meramente ilustrativas.</p>
<p style="margin-top:7px">Drogaria Total Ituverava &bull; Todos os direitos reservados.</p>
</div>
</footer>
<script>
var sacola = [];
var slIdx = 0;
function mudaOp(i){
  var c = document.querySelector("[data-i='" + i + "']");
  if(!c) return;
  var s = c.querySelector("input[type=radio]:checked");
  if(!s) return;
  c.querySelector("#pc"+i).textContent = s.dataset.pc;
  c.querySelector("#en"+i).value = s.value;
  c.querySelector("#nn"+i).value = c.querySelector(".nm").textContent + " - " + s.dataset.nm;
  var f = c.querySelector(".fot");
  if(f) f.src = "https://cdn-cosmos.bluesoft.com.br/products/" + s.value;
}
function addSac(i){
  var c = document.querySelector("[data-i='" + i + "']");
  if(!c) return;
  var ean = c.querySelector("#en"+i).value;
  var nm = c.querySelector("#nn"+i).value;
  var pc = parseFloat(c.querySelector("#pc"+i).textContent.replace(".","").replace(",","."));
  sacola.push({e: ean, n: nm, p: pc});
  atualizaSac();
  var b = c.querySelector(".btnadd");
  b.textContent = "ADICIONADO";
  b.style.background = "#16a34a";
  setTimeout(function(){ b.textContent = "ADICIONAR A SACOLA"; b.style.background = "#c1121f"; }, 1300);
}
function atualizaSac(){
  document.getElementById("ctSac").textContent = sacola.length;
  var h = "";
  var tot = 0;
  for(var i=0;i<sacola.length;i++){
    tot = tot + sacola[i].p;
    h = h + "<div class='mitem'><div><b>" + sacola[i].n + "</b><small>R$ " + sacola[i].p.toFixed(2).replace(".",",") + "</small></div><button class='mrm' onclick='rmSac(" + i + ")'>&times;</button></div>";
  }
  if(sacola.length === 0){ h = "<div class='mitem'>Sua sacola esta vazia.</div>"; }
  document.getElementById("listaSac").innerHTML = h;
  document.getElementById("totSac").textContent = "R$ " + tot.toFixed(2).replace(".",",");
}
function rmSac(i){ sacola.splice(i,1); atualizaSac(); }
function finSac(){
  if(sacola.length === 0){ alert("Sua sacola esta vazia."); return; }
  var msg = "Ola, Drogaria Total Ituverava! Gostaria de fazer um pedido:\n\n";
  var tot = 0;
  for(var i=0;i<sacola.length;i++){
    msg = msg + (i+1) + ") " + sacola[i].n + "\n   Cod: " + sacola[i].e + "\n   R$ " + sacola[i].p.toFixed(2).replace(".",",") + "\n\n";
    tot = tot + sacola[i].p;
  }
  msg = msg + "TOTAL ESTIMADO: R$ " + tot.toFixed(2).replace(".",",") + "\n\n";
  msg = msg + "STATUS: AGUARDANDO CONFIRMACAO\n";
  msg = msg + "(A compra sera garantida apos o atendente confirmar)\n\n";
  msg = msg + "Meu nome: \nMeu endereco: \nForma de pagamento: Pix / Cartao / Dinheiro\n";
  msg = msg + "Meu CPF (para o Sorte Real): ";
  window.open("https://wa.me/5516991067477?text=" + encodeURIComponent(msg), "_blank");
  fechaSac();
}
function abreSac(){ atualizaSac(); document.getElementById("modalSac").className = "modal on"; }
function fechaSac(){ document.getElementById("modalSac").className = "modal"; }
function giraCar(){
  var s = document.querySelectorAll(".cpalco img");
  var d = document.querySelectorAll(".dpg");
  if(s.length < 2) return;
  slIdx = slIdx + 1;
  if(slIdx >= s.length) slIdx = 0;
  for(var i=0;i<s.length;i++){
    s[i].className = (i === slIdx) ? "slide on" : "slide";
  }
  for(var j=0;j<d.length;j++){
    d[j].className = (j === slIdx) ? "dpg at" : "dpg";
  }
}
setInterval(giraCar, 2000);
</script>
</body>
</html>"""

if __name__ == "__main__":
    app.run(debug=True)