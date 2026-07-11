# -*- coding: utf-8 -*-
# ESWERK — l'assembleur du Llibret. Part de gr/index.html (moteur v5, peau STELE-ORACLE)
# et produit es/index.html (peau SOCARRAT-LLIBRET). Chaque substitution est ancrée,
# comptée, assertée. Deux gates finaux : zéro grec dans le JS, zéro entité grecque au HTML.
import re, json, sys

import contenido_a_es as ca
import contenido_b_es as cb
import cronica_es as cr
import glosario_es as gl
import preguntas_es as pq
import examen_es as ex

S = open('gr_index.html', encoding='utf-8').read()
N0 = len(S)

def rplc(anchor_pat, nouveau, n=1, regex=False, why=''):
    """Remplace exactement n occurrences, sinon on arrête tout."""
    global S
    if regex:
        trouve = re.findall(anchor_pat, S, re.S)
        assert len(trouve) == n, f"[{why}] ancre regex : {len(trouve)} occurrence(s), attendu {n} :: {anchor_pat[:80]}"
        S = re.sub(anchor_pat, lambda m: nouveau, S, count=n, flags=re.S)
    else:
        c = S.count(anchor_pat)
        assert c == n, f"[{why}] ancre : {c} occurrence(s), attendu {n} :: {anchor_pat[:80]}"
        S = S.replace(anchor_pat, nouveau, n)

def swap_section(idn, nouveau, why=''):
    rplc(r'<section[^>]*\bid="' + re.escape(idn) + r'"[^>]*>.*?</section>', nouveau, 1, regex=True, why=why or idn)

# ---------------------------------------------------------------- 1. HEAD
rplc('<title>&Eta; &Sigma;&tau;&#942;&lambda;&eta; &mdash; guide grec</title>',
     '<title>El Llibret &mdash; guide espagnol</title>', why='title')
rplc(r'<meta name="description" content="[^"]*">',
     '<meta name="description" content="Guide de terrain pour Val&egrave;ncia &mdash; retablos de c&eacute;ramique, '
     'Glosario parlant, La Prueba &agrave; la noria, couronne d&rsquo;azahar.">', 1, regex=True, why='meta desc')
rplc("family=Caudex:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;600;700&family=IBM+Plex+Sans:wght@400;600;700&display=swap",
     "family=Abril+Fatface&family=Alegreya:ital,wght@0,400;0,500;0,700;1,400&family=IBM+Plex+Mono:wght@400;600;700&display=swap",
     why='google fonts')

# ---------------------------------------------------------- 2. CSS : tokens
CSS_VARS = [
    ("--egee:#1E5FA8",  "--egee:#9C4722"),    # primaire : terracotta
    ("--nuit:#0C2340",  "--nuit:#7E2D1E"),    # sombre structurant : oxyde socarrat
    ("--adyton:#0B1220","--adyton:#1C0E06"),  # écran caché : braise
    ("--soleil:#E3A20F","--soleil:#D98E04"),  # safran
    ("--olive:#6E7F3C", "--olive:#5C7345"),   # huerta
    ("--terre:#C0532B", "--terre:#C75B12"),   # naranja
    ("--marbre:#F4EFE2","--marbre:#F2E3C6"),  # crème de riz
    ("--fond:#CDCCC0",  "--fond:#E6D7B8"),    # papier llibret chaud
    ("--encre:#1B2430", "--encre:#2B1E16"),   # noir fumée
    ("--sourd:#5D6470", "--sourd:#8A6F5C"),   # brun sourd
    ("--refus:#9E2B25", "--refus:#A6301C"),   # almagra
    ("--mono:'IBM Plex Mono',monospace", "--mono:'IBM Plex Mono',monospace"),
    ("--corps:'IBM Plex Sans',sans-serif","--corps:'Alegreya',serif"),
    ("--titre:'Caudex',serif","--titre:'Abril Fatface',serif"),
]
for a, b in CSS_VARS:
    if a != b: rplc(a, b, why='css var')

# hex durs du CSS (hors variables)
CSS_HEX = [("#7FE0C3","#F2C24B",4),("#C3D2E4","#EBD9BC",3),("#284A78","#8A3A1E",2),
           ("#E8DCC0","#EFE2C4",1),("#9A6E0A","#A66903",1),("#8B8778","#9C8870",1)]
for a,b,n in CSS_HEX: rplc(a,b,n,why='css hex '+a)

# cartouche d'en-tête du CSS
rplc(r'/\* Η ΣΤΗΛΗ — vibe stèle-oracle[^*]*\*/',
     '/* EL LLIBRET \u2014 vibe socarrat-llibret : terracotta de Paterna, safran, cr\u00e8me de riz, feu ma\u00eetris\u00e9 */',
     1, regex=True, why='cartouche css')

# méandre grec (soulignés/frises) -> sanefa de dents socarrat (triangles pleins/vides)
rplc("background:repeating-linear-gradient(90deg,var(--egee) 0 2px,transparent 2px 4px,var(--egee) 4px 6px,transparent 6px 16px) 0 0/16px 12px;",
     "background:repeating-linear-gradient(135deg,var(--egee) 0 5px,transparent 5px 10px),repeating-linear-gradient(45deg,var(--terre) 0 5px,transparent 5px 10px);background-size:14px 12px;",
     why='méandre->sanefa')

# ------------------------------------------------- 3. Navbar : orange tournante
# le soleil ilios (16 rais) devient l'orange de la huerta ; id + origin conservés pour le moteur
m = re.search(r'<svg class="ilios-nav"[^>]*>.*?</svg>', S, re.S)
assert m, "svg ilios-nav introuvable"
ORANGE_NAV = ('<svg class="ilios-nav" viewBox="0 0 48 48" aria-hidden="true">'
 '<g id="ilios-nav-g" style="transform-origin:24px 24px">'
 '<circle cx="24" cy="24" r="17" fill="#C75B12" stroke="#2B1E16" stroke-width="1.6"/>'
 '<circle cx="24" cy="24" r="12.5" fill="#F2C24B" stroke="#2B1E16" stroke-width="1.1"/>'
 '<g stroke="#C75B12" stroke-width="1.6">'
 '<line x1="24" y1="12.5" x2="24" y2="35.5"/><line x1="12.5" y1="24" x2="35.5" y2="24"/>'
 '<line x1="16" y1="16" x2="32" y2="32"/><line x1="32" y1="16" x2="16" y2="32"/></g>'
 '<circle cx="24" cy="24" r="2.6" fill="#C75B12"/>'
 '<path d="M27 8 q7 -6 12 -2 q-5 6 -12 2 z" fill="#5C7345" stroke="#2B1E16" stroke-width="1.1"/>'
 '</g></svg>')
S = S[:m.start()] + ORANGE_NAV + S[m.end():]
rplc('<span>&Alpha;&Gamma;&Omicron;&Rho;&Alpha;</span>', '<span>EL PATIO</span>', why='navbar label')

# --------------------------------------------------- 4. Sections de contenu
swap_section('stele', ca.STELE, 'couverture')
swap_section('agora', ca.AGORA, 'patio')
fiches = ca.FICHES_A + cb.FICHES_B
assert len(fiches) == 18, f"18 retablos attendus, {len(fiches)}"
for i in range(1, 10):
    swap_section(f'p{i}-1', fiches[(i-1)*2],   f'p{i}-1')
    swap_section(f'p{i}-2', fiches[(i-1)*2+1], f'p{i}-2')
assert len(gl.FICHES_TAAL) == 9
for j in range(1, 10):
    swap_section(f'p10-{j}', gl.FICHES_TAAL[j-1], f'glosario p10-{j}')
swap_section('manteion', pq.PRUEBA, 'la prueba')
swap_section('examen', ex.CORONA, 'examen azahar')
assert len(cr.FICHES_X) == 8
for k in range(1, 9):
    swap_section(f'x-{k}', cr.FICHES_X[k-1], f'crónica x-{k}')
swap_section('p11-1', cb.DESPEDIDA, 'despedida')
swap_section('kolophon', cb.KOLOPHON, 'colofón')
swap_section('geheim', cb.GEHEIM, 'la cremà')

# ------------------------------------------------------------ 5. Pinakas ES
PINAKAS = ('<section class="fiche" id="pinakas"><div class="corps-sec inhoud-corps">'
 '<h2 class="inhoud-titre">&Iacute;ndice &mdash; table des mati&egrave;res</h2><ol class="inhoud-liste">'
 '<li><a href="#p1-1">&sect;&nbsp;1 &mdash; L&rsquo;&acirc;me&nbsp;: sobremesa, fiesta, Lo Rat Penat</a></li>'
 '<li><a href="#p2-1">&sect;&nbsp;2 &mdash; Las Fallas&nbsp;: mascletà, ninots, la crem&agrave;</a></li>'
 '<li><a href="#p3-1">&sect;&nbsp;3 &mdash; Les codes&nbsp;: deux langues, bises, tact &amp; DANA</a></li>'
 '<li><a href="#p4-1">&sect;&nbsp;4 &mdash; La mesa&nbsp;: la vraie paella, o&ugrave;, quand, comment</a></li>'
 '<li><a href="#p5-1">&sect;&nbsp;5 &mdash; Boire&nbsp;: horchata, Agua de Valencia, cremaet</a></li>'
 '<li><a href="#p6-1">&sect;&nbsp;6 &mdash; La ville&nbsp;: Ciutat Vella, Calatrava, quartiers</a></li>'
 '<li><a href="#p7-1">&sect;&nbsp;7 &mdash; Huerta &amp; Albufera&nbsp;: barques, rizi&egrave;res, El Palmar</a></li>'
 '<li><a href="#p8-1">&sect;&nbsp;8 &mdash; Escapades&nbsp;: Sagunt, X&agrave;tiva, Pe&ntilde;&iacute;scola</a></li>'
 '<li><a href="#p9-1">&sect;&nbsp;9 &mdash; En camino&nbsp;: m&eacute;tro, Valenbisi, argent, s&eacute;curit&eacute;</a></li>'
 '<li><a href="#p10-1">&sect;&nbsp;10 &mdash; Glosario&nbsp;: l&rsquo;espagnol qui parle</a></li>'
 '<li><a href="#manteion">La Prueba &mdash; 12 situations, la noria juge</a></li>'
 '<li><a href="#examen">El Examen &mdash; 14 questions, la couronne d&rsquo;azahar</a></li>'
 '<li><a href="#x-1">Cr&oacute;nica &mdash; de Valentia &agrave; 2026</a></li>'
 '</ol><a class="retour-classeur" href="#agora">&larr; EL PATIO &mdash; retour &agrave; la cour</a></div></section>')
swap_section('pinakas', PINAKAS, 'índice')

# --------------------------------------------------------------- 6. LE SCRIPT
mjs = re.search(r'(<script[^>]*>)(.*?)(</script>)', S, re.S)
js = mjs.group(2)

# 6a. Lyra -> Dolcaina (bloc complet, du commentaire d'en-tête à l'alias Enigma inclus)
dolc = open('dolcaina.js', encoding='utf-8').read()
pat = r'/\* =+ Moteur sonore ENIGMA[^*]*\*/\s*const Lyra=\(function\(\)\{.*?\}\)\(\);\s*const Enigma=Lyra;'
assert len(re.findall(pat, js, re.S)) == 1, "bloc Lyra introuvable"
js = re.sub(pat, lambda m: dolc.strip(), js, count=1, flags=re.S)

# 6b. Stimme : voix es-ES (sélection exacte puis fallback préfixe 'es')
a = "voix=vs.find(v=>v.lang==='el-GR')||vs.find(v=>v.lang&&v.lang.indexOf('de')===0)||null;"
b = "voix=vs.find(v=>v.lang==='es-ES')||vs.find(v=>v.lang&&v.lang.indexOf('es')===0)||null;"
assert js.count(a) == 1, "sélecteur de voix Stimme introuvable"
js = js.replace(a, b)

# 6c. FRAGEN -> les 12 situations valenciennes
pat = r'const FRAGEN=\[.*?\n\];'
assert len(re.findall(pat, js, re.S)) == 1, "bloc FRAGEN"
js = re.sub(pat, lambda m: pq.FRAGEN_JS.strip(), js, count=1, flags=re.S)

# 6d. LEXICON -> récolte automatique du glosario (le récolteur d'examen adapté)
lex_js, lex = ex.lexicon_js("".join(gl.FICHES_TAAL))
pieges = [e for e in lex if e['piege']]
assert len(lex) >= 44, f"lexique trop maigre : {len(lex)}"
assert any('constipada' in e['nl'].lower() for e in pieges) and any('embarazada' in e['nl'].lower() for e in pieges), \
    "les deux faux amis doivent être marqués pièges"
pat = r'const LEXICON=\[.*?\];'
assert len(re.findall(pat, js, re.S)) == 1, "bloc LEXICON"
js = re.sub(pat, lambda m: lex_js, js, count=1, flags=re.S)

# 6e. L'egg des cordes : fréquences de guitare (mi-la-ré-sol graves) + tampon cremà
rplc_js = [("const FREQ={1:146.83,2:174.61,3:220.00,4:293.66};",
            "const FREQ={1:82.41,2:110.00,3:146.83,4:196.00};", 1),
           ("'\\u039a\\u0395\\u03a1\\u0391\\u03a5\\u039d\\u039f\\u03a3!'", "'\\u00a1A LA CREM\\u00c0!'", 1)]
# 6f. Libellés d'interface (échelle des notes espagnoles authentiques)
rplc_js += [
    ("'\\u0395\\u03a1\\u03a9\\u03a4\\u0397\\u03a3\\u0397 '", "'PREGUNTA '", 2),
    ("'\\u039a\\u03b1\\u03c4\\u03ac\\u03c3\\u03c4\\u03b1\\u03c3\\u03b7 \\u2014 '", "'Situaci\\u00f3n \\u2014 '", 1),
    ("'\\u0395\\u03a0\\u039f\\u039c\\u0395\\u039d\\u0397 \\u2192'", "'SIGUIENTE \\u2192'", 2),
    ("'\\u039a\\u03a1\\u0399\\u03a3\\u0397 \\u2192'", "'VEREDICTO \\u2192'", 2),
    ("'\\u0391\\u03a1\\u0399\\u03a3\\u03a4\\u0391'", "'MATR\\u00cdCULA DE HONOR'", 2),
    ("'\\u039b\\u0399\\u0391\\u039d \\u039a\\u0391\\u039b\\u03a9\\u03a3'", "'NOTABLE'", 2),
    ("'\\u039a\\u0391\\u039b\\u03a9\\u03a3'", "'BIEN'", 2),
    ("'\\u0391\\u03a0\\u0395\\u03a1\\u03a1\\u0399\\u03a6\\u0398\\u0397'", "'QUEMADO'", 2),
    ("'\\u0391\\u039e\\u0399\\u039f\\u039d'", "'\\u00a1FET!'", 2),
    ("'\\u0391\\u03a0\\u039f\\u039a\\u0391\\u039b\\u03a5\\u03a8\\u0397 \\u2014 montre tout'",
     "'REVELA \\u2014 montre tout'", 1),
    ("'\\u039a\\u03a1\\u03a5\\u03a8\\u0395 \\u03a4\\u0391 \\u2014 cache les sens'",
     "'A PRUEBA \\u2014 cache les sens'", 1),
]
for a, b, n in rplc_js:
    c = js.count(a)
    assert c == n, f"libellé JS [{a[:40]}…] : {c} occ., attendu {n}"
    js = js.replace(a, b)

# 6g. Les écrans de verdict (chaînes composites restantes contenant du grec)
lignes_grecques = [l for l in js.split('\n') if re.search(r'\\u03[0-9a-fA-F][0-9a-fA-F]', l)]
VERDICTS = {
    "TO MANTEIO": ("'<p class=\"bilan-titre\">'+t+'</p><p class=\"bilan-s\">'+s+'/12 \\u2014 '+lbl+'</p>'",),
}
# — le bilan du quiz : « ΤΟ ΜΑΝΤΕΙΟ ΕΚΛΕΙΣΕ » -> « LA PAELLA ESTÁ SERVIDA » ;
#   « Η κρίση του Μαντείου » -> « El veredicto de la noria »
for src, dst, n in [
    ("'\\u03a4\\u039f \\u039c\\u0391\\u039d\\u03a4\\u0395\\u0399\\u039f \\u0395\\u039a\\u039b\\u0395\\u0399\\u03a3\\u0395'",
     "'LA PAELLA EST\\u00c1 SERVIDA'", 1),
    ("'<span class=\"amtston\">\\u0397 \\u03ba\\u03c1\\u03af\\u03c3\\u03b7 \\u03c4\\u03bf\\u03c5 \\u039c\\u03b1\\u03bd\\u03c4\\u03b5\\u03af\\u03bf\\u03c5</span>'",
     "'<span class=\"amtston\">El veredicto de la noria</span>'", 1),
    ("'\\u039c\\u0395\\u03a4\\u0395\\u039e\\u0395\\u03a4\\u0391\\u03a3\\u03a4\\u0395\\u0391'", "'SUSPENSO'", 2),
    ("'\\u039e\\u0391\\u039d\\u0391 (recommencer)'", "'OTRA VEZ (recommencer)'", 2),
    ("'\\u0393\\u03c1\\u03ac\\u03c8\\u03b5 \\u03c4\\u03bf \\u03bd\\u03cc\\u03b7\\u03bc\\u03b1'", "'Escribe el sentido'", 1),
    ("'\\u0394\\u03b9\\u03ac\\u03bb\\u03b5\\u03be\\u03b5 \\u03c4\\u03bf \\u03bd\\u03cc\\u03b7\\u03bc\\u03b1'", "'Elige el sentido'", 1),
    ("'\\u0386\\u03ba\\u03bf\\u03c5\\u03c3\\u03b5'", "'Escucha'", 1),
    ("'\\u0395\\u039b\\u0395\\u0393\\u03a7\\u039f\\u03a3'", "'COMPROBAR'", 1),
    ("'\\u039f \\u0391\\u0393\\u03a9\\u039d \\u0395\\u03a4\\u0395\\u039b\\u0395\\u03a3\\u0398\\u0397'", "'EXAMEN TERMINADO'", 1),
    ("'\\u039f\\u03a7\\u0399'", "'NO'", 1),
    ("'\\u039d\\u0391\\u0399'", "'S\\u00cd'", 1),
]:
    c = js.count(src)
    assert c == n, f"verdict [{src[:50]}…] : {c} occ."
    js = js.replace(src, dst)

# 6h. GATE : plus un seul caractère grec (échappé ou brut) dans le JS
restes = re.findall(r'.{0,40}\\u03[0-9a-fA-F]{2}.{0,40}', js)
restes += re.findall(r'.{0,40}[\u0370-\u03ff].{0,40}', js)
assert not restes, "grec résiduel dans le JS :\n" + "\n".join(restes[:8])

S = S[:mjs.start()] + mjs.group(1) + js + mjs.group(3) + S[mjs.end():]

# ------------------------------------------- 7. Reskin hex global des résidus SVG
for a, b in [("#1E5FA8","#9C4722"),("#0C2340","#7E2D1E"),("#E3A20F","#D98E04"),
             ("#6E7F3C","#5C7345"),("#C0532B","#C75B12"),("#F4EFE2","#F2E3C6"),
             ("#1B2430","#2B1E16"),("#3F4A22","#4A3A20"),("Caudex,serif","Abril Fatface,serif")]:
    S = S.replace(a, b)

# ------------------------------------------------------ 8. GATES finaux HTML
ent = re.findall(r'&(?:Alpha|Beta|Gamma|Delta|Epsilon|Zeta|Eta|Theta|Iota|Kappa|Lambda|Mu|Nu|Xi|Omicron|Pi|Rho|Sigma|Tau|Upsilon|Phi|Chi|Psi|Omega|alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|omicron|pi|rho|sigmaf|sigma|tau|upsilon|phi|chi|psi|omega);', S)
num = [x for x in re.findall(r'&#(9\d\d);', S) if 913 <= int(x) <= 974]
assert not ent and not num, f"entités grecques résiduelles : {ent[:6]} {num[:6]}"
assert '\u0370' not in S and not re.search(r'[\u0370-\u03ff]', S), "grec brut résiduel dans le HTML"

for must in ['id="agora"','id="manteion"','id="examen"','id="geheim"','id="pinakas"',
             'id="chorde-1"','id="chorde-4"','id="meule"','amfora-1-vul','amfora-3-vul',
             'id="cachet-0"','id="cachet-13"','const Dolcaina','const Lyra=Dolcaina',
             'PREGUNTA','SOCARRAT','id="baukasten"','data-nofrappe']:
    assert must in S, f"attendu absent du build : {must}"

open('es_index.html', 'w', encoding='utf-8').write(S)
print(f"ESWERK ✓ — es_index.html : {len(S.encode('utf-8'))} octets (grec : {N0})")
print(f"  lexique récolté : {len(lex)} paires, dont {len(pieges)} pièges QCM-only")
print("  stempel couverture :", re.search(r'stempel-header">([^<]*)<', ca.STELE).group(1))
