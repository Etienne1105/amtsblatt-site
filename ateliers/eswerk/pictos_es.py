# -*- coding: utf-8 -*-
# Pictos ES — trait encre, aplat terracotta, rehaut safran (classe .jaune du moteur),
# accent naranja (classe .oranj). Micro-animations héritées : gr-pousse, gr-flamme,
# gr-cligne, gr-onde, gr-tourne. viewBox 96x96, trait "main levée" (courbes q).

def _svg(label, corps):
    return ('<svg class="picto" viewBox="0 0 96 96" role="img" aria-label="'
            + label + '">' + corps + '</svg>')

PICTOS = {}

# 1 — El alma : l'orange de Valence, feuille de huerta, fleur d'azahar qui pousse
PICTOS[1] = _svg("Orange de Valence &agrave; la fleur d&rsquo;azahar",
 '<circle class="oranj" cx="48" cy="54" r="26"/>'
 '<path class="trait" d="M34 44 q6 -6 14 -4" fill="none"/>'
 '<path class="plein" d="M48 28 q2 -10 12 -12 q0 10 -12 12 z"/>'
 '<g class="gr-pousse">'
 '<path class="trait" d="M52 26 q4 -10 14 -12" fill="none"/>'
 '<circle class="jaune" cx="68" cy="12" r="4"/>'
 '<circle fill="#F2E3C6" cx="64" cy="16" r="2.6"/><circle fill="#F2E3C6" cx="72" cy="15" r="2.6"/>'
 '</g>'
 '<line class="trait" x1="20" y1="86" x2="76" y2="86"/>')

# 2 — Las Fallas : le monument (ninot) et la flamme de la crem&agrave;
PICTOS[2] = _svg("Falla dress&eacute;e et flamme de la crem&agrave;",
 '<path class="plein" d="M34 82 l14 -46 l14 46 z"/>'
 '<circle class="jaune" cx="48" cy="30" r="7"/>'
 '<path class="trait" d="M28 82 h40" fill="none"/>'
 '<g class="gr-flamme">'
 '<path class="oranj" d="M70 60 q6 -12 0 -20 q-6 8 0 20 z"/>'
 '<path class="jaune" d="M70 56 q3 -7 0 -11 q-3 4 0 11 z"/>'
 '</g>'
 '<line class="trait" x1="16" y1="86" x2="80" y2="86"/>')

# 3 — Los códigos : deux bulles qui se répondent (valencien · castillan)
PICTOS[3] = _svg("Deux bulles de dialogue &mdash; valencien et castillan",
 '<path class="plein" d="M12 20 h44 v26 h-24 l-10 10 v-10 h-10 z"/>'
 '<path class="oranj" d="M42 48 h42 v24 h-10 v10 l-10 -10 h-22 z"/>'
 '<circle fill="#F2E3C6" cx="26" cy="33" r="3"/><circle fill="#F2E3C6" cx="36" cy="33" r="3"/><circle fill="#F2E3C6" cx="46" cy="33" r="3"/>'
 '<g class="gr-cligne"><circle class="jaune" cx="63" cy="60" r="4"/></g>'
 '<line class="trait" x1="14" y1="86" x2="82" y2="86"/>')

# 4 — La mesa : la paella vue de dessus, deux anses, le riz qui dore
PICTOS[4] = _svg("Paella aux deux anses, riz au safran",
 '<circle class="plein" cx="48" cy="50" r="26"/>'
 '<circle class="jaune" cx="48" cy="50" r="19"/>'
 '<path class="trait" d="M22 46 q-8 -2 -12 4 M74 46 q8 -2 12 4" fill="none" stroke-width="4"/>'
 '<circle class="oranj" cx="41" cy="45" r="3"/><circle class="oranj" cx="56" cy="52" r="3"/>'
 '<path class="trait" d="M44 56 q4 3 8 0" fill="none"/>'
 '<g class="gr-onde"><path class="trait" d="M40 22 q2 -6 0 -10 M52 22 q2 -6 0 -10" fill="none"/></g>'
 '<line class="trait" x1="18" y1="86" x2="78" y2="86"/>')

# 5 — Para beber : verre d'horchata embué, farton qui plonge
PICTOS[5] = _svg("Verre d&rsquo;horchata au farton",
 '<path class="plein" d="M30 30 l6 50 h24 l6 -50 z"/>'
 '<path d="M34 40 l3 34 h22 l3 -34 z" fill="#F2E3C6"/>'
 '<path class="jaune" d="M58 12 q16 4 12 22 l-8 14 q-3 -2 -2 -6 l6 -10 q2 -12 -8 -14 z"/>'
 '<g class="gr-onde"><path class="trait" d="M40 24 q2 -6 0 -10" fill="none"/></g>'
 '<line class="trait" x1="22" y1="86" x2="74" y2="86"/>')

# 6 — La ciudad : le Miguelete (tour octogonale) et l'&oelig;il de l'Hemisf&egrave;ric
PICTOS[6] = _svg("Le Miguelete et l&rsquo;&oelig;il de Calatrava",
 '<path class="plein" d="M28 82 v-48 l10 -8 v-6 h4 v6 l4 -3 v57 z"/>'
 '<rect class="jaune" x="34" y="58" width="7" height="12"/>'
 '<path class="trait" d="M26 34 h24" fill="none"/>'
 '<path class="oranj" d="M54 66 q14 -14 34 0 q-20 12 -34 0 z"/>'
 '<g class="gr-cligne"><circle class="plein" cx="71" cy="65" r="5"/></g>'
 '<line class="trait" x1="16" y1="86" x2="84" y2="86"/>')

# 7 — La huerta & l'Albufera : la barraca au toit pentu, roseaux, eau
PICTOS[7] = _svg("Barraca de l&rsquo;Albufera aux roseaux",
 '<path class="plein" d="M24 52 l24 -22 l24 22 z"/>'
 '<path d="M30 52 h36 v22 h-36 z" fill="#F2E3C6"/>'
 '<path class="trait" d="M30 52 h36 M45 74 v-12 h6 v12" fill="none"/>'
 '<path class="trait" d="M48 30 v-8 M48 22 l6 3" fill="none"/>'
 '<g class="gr-pousse"><path class="plein" d="M16 74 q-2 -14 4 -20 q4 8 -1 20 z" style="fill:#5C7345"/>'
 '<path class="plein" d="M80 74 q2 -14 -4 -20 q-4 8 1 20 z" style="fill:#5C7345"/></g>'
 '<path class="trait" d="M12 82 q10 5 20 0 q10 -5 20 0 q10 5 20 0 q6 -3 12 0" fill="none"/>')

# 8 — Las escapadas : château sur la colline, chemin qui grimpe
PICTOS[8] = _svg("Ch&acirc;teau perch&eacute; de X&agrave;tiva",
 '<path class="plein" d="M14 84 q34 -34 68 0 z"/>'
 '<path class="oranj" d="M38 50 v-14 h5 v4 h5 v-4 h5 v4 h5 v-4 h5 v14 z"/>'
 '<rect class="jaune" x="52" y="42" width="5" height="8"/>'
 '<path class="trait" d="M30 82 q10 -8 6 -16 q10 2 14 -8" fill="none" stroke-dasharray="4 4"/>'
 '<line class="trait" x1="12" y1="86" x2="84" y2="86"/>')

# 9 — En camino : le v&eacute;lo (Valenbisi) — la ville plate se roule
PICTOS[9] = _svg("V&eacute;lo dans la ville plate",
 '<circle class="trait" cx="28" cy="64" r="14" fill="none" stroke-width="4"/>'
 '<circle class="trait" cx="70" cy="64" r="14" fill="none" stroke-width="4"/>'
 '<path class="trait" d="M28 64 l14 -24 h16 l12 24 M42 40 l8 24 h-22" fill="none"/>'
 '<path class="oranj" d="M40 36 h12 v5 h-12 z"/>'
 '<g class="gr-onde"><path class="trait" d="M12 42 q-6 2 -8 6 M14 52 q-5 2 -7 5" fill="none"/></g>'
 '<line class="trait" x1="10" y1="86" x2="88" y2="86"/>')

# 10 — Glosario : la bulle qui parle, marqu&eacute;e &Ntilde;
PICTOS[10] = _svg("Bulle de parole &agrave; l&rsquo;e&ntilde;e",
 '<path class="plein" d="M16 20 h52 v36 h-30 l-12 12 v-12 h-10 z"/>'
 '<text x="42" y="50" text-anchor="middle" font-family="Abril Fatface,serif" font-size="30" fill="#F2E3C6">&Ntilde;</text>'
 '<g class="gr-onde"><path class="trait" d="M72 30 q5 8 0 16 M79 26 q8 12 0 24" fill="none"/></g>'
 '<circle class="oranj" cx="76" cy="72" r="6"/>')

# 11 — La despedida : le tampon socarrat rond, point final
PICTOS[11] = _svg("Tampon socarrat du dernier mot",
 '<circle class="plein" cx="48" cy="48" r="28"/>'
 '<circle class="trait" cx="48" cy="48" r="21" fill="none" stroke-dasharray="3 4"/>'
 '<path class="jaune" d="M36 48 l8 8 l16 -18 l-4 -4 l-12 14 l-4 -4 z"/>'
 '<g class="gr-cligne"><circle class="oranj" cx="72" cy="24" r="5"/></g>')

# 12 — réserve chronique : la noria qui tourne (héritage hydraulique)
PICTOS[12] = _svg("Noria de la huerta en marche",
 '<g class="gr-tourne" style="transform-origin:48px 48px">'
 '<circle class="trait" cx="48" cy="48" r="26" fill="none" stroke-width="4"/>'
 '<line class="trait" x1="48" y1="22" x2="48" y2="74"/><line class="trait" x1="22" y1="48" x2="74" y2="48"/>'
 '<line class="trait" x1="30" y1="30" x2="66" y2="66"/><line class="trait" x1="66" y1="30" x2="30" y2="66"/>'
 '<rect class="jaune" x="44" y="18" width="8" height="8"/><rect class="jaune" x="44" y="70" width="8" height="8"/>'
 '</g>'
 '<circle class="oranj" cx="48" cy="48" r="6"/>'
 '<path class="trait" d="M12 84 q10 5 20 0 q10 -5 20 0 q10 5 20 0 q6 -3 12 0" fill="none"/>')
