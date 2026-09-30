import urllib.parse
from flask import Flask, request

app = Flask(__name__)

# ============================================================
# ARGD FARMA - Drogaria Total Ituverava Delivery
# Pedidos: WhatsApp (16) 99106-7477
# Campanha: Sorte Real na Total - Especial 30 Anos
# ============================================================

NOME_SITE = "ARGD Farma"
ZAP_PEDIDOS = "5516991067477"
ZAP_LOJA = "5516999982256"
CDN_IMG = "https://cdn-cosmos.bluesoft.com.br/products/"
CAMPANHA_INICIO = "05/09/2026"
CAMPANHA_FIM = "31/12/2026"


BEMME = [
    {"n": "WAFER PROTEIN COOKIES CREAM ZERO 25G BEMME", "c": "Bemme - 5x Chances", "de": 12.9, "pc": 12.9, "e": 13, "f": "Bemme", "ean": "7898775460583", "campanha": 1},
    {"n": "BARRA BANANA C/ AMENDOIM ZERO 25G BEMME", "c": "Bemme - 5x Chances", "de": 5.99, "pc": 5.99, "e": 11, "f": "Bemme", "ean": "7898775460538", "campanha": 1},
    {"n": "BARRA NUTS CRANBERRY ZERO 25G BEMME", "c": "Bemme - 5x Chances", "de": 6.99, "pc": 6.99, "e": 11, "f": "Bemme", "ean": "7898775460576", "campanha": 1},
    {"n": "COND.BEMME RECONSTRUCAO 300ML", "c": "Bemme - 5x Chances", "de": 31.9, "pc": 28.7, "e": 11, "f": "Bemme", "ean": "7897799835318", "campanha": 1},
    {"n": "MASC.BEMME NUTRICAO 250ML", "c": "Bemme - 5x Chances", "de": 33.3, "pc": 29.9, "e": 11, "f": "Bemme", "ean": "7897799835400", "campanha": 1},
    {"n": "SH.BEMME NUTRICAO 300ML", "c": "Bemme - 5x Chances", "de": 31.5, "pc": 28.3, "e": 11, "f": "Bemme", "ean": "7897799835387", "campanha": 1},
    {"n": "SH.BEMME RECONSTRUCAO 300ML", "c": "Bemme - 5x Chances", "de": 31.5, "pc": 28.3, "e": 11, "f": "Bemme", "ean": "7897799835301", "campanha": 1},
    {"n": "BARRA COCADA C/CHOCOLATE ZERO 25G BEMME", "c": "Bemme - 5x Chances", "de": 6.99, "pc": 6.99, "e": 10, "f": "Bemme", "ean": "7898775460552", "campanha": 1},
    {"n": "BEMME GUMMIES SENIOR 50+ C/60 GOMAS SABOR MELANCIA", "c": "Bemme - 5x Chances", "de": 100.2, "pc": 89.9, "e": 7, "f": "Bemme", "ean": "7896321041746", "campanha": 1},
    {"n": "BEMME PERFUME IV VIP ROSE WOMAN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 7, "f": "Bemme", "ean": "7899918942006", "campanha": 1},
    {"n": "BARRA COCADA C/ABACAXI ZERO 25G BEMME", "c": "Bemme - 5x Chances", "de": 5.99, "pc": 5.99, "e": 6, "f": "Bemme", "ean": "7898775460590", "campanha": 1},
    {"n": "BEMME PERFUME IV OLIMPYC WOMAN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 6, "f": "Bemme", "ean": "7899918942020", "campanha": 1},
    {"n": "BEMME PERFUME IV PASSION WOMAN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 6, "f": "Bemme", "ean": "7899918942013", "campanha": 1},
    {"n": "BEMME PERFUME IV CREEDY AVENTUS MEN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 5, "f": "Bemme", "ean": "7899918942044", "campanha": 1},
    {"n": "BEMME PERFUME IV ESTY BELLA WOMAM 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 5, "f": "Bemme", "ean": "7899918941948", "campanha": 1},
    {"n": "BEMME PERFUME IV GYRL BLUSH WOMAN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 5, "f": "Bemme", "ean": "7899918941955", "campanha": 1},
    {"n": "BEMME PERFUME IV GYRL WOMAM 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 5, "f": "Bemme", "ean": "7899918942174", "campanha": 1},
    {"n": "BEMME PERFUME IV INVYCTUS MEN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 5, "f": "Bemme", "ean": "7899918942037", "campanha": 1},
    {"n": "BEMME PERFUME IV SAVAGE MEN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 5, "f": "Bemme", "ean": "7899918942181", "campanha": 1},
    {"n": "COND.BEMME CACHOS 300ML", "c": "Bemme - 5x Chances", "de": 31.9, "pc": 28.7, "e": 5, "f": "Bemme", "ean": "7897799835356", "campanha": 1},
    {"n": "LEAVE IN BEMME CACHOS 250ML", "c": "Bemme - 5x Chances", "de": 33.3, "pc": 29.9, "e": 5, "f": "Bemme", "ean": "7897799835363", "campanha": 1},
    {"n": "BEMME PERFUME IV MAN NY MEN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 4, "f": "Bemme", "ean": "7899918941979", "campanha": 1},
    {"n": "BEMME PERFUME IV MILION MEN 15ML", "c": "Bemme - 5x Chances", "de": 44.8, "pc": 39.9, "e": 4, "f": "Bemme", "ean": "7899918941986", "campanha": 1},
    {"n": "BODY SPLASH ESTY BELLA INVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 4, "f": "Bemme", "ean": "7899918943232", "campanha": 1},
    {"n": "KIT ENX.BUCAL ZERO ALCOOL MENTA 500ML+250ML BEMME", "c": "Bemme - 5x Chances", "de": 28.8, "pc": 23.95, "e": 4, "f": "Bemme", "ean": "7908324802511", "campanha": 1},
    {"n": "BODY SPLASH LOVY SPELL INVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 3, "f": "Bemme", "ean": "7899918943256", "campanha": 1},
    {"n": "MASC.BEMME CACHOS 250ML", "c": "Bemme - 5x Chances", "de": 33.3, "pc": 29.9, "e": 3, "f": "Bemme", "ean": "7897799835370", "campanha": 1},
    {"n": "BODY SPLASH AMALFY SUNSET INVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 2, "f": "Bemme", "ean": "7899918943263", "campanha": 1},
    {"n": "BODY SPLASH IV GIRL INVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 2, "f": "Bemme", "ean": "7899918943225", "campanha": 1},
    {"n": "BODY SPLASH MAN NY IVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 44.9, "e": 2, "f": "Bemme", "ean": "7898976443432", "campanha": 1},
    {"n": "COND.BEMME ANTICASPA 300ML", "c": "Bemme - 5x Chances", "de": 29.9, "pc": 29.9, "e": 2, "f": "Bemme", "ean": "7897799835448", "campanha": 1},
    {"n": "COND.BEMME NUTRICAO 300ML", "c": "Bemme - 5x Chances", "de": 31.9, "pc": 28.7, "e": 2, "f": "Bemme", "ean": "7897799835394", "campanha": 1},
    {"n": "KIT BEMME PERFUME INVENCY + BODY SPLASH", "c": "Bemme - 5x Chances", "de": 109.9, "pc": 94.9, "e": 2, "f": "Bemme", "ean": "7898976443470", "campanha": 1},
    {"n": "LEAVE IN BEMME RECONSTRUCAO 250ML", "c": "Bemme - 5x Chances", "de": 33.3, "pc": 29.9, "e": 2, "f": "Bemme", "ean": "7897799835325", "campanha": 1},
    {"n": "MASC.BEMME RECONSTRUCAO 250ML", "c": "Bemme - 5x Chances", "de": 33.3, "pc": 29.9, "e": 2, "f": "Bemme", "ean": "7897799835332", "campanha": 1},
    {"n": "SH.BEMME ANTICASPA 300ML", "c": "Bemme - 5x Chances", "de": 29.9, "pc": 29.9, "e": 2, "f": "Bemme", "ean": "7897799835431", "campanha": 1},
    {"n": "SH.BEMME ANTIQUEDA 300ML", "c": "Bemme - 5x Chances", "de": 31.5, "pc": 28.3, "e": 2, "f": "Bemme", "ean": "7897799835455", "campanha": 1},
    {"n": "SH.BEMME CACHOS 300ML", "c": "Bemme - 5x Chances", "de": 31.5, "pc": 28.3, "e": 2, "f": "Bemme", "ean": "7897799835349", "campanha": 1},
    {"n": "BODY SPLASH BARY VANILLA INVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 1, "f": "Bemme", "ean": "7899918943270", "campanha": 1},
    {"n": "BODY SPLASH PASSION INVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 1, "f": "Bemme", "ean": "7899918943249", "campanha": 1},
    {"n": "BODY SPLASH SAVAGE IVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 1, "f": "Bemme", "ean": "7898976443449", "campanha": 1},
    {"n": "BODY SPLASH URBANY BEAT INVENCY 220ML BEMME", "c": "Bemme - 5x Chances", "de": 57.4, "pc": 51.4, "e": 1, "f": "Bemme", "ean": "7899918943287", "campanha": 1}
]


ESSENCE = [
    {"n": "TOALHA UMED.ESSENCE ALL BABY C/140UN", "c": "Linha Essence All", "de": 10.99, "pc": 7.99, "e": 224, "f": "Essence All", "ean": "7898197416628", "comissao": 1},
    {"n": "ESSENCE ALL VITAMINA B12 C/60 CPS MORANGO MASTI", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 17, "f": "Essence All", "ean": "0040141781529", "comissao": 1},
    {"n": "ESSENCE ALL MAG5 C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 16, "f": "Essence All", "ean": "0040141781413", "comissao": 1},
    {"n": "ESSENCE ALL HOMEM C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 15, "f": "Essence All", "ean": "0040141781475", "comissao": 1},
    {"n": "ESSENCE ALL SENIOR C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 13, "f": "Essence All", "ean": "0040141781420", "comissao": 1},
    {"n": "ESSENCE ALL 6 MAGNESIOS C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 12, "f": "Essence All", "ean": "0631430486395", "comissao": 1},
    {"n": "ESSENCE ALL CABELO PELE E UNHA C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 12, "f": "Essence All", "ean": "0042882082231", "comissao": 1},
    {"n": "ESSENCE ALL MULHER C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 12, "f": "Essence All", "ean": "0040141781505", "comissao": 1},
    {"n": "ESSENCE ALL COLAGENO CURCUMA  A.H C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 11, "f": "Essence All", "ean": "0040141781451", "comissao": 1},
    {"n": "ESSENCE ALL COLAGENO TIPO 2 C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 11, "f": "Essence All", "ean": "0042882082217", "comissao": 1},
    {"n": "ESSENCE ALL COMPLEXO B C/100 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 11, "f": "Essence All", "ean": "0040141779038", "comissao": 1},
    {"n": "ESSENCE ALL OMEGA 3  C/120 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 11, "f": "Essence All", "ean": "0040141779014", "comissao": 1},
    {"n": "ESSENCE ALL CALCIO MDK C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 9, "f": "Essence All", "ean": "0042882082224", "comissao": 1},
    {"n": "ESSENCE ALL AZ C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 7, "f": "Essence All", "ean": "0040141781437", "comissao": 1},
    {"n": "ESSENCE ALL SENIOR 50+ CHOCOLATE 800G", "c": "Linha Essence All", "de": 124.9, "pc": 109.9, "e": 6, "f": "Essence All", "ean": "0631430487125", "comissao": 1},
    {"n": "ESSENCE ALL CURCUMA LONGA C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 5, "f": "Essence All", "ean": "0040141779045", "comissao": 1},
    {"n": "ESSENCE ALL MELATONINA SL C/100 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 4, "f": "Essence All", "ean": "0040141781499", "comissao": 1},
    {"n": "ESSENCE ALL MULTI KIDS C/60 CPS MORANGO", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 4, "f": "Essence All", "ean": "0042882082200", "comissao": 1},
    {"n": "ESSENCE ALL THERMO ALL C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 4, "f": "Essence All", "ean": "0040141778987", "comissao": 1},
    {"n": "ESSENCE ALL BIOTINA C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 3, "f": "Essence All", "ean": "0040141779007", "comissao": 1},
    {"n": "ESSENCE ALL SENIOR 50+ SEM SABOR 800G", "c": "Linha Essence All", "de": 124.9, "pc": 109.9, "e": 3, "f": "Essence All", "ean": "0631430487132", "comissao": 1},
    {"n": "ESSENCE ALL TESTO ENERGY C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 3, "f": "Essence All", "ean": "0040141781512", "comissao": 1},
    {"n": "ESSENCE ALL VITAMINA B12 C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 3, "f": "Essence All", "ean": "0040141779069", "comissao": 1},
    {"n": "ESSENCE ALL CAFEINA C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 2, "f": "Essence All", "ean": "0040141781444", "comissao": 1},
    {"n": "ESSENCE ALL CLORETO MAGNESIO P.A. C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 2, "f": "Essence All", "ean": "0040141779052", "comissao": 1},
    {"n": "ESSENCE ALL MAGNESIO INOSITOL 180G", "c": "Linha Essence All", "de": 84.9, "pc": 69.9, "e": 2, "f": "Essence All", "ean": "0631430486388", "comissao": 1},
    {"n": "ESSENCE ALL NAC C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 2, "f": "Essence All", "ean": "0631430486371", "comissao": 1},
    {"n": "ESSENCE ALL PICOLINATO DE CROMO C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 2, "f": "Essence All", "ean": "0040141778994", "comissao": 1},
    {"n": "ESSENCE ALL CARBONATO DE CALCIO C/60 CPS", "c": "Linha Essence All", "de": 105.9, "pc": 69.9, "e": 1, "f": "Essence All", "ean": "0631430486401", "comissao": 1}
]


JORNAL = [
    {"n": "KIT SEDA SH 300ML+COND 190ML LUMINOUS GLYCOL+VITAM C COMPLEX RB", "c": "Cabelos", "de": 19.99, "pc": 17.99, "e": 1, "f": "UNILEVER", "ean": "7891150099982", "jornal": 1},
    {"n": "KIT SEDA SH 300ML+COND 190ML TOQUE DE SEDA RB", "c": "Cabelos", "de": 19.99, "pc": 17.99, "e": 4, "f": "UNILEVER", "ean": "7891150101630", "jornal": 1},
    {"n": "DES DOVE AER ORIGINAL 150ML RB JORNAL", "c": "Perfumes & Desodorantes", "de": 20, "pc": 15.89, "e": 181, "f": "UNILEVER", "ean": "7506306241183", "jornal": 1},
    {"n": "DES DOVE ROLL ON ORIGINAL 50ML RB", "c": "Perfumes & Desodorantes", "de": 15.9, "pc": 11.29, "e": 9, "f": "UNILEVER", "ean": "78924468", "jornal": 1},
    {"n": "SAB REXONA ANTIBACTERIAL FRESH 84G RB", "c": "Higiene & Banho", "de": 4.5, "pc": 2.49, "e": 3, "f": "UNILEVER", "ean": "7891150034952", "jornal": 1},
    {"n": "SAB REXONA ANTIBACTERIAL LIMP PROFUNDA 84G RB", "c": "Dermocosmeticos", "de": 4.5, "pc": 2.49, "e": 3, "f": "UNILEVER", "ean": "7891150066908", "jornal": 1},
    {"n": "SAB REXONA ANTIBACTERIAL BAMBOO & ALOE 84G RB", "c": "Higiene & Banho", "de": 4.5, "pc": 2.49, "e": 5, "f": "UNILEVER", "ean": "7891150024816", "jornal": 1},
    {"n": "SAB REXONA ANTIBACTERIAL MULTIVITAMINAS 84G RB", "c": "Higiene & Banho", "de": 4.5, "pc": 2.49, "e": 4, "f": "UNILEVER", "ean": "7891150083288", "jornal": 1},
    {"n": "SAB REXONA ANTIBACTERIAL FRUTAS VERMELHAS 84G RB", "c": "Higiene & Banho", "de": 4.5, "pc": 2.49, "e": 1, "f": "UNILEVER", "ean": "7891150083271", "jornal": 1},
    {"n": "SAB REXONA ANTIBACTERIAL ERVA DOCE 84G RB", "c": "Dermocosmeticos", "de": 4.5, "pc": 2.49, "e": 13, "f": "UNILEVER", "ean": "7891150083264", "jornal": 1},
    {"n": "SAB LIQ DOVE OLEO DE BANHO GLICERINADO 240ML RB JORNAL", "c": "Higiene & Banho", "de": 39.1, "pc": 29.99, "e": 3, "f": "UNILEVER", "ean": "7891150098442", "jornal": 1},
    {"n": "SH PANTENE BAMBU 400ML RB", "c": "Cabelos", "de": 41.8, "pc": 24.8, "e": 2, "f": "P&G", "ean": "7500435154239", "jornal": 1},
    {"n": "CR HID NIVEA LATA 56G RB", "c": "Dermocosmeticos", "de": 26.55, "pc": 21.59, "e": 20, "f": "NIVEA", "ean": "78906617", "jornal": 1},
    {"n": "FIO DENTAL J&J ESSENCIAL MENTA 100MT RB", "c": "Higiene Bucal", "de": 23.8, "pc": 16.99, "e": 5, "f": "JOHNSON & JOHNSON LT", "ean": "7891010501105", "jornal": 1},
    {"n": "ENX BUC LISTERINE COOL MINT SUAVE S/AL 500ML RB", "c": "Higiene Bucal", "de": 31.25, "pc": 20.49, "e": 6, "f": "JOHNSON & JOHNSON", "ean": "7891010974312", "jornal": 1},
    {"n": "ENX BUC LISTERINE MELANCIA E HORTELA ZERO 500ML RB", "c": "Higiene Bucal", "de": 28.99, "pc": 20.49, "e": 3, "f": "JOHNSON OTC", "ean": "7891010256050", "jornal": 1},
    {"n": "ESC DENT COLG CLASSIC CLEAN 3UN RB", "c": "Higiene Bucal", "de": 17.8, "pc": 11.49, "e": 3, "f": "COLGATE", "ean": "7891024026434", "jornal": 1},
    {"n": "CR DENT COLG T12 ADVANCED FRESH 90G RB", "c": "Higiene Bucal", "de": 18.3, "pc": 11.99, "e": 1, "f": "JOHNSON OTC", "ean": "7891024135310", "jornal": 1},
    {"n": "ABS INTIMUS TD PROTEGIDA TRI PROT SUA C/ABAS 32UN RB", "c": "Higiene Intima", "de": 21.1, "pc": 14.99, "e": 8, "f": "UNILEVER", "ean": "7896007544042", "jornal": 1},
    {"n": "ABS INTIMUS TD PROTEGIDA TRI PROT SEC C/ABAS 32UN RB", "c": "Higiene Intima", "de": 21.1, "pc": 14.99, "e": 8, "f": "JOHNSON OTC", "ean": "7896007544059", "jornal": 1},
    {"n": "DES NIVEA STICK MEN CLINICAL DERMA PROTECT 54G RB", "c": "Perfumes & Desodorantes", "de": 33.5, "pc": 24.89, "e": 1, "f": "NIVEA", "ean": "4006000045504", "jornal": 1},
    {"n": "ROUPA INTIMA PLENITUD PLUS FIT G/XG (2X16UN) RB JORNAL", "c": "Fraldas", "de": 98.25, "pc": 64.9, "e": 7, "f": "KIMBERLY CLARK", "ean": "7896007547210", "jornal": 1},
    {"n": "ROUPA INTIMA PLENITUD PLUS FIT P/M (2X16UN) RB JORNAL", "c": "Fraldas", "de": 98.25, "pc": 64.9, "e": 2, "f": "KIMBERLY CLARK", "ean": "7896007547203", "jornal": 1},
    {"n": "DES MONANGE AER HIDR INT EXT OLIVA 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 19, "f": "20", "ean": "7891350034646", "jornal": 1},
    {"n": "DES MONANGE AER INVISIBLE 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 12, "f": "20", "ean": "7898919411900", "jornal": 1},
    {"n": "DES MONANGE AER SENSIVEL S/PERF 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 7, "f": "JOHNSON OTC", "ean": "7891350034615", "jornal": 1},
    {"n": "DES MONANGE AER ANTITRANSP DETOX 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 7, "f": "20", "ean": "7896235353904", "jornal": 1},
    {"n": "DES MONANGE AER PROTECAO SECA 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 10, "f": "20", "ean": "7896235353911", "jornal": 1},
    {"n": "DES MONANGE AER ESPORTE 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 2, "f": "JOHNSON OTC", "ean": "7896235354208", "jornal": 1},
    {"n": "DES BOZZANO AER EXTREME 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 12, "f": "BOZZANO", "ean": "7891350032857", "jornal": 1},
    {"n": "DES BOZZANO AER FRESH 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 4, "f": "HYPERMARCAS", "ean": "7891350032741", "jornal": 1},
    {"n": "DES BOZZANO AER S/PERF 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 11, "f": "HYPERMARCAS", "ean": "7891350032406", "jornal": 1},
    {"n": "DES BOZZANO AER INVISIBLE 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 22, "f": "20", "ean": "7891350032970", "jornal": 1},
    {"n": "DES BOZZANO AER ANTI CARVAO 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 5, "f": "BOZZANO", "ean": "7891350037807", "jornal": 1},
    {"n": "DES BOZZANO AER DRY 150ML RB", "c": "Perfumes & Desodorantes", "de": 11.2, "pc": 9.49, "e": 7, "f": "BOZZANO", "ean": "7891350037791", "jornal": 1},
    {"n": "OLEO DE AMENDOAS DES CORPO PAIXAO TENTADORA 100ML RB", "c": "Perfumes & Desodorantes", "de": 16, "pc": 10.99, "e": 1, "f": "JOHNSON & JOHNSON", "ean": "7898919411931", "jornal": 1},
    {"n": "OLEO DE AMENDOAS DES CORPO PAIXAO FLOR BAUNILHA 100ML RB", "c": "Perfumes & Desodorantes", "de": 16, "pc": 10.99, "e": 1, "f": "20", "ean": "7896235354048", "jornal": 1},
    {"n": "OLEO DE AMENDOAS DES CORPO PAIXAO INSP ROSAS BRANCAS 100ML RB", "c": "Dermocosmeticos", "de": 16, "pc": 10.99, "e": 1, "f": "JOHNSON & JOHNSON", "ean": "7896235354017", "jornal": 1},
    {"n": "OLEO DE AMENDOAS DES CORPO PAIXAO IRRES FLOR DE LIS 100ML RB", "c": "Dermocosmeticos", "de": 16, "pc": 10.99, "e": 4, "f": "JOHNSON & JOHNSON", "ean": "7896235354024", "jornal": 1},
    {"n": "PROT SOL SUNDOWN TRIPLA PROTECAO FPS50 100ML RB", "c": "Dermocosmeticos", "de": 49.7, "pc": 41.99, "e": 1, "f": "JOHNSON OTC", "ean": "7891010258139", "jornal": 1},
    {"n": "PROT FACIAL NEUTROGENA SUN FRESH DERM CARE FPS70 40G RB", "c": "Dermocosmeticos", "de": 96.2, "pc": 66.99, "e": 2, "f": "JOHNSON & JOHNSON", "ean": "7891010253196", "jornal": 1},
    {"n": "PROT FACIAL NEUTROGENA SUN FRESH DERM CARE MORENA FPS70 40G RB", "c": "Dermocosmeticos", "de": 79.5, "pc": 66.99, "e": 1, "f": "JOHNSON & JOHNSON", "ean": "7891010253219", "jornal": 1},
    {"n": "TOALHA UMED BEBE FOFINHO PREMIUM 120UN (CX 12UN) RB JORNAL", "c": "Bebe & Infantil", "de": 15.99, "pc": 11.99, "e": 12, "f": "20", "ean": "7897622318568", "jornal": 1},
    {"n": "TOALHA UMED BEBE FOFINHO PLUS 140UN (CX 12UN) RB JORNAL", "c": "Bebe & Infantil", "de": 10, "pc": 7.99, "e": 143, "f": "20", "ean": "7897622318605", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PLUS TAMANHO P (4X96UN) RB", "c": "Fraldas", "de": 58.9, "pc": 47.9, "e": 3, "f": "20", "ean": "7898972620165", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PLUS TAMANHO M (4X80UN) RB", "c": "Fraldas", "de": 58.9, "pc": 47.9, "e": 5, "f": "20", "ean": "7898972620172", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PLUS TAMANHO G (4X72UN) RB", "c": "Fraldas", "de": 58.9, "pc": 47.9, "e": 6, "f": "20", "ean": "7898972620189", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PLUS TAMANHO XG (4X64UN) RB", "c": "Fraldas", "de": 58.9, "pc": 47.9, "e": 8, "f": "20", "ean": "7898972620196", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PLUS TAMANHO XXG (4X54UN) RB", "c": "Fraldas", "de": 58.9, "pc": 47.9, "e": 8, "f": "20", "ean": "7898972620202", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PREMIUM JUMBO XG (4X56UN) RB", "c": "Fraldas", "de": 68.4, "pc": 54.9, "e": 7, "f": "20", "ean": "7899693238905", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PREMIUM JUMBO M (4X68UN) RB", "c": "Fraldas", "de": 68.4, "pc": 54.9, "e": 4, "f": "20", "ean": "7899693238882", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PREMIUM JUMBO XXG (4X48UN) RB", "c": "Fraldas", "de": 68.4, "pc": 54.9, "e": 4, "f": "20", "ean": "7899693238912", "jornal": 1},
    {"n": "FRALDA BEBE FOFINHO PREMIUM JUMBO G (4X60UN) RB", "c": "Fraldas", "de": 68.4, "pc": 54.9, "e": 4, "f": "20", "ean": "7899693238899", "jornal": 1},
    {"n": "FRALDA HUGGIES MAXIMA PROTECAO HIPERZINHA XXG (3X54UN) JORNAL RB", "c": "Fraldas", "de": 99, "pc": 79.9, "e": 8, "f": "KIMBERLY -CLARK BRASIL INDUSTRIA E COMER", "ean": "7896007552849", "jornal": 1},
    {"n": "FRALDA HUGGIES MAXIMA PROTECAO HIPERZINHA M (3X66UN) JORNAL RB", "c": "Fraldas", "de": 99, "pc": 79.9, "e": 5, "f": "LIMA  PERGHER", "ean": "7896007552788", "jornal": 1},
    {"n": "FRALDA HUGGIES MAXIMA PROTECAO HIPERZINHA G (3X58UN) JORNAL RB", "c": "Fraldas", "de": 99, "pc": 79.9, "e": 6, "f": "KIMBERLY -CLARK BRASIL INDUSTRIA E COMER", "ean": "7896007552801", "jornal": 1},
    {"n": "FRALDA MILI BABY GIGA G (4X72UN) JORNAL", "c": "Fraldas", "de": 75.88, "pc": 64.9, "e": 9, "f": "MILI S.A", "ean": "7896104992159", "jornal": 1},
    {"n": "FRALDA MILI BABY GIGA M (4X80UN) JORNAL", "c": "Fraldas", "de": 75.88, "pc": 64.9, "e": 2, "f": "MILI S.A", "ean": "7896104992166", "jornal": 1},
    {"n": "FRALDA MILI BABY GIGA XG (4X62UN) JORNAL", "c": "Fraldas", "de": 75.88, "pc": 64.9, "e": 9, "f": "MILI S.A", "ean": "7896104992142", "jornal": 1},
    {"n": "FRALDA MILI BABY GIGA XXG (4X52UN) JORNAL", "c": "Fraldas", "de": 75.88, "pc": 64.9, "e": 15, "f": "MILI S.A", "ean": "7896104992135", "jornal": 1},
    {"n": "SAB LIQ GRANADO BEBE TRADICIONAL 250ML RB", "c": "Higiene & Banho", "de": 33.8, "pc": 24.99, "e": 6, "f": "GRANADO", "ean": "7896512904621", "jornal": 1},
    {"n": "CREATINA HARDCORE 300G JORNAL RB", "c": "Vitaminas & Nutricao", "de": 89.9, "pc": 54.9, "e": 1, "f": "INTEGRAL MEDICA", "ean": "7896311708314", "jornal": 1},
    {"n": "MAG PLUS 6 60CAPS RB", "c": "Vitaminas & Nutricao", "de": 59.95, "pc": 50.89, "e": 2, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303264594", "jornal": 1},
    {"n": "COBALAMAX SB FRUTAS VERMELHAS 60CPR MAST RB", "c": "Vitaminas & Nutricao", "de": 44.99, "pc": 35.9, "e": 1, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303265225", "jornal": 1}
]


CATALOGO = [
    {"n": "NUTRIOL LOC.ANTICOCEIRA 390ML", "c": "Dermocosmeticos", "de": 140.4, "pc": 125.9, "e": 3, "f": "DARROW LAB. S/A", "ean": "3282770388497"},
    {"n": "CR.NIVEA LUMINOUS FLUIDO FPS50 30ML", "c": "Dermocosmeticos", "de": 117.9, "pc": 105.9, "e": 3, "f": "NIVEA", "ean": "4005900813046"},
    {"n": "CR.HID.CERAVE 200G", "c": "Dermocosmeticos", "de": 101.8, "pc": 91.6, "e": 4, "f": "JOHNSON OTC", "ean": "7899706159173"},
    {"n": "CICAPLAST BAUME B5 40ML", "c": "Dermocosmeticos", "de": 103, "pc": 91.9, "e": 6, "f": "LA ROCHE-POSAY", "ean": "7908615000244"},
    {"n": "EPISOL INTENSE FPS60 200ML", "c": "Dermocosmeticos", "de": 126.39, "pc": 108.9, "e": 6, "f": "COSMED INDUSTRIA DE COSMETICOS E MEDICAM", "ean": "7891142205131"},
    {"n": "EPISOL SEC ACQUA FPS60 40ML", "c": "Dermocosmeticos", "de": 107.45, "pc": 96.7, "e": 3, "f": "MANTECORP", "ean": "7891142984203"},
    {"n": "FUTURA BIOTECH ANTIT.DERM ONE ROLLON 65ML", "c": "Dermocosmeticos", "de": 58.99, "pc": 52.8, "e": 16, "f": "FUTURA BIOTECH", "ean": "7898901366621"},
    {"n": "PRINCIPIA 10% UREIA+5% GLICERINA+5% OL DE SEMENTE", "c": "Dermocosmeticos", "de": 74.79, "pc": 67.3, "e": 3, "f": "PRINCIPIA", "ean": "0070341368879"},
    {"n": "CR.HID.CERAVE 340G", "c": "Dermocosmeticos", "de": 94.75, "pc": 85.2, "e": 3, "f": "JOHNSON OTC", "ean": "7908615086309"},
    {"n": "LOC.HID.NIVEA BODY MILK 200Ml", "c": "Dermocosmeticos", "de": 17.5, "pc": 15.75, "e": 26, "f": "NIVEA", "ean": "4005808309436"},
    {"n": "P.SOLAR ANASOL OIL FREE E TOQUE SECO FPS75 200G", "c": "Dermocosmeticos", "de": 50.8, "pc": 45.7, "e": 3, "f": "DAHUER LABORATORIO LTDA", "ean": "7897230305165"},
    {"n": "P.SOLAR NIVEA SUN FPS30 200ML", "c": "Dermocosmeticos", "de": 63, "pc": 56.7, "e": 3, "f": "NIVEA", "ean": "4005808555307"},
    {"n": "LOC.HID.NIVEA BODY Q10 FIRMADOR 400ML", "c": "Dermocosmeticos", "de": 57.4, "pc": 51.5, "e": 4, "f": "NIVEA", "ean": "4005900116192"},
    {"n": "PRINCIPIA GEL DE LIMPEZA 350G GL-01 JORNAL", "c": "Dermocosmeticos", "de": 57.6, "pc": 54, "e": 3, "f": "PRINCIPIA", "ean": "0609963220564"},
    {"n": "ABELHA RAINHA OLEO ROSA MOSQUETA PURO 20ML", "c": "Dermocosmeticos", "de": 46.4, "pc": 41.75, "e": 3, "f": "ABELHA RAINHA", "ean": "7898728324996"},
    {"n": "PRINCIPIA CREME CALMANTE MULTIREPARADOR 17,5%", "c": "Dermocosmeticos", "de": 54.6, "pc": 49, "e": 3, "f": "PRINCIPIA", "ean": "0609963220670"},
    {"n": "EPISOL SEC OC FPS60 CLARO 60G", "c": "Dermocosmeticos", "de": 103.79, "pc": 92.5, "e": 3, "f": "MANTECORP", "ean": "7891142207166"},
    {"n": "EPISOL COLOR TOM2 CLARO FPS70 40ML", "c": "Dermocosmeticos", "de": 94.85, "pc": 84.99, "e": 3, "f": "MANTECORP", "ean": "7891142205643"},
    {"n": "EPISOL COLOR TOM3 MEDIO FPS70 40ML", "c": "Dermocosmeticos", "de": 94.85, "pc": 84.99, "e": 3, "f": "MANTECORP", "ean": "7891142205704"},
    {"n": "LOC.HID.VASENOL GELEIA VASELINA 100ML", "c": "Dermocosmeticos", "de": 36.7, "pc": 32.9, "e": 7, "f": "JOHNSON OTC", "ean": "7891150029323"},
    {"n": "REPEL.OFF ACTIVE SPRAY 170ML", "c": "Dermocosmeticos", "de": 43.69, "pc": 39.3, "e": 4, "f": "JOHNSON OTC", "ean": "7894650009598"},
    {"n": "LOC.HID.NIVEA BODY Q10 FIRMADOR 200ML", "c": "Dermocosmeticos", "de": 39.85, "pc": 35.8, "e": 3, "f": "JOHNSON OTC", "ean": "4005808311286"},
    {"n": "CR.HID.NIVEA VISAGE Q10 PLUS NOT.50G.", "c": "Dermocosmeticos", "de": 52.2, "pc": 46.9, "e": 3, "f": "NIVEA", "ean": "4005808812899"},
    {"n": "P.SOLAR NIVEA  FACIAL FPS70 40ML", "c": "Dermocosmeticos", "de": 49.5, "pc": 44.5, "e": 4, "f": "NIVEA", "ean": "4005900980397"},
    {"n": "CR.HID.NIVEA 145G", "c": "Dermocosmeticos", "de": 48, "pc": 42.9, "e": 5, "f": "NIVEA", "ean": "4005900408891"},
    {"n": "LOC.HID.NIVEA BODY SOFT MILK 400ML", "c": "Dermocosmeticos", "de": 32.2, "pc": 28.9, "e": 7, "f": "NIVEA", "ean": "4005900004956"},
    {"n": "P.SOLAR EXP FAC.ANTIRRUGAS COR FPS60 40G", "c": "Dermocosmeticos", "de": 60.5, "pc": 54.45, "e": 4, "f": "LOREAL", "ean": "7899706184960"},
    {"n": "EPISOL COLOR  SMART FPS50 40ML", "c": "Dermocosmeticos", "de": 93.6, "pc": 83.5, "e": 3, "f": "MANTECORP", "ean": "7891142205735"},
    {"n": "ABS.MILI NOTURNO SUAVE C/ABAS 32UN", "c": "Higiene Intima", "de": 29.8, "pc": 26.8, "e": 156, "f": "MILI S.A", "ean": "7896104992777"},
    {"n": "ABS.INTIMUS NOT SUAVE C/ABAS 30UN", "c": "Higiene Intima", "de": 35.75, "pc": 32.1, "e": 14, "f": "KIMBERLY CLARK", "ean": "7896007550890"},
    {"n": "ABS.ALWAYS NOTURNO SECA C/ABAS XXG C/10", "c": "Higiene Intima", "de": 45.45, "pc": 40.9, "e": 6, "f": "PROCTER & GAMBLE", "ean": "7506309805498"},
    {"n": "ABS.INTIMUS NOT SECA C/ABAS 30UN", "c": "Higiene Intima", "de": 35.75, "pc": 32.5, "e": 4, "f": "KIMBERLY CLARK", "ean": "7896007550906"},
    {"n": "AP.VENUS SIMPLY ROSA C/2", "c": "Higiene Intima", "de": 25.8, "pc": 23.2, "e": 4, "f": "P&G", "ean": "7702018072392"},
    {"n": "ABS.BIOFRAL MAXI GERIATRIC C/20", "c": "Higiene Intima", "de": 32.7, "pc": 29.4, "e": 5, "f": "DIVERSOS", "ean": "7896770900038"},
    {"n": "ABS.INTIMUS NOT.SUAVE C/ABAS 16UN", "c": "Higiene Intima", "de": 23, "pc": 20.7, "e": 8, "f": "KIMBERLY CLARK", "ean": "7896007550883"},
    {"n": "COTONETE J&J C/150", "c": "Higiene Intima", "de": 21, "pc": 18.9, "e": 6, "f": "JOHNSON & JOHNSON", "ean": "7891010560812"},
    {"n": "DES.REXONA CLINICAL EXTRA DRY 58G", "c": "Higiene Intima", "de": 36, "pc": 32.4, "e": 9, "f": "UNILEVER", "ean": "0000075076870"},
    {"n": "ABS.BIGFRAL REGULAR 20UN", "c": "Higiene Intima", "de": 27.7, "pc": 24.9, "e": 6, "f": "ONTEX", "ean": "7896012880531"},
    {"n": "ABS.OB INTERNO COMFORT MEDIO C/16", "c": "Higiene Intima", "de": 29.99, "pc": 26.99, "e": 4, "f": "JOHNSON & JOHNSON", "ean": "7891010245085"},
    {"n": "DEPIL.NEORLY CR.P/ CORPO SENSE DELICADA 120GR.", "c": "Higiene Intima", "de": 39.4, "pc": 35.4, "e": 3, "f": "JOHNSON OTC", "ean": "7898302722507"},
    {"n": "ABS.S.L.SUAVE NOT C/ABAS LV 32 PG24", "c": "Higiene Intima", "de": 47.3, "pc": 42.5, "e": 4, "f": "KIMBERLY CLARK", "ean": "7891010518844"},
    {"n": "COTONETE JEJ CX C/300 NEU", "c": "Higiene Intima", "de": 34.85, "pc": 31.3, "e": 4, "f": "JOHNSON & JOHNSON", "ean": "7891010047764"},
    {"n": "ABS.DRY MAN MASC. C/10", "c": "Higiene Intima", "de": 26.3, "pc": 23.59, "e": 4, "f": "PADRO CLB MACEDO", "ean": "7894513142066"},
    {"n": "ABS.S.L.ADAPT.PLUS SUAVE C/AB C/32", "c": "Higiene Intima", "de": 31.5, "pc": 28.35, "e": 4, "f": "JOHNSON & JOHNSON", "ean": "7891010704780"},
    {"n": "COTONETE J&J C/150 POTE", "c": "Higiene Intima", "de": 24.5, "pc": 21.9, "e": 6, "f": "JOHNSON OTC", "ean": "7891010032937"},
    {"n": "TENYS PE JATO SECO CANFORADO 92G", "c": "Higiene Intima", "de": 26.6, "pc": 23.9, "e": 3, "f": "BARUEL LTDA", "ean": "7896020160168"},
    {"n": "ABS.CAREFREE NEUTRALIZE S/PERF.C/40", "c": "Higiene Intima", "de": 24.2, "pc": 21.7, "e": 3, "f": "JOHNSON OTC", "ean": "7891010875596"},
    {"n": "ABS.INTIMUS DAYS S/PERF. L80P70", "c": "Higiene Intima", "de": 23.61, "pc": 21.22, "e": 3, "f": "KIMBERLY CLARK", "ean": "7896007546039"},
    {"n": "ABS.S.L.ADAPT.PLUS SUAVE C/AB C/16", "c": "Higiene Intima", "de": 19.3, "pc": 17.3, "e": 3, "f": "JOHNSON & JOHNSON", "ean": "7891010579616"},
    {"n": "AP.GILLETTE CORPO C/2UN", "c": "Higiene Intima", "de": 24.7, "pc": 22.2, "e": 3, "f": "GILHETE DO BRASIL", "ean": "7500435178594"},
    {"n": "ABS.INTIMUS DAYS S/PERF.L40P30", "c": "Higiene Intima", "de": 18.2, "pc": 16.3, "e": 4, "f": "JOHNSON OTC", "ean": "7896007542482"},
    {"n": "ABS P/SEIOS AMAMENTE C/12 UNID", "c": "Higiene Intima", "de": 16.99, "pc": 15.29, "e": 4, "f": "JOHNSON OTC", "ean": "7897211100130"},
    {"n": "SUSTAGEN SENIOR ADULTOS 50+ SEM SABOR 740G", "c": "Vitaminas & Nutricao", "de": 197.34, "pc": 169.91, "e": 3, "f": "APENAS BOA NUTRIÇÃO INDUSTRIA", "ean": "7898941911300"},
    {"n": "MAG PLUS 5 550MG 60CAPS", "c": "Vitaminas & Nutricao", "de": 55.99, "pc": 49.99, "e": 5, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7908699000024"},
    {"n": "ESSENCE ALL SENIOR 50+ SEM SABOR 800G", "c": "Vitaminas & Nutricao", "de": 124.9, "pc": 109.9, "e": 3, "f": "LIV HEALTH LTDA", "ean": "0631430487132"},
    {"n": "NUTREN SENIOR PO CAFE C/LEITE 740G", "c": "Vitaminas & Nutricao", "de": 187.3, "pc": 168.5, "e": 3, "f": "NESTLE  IND. COM. LT", "ean": "7891000287699"},
    {"n": "NUTREN SENIOR PO S/SABOR 740G", "c": "Vitaminas & Nutricao", "de": 187.3, "pc": 168.5, "e": 3, "f": "NESTLE  IND. COM. LT", "ean": "7891000103487"},
    {"n": "ENSURE BAUNILHA 850G", "c": "Vitaminas & Nutricao", "de": 271.7, "pc": 239.9, "e": 3, "f": "ABBOTT", "ean": "7891158105203"},
    {"n": "ZINCO QUELATO 60CAPS HERBAMED", "c": "Vitaminas & Nutricao", "de": 33.15, "pc": 28.7, "e": 4, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303260954"},
    {"n": "APIS FLORA EXT. PROPOLIS S/ALCOOL  30ML", "c": "Vitaminas & Nutricao", "de": 44.2, "pc": 39.6, "e": 5, "f": "APIS FLORA", "ean": "7896663301317"},
    {"n": "APIS FLORA EXTRATO DE PROPOLIS VERDE 30ML", "c": "Vitaminas & Nutricao", "de": 42.5, "pc": 38.25, "e": 9, "f": "APIS FLORA", "ean": "7896663302550"},
    {"n": "MAGNESIO DIMALATO 400MG 60CAPS HERBAMED", "c": "Vitaminas & Nutricao", "de": 40.6, "pc": 33.9, "e": 3, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303262699"},
    {"n": "NUTREN SENIOR PO BAUNILHA 370G", "c": "Vitaminas & Nutricao", "de": 97, "pc": 85.5, "e": 3, "f": "NESTLE LTDA", "ean": "7891000241547"},
    {"n": "BARRA NUTRATA CHARGE 45G", "c": "Vitaminas & Nutricao", "de": 18.9, "pc": 18.9, "e": 9, "f": "MMC INDUSTRIA DE PRODUTOS NUTRACEUTICOS", "ean": "7900392000103"},
    {"n": "APIS FLORA EXTRATO DE PROPOLIS VERDE 70ML", "c": "Vitaminas & Nutricao", "de": 60.9, "pc": 54.8, "e": 4, "f": "APIS FLORA", "ean": "7896663322473"},
    {"n": "ADOC.STEVIA PLUS 80ML", "c": "Vitaminas & Nutricao", "de": 23.3, "pc": 20.9, "e": 4, "f": "LOWCUCAR INDUSTRIA E COMERCIO DE ALIMENT", "ean": "7896292000186"},
    {"n": "APIS FLORA EXTRATO DE PROPOLIS 30ML", "c": "Vitaminas & Nutricao", "de": 31.99, "pc": 28.79, "e": 4, "f": "APIS FLORA", "ean": "7896663300204"},
    {"n": "GUARANA PO 170G.CAXINAUA", "c": "Vitaminas & Nutricao", "de": 68.9, "pc": 61.9, "e": 3, "f": "CAXINAUA LAB.", "ean": "7897554400027"},
    {"n": "SUSTAGEN KIDS MORANGO 380G", "c": "Vitaminas & Nutricao", "de": 41.9, "pc": 37.5, "e": 5, "f": "APENAS BOA NUTRIÇÃO INDUSTRIA", "ean": "7898941911072"},
    {"n": "SUSTAGEN KIDS BAUNILHA 380G", "c": "Vitaminas & Nutricao", "de": 41.9, "pc": 37.5, "e": 3, "f": "JOHNSON & JOHNSON", "ean": "7898941911058"},
    {"n": "COENZIMA Q10 100MG 60CAPS HERBAMED", "c": "Vitaminas & Nutricao", "de": 62.24, "pc": 52.9, "e": 3, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7908699000239"},
    {"n": "SIMFORT PLUS C/60 CAPS", "c": "Vitaminas & Nutricao", "de": 149.7, "pc": 126.95, "e": 3, "f": "VITAFOR", "ean": "7898665433256"},
    {"n": "HERBAMED CAFEINA 210MG C/60 CPS HERBAMED", "c": "Vitaminas & Nutricao", "de": 42.01, "pc": 35.9, "e": 4, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303261135"},
    {"n": "FLEXIGOLD 40MG C/30 + 30", "c": "Vitaminas & Nutricao", "de": 108.95, "pc": 49.9, "e": 4, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303263597"},
    {"n": "HERBAMED CRANBERRY 500MG C/60 CPS", "c": "Vitaminas & Nutricao", "de": 39.05, "pc": 31.7, "e": 3, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303261180"},
    {"n": "BIOTINA 45MCG 60CAPS", "c": "Vitaminas & Nutricao", "de": 28.56, "pc": 19.9, "e": 4, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303263870"},
    {"n": "CLORETO DE MAGNESIO P.A 500MG C/60 CPSHERBAMED", "c": "Vitaminas & Nutricao", "de": 28.82, "pc": 19.9, "e": 4, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -", "ean": "7898303261050"},
    {"n": "BIONATUS CRISTAIS GENGIBRE LIMAO SAL ARDRAK", "c": "Vitaminas & Nutricao", "de": 21.6, "pc": 19.2, "e": 4, "f": "BIONATUS", "ean": "7896755400058"},
    {"n": "AGUA COLONIA POMPOM 100ML", "c": "Bebe & Infantil", "de": 22.2, "pc": 19.9, "e": 4, "f": "HYPERMARCAS", "ean": "7896012800867"},
    {"n": "MAM.AVENT PETALA BICO RITMO INDIVIDUAL 125ML", "c": "Bebe & Infantil", "de": 121.45, "pc": 109.3, "e": 3, "f": "PHILIPS.AVENT", "ean": "8720689007344"},
    {"n": "ASPIRADOR NASAL DE SUCCAO C/ESTOJO BUBA", "c": "Bebe & Infantil", "de": 42.35, "pc": 38.1, "e": 4, "f": "BUBA", "ean": "7908103718590"},
    {"n": "TALCO INF.J&J BABY REG. 100G", "c": "Bebe & Infantil", "de": 34.2, "pc": 30.5, "e": 3, "f": "JOHNSON OTC", "ean": "7702031244646"},
    {"n": "CHUP.AVENT SOOTHIE 4 A 6 MESES AZUL C/2 (AVENT)", "c": "Bebe & Infantil", "de": 121.45, "pc": 109.3, "e": 3, "f": "PHILIPS.AVENT", "ean": "8710103962342"},
    {"n": "LENCO UMED.BEPANTOL BABY 96UN L96P80", "c": "Bebe & Infantil", "de": 39, "pc": 34.9, "e": 6, "f": "BAYER", "ean": "7891106915182"},
    {"n": "BUBA KIT ESCOVA MAMADEIRA E BICO AZUL", "c": "Bebe & Infantil", "de": 30.4, "pc": 30.4, "e": 3, "f": "MOAS INDUSTRIA E COMERCIO IMPORTACAO E E", "ean": "7899525654149"},
    {"n": "SH.DOVE BABY 200ML", "c": "Bebe & Infantil", "de": 25.15, "pc": 22.6, "e": 3, "f": "UNILEVER", "ean": "7891150025929"},
    {"n": "KIT BANHO BABY MURIEL ROSA MENINA", "c": "Bebe & Infantil", "de": 39.99, "pc": 35.99, "e": 6, "f": "MURIEL", "ean": "7896279113502"},
    {"n": "COND.MEU LISINHO KIDS S.LINE 300ML", "c": "Bebe & Infantil", "de": 24.35, "pc": 21.9, "e": 4, "f": "SALONLINE", "ean": "7898623956209"},
    {"n": "KIT ESCOVA PARA MAMADEIRA BRANCO E ROSA", "c": "Bebe & Infantil", "de": 25.5, "pc": 25.5, "e": 3, "f": "MOAS INDUSTRIA E COMERCIO IMPORTACAO E E", "ean": "7899525654156"},
    {"n": "GIZ COLORIR CABELO IMPALA STITCH ANGEL AZUL 7,3G", "c": "Bebe & Infantil", "de": 38.18, "pc": 34.35, "e": 4, "f": "IMPALA", "ean": "7896111903155"},
    {"n": "BICO MAM.LILLO SUPER RED.LATEX C/1 REF.9497", "c": "Bebe & Infantil", "de": 35.33, "pc": 31.8, "e": 3, "f": "LILLO DO BRASIL", "ean": "7896033294973"},
    {"n": "BUBA BOWL EM SILICONE 350ML", "c": "Bebe & Infantil", "de": 61.2, "pc": 54.9, "e": 6, "f": "BUBA", "ean": "7908103756349"},
    {"n": "BUBA PRATINHO EM SILICONE", "c": "Bebe & Infantil", "de": 61.2, "pc": 54.9, "e": 4, "f": "BUBA", "ean": "7908103756318"},
    {"n": "BUBA KIT TALHER EM SILICONE E BAMBU", "c": "Bebe & Infantil", "de": 54.4, "pc": 48.9, "e": 4, "f": "BUBA", "ean": "7908103758275"},
    {"n": "OLEO DE GIRASSOL FARMAX 200ML", "c": "Higiene & Banho", "de": 28.99, "pc": 25.99, "e": 7, "f": "FARMAX", "ean": "7896902210998"},
    {"n": "BAND-AID C/40", "c": "Higiene & Banho", "de": 24.99, "pc": 22.49, "e": 15, "f": "JOHNSON OTC", "ean": "7891010504755"},
    {"n": "SAB.LIQ.DOVE OLEO DE BANHO GLICERINADO 240ML JORNAL", "c": "Higiene & Banho", "de": 39.1, "pc": 35.19, "e": 3, "f": "UNILEVER", "ean": "7891150098442"},
    {"n": "LENCO PAPEL ELITE C/150", "c": "Higiene & Banho", "de": 23.75, "pc": 21.3, "e": 5, "f": "JOHNSON OTC", "ean": "7896061953279"},
    {"n": "SAB.LIQ.GRANADO GLICERINA TRADICIONAL 300ML", "c": "Higiene & Banho", "de": 33.65, "pc": 29.99, "e": 3, "f": "GRANADO", "ean": "7896512939593"},
    {"n": "BAND-AID VARIADOS C 30", "c": "Higiene & Banho", "de": 29.99, "pc": 26.99, "e": 3, "f": "JOHNSON OTC", "ean": "7891010247263"},
    {"n": "AP.BARB.BIC SOLEIL COLOR L4P3", "c": "Higiene & Banho", "de": 25.2, "pc": 22.6, "e": 3, "f": "BIC.AP.BARB.", "ean": "0070330734425"},
    {"n": "SAB.LIQ.J&J BABY CABECA/PES GLICERINA 180ML REFIL", "c": "Higiene & Banho", "de": 23, "pc": 20.7, "e": 3, "f": "JOHNSON & JOHNSON", "ean": "7891010871031"},
    {"n": "ASEPXIA SAB.DETOX 80G", "c": "Higiene & Banho", "de": 22.09, "pc": 19.88, "e": 3, "f": "JOHNSON OTC", "ean": "7898636190874"},
    {"n": "MANITOL 20% 250ML", "c": "Higiene & Banho", "de": 22.3, "pc": 19.99, "e": 8, "f": "JOHNSON OTC", "ean": "7896137607730"},
    {"n": "SAB.LIQ.GRANADO BEBE GLICERINA 250ML JORNAL", "c": "Higiene & Banho", "de": 33.8, "pc": 24.99, "e": 6, "f": "GRANADO", "ean": "7896512904621"},
    {"n": "SAB.LIQ.DOVE ANTIBACTERIANO CUIDA PROTEGE 250ML", "c": "Higiene & Banho", "de": 23.4, "pc": 20.99, "e": 3, "f": "UNILEVER", "ean": "7891150075405"},
    {"n": "SAB.LIQ.OLEO MURIEL ARABE 230ML", "c": "Higiene & Banho", "de": 20.4, "pc": 18.3, "e": 3, "f": "MURIEL", "ean": "7896279129299"},
    {"n": "OLEO E SERUM DOVE UV REPAIR E GLOW+FERULICO 110ML", "c": "Cabelos", "de": 47.1, "pc": 42.39, "e": 3, "f": "UNILEVER", "ean": "7891150102798"},
    {"n": "OLEO ELSEVE EXTRAORDINARIO 100ML", "c": "Cabelos", "de": 47, "pc": 42.3, "e": 29, "f": "JOHNSON OTC", "ean": "7899026478909"},
    {"n": "SPRAY KARINA EXTRA FORTE 400ML", "c": "Cabelos", "de": 41, "pc": 36.9, "e": 4, "f": "JOHNSON OTC", "ean": "7893300521169"},
    {"n": "SPRAY KARINA NORMAL 400ML", "c": "Cabelos", "de": 41, "pc": 36.9, "e": 3, "f": "JOHNSON OTC", "ean": "7893300521084"},
    {"n": "PASTA D AGUA (PASTOL)100G", "c": "Cabelos", "de": 21, "pc": 18.8, "e": 16, "f": "JOHNSON OTC", "ean": "7897780209159"},
    {"n": "CR.NIELY GOLD QUERATINA 80G", "c": "Cabelos", "de": 28.14, "pc": 25.33, "e": 3, "f": "NIELYGOLD", "ean": "7908785464525"},
    {"n": "CR.TRAT.ELSEVE BOND REPAIR 200G", "c": "Cabelos", "de": 79.5, "pc": 71.5, "e": 3, "f": "LOREAL", "ean": "7908615092959"},
    {"n": "TINT.IMEDIA 3 CAST.ESC", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 16, "f": "LOREAL", "ean": "7896014140442"},
    {"n": "SH.PANTENE MOLECULAR 510ML", "c": "Cabelos", "de": 54.2, "pc": 48.7, "e": 4, "f": "PROCTER & GAMBLE", "ean": "7500435260312"},
    {"n": "SERUM ELSEVE COLLAGEN LIFTER 100ML", "c": "Cabelos", "de": 61, "pc": 54.9, "e": 4, "f": "JOHNSON OTC", "ean": "7908966529333"},
    {"n": "COND.ELSEVE CACHOS SELADOR 400ML", "c": "Cabelos", "de": 50.2, "pc": 44.9, "e": 10, "f": "LOREAL", "ean": "7899706197588"},
    {"n": "TINT.IMEDIA 6 LOURO ESCURO", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 8, "f": "LOREAL", "ean": "7896014140527"},
    {"n": "SERUM ELSEVE LISO DOS SONHOS 100ML", "c": "Cabelos", "de": 45.79, "pc": 41.2, "e": 6, "f": "LOREAL", "ean": "7908785461555"},
    {"n": "TINT.IMEDIA 4 CASTANHO NATURAL", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 7, "f": "LOREAL", "ean": "7896014140459"},
    {"n": "COND.ELSEVE LISO DOS SONHOS LIQUID HAIR 400ML", "c": "Cabelos", "de": 50.2, "pc": 44.9, "e": 7, "f": "LOREAL", "ean": "7908785461609"},
    {"n": "KIT TIONACHO SH+COND. ANTIQU/ENGR 415ML+200ML", "c": "Cabelos", "de": 68.69, "pc": 61.8, "e": 5, "f": "GENOM", "ean": "7898636191581"},
    {"n": "TINT.IMEDIA 5 CAST.CLARO", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 5, "f": "LOREAL", "ean": "7896014140480"},
    {"n": "COND.ELSEVE COLLAGEN LIFTER 400ML", "c": "Cabelos", "de": 50.2, "pc": 44.9, "e": 6, "f": "LOREAL", "ean": "7908966527193"},
    {"n": "TINT.IMEDIA 8 LOURO", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 4, "f": "LOREAL", "ean": "7896014140633"},
    {"n": "TINT.IMEDIA 8.1 LOU.SUECO", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 4, "f": "LOREAL", "ean": "7896014140640"},
    {"n": "TINT.IMEDIA 1 PRETO", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 3, "f": "LOREAL", "ean": "7896014140435"},
    {"n": "TINT.IMEDIA 6.1 LOU.ESC.ACINZ", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 3, "f": "LOREAL", "ean": "7896014140534"},
    {"n": "TINT.IMEDIA 6.41 MARRON", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 3, "f": "LOREAL", "ean": "7896014140558"},
    {"n": "CR.TRAT.ELSEVE COLLAGEN LIFTER 300G", "c": "Cabelos", "de": 35, "pc": 31.5, "e": 9, "f": "LOREAL", "ean": "7908966528367"},
    {"n": "SH.J&J BABY REGULAR 400ML", "c": "Cabelos", "de": 40.9, "pc": 36.8, "e": 4, "f": "JOHNSON OTC", "ean": "7891010800048"},
    {"n": "COND.ELSEVE OL.EXTRAOR.NUTRICAO 400ML", "c": "Cabelos", "de": 50.2, "pc": 44.9, "e": 3, "f": "LOREAL", "ean": "7898587774376"},
    {"n": "SH.J&J BABY 2 EM 1 400ML", "c": "Cabelos", "de": 45.1, "pc": 40.59, "e": 3, "f": "JOHNSON OTC", "ean": "7891010257101"},
    {"n": "AP.BARB.GILLETTE MACH 3 REGULAR C/1", "c": "Preservativos & Barbear", "de": 44, "pc": 39.6, "e": 8, "f": "GILHETE DO BRASIL", "ean": "7702018001071"},
    {"n": "AP.BARB.GILLETTE VENUS FEM.SIMPLY L4P3", "c": "Preservativos & Barbear", "de": 37.2, "pc": 33.4, "e": 5, "f": "P&G", "ean": "7500435004220"},
    {"n": "PRES.JONTEX SENSITIVE C/3", "c": "Preservativos & Barbear", "de": 21.59, "pc": 19.3, "e": 7, "f": "JOHNSON PR. PESSO", "ean": "7896222720009"},
    {"n": "AP.BARB.GILLETTE PREST.3 ICE C/2", "c": "Preservativos & Barbear", "de": 26.5, "pc": 23.85, "e": 6, "f": "JOHNSON OTC", "ean": "7702018983872"},
    {"n": "AP.PREST MASC ULTRAGRIP 3 PBC/2", "c": "Preservativos & Barbear", "de": 21.95, "pc": 19.75, "e": 9, "f": "GILHETE DO BRASIL", "ean": "7500435011297"},
    {"n": "CARGA GILLETTE MACH3 C/2", "c": "Preservativos & Barbear", "de": 20.5, "pc": 18.45, "e": 11, "f": "GILHETE DO BRASIL", "ean": "7500435179829"},
    {"n": "PRES.JONTEX LUBRIFICADO LV8 PG7", "c": "Preservativos & Barbear", "de": 27.3, "pc": 24.5, "e": 4, "f": "JOHNSON OTC", "ean": "7896222721075"},
    {"n": "PRES.OLLA LUB.BOL.LV8PG6", "c": "Preservativos & Barbear", "de": 23.1, "pc": 20.79, "e": 6, "f": "HYPERMARCAS", "ean": "7896222717788"},
    {"n": "AP.BARB.GILLETTE PREST.CARVAO ATIVADO C/2 UND", "c": "Preservativos & Barbear", "de": 24.5, "pc": 21.9, "e": 4, "f": "GILLETE DO BRASIL", "ean": "7500435245821"},
    {"n": "PRES.OLLA MORANGO C/6", "c": "Preservativos & Barbear", "de": 21.7, "pc": 19.5, "e": 3, "f": "HYPERMARCAS", "ean": "7896222718273"},
    {"n": "AP.PREST.PROBAK LEVE 7 PAGUE 5", "c": "Preservativos & Barbear", "de": 17.9, "pc": 15.9, "e": 5, "f": "JOHNSON OTC", "ean": "7891051040403"},
    {"n": "PRES.OLLA SENSITIVE C/6", "c": "Preservativos & Barbear", "de": 20.35, "pc": 18.3, "e": 4, "f": "HYPERMARCAS", "ean": "7896222717962"},
    {"n": "AP.BARB.BIC FLEX3 EXTRA SUAVE C/2UNID", "c": "Preservativos & Barbear", "de": 23.5, "pc": 23.5, "e": 4, "f": "BIC.AP.BARB.", "ean": "7501843503350"},
    {"n": "PRES.OLLA SENSITIVE C/3", "c": "Preservativos & Barbear", "de": 15.66, "pc": 15.66, "e": 5, "f": "HYPERMARCAS", "ean": "7896222717948"},
    {"n": "PRES.OLLA LUBRIF. C/6", "c": "Preservativos & Barbear", "de": 20.7, "pc": 18.6, "e": 5, "f": "HYPERMARCAS", "ean": "7896222716262"},
    {"n": "COREGA ULTRA CR.S/SABOR 40G", "c": "Higiene Bucal", "de": 86.3, "pc": 71.9, "e": 4, "f": "GLAXOSMITHKLINE", "ean": "7896009490651"},
    {"n": "PERIODENT DENTRAT ZERO 250ML", "c": "Higiene Bucal", "de": 22.3, "pc": 19.9, "e": 6, "f": "DENTRAT", "ean": "7898395843394"},
    {"n": "COREGA ULTRA TRIPLA  ACAO 70G", "c": "Higiene Bucal", "de": 93.9, "pc": 84.3, "e": 4, "f": "GLAXOSMITHKLINE", "ean": "7896009498787"},
    {"n": "PERIODENT DENTRAT 250ML", "c": "Higiene Bucal", "de": 20, "pc": 17.9, "e": 3, "f": "DENTRAT", "ean": "7898395843370"},
    {"n": "CR.D.COLG.SENSITIVE PRO ALIVIO IMEDIATO ORIG 140G", "c": "Higiene Bucal", "de": 31, "pc": 27.9, "e": 3, "f": "COLGATE", "ean": "7509546653402"},
    {"n": "FIO D.J&J EXP.PLUS 50MTS", "c": "Higiene Bucal", "de": 23.4, "pc": 20.99, "e": 5, "f": "JOHNSON OTC", "ean": "7891010038892"},
    {"n": "LISTERINE TARTAR CONTROL 500ML", "c": "Higiene Bucal", "de": 44.1, "pc": 39.6, "e": 4, "f": "JOHNSON & JOHNSON", "ean": "7891010256791"},
    {"n": "FITA D.J&J EXP.PLUS 50MTS", "c": "Higiene Bucal", "de": 23.4, "pc": 20.99, "e": 4, "f": "JOHNSON OTC", "ean": "7891010038953"},
    {"n": "LISTERINE PRO GENGIVA EXPERT 250ML", "c": "Higiene Bucal", "de": 44.5, "pc": 38.5, "e": 7, "f": "JOHNSON & JOHNSON", "ean": "7891010256883"},
    {"n": "BITUFO LIMPADOR LINGUA DUPLA AÇAO", "c": "Higiene Bucal", "de": 26.7, "pc": 23.99, "e": 3, "f": "JOHNSON OTC", "ean": "7897144600370"},
    {"n": "MALVATRIKIDS INFANTIL 4-7 ANOS 70G", "c": "Higiene Bucal", "de": 30.1, "pc": 26.99, "e": 3, "f": "DAUDT OLIVEIRA S/A", "ean": "7896026170390"},
    {"n": "CR.D.SENSODYNE ORIGINAL 90G", "c": "Higiene Bucal", "de": 20.5, "pc": 18.45, "e": 6, "f": "GLAXOSMITHKLINE", "ean": "7896009419324"},
    {"n": "CR.D.COLG.SENSITIVE PRO ALIVIO IMEDIATO 60G", "c": "Higiene Bucal", "de": 21.5, "pc": 19.35, "e": 5, "f": "COLGATE", "ean": "7509546653396"},
    {"n": "FIO D.J&J ESSENCIAL 100MT JORNAL", "c": "Higiene Bucal", "de": 23.8, "pc": 21.4, "e": 5, "f": "JOHNSON & JOHNSON LT", "ean": "7891010501105"},
    {"n": "PERIOGARD ENX.BUC.S/ALC.EXTRA MINT 250ML", "c": "Higiene Bucal", "de": 41.7, "pc": 37.4, "e": 10, "f": "JOHNSON OTC", "ean": "7891024033425"},
    {"n": "CR.D.COLGATE TOTAL LIMPEZA PROFUNDA INTERDENTAL 90G", "c": "Higiene Bucal", "de": 19.6, "pc": 17.5, "e": 4, "f": "COLGATE", "ean": "7509546704067"},
    {"n": "PERIOGARD 250ML COLG.S/ALCOOL", "c": "Higiene Bucal", "de": 41.7, "pc": 37.4, "e": 6, "f": "COLGATE PALMOLIVE", "ean": "7891024179925"},
    {"n": "LISTERINE MELANCIA E HORTELA 500ML JORNAL", "c": "Higiene Bucal", "de": 28.99, "pc": 25.9, "e": 3, "f": "JOHNSON OTC", "ean": "7891010256050"},
    {"n": "FIXODENT ORIG.21G", "c": "Higiene Bucal", "de": 55.2, "pc": 41.9, "e": 5, "f": "JOHNSON OTC", "ean": "0076660008625"},
    {"n": "COREGA ULTRA CREME SEM SABOR 8,5G", "c": "Higiene Bucal", "de": 24.4, "pc": 19.9, "e": 3, "f": "GLAXOSMITHKLINE", "ean": "7896015591007"},
    {"n": "MASCARA CIRURGICA DESCARPACK MEDIX C/50 UND", "c": "Curativos & Hospitalar", "de": 21.2, "pc": 18.99, "e": 4, "f": "JOHNSON OTC", "ean": "7898283813065"},
    {"n": "ESP.SALVELOX BRANCO 5.0X4.5", "c": "Curativos & Hospitalar", "de": 17.6, "pc": 15.8, "e": 11, "f": "CREMER S/A", "ean": "7891800628432"},
    {"n": "CURATIVO CREMER EXTRA GRANDE XXG C/8 -", "c": "Curativos & Hospitalar", "de": 21.5, "pc": 19.3, "e": 4, "f": "CREMER S/A PROD.TEXTIS CIRURG", "ean": "7891800644470"},
    {"n": "CURATIVO CREMER A PROVA DAGUA C/15 - 372847", "c": "Curativos & Hospitalar", "de": 23.99, "pc": 21.5, "e": 5, "f": "CREMER S/A", "ean": "7891800372847"},
    {"n": "ESP. SALVELOX BRANCO 10CMX3CM", "c": "Curativos & Hospitalar", "de": 23.99, "pc": 21.5, "e": 5, "f": "JOHNSON OTC", "ean": "7891800670608"},
    {"n": "DES.DOVE AERO ORIGINAL 150ML(JORNAL)", "c": "Perfumes & Desodorantes", "de": 20, "pc": 15.89, "e": 181, "f": "UNILEVER", "ean": "7506306241183"},
    {"n": "DES.PIERRE CREME 50G", "c": "Perfumes & Desodorantes", "de": 31.3, "pc": 27.9, "e": 48, "f": "PIERRE FABRE", "ean": "0000000022002"},
    {"n": "DES.ABOVE AERO ZERO MEN 150ML", "c": "Perfumes & Desodorantes", "de": 18, "pc": 15.99, "e": 12, "f": "BASTON IND.AEROSSOIS", "ean": "7899674030559"},
    {"n": "DES.DOVE CR.F.PREVINE ESCURECIMENTO 50ML", "c": "Perfumes & Desodorantes", "de": 25.5, "pc": 22.9, "e": 6, "f": "UNILEVER", "ean": "7891150096783"},
    {"n": "KNUT SH.K-FORCE 250ML", "c": "Perfumes & Desodorantes", "de": 66.2, "pc": 59.9, "e": 6, "f": "SHT IND.E COM.COSMETICOS LTDA", "ean": "7898483150601"},
    {"n": "DES.DOVE CR.F.PREVINE IRRITACAO 50ML", "c": "Perfumes & Desodorantes", "de": 25.5, "pc": 22.9, "e": 4, "f": "UNILEVER", "ean": "7891150096790"},
    {"n": "DES.GIOVANNA BABY AERO S/ALUMINIO CLASSIC 150ML", "c": "Perfumes & Desodorantes", "de": 25.99, "pc": 23.39, "e": 3, "f": "PRO NOVA.GIOVANNA BABY", "ean": "7896044998723"},
    {"n": "DES.DOVE CR.F.REPARACAO DIARIA 50ML", "c": "Perfumes & Desodorantes", "de": 25.5, "pc": 22.9, "e": 3, "f": "UNILEVER", "ean": "7891150094741"},
    {"n": "DES.DOVE SERUM F.STICK TROPICAL HIBISCUS 45G", "c": "Perfumes & Desodorantes", "de": 38.8, "pc": 34.9, "e": 4, "f": "UNILEVER", "ean": "0079400526359"},
    {"n": "DES.REX CLINICAL CLEAN 58G", "c": "Perfumes & Desodorantes", "de": 36, "pc": 32.4, "e": 12, "f": "UNILEVER", "ean": "0000075076825"},
    {"n": "DES.REX CLINICAL CLASSIC 58GR", "c": "Perfumes & Desodorantes", "de": 36, "pc": 32.4, "e": 9, "f": "UNILEVER", "ean": "0000075076818"},
    {"n": "DES.REX.AERO F.POWDER DRY 250ML.", "c": "Perfumes & Desodorantes", "de": 28.5, "pc": 25.65, "e": 10, "f": "UNILEVER", "ean": "7891150081253"},
    {"n": "FR.PAMPERS T.CONF. FORTEBAG G/60UN", "c": "Fraldas", "de": 122, "pc": 108.9, "e": 6, "f": "P&G", "ean": "7500435106672"},
    {"n": "FR.PAMPERS T.CONF.FORTEBAG M/70UN", "c": "Fraldas", "de": 122, "pc": 108.9, "e": 6, "f": "P&G", "ean": "7500435106665"},
    {"n": "FR.PAMPERS T.CONF. FORTEBAG XXG/56UN", "c": "Fraldas", "de": 122, "pc": 108.9, "e": 5, "f": "P&G", "ean": "0000010330531"},
    {"n": "FR.PAMPERS SUPERSEQUINHA SUPER G 60UN", "c": "Fraldas", "de": 109.99, "pc": 98.99, "e": 4, "f": "P&G", "ean": "7500435250207"},
    {"n": "FR.PAMPERS SUPERSEQUINHA SUPER XXG 50UN", "c": "Fraldas", "de": 109.99, "pc": 98.99, "e": 4, "f": "P&G", "ean": "7500435250191"},
    {"n": "FR.PAMPERS SUPERSEQUINHA SUPER M 68UN", "c": "Fraldas", "de": 109.99, "pc": 98.99, "e": 3, "f": "P&G", "ean": "7500435250214"},
    {"n": "FR.TENA PANTS DERMACARE G/EG C/24UN", "c": "Fraldas", "de": 133.45, "pc": 110.49, "e": 3, "f": "JOHNSON OTC", "ean": "7896770981808"},
    {"n": "FR.TENA SLIP NOTURNA  EG LV16PG14", "c": "Fraldas", "de": 78, "pc": 69.9, "e": 6, "f": "JONHSONS", "ean": "7896770983611"},
    {"n": "FR.TENA PANTS DERMACARE G/EG L16P14", "c": "Fraldas", "de": 73.6, "pc": 65.9, "e": 14, "f": "JOHNSON OTC", "ean": "7896770982867"},
    {"n": "FR.TENA PANTS DERMACARE P/M L16P14", "c": "Fraldas", "de": 73.6, "pc": 65.9, "e": 14, "f": "JOHNSON OTC", "ean": "7896770982850"},
    {"n": "FR.TENA PANTS NOTURNA G/EG L16P14", "c": "Fraldas", "de": 81.79, "pc": 72.9, "e": 14, "f": "JONHSONS", "ean": "7896770908867"},
    {"n": "FR.MAMYPOKO CALCA DIA&NOITE AMARELA G C/30", "c": "Fraldas", "de": 84, "pc": 75.6, "e": 6, "f": "UNICHARM", "ean": "7898656390216"},
    {"n": "FR.HIPOPO BABY HIPER G C/74", "c": "Fraldas", "de": 64.99, "pc": 58.4, "e": 18, "f": "JOHNSON OTC", "ean": "7899700800194"},
    {"n": "FR.BIGFRAL DERMA PLUS SEVERA G C/16UN", "c": "Fraldas", "de": 71, "pc": 63.9, "e": 9, "f": "ONTEX", "ean": "7896012880210"},
    {"n": "FR.PLENITUD PLU P-M L24P22", "c": "Fraldas", "de": 111.55, "pc": 99.9, "e": 3, "f": "KIMBERLY CLARK", "ean": "7896007549993"},
    {"n": "FR.POMPOM PROTEK HIPER G C/68", "c": "Fraldas", "de": 83.8, "pc": 75.4, "e": 8, "f": "ONTEX", "ean": "7896012878491"},
    {"n": "FR.TENA PANTS NOTURNA P/M L16P14", "c": "Fraldas", "de": 81.79, "pc": 72.9, "e": 6, "f": "JONHSONS", "ean": "7896770908850"},
    {"n": "FR.TENA PANTS DERMACARE G/EG L24P21", "c": "Fraldas", "de": 96, "pc": 85.9, "e": 3, "f": "JOHNSON OTC", "ean": "7896770983635"},
    {"n": "FR.PAMPERS PREMIUM CARE RN C/36", "c": "Fraldas", "de": 83.9, "pc": 75.5, "e": 4, "f": "P&G", "ean": "7500435132534"},
    {"n": "FR.PAMPERS PREMIUM CARE MEGA M C/80UN", "c": "Fraldas", "de": 188, "pc": 167.49, "e": 4, "f": "P&G", "ean": "7500435132435"},
    {"n": "FR.TENA PANTS MEN G/XG C/16", "c": "Fraldas", "de": 79.6, "pc": 71.4, "e": 10, "f": "JOHNSON OTC", "ean": "7896770982201"},
    {"n": "FR.PAMPERS PREMIUM CARE MEGA G C/68", "c": "Fraldas", "de": 188, "pc": 167.49, "e": 3, "f": "P&G", "ean": "7500435132442"},
    {"n": "FR.HIPOPO BABY HIPER XG 64UN", "c": "Fraldas", "de": 64.99, "pc": 58.4, "e": 11, "f": "JOHNSON & JOHNSON", "ean": "7899700802594"},
    {"n": "FR.HUGGIES SUPREME CARE XXG HIPZI 3X54 JORNAL", "c": "Fraldas", "de": 99, "pc": 79.9, "e": 8, "f": "KIMBERLY -CLARK BRASIL INDUSTRIA E COMER", "ean": "7896007552849"},
    {"n": "FR.HUGGIES SUPREME CARE MEGA G C/32(VERMELHO)", "c": "Fraldas", "de": 71, "pc": 60.69, "e": 4, "f": "KIMBERLY CLARK", "ean": "7896007548415"},
    {"n": "FR.HUGGIES SUPREME CARE G HIPZI 3X58 JORNAL", "c": "Fraldas", "de": 99, "pc": 79.9, "e": 6, "f": "KIMBERLY -CLARK BRASIL INDUSTRIA E COMER", "ean": "7896007552801"},
    {"n": "FR.HIPOPO BABY HIPER M C/84", "c": "Fraldas", "de": 64.99, "pc": 58.4, "e": 8, "f": "JOHNSON OTC", "ean": "7899700800187"},
    {"n": "FR.HUGGIES SUP M HIPZINHA 3X66 JORNAL", "c": "Fraldas", "de": 99, "pc": 79.9, "e": 5, "f": "LIMA  PERGHER", "ean": "7896007552788"},
    {"n": "FR.PAMPERS PANTS MEGA  AJUSTE TOTAL XXG 20UN", "c": "Fraldas", "de": 81.9, "pc": 73.7, "e": 4, "f": "NÃO INFORMADO", "ean": "7500435260838"},
    {"n": "FR.PLENITUD CLASSIC INTENSA UNISEX G/X 16UND", "c": "Fraldas", "de": 72.19, "pc": 64.9, "e": 3, "f": "KIMBERLY CLARK", "ean": "7896007552986"},
    {"n": "LEITE NAN SUPREME 1 800G", "c": "Leites & Nutricao", "de": 156.69, "pc": 128.9, "e": 7, "f": "NESTLE  IND. COM. LT", "ean": "7613034968364"},
    {"n": "LEITE NAN SENSITIVE 800G", "c": "Leites & Nutricao", "de": 165, "pc": 147.49, "e": 5, "f": "NESTLE  IND. COM. LT", "ean": "7613036671927"},
    {"n": "LEITE APTANUTRI SOJA  3 800G", "c": "Leites & Nutricao", "de": 148.5, "pc": 125.65, "e": 3, "f": "DANONE", "ean": "7795323776116"},
    {"n": "LEITE NAN S/LACTOSE 400G", "c": "Leites & Nutricao", "de": 112.25, "pc": 93.1, "e": 4, "f": "NESTLE  IND. COM. LT", "ean": "7613034909480"},
    {"n": "LEITE NESTOGENO 2 800G", "c": "Leites & Nutricao", "de": 77, "pc": 67.8, "e": 8, "f": "NESTLE LTDA", "ean": "7891000062760"},
    {"n": "LEITE NAN COMFOR 1 800G", "c": "Leites & Nutricao", "de": 91.79, "pc": 80.9, "e": 8, "f": "NESTLE  IND. COM. LT", "ean": "7891000071625"},
    {"n": "LEITE NINHO FASES CRES PREBIO 3+800G LT.", "c": "Leites & Nutricao", "de": 62.5, "pc": 55.8, "e": 14, "f": "NESTLE  IND. COM. LT", "ean": "7891000282809"},
    {"n": "LEITE NANLAC COMFOR 1A3 800G", "c": "Leites & Nutricao", "de": 93.99, "pc": 81.5, "e": 3, "f": "NESTLE  IND. COM. LT", "ean": "7891000097649"},
    {"n": "LEITE NESTOGENO 1 800G", "c": "Leites & Nutricao", "de": 72.8, "pc": 65.5, "e": 6, "f": "NESTLE LTDA", "ean": "7891000062722"},
    {"n": "LEITE NESTONUTRI 1 A 3.800G", "c": "Leites & Nutricao", "de": 72.6, "pc": 62.5, "e": 6, "f": "NESTLE  IND. COM. LT", "ean": "7891000255544"},
    {"n": "LEITE NINHO ZERO LACTOSE 380GR", "c": "Leites & Nutricao", "de": 28.29, "pc": 24.3, "e": 4, "f": "NESTLE  IND. COM. LT", "ean": "7891000109908"},
    {"n": "TALA CURTA BILATERAL PRETA M MERCUR", "c": "Ortopedicos", "de": 70, "pc": 56.9, "e": 3, "f": "MERCUR", "ean": "7896342452187"},
    {"n": "SUSP.ESCROTAL TENSOR PEQ. 3981", "c": "Ortopedicos", "de": 31, "pc": 27.9, "e": 3, "f": "TENSOR SPORTS PROTEC", "ean": "7896191239816"}
]


ABAS = [
    "Fraldas",
    "Leites & Nutricao",
    "Dermocosmeticos",
    "Perfumes & Desodorantes",
    "Cabelos",
    "Higiene Intima",
    "Higiene Bucal",
    "Higiene & Banho",
    "Vitaminas & Nutricao",
    "Bebe & Infantil",
    "Preservativos & Barbear",
]

def desconto(de, por):
    if de > por and de > 0:
        return int(round((1 - (por / de)) * 100))
    return 0

def brl(v):
    return ("%.2f" % v).replace(".", ",")

def card(p, selo):
    d = desconto(p["de"], p["pc"])
    msg = (
        "Ola, ARGD Farma! Gostaria de fazer um pedido:\n\n"
        "Produto: " + p["n"] + "\n"
        "Marca: " + p["f"] + "\n"
        "Codigo de barras: " + p["ean"] + "\n"
        "Valor: R$ " + brl(p["pc"]) + "\n\n"
        "Nome:\nEndereco (rua, numero, bairro):\nForma de pagamento (Pix / Cartao / Dinheiro):"
    )
    link = "https://wa.me/" + ZAP_PEDIDOS + "?text=" + urllib.parse.quote(msg)

    badge = ""
    if d > 0:
        badge = '<span class="badge-desc">-' + str(d) + '% OFF</span>'
    selo_html = ('<span class="selo">' + selo + '</span>') if selo else ""

    de_html = ""
    if d > 0:
        de_html = '<div class="preco-de">De R$ ' + brl(p["de"]) + '</div>'

    if p["e"] <= 10:
        est = '<div class="estoque">Apenas ' + str(int(p["e"])) + ' unid.</div>'
    else:
        est = '<div class="estoque ok">Disponivel</div>'

    foto = ('<img class="foto" src="' + CDN_IMG + p["ean"] + '" alt="' + p["n"] + '" loading="lazy" '
            'onerror="this.style.display=&#39;none&#39;;this.nextElementSibling.style.display=&#39;flex&#39;;">'
            '<div class="foto-fallback" style="display:none"><span class="ico">&#128138;</span><span class="fab">' + p["f"] + '</span></div>')

    return ('<article class="card">'
        '<div class="card-topo">' + badge + selo_html + '</div>'
        '<div class="img-box">' + foto + '</div>'
        '<div class="card-body">'
        '<h3 class="nome">' + p["n"] + '</h3>'
        '<div class="fab-linha">' + p["f"] + '</div>'
        '<div class="precos">' + de_html + '<div class="preco-por"><span>R$</span> ' + brl(p["pc"]) + '</div>' + est + '</div>'
        '<a class="btn-zap" href="' + link + '" target="_blank" rel="noopener">PEDIR NO WHATSAPP</a>'
        '</div></article>')

@app.route("/")
def index():
    aba = request.args.get("aba", "").strip()
    q = request.args.get("q", "").strip().lower()

    if aba:
        lista = [p for p in CATALOGO if p["c"] == aba]
        if q:
            lista = [p for p in lista if q in p["n"].lower() or q in p["f"].lower()]
        cards = "".join(card(p, "") for p in lista)
        return page_aba(aba, cards, len(lista))

    if q:
        lista = [p for p in CATALOGO if q in p["n"].lower() or q in p["f"].lower()]
        cards = "".join(card(p, "") for p in lista)
        return page_aba('Busca: "' + q + '"', cards, len(lista))

    # HOME = Jornal de Ofertas + blocos
    jornal_cards = "".join(card(p, "OFERTA DO JORNAL") for p in JORNAL)
    bemme_cards = "".join(card(p, "5x CHANCES") for p in BEMME)
    essence_cards = "".join(card(p, "LINHA EXCLUSIVA") for p in ESSENCE)
    return home(jornal_cards, bemme_cards, essence_cards)

def page_aba(titulo, cards, total):
    pills = '<a class="pill" href="/">Inicio</a>'
    for a in ABAS:
        if not any(p["c"] == a for p in CATALOGO):
            continue
        on = "on" if titulo == a else ""
        pills += '<a class="pill ' + on + '" href="/?aba=' + urllib.parse.quote_plus(a) + '">' + a + '</a>'
    return PAGINA.replace("__PILLS__", pills).replace("__CONTEUDO__",
        '<div class="meta">' + str(total) + ' produtos</div><div class="grid">' + cards + '</div>')

def home(jornal_cards, bemme_cards, essence_cards):
    pills = '<a class="pill on" href="/">Inicio</a>'
    for a in ABAS:
        if not any(p["c"] == a for p in CATALOGO):
            continue
        pills += '<a class="pill" href="/?aba=' + urllib.parse.quote_plus(a) + '">' + a + '</a>'
    conteudo = (
        BANNER +
        '<div class="sec"><div class="sec-tit"><span class="dot jornal-dot"></span>Jornal de Ofertas</div>'
        '<div class="sec-sub">Ofertas validas enquanto durar o estoque</div>'
        '<div class="grid">' + jornal_cards + '</div></div>' +
        '<div class="sec"><div class="sec-tit"><span class="dot bemme-dot"></span>Linha Bemme</div>'
        '<div class="sec-sub">Compre Bemme e ganhe 5 numeros da sorte extras no Sorte Real na Total</div>'
        '<div class="grid">' + bemme_cards + '</div></div>' +
        '<div class="sec"><div class="sec-tit"><span class="dot ess-dot"></span>Linha Essence All</div>'
        '<div class="sec-sub">Suplementacao completa - 60 capsulas</div>'
        '<div class="grid">' + essence_cards + '</div></div>'
    )
    return PAGINA.replace("__PILLS__", pills).replace("__CONTEUDO__", conteudo)


BANNER = """
<div class="banner">
  <div class="banner-badge">ESPECIAL 30 ANOS</div>
  <h2>SORTE REAL NA TOTAL</h2>
  <p>Compre e concorra a <strong>4 carros 0km</strong></p>
  <div class="banner-info">
    <span>Periodo: 05/09/2026 a 31/12/2026</span>
    <span>Informe seu CPF no pedido</span>
  </div>
</div>
"""

PAGINA = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ARGD Farma - Drogaria Total Ituverava Delivery</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:Inter,sans-serif}
body{background:#f1f5f9;color:#0f172a}
.topo{background:#0f172a;color:#fff;font-size:13px;padding:10px 16px;text-align:center;font-weight:600;display:flex;justify-content:center;gap:22px;flex-wrap:wrap}
.topo b{color:#4ade80}
header{background:#fff;border-bottom:2px solid #e0f2fe;padding:16px 20px}
.hw{max-width:1240px;margin:auto;display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}
.marca h1{font-size:23px;font-weight:900;color:#0284c7}
.marca p{font-size:12px;color:#475569;font-weight:600}
form.busca{flex:1;min-width:240px;max-width:520px;display:flex;border:2px solid #cbd5e1;border-radius:12px;overflow:hidden}
form.busca input{flex:1;padding:11px 16px;border:none;outline:none;font-size:15px}
form.busca button{background:#0284c7;color:#fff;border:none;padding:0 20px;font-weight:700;cursor:pointer}
main{max-width:1240px;margin:20px auto;padding:0 16px}
.pills{display:flex;gap:8px;overflow-x:auto;padding-bottom:12px;margin-bottom:16px}
.pill{text-decoration:none;padding:8px 15px;background:#fff;border:1px solid #e2e8f0;border-radius:20px;font-size:13px;font-weight:700;color:#475569;white-space:nowrap}
.pill.on{background:#0284c7;color:#fff;border-color:#0284c7}
.banner{background:linear-gradient(135deg,#c1121f,#8b0000);border-radius:18px;padding:26px 22px;color:#fff;text-align:center;margin-bottom:24px;box-shadow:0 10px 30px rgba(193,18,31,.28)}
.banner-badge{display:inline-block;background:#fbbf24;color:#7c2d12;font-size:11px;font-weight:900;padding:5px 14px;border-radius:20px;margin-bottom:10px}
.banner h2{font-size:30px;font-weight:900;letter-spacing:-.5px;line-height:1.1}
.banner p{font-size:15px;margin-top:6px;opacity:.95}
.banner-info{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-top:12px;font-size:12px;font-weight:600;opacity:.9}
.sec{margin-bottom:34px}
.sec-tit{display:flex;align-items:center;gap:9px;font-size:19px;font-weight:900;color:#0f172a}
.dot{width:11px;height:11px;border-radius:50%}
.jornal-dot{background:#dc2626}
.bemme-dot{background:#22c55e}
.ess-dot{background:#8b5cf6}
.sec-sub{font-size:12.5px;color:#64748b;font-weight:600;margin:4px 0 14px 20px}
.meta{font-weight:700;color:#475569;margin-bottom:14px;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.card{background:#fff;border-radius:16px;border:1px solid #e2e8f0;box-shadow:0 4px 15px rgba(0,0,0,.04);display:flex;flex-direction:column;position:relative;overflow:hidden;transition:.2s}
.card:hover{transform:translateY(-3px);box-shadow:0 10px 25px rgba(0,0,0,.09)}
.card-topo{position:absolute;top:10px;left:10px;right:10px;display:flex;justify-content:space-between;gap:6px;z-index:2;pointer-events:none}
.badge-desc{background:#dc2626;color:#fff;font-size:11px;font-weight:900;padding:4px 8px;border-radius:8px}
.selo{background:#0f172a;color:#fff;font-size:9.5px;font-weight:800;padding:4px 8px;border-radius:8px;letter-spacing:.3px}
.img-box{height:180px;background:#fff;display:flex;align-items:center;justify-content:center;border-bottom:1px solid #e2e8f0;overflow:hidden}
.foto{max-width:100%;max-height:100%;object-fit:contain;padding:8px}
.foto-fallback{flex-direction:column;align-items:center;justify-content:center;width:100%;height:100%;background:#f0f9ff}
.ico{font-size:36px}
.fab{font-size:10.5px;font-weight:800;color:#0284c7;text-transform:uppercase;margin-top:6px;text-align:center;padding:0 10px}
.card-body{padding:13px;display:flex;flex-direction:column;flex:1;justify-content:space-between}
.nome{font-size:12.5px;font-weight:700;line-height:1.4;margin-bottom:4px;min-height:35px}
.fab-linha{font-size:10px;color:#0284c7;font-weight:800;text-transform:uppercase;margin-bottom:9px}
.precos{background:#f8fafc;padding:8px 10px;border-radius:9px;margin-bottom:11px}
.preco-de{font-size:11.5px;text-decoration:line-through;color:#94a3b8;font-weight:600}
.preco-por{font-size:21px;font-weight:900;color:#16a34a;line-height:1.1}
.preco-por span{font-size:13px}
.estoque{font-size:10.5px;font-weight:700;color:#dc2626;margin-top:3px}
.estoque.ok{color:#059669}
.btn-zap{text-decoration:none;background:#16a34a;color:#fff;padding:10px;border-radius:9px;font-size:11.5px;font-weight:800;text-align:center;box-shadow:0 4px 12px rgba(22,163,74,.28)}
footer{background:#0f172a;color:#94a3b8;padding:42px 20px 22px;margin-top:50px;font-size:13px}
.fg{max-width:1240px;margin:auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:28px;padding-bottom:26px;border-bottom:1px solid #1e293b}
.fg h3{color:#fff;font-size:15px;margin-bottom:11px}
.fg p{line-height:1.65;margin-bottom:7px}
.legal{max-width:1240px;margin:20px auto 0;font-size:11.5px;text-align:center;color:#64748b;line-height:1.6}
</style>
</head>
<body>
<div class="topo">
<span>&#128666; Entrega rapida em Ituverava - SP</span>
<span>&#9200; Pedidos ate 18h: entrega no <b>mesmo dia</b></span>
<span>&#127769; Pedidos apos 18h: <b>dia seguinte a partir das 8h</b></span>
<span>&#128172; Pedidos: <b>(16) 99106-7477</b></span>
</div>
<header><div class="hw">
<div class="marca"><h1>ARGD Farma</h1><p>Drogaria Total Ituverava Delivery &bull; As marcas que voce ja conhece</p></div>
<form class="busca" method="GET" action="/"><input type="text" name="q" placeholder="Buscar produto ou marca..."><button type="submit">Buscar</button></form>
</div></header>
<main>
<div class="pills">__PILLS__</div>
__CONTEUDO__
</main>
<footer>
<div class="fg">
<div><h3>Drogaria Total Ituverava Delivery</h3>
<p>Atendimento farmaceutico de confianca e entrega rapida em Ituverava - SP.</p>
<p><strong>Pedidos e Delivery:</strong> (16) 99106-7477</p>
<p><strong>Atendimento na loja:</strong> (16) 99998-2256</p>
<p>Localizacao: Ituverava - SP &bull; CEP 14500-053</p></div>
<div><h3>Politica de Entrega</h3>
<p>Pedidos ate as 18h: entrega no <strong>mesmo dia</strong>, em ate 45 minutos.</p>
<p>Pedidos a partir das 18h: entrega no <strong>dia seguinte, a partir das 8h</strong>.</p>
<p>Entregas por motoboy identificado da loja.</p></div>
<div><h3>Sorte Real na Total</h3>
<p>Campanha valida de 05/09/2026 a 31/12/2026.</p>
<p>Informe seu CPF no pedido para acumular numeros da sorte.</p>
<p>Produtos Bemme dao <strong>5 numeros extras</strong> por compra.</p>
<p>Medicamentos, vacinas e itens de primeira infancia nao participam da campanha.</p></div>
</div>
<div class="legal">Drogaria Total Ituverava Delivery &bull; Todos os direitos reservados. Imagens meramente ilustrativas. Precos e estoques podem sofrer alteracoes sem aviso previo.</div>
</footer>
</body>
</html>"""

if __name__ == "__main__":
    app.run(debug=True)
