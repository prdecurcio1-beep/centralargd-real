import urllib.parse
from flask import Flask, request

app = Flask(__name__)

# ============================================================
# ARGD FARMA - Drogaria Total Ituverava Delivery
# Atendente virtual: ARGD Farma (formal, com gatilhos de venda)
# Pedidos: WhatsApp (16) 99106-7477
# ============================================================

NOME_SITE = "ARGD Farma"
NOME_LOJA = "Drogaria Total Ituverava Delivery"
CIDADE = "Ituverava - SP"
CEP = "14500-053"
ZAP_PEDIDOS = "5516991067477"
ZAP_LOJA = "5516999982256"

CATALOGO = [
    {"n": "BRINCO DROGARIA TOTAL", "c": "Perfumaria & Beleza", "de": 29.9, "pc": 29.9, "e": 207, "f": "NEW STAR FOLHEADOS ART BIJUTERIA EM GERA"},
    {"n": "BRINCO ARGOLINHA DROGARIA TOTAL", "c": "Perfumaria & Beleza", "de": 34.9, "pc": 34.9, "e": 36, "f": "NEW STAR FOLHEADOS ART BIJUTERIA EM GERA"},
    {"n": "LIP GLOSS LABIAL VIVAI HIDRA GLOSS (PONMAKE)", "c": "Perfumaria & Beleza", "de": 23.99, "pc": 21.4, "e": 13, "f": "20"},
    {"n": "BASE LIQ.UNI MAKEUP MATTE", "c": "Perfumaria & Beleza", "de": 24.5, "pc": 21.95, "e": 9, "f": "20"},
    {"n": "DESODORANTE CORPORAL 250ML CLIVE DORRIS (PONMAKE)", "c": "Perfumaria & Beleza", "de": 72.9, "pc": 63.95, "e": 26, "f": "20"},
    {"n": "BEMME PERFUME IV MAN NY MEN 15ML", "c": "Perfumaria & Beleza", "de": 44.8, "pc": 39.9, "e": 4, "f": "20"},
    {"n": "BATOM 3Q BEAUTY", "c": "Perfumaria & Beleza", "de": 15, "pc": 13.5, "e": 14, "f": "20"},
    {"n": "KIT PERFUME+HID.FEM.V V LOVE (PONMAKE)", "c": "Perfumaria & Beleza", "de": 84, "pc": 75.6, "e": 3, "f": "20"},
    {"n": "BRINCO DROGARIA TOTAL COLECAO LUXO", "c": "Perfumaria & Beleza", "de": 49.9, "pc": 49.9, "e": 34, "f": "NEW STAR FOLHEADOS ART BIJUTERIA EM GERA"},
    {"n": "ARA AL KHALEEJ BODY MIST DHAHABI FOR MEN 250ML", "c": "Perfumaria & Beleza", "de": 109.8, "pc": 98.6, "e": 5, "f": "20"},
    {"n": "DES.DOVE AERO ORIGINAL 150ML(JORNAL)", "c": "Perfumaria & Beleza", "de": 20, "pc": 15.89, "e": 181, "f": "UNILEVER"},
    {"n": "ARA AL KHALEEJ BODY MIST JALALA FOR MEN 250ML", "c": "Perfumaria & Beleza", "de": 109.8, "pc": 98.6, "e": 4, "f": "20"},
    {"n": "ANEL DROGARIA TOTAL", "c": "Perfumaria & Beleza", "de": 49.9, "pc": 49.9, "e": 41, "f": "NEW STAR FOLHEADOS ART BIJUTERIA EM GERA"},
    {"n": "PERFUME ONLYOU COLLECTION 30ML", "c": "Perfumaria & Beleza", "de": 53.8, "pc": 47.9, "e": 5, "f": "20"},
    {"n": "ABS.MILI NOTURNO SUAVE C/ABAS 32UN", "c": "Higiene & Cuidados", "de": 29.8, "pc": 26.8, "e": 156, "f": "MILI S.A"},
    {"n": "ABS.MILI PROTECAO TOTAL SUAVE C/ABAS 16UN", "c": "Higiene & Cuidados", "de": 8.9, "pc": 7.99, "e": 211, "f": "MILI S.A"},
    {"n": "OLEO DE GIRASSOL FARMAX 200ML", "c": "Higiene & Cuidados", "de": 28.99, "pc": 25.99, "e": 7, "f": "FARMAX"},
    {"n": "ESC.D.ORALGOS ELEGANCE UNITARIA", "c": "Higiene & Cuidados", "de": 16.6, "pc": 14.9, "e": 3, "f": "20"},
    {"n": "ABS.INTIMUS NOT SUAVE C/ABAS 30UN", "c": "Higiene & Cuidados", "de": 35.75, "pc": 32.1, "e": 14, "f": "KIMBERLY CLARK"},
    {"n": "ABS.ALWAYS NOTURNO SECA C/ABAS XXG C/10", "c": "Higiene & Cuidados", "de": 45.45, "pc": 40.9, "e": 6, "f": "PROCTER & GAMBLE"},
    {"n": "COREGA ULTRA CR.S/SABOR 40G", "c": "Higiene & Cuidados", "de": 86.3, "pc": 71.9, "e": 4, "f": "GLAXOSMITHKLINE"},
    {"n": "ABS.INTIMUS NOT SECA C/ABAS 30UN", "c": "Higiene & Cuidados", "de": 35.75, "pc": 32.5, "e": 4, "f": "KIMBERLY CLARK"},
    {"n": "BUCHA VEGETAL QUADRADA ISSAM", "c": "Higiene & Cuidados", "de": 8.9, "pc": 8, "e": 20, "f": "20"},
    {"n": "FIO D.HILLO WOMAN 100M", "c": "Higiene & Cuidados", "de": 10.45, "pc": 9.4, "e": 4, "f": "APERIFIO INDUSTRIA COMERCIO E REPRESENTA"},
    {"n": "FITA D.HILLO WOMAN 100 MT", "c": "Higiene & Cuidados", "de": 10.45, "pc": 9.4, "e": 4, "f": "JOHNSON OTC"},
    {"n": "PERIODENT DENTRAT ZERO 250ML", "c": "Higiene & Cuidados", "de": 22.3, "pc": 19.9, "e": 6, "f": "DENTRAT"},
    {"n": "SAB.ASEPXIA ENXOFRE 90G", "c": "Higiene & Cuidados", "de": 9.99, "pc": 8.99, "e": 6, "f": "GENOMMA"},
    {"n": "ASEPXIA SAB.SUAVIZANTE ACAO EQUIL.90GR", "c": "Higiene & Cuidados", "de": 9.99, "pc": 8.99, "e": 3, "f": "JOHNSON OTC"},
    {"n": "TOALHA UMED.ESSENCE ALL BABY C/140UN", "c": "Bebe & Fraldas", "de": 10.99, "pc": 7.99, "e": 224, "f": "20"},
    {"n": "LEITE NAN SUPREME 1 800G", "c": "Bebe & Fraldas", "de": 156.69, "pc": 128.9, "e": 7, "f": "NESTLE  IND. COM. LT"},
    {"n": "BRINQUEDO DOCE POPFONE ISSAM", "c": "Bebe & Fraldas", "de": 14.9, "pc": 13.4, "e": 27, "f": "20"},
    {"n": "MAM.DECORADA C/BICO 240ML ISSAM", "c": "Bebe & Fraldas", "de": 32.9, "pc": 29.59, "e": 4, "f": "20"},
    {"n": "LEITE APTANUTRI SOJA  3 800G", "c": "Bebe & Fraldas", "de": 148.5, "pc": 125.65, "e": 3, "f": "DANONE"},
    {"n": "LEITE NAN S/LACTOSE 400G", "c": "Bebe & Fraldas", "de": 112.25, "pc": 93.1, "e": 4, "f": "NESTLE  IND. COM. LT"},
    {"n": "LEITE NAN SENSITIVE 800G", "c": "Bebe & Fraldas", "de": 165, "pc": 147.49, "e": 5, "f": "NESTLE  IND. COM. LT"},
    {"n": "FR.PAMPERS T.CONF. FORTEBAG G/60UN", "c": "Bebe & Fraldas", "de": 122, "pc": 108.9, "e": 6, "f": "P&G"},
    {"n": "FR.PAMPERS T.CONF.FORTEBAG M/70UN", "c": "Bebe & Fraldas", "de": 122, "pc": 108.9, "e": 6, "f": "P&G"},
    {"n": "FR.PAMPERS T.CONF. FORTEBAG XXG/56UN", "c": "Bebe & Fraldas", "de": 122, "pc": 108.9, "e": 5, "f": "P&G"},
    {"n": "FR.PAMPERS SUPERSEQUINHA SUPER G 60UN", "c": "Bebe & Fraldas", "de": 109.99, "pc": 98.99, "e": 4, "f": "P&G"},
    {"n": "FR.PAMPERS SUPERSEQUINHA SUPER XXG 50UN", "c": "Bebe & Fraldas", "de": 109.99, "pc": 98.99, "e": 4, "f": "P&G"},
    {"n": "FR.PAMPERS SUPERSEQUINHA SUPER M 68UN", "c": "Bebe & Fraldas", "de": 109.99, "pc": 98.99, "e": 3, "f": "P&G"},
    {"n": "AGUA COLONIA POMPOM 100ML", "c": "Bebe & Fraldas", "de": 22.2, "pc": 19.9, "e": 4, "f": "HYPERMARCAS"},
    {"n": "SUPER GREEN BLACK C/60 CPS", "c": "Vitaminas & Suplementos", "de": 334.4, "pc": 300, "e": 9, "f": "20"},
    {"n": "MAG PLUS 5 550MG 60CAPS", "c": "Vitaminas & Suplementos", "de": 55.99, "pc": 49.99, "e": 5, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -"},
    {"n": "SUSTAGEN SENIOR ADULTOS 50+ SEM SABOR 740G", "c": "Vitaminas & Suplementos", "de": 197.34, "pc": 169.91, "e": 3, "f": "APENAS BOA NUTRIÇÃO INDUSTRIA"},
    {"n": "FULL PERFORMANCE CREATINA EM CARAMELO LEITE C/60", "c": "Vitaminas & Suplementos", "de": 150.2, "pc": 134.89, "e": 3, "f": "20"},
    {"n": "ESSENCE ALL SENIOR 50+ CHOCOLATE 800G", "c": "Vitaminas & Suplementos", "de": 124.9, "pc": 109.9, "e": 6, "f": "LIV HEALTH LTDA"},
    {"n": "ESSENCE ALL SENIOR 50+ SEM SABOR 800G", "c": "Vitaminas & Suplementos", "de": 124.9, "pc": 109.9, "e": 3, "f": "LIV HEALTH LTDA"},
    {"n": "FULL PERFORMANCE CREATINA 100% PURA 300G", "c": "Vitaminas & Suplementos", "de": 79.9, "pc": 69.9, "e": 10, "f": "20"},
    {"n": "NUTREN SENIOR PO CAFE C/LEITE 740G", "c": "Vitaminas & Suplementos", "de": 187.3, "pc": 168.5, "e": 3, "f": "NESTLE  IND. COM. LT"},
    {"n": "NUTREN SENIOR PO S/SABOR 740G", "c": "Vitaminas & Suplementos", "de": 187.3, "pc": 168.5, "e": 3, "f": "NESTLE  IND. COM. LT"},
    {"n": "WAFER PROTEIN COOKIES CREAM ZERO 25G BEMME", "c": "Vitaminas & Suplementos", "de": 12.9, "pc": 12.9, "e": 13, "f": "DUPRATA ALIMENTOS LTDA"},
    {"n": "SUPER COFFEE 3.0 CHOCOLATE ED.LINGUA DE GATO 140G UNITARIO", "c": "Vitaminas & Suplementos", "de": 14.4, "pc": 12.9, "e": 6, "f": "WORLD BLEND MASTER"},
    {"n": "BEMME PERFUME IV GYRL WOMAM 15ML", "c": "Vitaminas & Suplementos", "de": 44.8, "pc": 39.9, "e": 5, "f": "20"},
    {"n": "ZINCO QUELATO 60CAPS HERBAMED", "c": "Vitaminas & Suplementos", "de": 33.15, "pc": 28.7, "e": 4, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -"},
    {"n": "MAGNESIO DIMALATO 400MG 60CAPS HERBAMED", "c": "Vitaminas & Suplementos", "de": 40.6, "pc": 33.9, "e": 3, "f": "HERBAMED LABORATORIO NUTRACEUTICO LTDA -"},
    {"n": "OLEO E SERUM DOVE UV REPAIR E GLOW+FERULICO 110ML", "c": "Cabelos", "de": 47.1, "pc": 42.39, "e": 3, "f": "UNILEVER"},
    {"n": "SPRAY KARINA EXTRA FORTE 400ML", "c": "Cabelos", "de": 41, "pc": 36.9, "e": 4, "f": "JOHNSON OTC"},
    {"n": "SPRAY KARINA NORMAL 400ML", "c": "Cabelos", "de": 41, "pc": 36.9, "e": 3, "f": "JOHNSON OTC"},
    {"n": "OLEO ELSEVE EXTRAORDINARIO 100ML", "c": "Cabelos", "de": 47, "pc": 42.3, "e": 29, "f": "JOHNSON OTC"},
    {"n": "CR.NIELY GOLD QUERATINA 80G", "c": "Cabelos", "de": 28.14, "pc": 25.33, "e": 3, "f": "NIELYGOLD"},
    {"n": "PASTA D AGUA (PASTOL)100G", "c": "Cabelos", "de": 21, "pc": 18.8, "e": 16, "f": "JOHNSON OTC"},
    {"n": "CR.PENT.SEDA CACHOS DEFINIDOS 300ML (VERDE)", "c": "Cabelos", "de": 16, "pc": 14.4, "e": 4, "f": "UNILEVER"},
    {"n": "CR.TRAT.ELSEVE BOND REPAIR 200G", "c": "Cabelos", "de": 79.5, "pc": 71.5, "e": 3, "f": "LOREAL"},
    {"n": "TINT.IMEDIA 3 CAST.ESC", "c": "Cabelos", "de": 43.6, "pc": 39.2, "e": 16, "f": "LOREAL"},
    {"n": "SH.PANTENE MOLECULAR 510ML", "c": "Cabelos", "de": 54.2, "pc": 48.7, "e": 4, "f": "PROCTER & GAMBLE"},
    {"n": "SIAGE SH.LISO INTENSO 250ML", "c": "Cabelos", "de": 63, "pc": 56.7, "e": 4, "f": "BOTICA COMERCIAL FARMACEUTICA LTDA"},
    {"n": "SERUM ELSEVE COLLAGEN LIFTER 100ML", "c": "Cabelos", "de": 61, "pc": 54.9, "e": 4, "f": "JOHNSON OTC"},
    {"n": "GEL NYLOOKS FIX1 INCOLOR 240G", "c": "Cabelos", "de": 11.69, "pc": 11.69, "e": 4, "f": "JOHNSON OTC"},
    {"n": "OLEO CAPILAR S.LINE XEROSA BAUNILHA DOCE 60ML", "c": "Cabelos", "de": 33.4, "pc": 29.99, "e": 3, "f": "SALONLINE"},
    {"n": "CR.HID.MONANGE FLOR DE LAVANDA 200ML.", "c": "Dermocosmeticos", "de": 17, "pc": 14.6, "e": 3, "f": "JOHNSON OTC"},
    {"n": "CR.NIVEA LUMINOUS FLUIDO FPS50 30ML", "c": "Dermocosmeticos", "de": 117.9, "pc": 105.9, "e": 3, "f": "NIVEA"},
    {"n": "CR.HID.CERAVE 200G", "c": "Dermocosmeticos", "de": 101.8, "pc": 91.6, "e": 4, "f": "JOHNSON OTC"},
    {"n": "NUTRIOL LOC.ANTICOCEIRA 390ML", "c": "Dermocosmeticos", "de": 140.4, "pc": 125.9, "e": 3, "f": "DARROW LAB. S/A"},
    {"n": "CICAPLAST BAUME B5 40ML", "c": "Dermocosmeticos", "de": 103, "pc": 91.9, "e": 6, "f": "LA ROCHE-POSAY"},
    {"n": "SAB.CORPORAL PURO LEITE NELO 200G", "c": "Dermocosmeticos", "de": 14.9, "pc": 12.9, "e": 7, "f": "20"},
    {"n": "EPISOL INTENSE FPS60 200ML", "c": "Dermocosmeticos", "de": 126.39, "pc": 108.9, "e": 6, "f": "COSMED INDUSTRIA DE COSMETICOS E MEDICAM"},
    {"n": "FUTURA BIOTECH ANTIT.DERM ONE ROLLON 65ML", "c": "Dermocosmeticos", "de": 58.99, "pc": 52.8, "e": 16, "f": "FUTURA BIOTECH"},
    {"n": "PRINCIPIA 10% UREIA+5% GLICERINA+5% OL DE SEMENTE", "c": "Dermocosmeticos", "de": 74.79, "pc": 67.3, "e": 3, "f": "PRINCIPIA"},
    {"n": "EPISOL SEC ACQUA FPS60 40ML", "c": "Dermocosmeticos", "de": 107.45, "pc": 96.7, "e": 3, "f": "MANTECORP"},
    {"n": "LOC.HID.NIVEA BODY MILK 200Ml", "c": "Dermocosmeticos", "de": 17.5, "pc": 15.75, "e": 26, "f": "NIVEA"},
    {"n": "CR.HID.CERAVE 340G", "c": "Dermocosmeticos", "de": 94.75, "pc": 85.2, "e": 3, "f": "JOHNSON OTC"},
    {"n": "P.SOLAR ANASOL OIL FREE E TOQUE SECO FPS75 200G", "c": "Dermocosmeticos", "de": 50.8, "pc": 45.7, "e": 3, "f": "DAHUER LABORATORIO LTDA"},
    {"n": "LOC.HID.NIVEA BODY Q10 FIRMADOR 400ML", "c": "Dermocosmeticos", "de": 57.4, "pc": 51.5, "e": 4, "f": "NIVEA"}
]

ABAS = [
    "Bebe & Fraldas",
    "Perfumaria & Beleza",
    "Dermocosmeticos",
    "Cabelos",
    "Higiene & Cuidados",
    "Vitaminas & Suplementos",
]

def desconto(de, por):
    if de > por and de > 0:
        return int(round((1 - (por / de)) * 100))
    return 0

def brl(v):
    return ("%.2f" % v).replace(".", ",")

@app.route("/")
def index():
    q = request.args.get("q", "").strip().lower()
    aba = request.args.get("aba", "").strip()

    filtrados = []
    for p in CATALOGO:
        if aba and p["c"] != aba:
            continue
        if q and q not in p["n"].lower() and q not in p["f"].lower():
            continue
        filtrados.append(p)

    if not filtrados and not q and not aba:
        filtrados = CATALOGO

    cards = []
    for p in filtrados:
        d = desconto(p["de"], p["pc"])
        msg = (
            "Ola, ARGD Farma! Gostaria de fazer um pedido:\n\n"
            "Produto: " + p["n"] + "\n"
            "Valor: R$ " + brl(p["pc"]) + "\n\n"
            "Nome:\nEndereco (rua, numero, bairro):\nForma de pagamento (Pix / Cartao / Dinheiro):"
        )
        link = "https://wa.me/" + ZAP_PEDIDOS + "?text=" + urllib.parse.quote(msg)
        badge = ""
        if d > 0:
            badge = '<span class="badge-desc">-' + str(d) + '% OFF</span>'
        de_html = ""
        if d > 0:
            de_html = '<div class="preco-de">De R$ ' + brl(p["de"]) + '</div>'
        if p["e"] <= 10:
            est = '<div class="estoque">Apenas ' + str(int(p["e"])) + ' unidades em estoque</div>'
        else:
            est = '<div class="estoque ok">Disponivel em estoque</div>'
        cards.append(
            '<article class="card">'
            '<div class="card-topo">' + badge + '<span class="badge-cat">' + p["c"] + '</span></div>'
            '<div class="img-box"><span class="ico">&#128138;</span><span class="fab">' + p["f"] + '</span></div>'
            '<div class="card-body">'
            '<h3 class="nome">' + p["n"] + '</h3>'
            '<div class="precos">' + de_html +
            '<div class="preco-por"><span>R$</span> ' + brl(p["pc"]) + '</div>' +
            est + '</div>'
            '<a class="btn-zap" href="' + link + '" target="_blank" rel="noopener">PEDIR NO WHATSAPP</a>'
            '</div></article>'
        )

    pills = '<a class="pill ' + ("on" if not aba else "") + '" href="/">Todas</a>'
    for a in ABAS:
        on = "on" if aba == a else ""
        pills += '<a class="pill ' + on + '" href="/?aba=' + urllib.parse.quote_plus(a) + '">' + a + '</a>'

    return HTML.replace("__PILLS__", pills).replace("__CARDS__", "".join(cards)).replace("__TOTAL__", str(len(filtrados))).replace("__Q__", q)

HTML = """<!DOCTYPE html>
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
header{background:#fff;border-bottom:2px solid #e0f2fe;padding:18px 20px}
.hw{max-width:1240px;margin:auto;display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}
.marca h1{font-size:24px;font-weight:900;color:#0284c7}
.marca p{font-size:12px;color:#475569;font-weight:600}
form.busca{flex:1;min-width:260px;max-width:560px;display:flex;border:2px solid #cbd5e1;border-radius:12px;overflow:hidden}
form.busca input{flex:1;padding:12px 16px;border:none;outline:none;font-size:15px}
form.busca button{background:#0284c7;color:#fff;border:none;padding:0 22px;font-weight:700;cursor:pointer}
main{max-width:1240px;margin:22px auto;padding:0 16px}
.pills{display:flex;gap:8px;overflow-x:auto;padding-bottom:12px;margin-bottom:18px}
.pill{text-decoration:none;padding:8px 15px;background:#fff;border:1px solid #e2e8f0;border-radius:20px;font-size:13px;font-weight:700;color:#475569;white-space:nowrap}
.pill.on{background:#0284c7;color:#fff;border-color:#0284c7}
.meta{font-weight:700;color:#475569;margin-bottom:14px;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px}
.card{background:#fff;border-radius:16px;border:1px solid #e2e8f0;box-shadow:0 4px 15px rgba(0,0,0,.04);display:flex;flex-direction:column;position:relative;overflow:hidden}
.card-topo{position:absolute;top:10px;left:10px;right:10px;display:flex;justify-content:space-between;z-index:2;pointer-events:none}
.badge-desc{background:#dc2626;color:#fff;font-size:11px;font-weight:900;padding:4px 8px;border-radius:8px}
.badge-cat{background:rgba(15,23,42,.8);color:#fff;font-size:10px;font-weight:700;padding:4px 8px;border-radius:8px}
.img-box{height:120px;background:#f0f9ff;display:flex;flex-direction:column;align-items:center;justify-content:center;border-bottom:1px solid #e2e8f0}
.ico{font-size:32px}
.fab{font-size:11px;font-weight:800;color:#0284c7;text-transform:uppercase;margin-top:4px;text-align:center;padding:0 8px}
.card-body{padding:14px;display:flex;flex-direction:column;flex:1;justify-content:space-between}
.nome{font-size:13px;font-weight:700;line-height:1.4;margin-bottom:10px;min-height:36px}
.precos{background:#f8fafc;padding:9px 11px;border-radius:9px;margin-bottom:12px}
.preco-de{font-size:12px;text-decoration:line-through;color:#94a3b8;font-weight:600}
.preco-por{font-size:22px;font-weight:900;color:#16a34a;line-height:1.1}
.preco-por span{font-size:14px}
.estoque{font-size:11px;font-weight:700;color:#dc2626;margin-top:3px}
.estoque.ok{color:#059669}
.btn-zap{text-decoration:none;background:#16a34a;color:#fff;padding:11px;border-radius:9px;font-size:12px;font-weight:800;text-align:center;box-shadow:0 4px 12px rgba(22,163,74,.28)}
footer{background:#0f172a;color:#94a3b8;padding:44px 20px 22px;margin-top:56px;font-size:13px}
.fg{max-width:1240px;margin:auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:30px;padding-bottom:28px;border-bottom:1px solid #1e293b}
.fg h3{color:#fff;font-size:15px;margin-bottom:11px}
.fg p{line-height:1.65;margin-bottom:7px}
.legal{max-width:1240px;margin:22px auto 0;font-size:12px;text-align:center;color:#64748b;line-height:1.6}
</style>
</head>
<body>
<div class="topo">
<span>&#128666; Entrega rapida em Ituverava - SP</span>
<span>&#9200; Pedidos ate 18h: entrega no <b>mesmo dia</b></span>
<span>&#127769; Pedidos apos 18h: entrega no <b>dia seguinte a partir das 8h</b></span>
<span>&#128172; Pedidos: <b>(16) 99106-7477</b></span>
</div>
<header><div class="hw">
<div class="marca"><h1>ARGD Farma</h1><p>Drogaria Total Ituverava Delivery &bull; Ituverava - SP &bull; CEP 14500-053</p></div>
<form class="busca" method="GET" action="/"><input type="text" name="q" value="__Q__" placeholder="Buscar produto ou marca..."><button type="submit">Buscar</button></form>
</div></header>
<main>
<div class="pills">__PILLS__</div>
<div class="meta">__TOTAL__ produtos disponiveis</div>
<div class="grid">__CARDS__</div>
</main>
<footer>
<div class="fg">
<div><h3>Drogaria Total Ituverava Delivery</h3>
<p>Atendimento farmaceutico de confianca e entrega rapida em Ituverava - SP.</p>
<p><strong>Pedidos e Delivery:</strong> (16) 99106-7477</p>
<p><strong>Atendimento na loja:</strong> (16) 99998-2256</p>
<p>Localizacao: Ituverava - SP &bull; CEP 14500-053</p></div>
<div><h3>Politica de Entrega</h3>
<p>Pedidos realizados ate as 18h sao entregues no <strong>mesmo dia</strong>, em ate 45 minutos apos a confirmacao.</p>
<p>Pedidos realizados a partir das 18h sao entregues no <strong>dia seguinte, a partir das 8h</strong>.</p>
<p>Entregas realizadas exclusivamente por motoboy identificado da loja.</p></div>
<div><h3>Seguranca e Regulacao</h3>
<p>&bull; Dispensacao conforme RDC 44/2009 ANVISA</p>
<p>&bull; Farmaceutico Responsavel presente no horario de funcionamento</p>
<p>&bull; Medicamentos sob prescricao exigem receita apresentada ao farmaceutico</p>
<p>&bull; Medicamentos controlados nao sao comercializados pelo delivery</p></div>
</div>
<div class="legal">Drogaria Total Ituverava Delivery &bull; Todos os direitos reservados. Imagens meramente ilustrativas. Precos e estoques podem sofrer alteracoes sem aviso previo. Consulte sempre o farmaceutico.</div>
</footer>
</body>
</html>"""

if __name__ == "__main__":
    app.run(debug=True)
