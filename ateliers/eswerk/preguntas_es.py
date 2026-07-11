# -*- coding: utf-8 -*-
# La Prueba — 12 situations (format FRAGEN du moteur : sit/q/c[3]/b/ex)
# + l'écran quiz : noria correctrice (id=meule), frein, filet de caldo, paella
#   en coupe à 3 zones de socarrat (ids amfora-1..3-vul), rotors PREG./CROSTA.
import json

FRAGEN_ES = [
 {
  "sit": "Il est 20h, vous avez faim, et le petit restaurant du coin affiche une belle « paella valenciana ».",
  "q": "Tu commandes ?",
  "c": [
   "Oui, parfait pour souper",
   "Non — la paella, c'est le midi",
   "Oui, mais sans riz"
  ],
  "b": 1,
  "ex": "Plat du midi, toujours. Un restaurant qui pousse la paella le soir cuisine pour les touristes — et souvent au micro-ondes."
 },
 {
  "sit": "Le serveur pose la paella. Ta voisine québécoise cherche le chorizo des yeux.",
  "q": "Dans une paella valenciana, le chorizo…",
  "c": [
   "Est indispensable",
   "Se demande à part",
   "Est un sacrilège documenté"
  ],
  "b": 2,
  "ex": "Le canon tient en dix ingrédients : poulet, lapin, haricots, garrofó, tomate, paprika, safran, huile, riz, eau. Ni chorizo, ni fruits de mer."
 },
 {
  "sit": "Au fond de la poêle, une croûte de riz doré accroche à la cuillère.",
  "q": "Tu fais quoi ?",
  "c": [
   "Tu la grattes : c'est le trésor",
   "Tu la laisses : c'est brûlé",
   "Tu demandes une réduction"
  ],
  "b": 0,
  "ex": "C'est le socarrat — la partie la plus convoitée. On la gratte directement dans la poêle, et on complimente la maison."
 },
 {
  "sit": "Sur le panneau : « Xàtiva ». Sur ton billet de train : « Játiva ».",
  "q": "Il se passe quoi ?",
  "c": [
   "Deux villes différentes",
   "La même ville, deux langues officielles",
   "Une faute d'impression"
  ],
  "b": 1,
  "ex": "Valencien et castillan coexistent partout : Russafa/Ruzafa, València/Valencia. Ce n'est pas une erreur, c'est la ville."
 },
 {
  "sit": "Janvier. Une carte affiche des « clòchinas » (moules locales) en vedette.",
  "q": "Tu en penses quoi ?",
  "c": [
   "Méfiance : leur saison, c'est mai-août",
   "Chouette, c'est la saison",
   "Les clòchinas n'existent pas"
  ],
  "b": 0,
  "ex": "Les vraies clòchinas se pêchent de mai à août. Hors saison, ce sont des moules d'ailleurs déguisées en fierté locale."
 },
 {
  "sit": "1er mars, 13h55, Plaza del Ayuntamiento. La foule se masse, des locaux entrouvrent la bouche.",
  "q": "Pourquoi la bouche entrouverte ?",
  "c": [
   "Pour crier plus fort",
   "C'est une prière fallera",
   "Pour équilibrer la pression des explosions"
  ],
  "b": 2,
  "ex": "La mascletà approche : ~120 dB de rythme pyrotechnique. Bouche entrouverte = tympans protégés. Et bouchons d'oreilles dans la poche."
 },
 {
  "sit": "Addition : 42 €. Le service était impeccable. Ta voisine sort sa calculette à 15 %.",
  "q": "Le pourboire espagnol…",
  "c": [
   "15 % obligatoire, comme au Québec",
   "Optionnel : on arrondit, 5-10 % si excellent",
   "Interdit par la loi"
  ],
  "b": 1,
  "ex": "Le service est inclus. Arrondir suffit ; 5-10 % récompense un vrai bon moment. Personne ne courra après toi."
 },
 {
  "sit": "Tu renverses ton verre sur un inconnu. Confuse, tu lances : « ¡Estoy embarazada! »",
  "q": "Tu viens de dire…",
  "c": [
   "« Je suis enceinte »",
   "« Je suis embarrassée »",
   "« Je suis désolée »"
  ],
  "b": 0,
  "ex": "Le faux ami le plus célèbre de la langue. Pour la gêne : « ¡Qué vergüenza! » — et pour un rhume, evita « constipada »… qui veut dire enrhumée, justement."
 },
 {
  "sit": "Un chauffeur te propose un « tour photo » des communes touchées par la DANA de 2024.",
  "q": "Ta réponse ?",
  "c": [
   "Pourquoi pas, c'est historique",
   "Oui, si c'est gratuit",
   "Non — lieux de deuil, pas d'attraction"
  ],
  "b": 2,
  "ex": "Paiporta et ses voisines se reconstruisent dans le deuil. Le vrai geste utile : dépenser dans le centre, dont le tourisme finance la relance."
 },
 {
  "sit": "Fin du repas depuis 20 minutes. L'addition ne vient toujours pas. Personne ne s'agite.",
  "q": "Le restaurant…",
  "c": [
   "T'a oubliée",
   "Te laisse la sobremesa : demande-la quand TU veux",
   "Offre le repas"
  ],
  "b": 1,
  "ex": "Apporter l'addition sans qu'on la demande serait pousser dehors. « La cuenta, por favor » — avec le geste de signer dans l'air, ça marche aussi."
 },
 {
  "sit": "Ton vol atterrit. Tu ouvres Uber : aucun véhicule disponible, nulle part.",
  "q": "Que se passe-t-il ?",
  "c": [
   "Grève surprise",
   "Ton téléphone est cassé",
   "Uber n'opère pas à Valence : Cabify/Bolt/métro"
  ],
  "b": 2,
  "ex": "Pas d'Uber ici. Cabify est le réflexe local, le métro (lignes 3/5) fait le trajet en ~20 min, et le taxi est à tarif encadré."
 },
 {
  "sit": "Grosse chaleur. Tu commandes une horchata et réclames « beaucoup de glaçons, por favor ».",
  "q": "L'horchatero te regarde…",
  "c": [
   "Avec une douleur polie : les glaçons la noient",
   "Avec gratitude",
   "Sans réaction"
  ],
  "b": 0,
  "ex": "L'horchata se sert déjà glacée, souvent mi-granizada. Les glaçons diluent le lait de chufa — demande-la « bien fría », et trempe un farton."
 }
]
FRAGEN_JS = "const FRAGEN=" + json.dumps(FRAGEN_ES, ensure_ascii=False) + ";"

# ---------- L'ÉCRAN : LA PRUEBA ----------
# viewBox 300x340. Sol y=318. Noria à droite (meule tourne, frein cale rouge),
# filet = caldo safran qui coule du canal vers la paella. Paella en coupe à gauche,
# 3 zones clipPath ac1-3, rects socarrat amfora-N-vul scaleY(0) origin bottom.
PRUEBA = ('<section class="fiche" id="manteion" data-par="11" data-nofrappe>'
 '<div class="corps-sec quiz-corps"><div class="quiz-tete">'
 '<span class="parno">LA PRUEBA</span>'
 '<span id="quiz-prog" class="quiz-prog">PREGUNTA 1/12</span>'
 '<button type="button" class="mute" id="quiz-mute">SFX : S&Iacute;</button></div>'
 '<div class="presse-cadre">'
 '<svg class="presse" viewBox="0 0 300 340" role="img" aria-label="Noria correctrice et paella au socarrat">'
 '<line x1="10" y1="318" x2="290" y2="318" stroke="#2B1E16" stroke-width="4"/>'
 # branche d'oranger décorative en arc (id rameau conservé)
 '<g id="rameau">'
 '<path d="M96 44 q54 -26 108 0" fill="none" stroke="#5C7345" stroke-width="4"/>'
 '<g fill="#5C7345">'
 '<path d="M112 36 q8 -10 16 -6 q-4 10 -16 6z"/><path d="M136 28 q9 -9 17 -4 q-5 10 -17 4z"/>'
 '<path d="M164 26 q9 -7 16 -1 q-6 9 -16 1z"/><path d="M188 34 q10 -6 16 1 q-7 8 -16 -1z"/></g>'
 '<circle cx="128" cy="40" r="5" fill="#C75B12"/><circle cx="176" cy="36" r="5" fill="#C75B12"/></g>'
 # l'acequia (canal) surélevée qui alimente : support + bassin haut
 '<rect x="196" y="120" width="88" height="12" fill="#8A5A2B" stroke="#2B1E16" stroke-width="3"/>'
 '<rect x="206" y="132" width="10" height="118" fill="#8A5A2B" stroke="#2B1E16" stroke-width="3"/>'
 '<rect x="264" y="132" width="10" height="118" fill="#8A5A2B" stroke="#2B1E16" stroke-width="3"/>'
 # LA NORIA (id=meule) : roue à aubes, tourne de 90° par question
 '<g id="meule" style="transform-origin:240px 196px">'
 '<circle cx="240" cy="196" r="52" fill="#F2E3C6" stroke="#2B1E16" stroke-width="5"/>'
 '<circle cx="240" cy="196" r="52" fill="none" stroke="#8A6F5C" stroke-width="2" stroke-dasharray="4 7"/>'
 '<line x1="240" y1="150" x2="240" y2="242" stroke="#2B1E16" stroke-width="4"/>'
 '<line x1="194" y1="196" x2="286" y2="196" stroke="#2B1E16" stroke-width="4"/>'
 '<line x1="208" y1="164" x2="272" y2="228" stroke="#2B1E16" stroke-width="3"/>'
 '<line x1="272" y1="164" x2="208" y2="228" stroke="#2B1E16" stroke-width="3"/>'
 '<rect x="234" y="142" width="12" height="10" fill="#9C4722" stroke="#2B1E16" stroke-width="2.5"/>'
 '<rect x="234" y="244" width="12" height="10" fill="#9C4722" stroke="#2B1E16" stroke-width="2.5"/>'
 '<rect x="186" y="190" width="10" height="12" fill="#9C4722" stroke="#2B1E16" stroke-width="2.5"/>'
 '<rect x="284" y="190" width="10" height="12" fill="#9C4722" stroke="#2B1E16" stroke-width="2.5"/>'
 '<circle cx="240" cy="196" r="9" fill="#C75B12" stroke="#2B1E16" stroke-width="3"/></g>'
 # le frein (cale rouge, opacity 0, grince sur erreur)
 '<g id="frein"><path d="M286 156 L298 138 L306 152 L292 168 Z" transform="translate(-14,4)" '
 'fill="#A6301C" stroke="#2B1E16" stroke-width="3" opacity="0"/></g>'
 # la gouttière vers la paella + le filet de caldo (opacity 0, coule au storm)
 '<path d="M196 244 q-24 2 -32 16 l10 5 q8 -12 22 -11 z" fill="#9C4722" stroke="#2B1E16" stroke-width="3"/>'
 '<g id="filet"><rect x="160" y="264" width="5" height="30" fill="#D98E04" opacity="0"/></g>'
 # LA PAELLA en coupe : bord, deux anses, 3 zones de socarrat qui montent
 '<g id="amfora-1">'
 '<clipPath id="ac1"><rect x="34" y="292" width="40" height="22" rx="3"/></clipPath>'
 '<rect id="amfora-1-vul" x="34" y="292" width="40" height="22" fill="#D98E04" '
 'clip-path="url(#ac1)" style="transform-origin:54px 314px;transform:scaleY(0)"/></g>'
 '<g id="amfora-2">'
 '<clipPath id="ac2"><rect x="76" y="292" width="40" height="22" rx="3"/></clipPath>'
 '<rect id="amfora-2-vul" x="76" y="292" width="40" height="22" fill="#D98E04" '
 'clip-path="url(#ac2)" style="transform-origin:96px 314px;transform:scaleY(0)"/></g>'
 '<g id="amfora-3">'
 '<clipPath id="ac3"><rect x="118" y="292" width="40" height="22" rx="3"/></clipPath>'
 '<rect id="amfora-3-vul" x="118" y="292" width="40" height="22" fill="#D98E04" '
 'clip-path="url(#ac3)" style="transform-origin:138px 314px;transform:scaleY(0)"/></g>'
 '<path d="M28 290 h136 l-8 26 h-120 z" fill="none" stroke="#2B1E16" stroke-width="4"/>'
 '<path d="M28 292 q-10 0 -14 6 M164 292 q10 0 14 6" fill="none" stroke="#2B1E16" stroke-width="4"/>'
 '<text x="96" y="284" text-anchor="middle" font-family="IBM Plex Mono,monospace" '
 'font-size="9" fill="#2B1E16">EL SOCARRAT SUBE&hellip;</text>'
 # rotors compteurs : PREG. / CROSTA
 '<g id="manteion-rotors" font-family="IBM Plex Mono,monospace" font-size="15" font-weight="700">'
 '<rect x="238" y="256" width="42" height="26" fill="#F2E3C6" stroke="#2B1E16" stroke-width="3"/>'
 '<text id="rota-t" x="259" y="275" text-anchor="middle" fill="#2B1E16">01</text>'
 '<rect x="238" y="292" width="42" height="26" fill="#F2E3C6" stroke="#2B1E16" stroke-width="3"/>'
 '<text id="rotb-t" x="259" y="311" text-anchor="middle" fill="#9C4722">00</text>'
 '<text x="259" y="248" text-anchor="middle" font-size="9" fill="#2B1E16">PREG.</text>'
 '<text x="259" y="332" text-anchor="middle" font-size="9" fill="#2B1E16">CROSTA</text></g>'
 '</svg></div>'
 '<div class="quiz-zone" id="quiz-zone"></div>'
 '</div></section>')
