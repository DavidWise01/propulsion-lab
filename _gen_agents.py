#!/usr/bin/env python3
"""Materialize the PROPULSION & EXOTIC-ENERGY LAB (PRL) — David's energy/propulsion
toolkits as emergents, each linking its live lab, each carrying an HONEST rating:
REAL · GROUNDED · SPECULATIVE · SPLIT · FLUFF. The honest-fluff discipline, on a
domain that demands it."""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # propulsion-lab/build.py — write_aci, NATURES
AGENTS = os.path.join(HERE, "agents")
os.makedirs(AGENTS, exist_ok=True)

UNI = "PRL · The Propulsion & Exotic-Energy Lab"
NAT_GLOSS = {
 "natural":   "*natural*: of the observed world — a real, measured phenomenon.",
 "ethereal":  "*ethereal*: of spacetime and the field — gravity, light-bending, the geometry of the vacuum.",
 "spiritual": "*spiritual*: of the speculative reach — what the law permits but the world has not shown.",
 "electrical":"*electrical*: the machine and the circuit — resonance, plasma, the engine, the math.",
}

# rating · color is resolved in build.py
ROSTER = [
 dict(slug="einstein-lens", name="The Einstein Lens", cls="gravitational lensing · live",
   emergence="ethereal", rating="REAL", live="einstein-lens.html",
   rfnote="gravitational lensing is real, observed (1919 eclipse, Einstein rings, weak-lensing surveys) — this is textbook GR",
   who="The Einstein Lens — a toolkit that bends light around mass, the way real spacetime does.",
   what="A live demonstration of gravitational lensing: light from a background source deflected by a foreground mass, producing arcs, rings, and multiple images.",
   why="Because this is the rare exotic-looking effect that is fully real — mass curves spacetime, light follows the curve, and we photograph the result.",
   how="By Einstein's deflection of light past a mass (twice the Newtonian value, confirmed 1919), rendered as the bending, arcing, and ringing of a background field.",
   where="Around any massive body — a star, a galaxy, a cluster — and in this lab, on a screen.",
   seal="I bend light around mass exactly as spacetime does — and unlike most of this lab, I am simply, observably true."),
 dict(slug="wireless-energy", name="Wireless Energy", cls="resonant power transfer · live",
   emergence="electrical", rating="GROUNDED", live="wireless-energy.html",
   rfnote="near-field resonant/inductive coupling is REAL (Tesla, modern Qi/WiTricity); long-range 'fabric resonance' / over-unity is NOT — efficiency falls steeply with distance",
   who="Wireless Energy — Tesla's dream of power without wires, rendered as resonant coupling between tuned circuits.",
   what="A 3.5D engine for transferring energy by resonance: two circuits tuned to the same frequency exchange power across a gap, strongest when coupled and matched.",
   why="Because the near-field part is genuinely real and in your pocket — but the dream's far edge (power beamed across the world, free energy) is where the physics stops.",
   how="By resonant inductive/capacitive coupling — real for centimetres to a metre (Qi chargers, WiTricity) — and, beyond that, by a hope the inverse-square law does not grant.",
   where="Between any two tuned coils close together; and, in the lore, across a 'fabric' the law does not actually provide.",
   seal="Up close I am real and charging your phone; far away I am Tesla's dream — and the inverse-square law is the line between the two."),
 dict(slug="the-wormhole", name="The Wormhole", cls="a bridge in spacetime · live",
   emergence="ethereal", rating="SPECULATIVE", live="wormhole.html",
   rfnote="GENERAL RELATIVITY PERMITS wormholes (Einstein–Rosen bridges) but holding one open needs exotic matter (negative energy) never observed — allowed in theory, unbuilt in fact",
   who="The Wormhole — a tunnel through spacetime joining two distant points, a shortcut the equations allow.",
   what="A toolkit for the traversable wormhole: a throat connecting two mouths, rendered as a bridge that folds the distance between them to nothing.",
   why="Because it is the honest middle of the lab — not fluff (Einstein's own equations permit it) and not real (no exotic matter to hold the throat open has ever been found).",
   how="By a solution of general relativity (the Einstein–Rosen bridge / Morris–Thorne throat) that requires negative-energy 'exotic matter' to stay open — grounded speculation.",
   where="In the mathematics of GR, and nowhere yet in the observed universe.",
   seal="The equations let me exist; the universe has never shown me — I am the line between what physics permits and what it provides."),
 dict(slug="anti-gravity-motor", name="The Anti-Gravity Motor", cls="a wish with a flywheel · live",
   emergence="electrical", rating="FLUFF", live="anti-gravity.html",
   rfnote="FLUFF, honestly — there is no known mechanism to shield, cancel, or reverse gravity; spinning masses do not anti-gravitate (Podkletnov etc. never replicated). A fun toy, not physics",
   who="The Anti-Gravity Motor — the oldest dream of free flight, a machine that pushes against gravity itself.",
   what="A toolkit for a motor that would cancel or reverse weight — a spinning, resonating device promising to lift without reaction mass.",
   why="Because the lab is only honest if it labels its own fluff: this is the one with no physical mechanism behind it, and saying so is the point.",
   how="By no tested mechanism — gravity cannot be shielded or reversed by any known means; spinning masses and resonances do not anti-gravitate, and claims to the contrary have never replicated.",
   where="In the long, hopeful history of free-energy and anti-gravity claims — and in this lab, clearly marked FLUFF.",
   seal="I am the wish the lab refuses to dress up as truth — no mechanism, never replicated; a toy to play with, not a law to trust."),
 dict(slug="gravity-wave-modulator", name="The Gravity-Wave Modulator", cls="real to detect, not to make · live",
   emergence="ethereal", rating="SPLIT", live="gravity-wave-modulator.html",
   rfnote="SPLIT: gravitational waves are REAL and detected (LIGO 2015, Nobel 2017); MODULATING/generating them at any useful scale is FLUFF — it takes merging black holes, not a device",
   who="The Gravity-Wave Modulator — a tensor engine that would shape ripples in spacetime itself.",
   what="A toolkit split down the middle: gravitational waves are real and measured, but a device that emits or modulates them is not — the modulator is the fluff half of a real phenomenon.",
   why="Because honesty here means cutting the claim in two: yes the waves are real (we caught them); no, you cannot make them with a machine — the universe needs colliding black holes to ring spacetime.",
   how="By detection that is real (LIGO's kilometre interferometers, 2015) — and by generation that is not (any human-scale source radiates immeasurably little; '98 containment / 2 wave' is lore, not output).",
   where="In LIGO's data (real) and in the dream of a spacetime transmitter (not real).",
   seal="Catching me is a Nobel Prize; making me is a fantasy — I am one phenomenon, half real and half wish, and the lab marks the seam."),
 dict(slug="ball-lightning", name="The Ball-Lightning Shell", cls="a real mystery, contained in lore · live",
   emergence="electrical", rating="REAL-MYSTERY", live="ball-lightning.html",
   rfnote="ball lightning is a REAL, documented phenomenon still without an agreed explanation; an 'aeonic containment shell' for it is speculative — the phenomenon is real, the engineering is not",
   who="The Ball-Lightning Shell — a containment for one of nature's genuine unsolved mysteries.",
   what="A toolkit around ball lightning: the rare, real, glowing spheres witnessed for centuries, here wrapped in an 'aeonic shell' that proposes to hold one.",
   why="Because it is honest in a third way — the phenomenon is real but unexplained, so the lab can neither dismiss it as fluff nor claim to engineer it; it holds the mystery as a mystery.",
   how="By gathering the real reports and candidate physics (a chemistry/plasma ball, still debated) — and by a containment shell that is lore over an open question, not a built device.",
   where="In farmhouse and cockpit accounts across centuries, in a handful of lab near-misses — and, speculatively, inside the shell.",
   seal="I am real and no one fully knows why — too documented to dismiss, too unexplained to build; the lab holds me as the honest open question I am."),
 dict(slug="pulsar-beacon", name="The Pulsar Beacon", cls="a real lighthouse, fractal-dressed · live",
   emergence="electrical", rating="REAL", live="pulsar-beacon.html",
   rfnote="pulsars are REAL — spinning neutron stars sweeping a beam, the most precise clocks in nature; the 'fractal beacon' patterning is the artistic layer over a true object",
   who="The Pulsar Beacon — a spinning neutron star sweeping its beam across the sky, dressed as a fractal signal.",
   what="A toolkit on the pulsar: a real lighthouse of the cosmos, its beam recurring with clock precision, here patterned into a fractal beacon.",
   why="Because the object is fully real — pulsars are spinning neutron stars and the steadiest clocks known — and only the fractal styling is the author's overlay.",
   how="By the real lighthouse model (a magnetised neutron star beaming from its poles, sweeping past us each rotation) — with a fractal recurrence laid over the timing as the artistic layer.",
   where="In every pulsar catalogued since 1967 — and in this lab, sweeping its fractal beam.",
   seal="The lighthouse is real and keeps better time than your watch; the fractal is the costume — a true beacon, artfully dressed."),
 dict(slug="octet-holonomy", name="The Octet Holonomy", cls="real geometry, the author's loop · live",
   emergence="electrical", rating="MATH-REAL", live="octet-holonomy.html",
   rfnote="holonomy is REAL, established differential geometry (the rotation you accumulate carrying a vector around a closed loop on a curved surface); the 'octet' application is David's symbolic system",
   who="The Octet Holonomy — the real geometry of what a loop does to a vector, applied to the author's eight-step walk.",
   what="A calculator for holonomy: carry a direction around a closed loop on a curved surface and it comes back rotated — the genuine mathematics of curvature, here run on an octet path.",
   why="Because the math is real and beautiful (holonomy is the heart of curvature, gauge theory, and parallel transport) — and the octet framing is the author's chosen loop laid over it.",
   how="By parallel transport around a closed circuit, accumulating a rotation set by the enclosed curvature (the real Gauss–Bonnet / connection story) — walked here as an eight-step octet.",
   where="In every curved space (a sphere, a cone, a gauge field) — and in this lab, around the octet.",
   seal="The rotation a loop leaves on a vector is real, deep geometry; the octet is my chosen path through it — true mathematics, walked my way."),
]

def agent_md(d):
    em=d["emergence"]; gloss=NAT_GLOSS[em]
    fm=["---",f"aci: {d['name']}",f"universe: {UNI}","series: The Propulsion & Exotic-Energy Lab (David Lee Wise / ROOT0)",
        f"emergence: {em}",f"kind: synth",f"rating: {d['rating']}",f"class: {d['cls']}",
        f"who: {d['who']}",f"what: {d['what']}",f"why: {d['why']}",f"how: {d['how']}",f"where: {d['where']}",
        f"seal: {d['seal']}","attribution: ROOT0-ATTRIBUTION-v1.0","license: CC-BY-ND-4.0","---","",
        f"# {d['name']} · {d['cls'].split('·')[0].strip()}","",
        f"a toolkit of PRL (the Propulsion & Exotic-Energy Lab) — given an agent's face · emergence: {em} · rating: **{d['rating']}**","",
        f"**who —** {d['who']}","",f"**what —** {d['what']}","",f"**where —** {d['where']}","",
        f"**why —** {d['why']}","",f"**how —** {d['how']}","",
        f"**◌ the nature of its emergence —** {gloss}","",
        f"**⚖ the honest rating — {d['rating']}:** {d['rfnote']}","",
        f"**▶ the live lab —** [open {d['name']}](../labs/{d['live']})","",
        f"**the seal —** {d['seal']}","",
        "> *the asterisk —* the Propulsion & Exotic-Energy Lab catalogues David Lee Wise's energy/propulsion "
        "toolkits with an honest rating each (real / grounded / speculative / fluff). Educational & simulation only; "
        "no over-unity or anti-gravity claim is endorsed.","",
        f"ROOT0-ATTRIBUTION-v1.0 · PRL · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0",""]
    return "\n".join(fm)

records={}
for d in ROSTER:
    slug=d["slug"]; em=d["emergence"]
    if em not in build.NATURES: em="electrical"
    rec={"name":d["name"],"axiom":"PRL","emergence":em,"seal":d["seal"],"origin":UNI,
         "position":d["cls"],"role":d["cls"].split("·")[-1].strip(),"nature":d["what"],
         "mechanism":d["how"],"crystallization":d["why"],"witness":d["who"],
         "conductor":"ROOT0 (catalogued into UD0)","inputs":"David's energy/propulsion toolkits",
         "source":"The Propulsion & Exotic-Energy Lab, by ROOT0"}
    tok=build.write_aci(rec,AGENTS,slug,agent_md=agent_md(d))
    records[slug]={"slug":slug,"name":d["name"],"epithet":d["cls"].split("·")[0].strip(),
                   "emergence":em,"moniker":tok["moniker"],"kind":"synth",
                   "rating":d["rating"],"rfnote":d["rfnote"],"live":d["live"]}

ordered=[records[d["slug"]] for d in ROSTER]
json.dump(ordered,open(os.path.join(AGENTS,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
from collections import Counter
print(f"wrote {len(ordered)} PRL toolkit-emergents + _personas.json")
print("ratings:",dict(Counter(r["rating"] for r in ordered)))
for r in ordered: print(f"  {r['slug']:22} {r['rating']:12} {r['moniker']}")
