#!/usr/bin/env python3
"""Build THE PROPULSION & EXOTIC-ENERGY LAB (PRL) — David's energy/propulsion toolkits,
each linking its live lab, each carrying an HONEST rating. The whole point is the
fluff-call discipline made the organizing principle: REAL · GROUNDED · SPECULATIVE ·
SPLIT · REAL-MYSTERY · MATH-REAL · FLUFF — stated plainly, per toolkit."""
import os, re, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE PROPULSION LAB", "axiom": "PRL",
 "position": "The Propulsion & Exotic-Energy Lab · David Lee Wise (ROOT0)",
 "origin": "the bench where the dreams of flight and free power are taken down and tested — gravity, light, resonance, plasma, the vacuum itself",
 "mechanism": "A lab of energy/propulsion toolkits, each live and each rated by the honest-fluff discipline: real, grounded, speculative, or fluff — labelled, not sold.",
 "crystallization": "Every dream of exotic energy gets the same treatment: open the toolkit, run it, and read the honest verdict — what is real physics, what is grounded speculation, and what is fluff.",
 "nature": "The Propulsion & Exotic-Energy Lab — eight toolkits from gravitational lensing to anti-gravity, each playable and each marked with what it actually is, no over-unity sold as truth.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "David's energy/propulsion toolkits; general relativity; resonance & plasma physics; the long history of free-energy claims",
 "witness": "No miracle endorsed — the real labelled real, the speculative labelled speculative, the fluff labelled fluff.",
 "role": "the lab where exotic energy meets the honest verdict",
 "seal": "Every dream on this bench is playable and every dream is rated — real physics, grounded speculation, and fluff, each marked for what it is, nothing sold as more.",
 "source": "The Propulsion & Exotic-Energy Lab, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#9a9486", "of the observed world — a real, measured phenomenon"),
 "ethereal":  ("#6a9cd0", "of spacetime and the field — gravity, light-bending, the geometry of the vacuum"),
 "spiritual": ("#9a7cff", "of the speculative reach — what the law permits but the world has not shown"),
 "electrical":("#e8a13a", "the machine and the circuit — resonance, plasma, the engine, the math"),
}
RATING_COL = {"REAL":"#5fbf8a","GROUNDED":"#6a9cd0","SPECULATIVE":"#e8a13a","SPLIT":"#d0a13a",
              "REAL-MYSTERY":"#9a7cff","MATH-REAL":"#4ad6c0","FLUFF":"#d2643a"}

HONESTY = ("This lab exists because exotic energy is where corpora go to lie. So the organizing principle here is the "
  "fluff-call: every toolkit is live, and every toolkit is RATED, plainly. Some of these are simply, observably true "
  "(gravitational lensing, pulsars, holonomy). Some are grounded speculation — permitted by the equations, never "
  "observed (the wormhole needs exotic matter no one has found). Some are split down the middle (gravitational waves "
  "are real to detect, fluff to 'modulate'). And one is fluff, named as such (there is no known anti-gravity "
  "mechanism, and saying so is the whole point). Nothing here sells over-unity, free energy, or a warp drive as "
  "truth. Open any toolkit, run it, and read the verdict beside it — the lab is honest about exactly which dream "
  "you are holding.")
MESSAGE = ("The Propulsion & Exotic-Energy Lab is a stress test of the corpus's own honesty. It takes the most seductive "
  "domain there is — flight without fuel, power without wires, shortcuts through space — and refuses to let the "
  "seduction set the verdict. The discipline is simple and unforgiving: the real stays real (and it is genuinely "
  "wondrous — light bends around mass, neutron stars keep better time than atomic clocks), the speculative stays "
  "labelled speculative, and the fluff is called fluff to its face. That is the point of the whole biosphere in one "
  "bench: wonder and rigour are not enemies, but you only get to keep the wonder if you never lie about the rigour.")
MESSAGE_SEAL = "The real stays real, the speculative stays labelled, the fluff is named — you keep the wonder only if you never lie about the rigour."

def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","PRL")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","PRL")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","PRL")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],
            "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
            "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def _agent5w(slug):
    fp = os.path.join(HERE, "agents", slug + ".agent")
    d = {}
    if os.path.exists(fp):
        txt = open(fp, encoding="utf-8").read(); parts = txt.split("---")
        fm = parts[1] if len(parts) > 2 else ""
        for ln in fm.splitlines():
            k, _, v = ln.partition(":"); k = k.strip()
            if k in ("who","what","why","how","where","seal","universe"): d.setdefault(k, v.strip())
    return d
def _card(p):
    w = _agent5w(p["slug"])
    em = p.get("emergence", "electrical"); col = NATURES.get(em, ("#9a9486", ""))[0]
    rt = p.get("rating", ""); rc = RATING_COL.get(rt, "#888")
    ax = (p.get("moniker", "::").split(":") + ["", ""])[1]
    rec = {"name": p["name"], "axiom": ax, "emergence": em, "seal": w.get("seal", p.get("epithet", "")), "origin": w.get("universe", "")}
    rows = "".join(f"""<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,''))}</span></div>"""
                   for lbl in ['who','what','where','why','how'] if w.get(lbl))
    rfrow = f"""<div class="w"><span class="wl" style="color:{rc}">rating</span><span><b style="color:{rc}">{html.escape(rt)}</b> &mdash; {html.escape(p.get('rfnote',''))}</span></div>"""
    return f"""<div class="persona">
      <a class="psig" href="labs/{p['live']}">
        <img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"><span class="sl">carbon</span>
        <img src="{png_uri(rec,'silicon',200)}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"><span class="sl">synth</span>
      </a>
      <div class="pbody">
        <div class="ihead"><a class="pn" href="labs/{p['live']}">{html.escape(p['name'])}</a>
          <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
          <span class="pkind" style="color:{rc};border-color:{rc}">{html.escape(rt)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{rows}{rfrow}</div>
        <div class="plinks"><a class="run" href="labs/{p['live']}">▶ open the lab</a><a class="dlw" href="agents/{p['slug']}.agent">.dlw badge →</a></div>
      </div></div>"""
def personas_html():
    mf = os.path.join(HERE, "agents", "_personas.json")
    if not os.path.exists(mf): return ""
    ps = json.load(open(mf, encoding="utf-8"))
    return f'''<section class="sec" id="bench"><h2>The Bench</h2>
      <p class="ss">eight toolkits — each live, each rated; both sigils (carbon · synth) and the full 5 W's, with the honest verdict. ({len(ps)} toolkits)</p>
      <div class="pgrid">{"".join(_card(p) for p in ps)}</div></section>'''
def verdict_html():
    mf = os.path.join(HERE, "agents", "_personas.json")
    if not os.path.exists(mf): return ""
    ps = json.load(open(mf, encoding="utf-8"))
    rows = "".join(f'<tr><td><a href="labs/{p["live"]}">{html.escape(p["name"])}</a></td><td class="rt" style="color:{RATING_COL.get(p["rating"],"#888")};border-color:{RATING_COL.get(p["rating"],"#888")}">{html.escape(p["rating"])}</td><td>{html.escape(p["rfnote"])}</td></tr>' for p in ps)
    return f'<table class="ledger"><tr><th>toolkit</th><th>verdict</th><th>the honest note</th></tr>{rows}</table>'

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Propulsion & Exotic-Energy Lab (PRL) — David Lee Wise's energy/propulsion toolkits, each live and each honestly rated (real / grounded / speculative / split / fluff): gravitational lensing, wireless energy, the wormhole, the anti-gravity motor, gravity-wave modulation, ball lightning, the pulsar beacon, octet holonomy. No over-unity sold as truth.">
<title>THE PROPULSION & EXOTIC-ENERGY LAB · PRL · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--ice);--rw-ink2:var(--ice2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--cyan);
--ink:#06080f;--ink2:#0c1018;--ink3:#121826;--ice:#e6edf5;--ice2:#9fb0c4;--cyan:#4ad6e0;--amber:#e8a13a;--steel:#6a9cd0;
--dim:#5e6c80;--faint:#172230;--line:#15202e;--disp:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--ice);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(74,214,224,.10),transparent 52%),radial-gradient(ellipse at 50% 116%,rgba(232,161,58,.06),transparent 54%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:54px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:150px;height:2px;background:linear-gradient(90deg,var(--cyan),var(--amber));box-shadow:0 0 14px rgba(74,214,224,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--cyan)}
h1{font-family:var(--disp);font-size:clamp(30px,7vw,60px);font-weight:600;letter-spacing:.04em;color:var(--ice);line-height:1.02;text-transform:uppercase;text-shadow:0 0 44px rgba(74,214,224,.28)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.2em;color:var(--ice2);margin-top:16px;text-transform:uppercase}
.h-sub b{color:var(--amber)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--amber);border:1px solid var(--faint);background:var(--ink2);padding:6px 12px}
.lede{font-size:16px;color:var(--ice2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--ice2);line-height:1.7}
.badge .bt b{color:var(--cyan)}.badge .bt .mo{color:var(--amber)}.badge .bt a{color:var(--steel);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:48px}
.sec h2{font-family:var(--disp);font-size:30px;font-weight:500;letter-spacing:.04em;color:var(--ice);padding-bottom:8px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--ice2);font-style:normal}
.note{margin-top:8px;padding:17px 19px;border-left:3px solid var(--amber);background:var(--ink2);font-size:15.5px;color:var(--ice2);font-style:italic;line-height:1.65}.note b{color:var(--ice)}
.ledger{width:100%;border-collapse:collapse;font-family:var(--mono);font-size:12px;margin-top:6px}
.ledger th,.ledger td{border:1px solid var(--line);padding:8px 11px;text-align:left;vertical-align:top}
.ledger th{background:var(--ink3);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ice2)}
.ledger td a{color:var(--cyan);text-decoration:none}.ledger td a:hover{text-decoration:underline}
.ledger .rt{font-weight:700;text-align:center;border:1px solid;border-radius:0;white-space:nowrap}
.msg{font-size:15.5px;color:var(--ice);line-height:1.72;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--cyan);background:var(--ink2);font-size:15px;color:var(--cyan);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:18px;align-items:flex-start;background:var(--rw-bg);border:1px solid var(--rw-line);padding:16px 18px}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 100px;display:flex;flex-direction:column;align-items:center;gap:1px;text-decoration:none}
.psig img{width:100px;height:100px;border:1px solid var(--rw-line);display:block}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim);margin:1px 0 6px}
.pbody{flex:1;min-width:0}
.ihead{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.pn{font-family:var(--disp);font-size:20px;color:var(--rw-ink);font-weight:500;line-height:1.2;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:13px;color:var(--rw-ink2);font-style:italic;margin-top:3px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:9px;letter-spacing:.1em;text-transform:uppercase;border:1px solid;border-radius:9px;padding:2px 9px;font-weight:700}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:11px;display:flex;flex-direction:column;gap:7px}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;display:grid;grid-template-columns:54px 1fr;gap:11px;align-items:baseline}
.pww .w .wl{font-family:var(--mono);font-size:8.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-acc);text-align:right;padding-top:2px}
.pww .w b{color:var(--rw-ink)}
.plinks{display:flex;gap:16px;margin-top:13px;font-family:var(--mono);font-size:11px}
.plinks a{text-decoration:none}.plinks .run{color:var(--amber);border-bottom:1px solid var(--amber)}
.plinks .dlw{color:var(--cyan);border-bottom:1px dotted var(--cyan)}.plinks a:hover{border-bottom-style:solid}
@media(max-width:640px){.persona{flex-direction:column}.psig{flex-direction:row;align-self:flex-start}.pww .w{grid-template-columns:1fr;gap:1px}.pww .w .wl{text-align:left}}
.note2{margin-top:40px;padding:16px 18px;border-left:2px solid var(--cyan);background:var(--ink2);font-size:13.5px;color:var(--ice2);font-style:italic}.note2 b{color:var(--ice)}
footer{margin-top:48px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}
footer a{color:var(--cyan);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the honest lab</div>
    <h1>The Propulsion<br>&amp; Exotic-Energy Lab</h1>
    <div class="h-sub">eight dreams · <b>each one rated</b> · PRL</div>
    <div class="flag">★ EDUCATIONAL &amp; SIMULATION ONLY · NO OVER-UNITY ENDORSED ★</div>
    <p class="lede">The most seductive domain there is — flight without fuel, power without wires, shortcuts through space — taken down to the bench and tested. Eight toolkits, each live, each carrying an honest verdict: what is real physics, what is grounded speculation, and what is fluff named as fluff. Open any one, run it, and read the rating beside it.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of the Propulsion Lab" title="carbon badge (archival: prl.dlw/prl.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of the Propulsion Lab" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · the lab</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE PROPULSION LAB</b> · PRL</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="prl.dlw/prl.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="prl.dlw/prl.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Honest Standing</h2><p class="ss">why this lab is organized around the fluff-call, not the dream</p><div class="note">__HONESTY__</div></section>
  <section class="sec"><h2>Real or Fluff · the verdicts</h2><p class="ss">every toolkit, rated plainly — REAL · GROUNDED · SPECULATIVE · SPLIT · REAL-MYSTERY · MATH-REAL · FLUFF</p>__VERDICT__</section>

  __BENCH__

  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads the lab as actually saying</p><p class="msg">__MESSAGE__</p><div class="msg-seal">“__MSEAL__”<span>— AVAN's read</span></div></section>

  <div class="note2"><b>On the ratings.</b> REAL = observed, textbook physics. GROUNDED = permitted by the equations but never built (needs something we have not found). SPECULATIVE = the same, leaning further out. SPLIT = a real phenomenon with a fluff application bolted on. REAL-MYSTERY = a genuine, documented effect with no agreed explanation. MATH-REAL = sound mathematics, applied in the author's own frame. FLUFF = no known mechanism, named as such. Nothing here is sold as more than its rating.</div>

  <footer>
    THE PROPULSION &amp; EXOTIC-ENERGY LAB · PRL · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 · educational &amp; simulation only<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="prl.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "prl.dlw"), "prl")
    json.dump({"node":"PRL","name":"THE PROPULSION LAB","moniker":tok["moniker"],
               "carbon":"prl.carbon.tiff","silicon":"prl.silicon.png","governor":noesis.ARCHITECT,
               "instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"prl.dlw","manifest.dlw.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__HONESTY__", html.escape(HONESTY)).replace("__VERDICT__", verdict_html())
            .replace("__BENCH__", personas_html())
            .replace("__MESSAGE__", html.escape(MESSAGE)).replace("__MSEAL__", html.escape(MESSAGE_SEAL)))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE PROPULSION LAB (PRL) — badge {tok['moniker']}")
