from flask import Flask
import urllib.parse, re, requests
from bs4 import BeautifulSoup
app=Flask(__name__)
MAG="magazineargd"; AMZ="centralargd-20"; ML="aa20250201180225"
HEAD={"User-Agent":"Mozilla/5.0 Chrome/120.0.0.0"}

def busca_real(termo):
 l=[]
 try:
  u=f"https://www.magazinevoce.com.br/{MAG}/busca/{urllib.parse.quote(termo)}/"
  r=requests.get(u,headers=HEAD,timeout=15); s=BeautifulSoup(r.text,'html.parser')
  p=None; el=s.find(attrs={"data-testid":"price-value"})
  if el:
   m=re.search(r'R\$\s*([\d\.,]+)',el.text)
   if m: p=float(m.group(1).replace('.','').replace(',','.'))
  img=s.find('img',attrs={"data-testid":"product-card-image"})
  im=img['src'] if img else None
  if im and im.startswith('//'): im='https:'+im
  l.append({"n":"Magalu","p":p,"img":im,"link":u})
 except: 
  l.append({"n":"Magalu","p":None,"img":None,"link":f"https://www.magazinevoce.com.br/{MAG}/busca/{urllib.parse.quote(termo)}/"})
 try:
  u=f"https://lista.mercadolivre.com.br/{urllib.parse.quote(termo)}"
  r=requests.get(u,headers=HEAD,timeout=12); s=BeautifulSoup(r.text,'html.parser')
  p=None; f=s.select_one('span.andes-money-amount__fraction')
  if f:
   try: p=float(f.text.replace('.','').replace(',','.'))
   except: pass
  im=s.select_one('img.ui-search-result-image__element')
  im=im['src'] if im else None
  l.append({"n":"Mercado Livre","p":p,"img":im,"link":u+f"?matt_word={ML}"})
 except: 
  l.append({"n":"Mercado Livre","p":None,"img":None,"link":f"https://lista.mercadolivre.com.br/{urllib.parse.quote(termo)}?matt_word={ML}"})
 l.append({"n":"Amazon","p":None,"img":None,"link":f"https://www.amazon.com.br/s?k={urllib.parse.quote(termo)}&tag={AMZ}"})
 return l

@app.route('/produto/<path:t>')
def prod(t):
 td=urllib.parse.unquote(t); ds=busca_real(td)
 reais=sorted([x for x in ds if x["p"]],key=lambda x:x["p"])
 img=next((x["img"] for x in ds if x["img"]),None) or "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800"
 html=""
 for j in ds:
  if j["p"]:
   html+=f'<div style="border:3px solid #00C851;border-radius:14px;padding:12px;margin-bottom:10px;background:#f0fff0"><b>{j["n"]} - R$ {j["p"]:.2f} REAL AQUI DENTRO</b><br><button style="width:100%;background:#000;color:#FFDD00;padding:12px;border-radius:100px;font-weight:900;margin-top:8px" onclick="window.open(\'{j["link"]}\',\'_blank\')">COMPRAR AQUI NO SITE</button></div>'
  else:
   html+=f'<div style="border:2px solid #000;border-radius:14px;padding:12px;margin-bottom:10px"><b>{j["n"]}</b><br><button style="width:100%;background:#000;color:#FFDD00;padding:10px;border-radius:100px" onclick="window.open(\'{j["link"]}\',\'_blank\')">VER PREÇO REAL</button></div>'
 return f'<body style="font-family:Arial;margin:0"><div style="background:#000;color:#FFDD00;padding:12px;font-weight:900">CentralARGD - PREÇO REAL</div><div style="display:flex;gap:10px;padding:10px"><img src="{img}" style="width:45%;border:3px solid #000;border-radius:16px;object-fit:contain"><div><h2 style="font-size:16px">{td.title()}</h2></div></div><div style="padding:12px;background:#f5f5f5">{html}</div></body>'

@app.route('/')
def h(): return '<meta name=viewport content="width=device-width"><div style="text-align:center;padding:30px;font-family:Arial"><h2>CentralARGD</h2><input id=q placeholder="iPhone 17 Max Laranja" style="padding:12px;width:60%;border:2px solid #000;border-radius:100px"><button onclick="location.href=\'/produto/\'+encodeURIComponent(q.value)" style="padding:12px;background:#000;color:#FFDD00;border-radius:100px;font-weight:900">BUSCAR PREÇO REAL</button></div>'
