# -*- coding: utf-8 -*-
# El Examen — écran couronne d'azahar (14 fleurs = cachets du moteur, classe .appose)
# + récolteur : moissonne les paires es<->fr des tablo-sprach du glosario généré.
import re, json, html as _html

# ---- 14 fleurs le long de l'arc Q(40,130)(150,96)(260,130), légèrement au-dessus ----
def _pos():
    P0, P1, P2 = (40,130), (150,96), (260,130)
    out = []
    for i in range(14):
        t = 0.055 + 0.89 * i / 13.0
        x = (1-t)**2*P0[0] + 2*(1-t)*t*P1[0] + t**2*P2[0]
        y = (1-t)**2*P0[1] + 2*(1-t)*t*P1[1] + t**2*P2[1]
        # tangente -> normale (fleur posée sur la branche, tournée avec elle)
        dx = 2*(1-t)*(P1[0]-P0[0]) + 2*t*(P2[0]-P1[0])
        dy = 2*(1-t)*(P1[1]-P0[1]) + 2*t*(P2[1]-P1[1])
        import math
        ang = math.degrees(math.atan2(dy, dx))
        n = math.hypot(dx, dy)
        out.append((round(x - 9*dy/n, 1), round(y + 9*(-dx)/n*-1 - 9, 1), round(ang, 1)))
    return out

def _fleur(i, x, y, ang):
    petales = "".join(
        '<circle cx="%.1f" cy="%.1f" r="3.4" fill="#F2E3C6" stroke="#8A6F5C" stroke-width="0.7"/>'
        % (5.6 * __import__("math").cos(k*1.2566), 5.6 * __import__("math").sin(k*1.2566))
        for k in range(5))
    return ('<g class="cachet" id="cachet-%d" transform="translate(%s,%s) rotate(%s)">'
            % (i, x, y, ang)
            + petales + '<circle cx="0" cy="0" r="2.4" fill="#D98E04"/></g>')

_FLEURS = "".join(_fleur(i, x, y, a) for i, (x, y, a) in enumerate(_pos()))

CORONA = ('<section class="fiche" id="examen" data-par="10" data-nofrappe>'
 '<div class="corps-sec examen-corps"><div class="examen-tete">'
 '<span class="parno">EL EXAMEN</span>'
 '<span id="ex-prog" class="quiz-prog">PREGUNTA 1/14</span>'
 '<button type="button" class="mute" id="ex-mute">SFX : S&Iacute;</button></div>'
 '<div class="stefani-cadre">'
 '<svg class="stefani" viewBox="0 0 300 150" role="img" '
 'aria-label="Couronne de fleurs d&rsquo;oranger de l&rsquo;examen de langue">'
 '<rect x="8" y="8" width="284" height="26" fill="#9C4722"/>'
 '<text x="150" y="27" text-anchor="middle" font-family="Abril Fatface,serif" '
 'font-size="15" fill="#F2E3C6">LA CORONA D&rsquo;AZAHAR</text>'
 '<path d="M40 130 Q150 96 260 130" fill="none" stroke="#5C7345" stroke-width="3.5"/>'
 '<path d="M60 124 q6 -8 13 -5 q-4 8 -13 5z M228 121 q7 -6 13 -2 q-5 8 -13 2z" fill="#5C7345"/>'
 '<g id="cachets">' + _FLEURS + '</g>'
 '<circle cx="150" cy="112" r="5" fill="none" stroke="#D98E04" stroke-width="2"/>'
 '</svg></div>'
 '<div class="examen-zone" id="ex-zone"></div>'
 '</div></section>')

# ---- le récolteur : tablo-sprach -> LEXICON ----
def _clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = _html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def recolter(glosario_html):
    lex = []
    for tm in re.finditer(r'<table class="tablo-sprach">(.*?)</table>', glosario_html, re.S):
        t = tm.group(1)
        cap = _clean(re.search(r'<caption>(.*?)</caption>', t, re.S).group(1))
        for rm in re.finditer(
            r'<tr><td class="de"><span lang="es">(.*?)</span>.*?data-de="(.*?)".*?'
            r'<td class="fr">(.*?)</td></tr>', t, re.S):
            mot, tts, fr = _clean(rm.group(1)), _html.unescape(rm.group(2)), _clean(rm.group(3))
            piege = ('pi\u00e8ge' in fr.lower())
            lex.append({"nl": mot, "tts": tts, "fr": fr, "cat": cap, "piege": piege})
    return lex

def lexicon_js(glosario_html):
    lex = recolter(glosario_html)
    return "const LEXICON=" + json.dumps(lex, ensure_ascii=False) + ";", lex
