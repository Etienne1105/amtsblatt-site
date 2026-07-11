# -*- coding: utf-8 -*-
# Contenido ES — moitié A : couverture (stele), patio (agora), sections 1-4.
# Ids moteur conservés (stele, agora, btn-anavasi, chorde-N, lyra-keravnos).
from pictos_es import PICTOS

def T(fid, par, no, tot, titre, teil, corps, extra_cls=""):
    return ('<section class="fiche par-pair' + extra_cls + '" id="' + fid + '" data-par="' + str(par) + '">'
            '<header class="fiche-tete"><div><span class="parno">&sect; ' + str(par) + '</span>'
            '<h2>' + titre + '</h2><span class="teil">Retablo ' + str(no) + ' &middot; ' + str(tot)
            + (' &mdash; ' + teil if teil else '') + '</span></div>'
            + PICTOS[par] + '</header><div class="corps-sec">' + corps + '</div></section>')

# ---------- LA COUVERTURE ----------
STELE = ('<section class="fiche" id="stele"><div class="stele-cadre">'
 '<span class="stempel-header">SELLO</span>'
 '<p class="kicker">VAL&Egrave;NCIA &middot; GU&Iacute;A DE CAMPO &middot; ANNO 2026</p>'
 '<h1>El Llibret</h1>'
 '<p class="translit-h1">El Llibret &mdash; le livret des Fallas&nbsp;: satirique, br&ucirc;lable, indispensable</p>'
 '<p class="soustitre">Pour <strong>St&eacute;phanie</strong>, qui part vers Valence&nbsp;: un guide cuit '
 'au feu doux du socarrat, carrel&eacute; comme un retablo de Manises, &agrave; l&rsquo;orange de la huerta '
 '&mdash; scell&eacute; au safran.</p>'
 '<p class="edition">Guide de terrain &middot; Valence &amp; ses environs &middot; table, feu &amp; langue</p>'
 '<button type="button" id="btn-anavasi" class="aanmonsteren">LA ENTRADA &mdash; pousser la porte du patio</button>'
 '<p class="mention-bas">Neuf &sect; de c&eacute;ramique &middot; un Glosario parlant &middot; une Prueba &agrave; la noria</p>'
 '</div></section>')

# ---------- LE PATIO (agora) : intro + 13 tuiles + guitare ----------
def _tuile(href, no, picto, es, fr):
    return ('<a class="tuile" href="' + href + '"><span class="tno">' + no + '</span>'
            + picto + '<span class="tnom"><span lang="es">' + es + '</span><i>' + fr + '</i></span></a>')

_P = {}  # pictos propres aux tuiles, viewBox 96, langage socarrat
def _pv(label, corps): return ('<svg class="picto" viewBox="0 0 96 96" role="img" aria-label="' + label + '">' + corps + '</svg>')

_T = []
_T.append(_tuile('#p1-1','&sect; 1', PICTOS[1], 'El alma', 'L&rsquo;&acirc;me valencienne'))
_T.append(_tuile('#p2-1','&sect; 2', PICTOS[2], 'Las Fallas', 'Le feu sacr&eacute; de mars'))
_T.append(_tuile('#p3-1','&sect; 3', PICTOS[3], 'Los c&oacute;digos', 'Les codes &amp; le tact'))
_T.append(_tuile('#p4-1','&sect; 4', PICTOS[4], 'La mesa', 'La paella &amp; la table'))
_T.append(_tuile('#p5-1','&sect; 5', PICTOS[5], 'Para beber', 'Horchata &amp; agua de Valencia'))
_T.append(_tuile('#p6-1','&sect; 6', PICTOS[6], 'La ciudad', 'Valence, pierre &amp; futur'))
_T.append(_tuile('#p7-1','&sect; 7', PICTOS[7], 'La Albufera', 'La lagune &amp; la huerta'))
_T.append(_tuile('#p8-1','&sect; 8', PICTOS[8], 'Las escapadas', 'Ch&acirc;teaux &amp; thermes'))
_T.append(_tuile('#p9-1','&sect; 9', PICTOS[9], 'En camino', 'Bouger, payer, d&eacute;jouer'))

_T.append(('<a class="tuile tuile-examen" href="#examen"><span class="tno">EXAMEN</span>'
 + _pv("Couronne d&rsquo;azahar de l&rsquo;examen",
 '<path class="trait" d="M18 66 Q48 46 78 66" fill="none" stroke-width="3" style="stroke:#5C7345"/>'
 '<g class="gr-cligne"><circle fill="#F2E3C6" cx="34" cy="57" r="5"/><circle class="jaune" cx="34" cy="57" r="2"/></g>'
 '<circle fill="#F2E3C6" cx="48" cy="53" r="5"/><circle class="jaune" cx="48" cy="53" r="2"/>'
 '<circle fill="#F2E3C6" cx="62" cy="57" r="5"/><circle class="jaune" cx="62" cy="57" r="2"/>'
 '<line class="trait" x1="20" y1="84" x2="76" y2="84"/>')
 + '<span class="tnom"><span lang="es">El examen</span><i>14 questions &mdash; gagne ta couronne</i></span></a>'))

_T.append(('<a class="tuile tuile-oracle" href="#manteion"><span class="tno">PRUEBA</span>'
 + _pv("Noria de la Prueba",
 '<g class="gr-tourne" style="transform-origin:48px 46px"><circle class="trait" cx="48" cy="46" r="22" fill="none" stroke-width="4"/>'
 '<line class="trait" x1="48" y1="24" x2="48" y2="68"/><line class="trait" x1="26" y1="46" x2="70" y2="46"/>'
 '<rect class="jaune" x="44" y="20" width="8" height="8"/></g>'
 '<circle class="oranj" cx="48" cy="46" r="5"/>'
 '<path class="trait" d="M16 82 q10 5 20 0 q10 -5 20 0 q10 5 24 0" fill="none"/>')
 + '<span class="tnom"><span lang="es">La Prueba</span><i>12 situations &mdash; dore ton socarrat</i></span></a>'))

_T.append(('<a class="tuile tuile-taal" href="#p10-1"><span class="tno">&sect; 10</span>'
 + PICTOS[10]
 + '<span class="tnom"><span lang="es">El Glosario</span><i>L&rsquo;espagnol qui parle</i></span></a>'))

_T.append(('<a class="tuile tuile-chroniko" href="#x-1"><span class="tno">CR&Oacute;NICA</span>'
 + _pv("Noria du temps en marche", PICTOS[12].split('">',1)[1].rsplit('</svg>',1)[0])
 + '<span class="tnom">Histoire &mdash; de Valentia &agrave; aujourd&rsquo;hui, 2&nbsp;164 ans</span></a>'))

AGORA = ('<section class="fiche" id="agora"><div class="corps-sec agora-corps">'
 '<p class="agora-intro">&iexcl;Hola, <strong>St&eacute;phanie</strong>&nbsp;! Bienvenue dans le patio '
 'aux orangers. Neuf &sect; de c&eacute;ramique pour traverser Valence sans faux pas, un Glosario '
 '&agrave; voix haute, et une Prueba qui te met &agrave; l&rsquo;&eacute;preuve. Touche un carreau&nbsp;:</p>'
 '<div class="tuiles">' + "".join(_T) + '</div>'
 '<div class="agora-lyra">'
 '<p class="lyra-hint">Une guitare dort contre l&rsquo;oranger&hellip; '
 '<span class="lyra-murmure">pince ses quatre cordes, de la plus grave &agrave; la plus aigu&euml;.</span></p>'
 '<div class="lyra"><svg class="lyra" viewBox="0 0 120 110" role="img" '
 'aria-label="Guitare espagnole &agrave; quatre cordes &mdash; pince-les dans l&rsquo;ordre">'
 # l'oranger derrière
 '<path d="M14 96 v-34 q-10 -4 -8 -16 q2 -12 16 -12 q4 -10 16 -8 q10 2 10 14 q10 4 6 16 q-3 9 -14 8 v32 z" '
 'fill="#5C7345" stroke="#2B1E16" stroke-width="3"/>'
 '<circle cx="22" cy="46" r="5" fill="#C75B12" stroke="#2B1E16" stroke-width="2"/>'
 '<circle cx="40" cy="38" r="5" fill="#C75B12" stroke="#2B1E16" stroke-width="2"/>'
 '<circle cx="33" cy="56" r="5" fill="#C75B12" stroke="#2B1E16" stroke-width="2"/>'
 # flamme cachée de la cremà (révélée par .keravnos)
 '<g id="lyra-keravnos" opacity="0">'
 '<path d="M72 8 q10 14 2 26 q12 -2 10 12 q-2 12 -14 10 q4 10 -6 14 q-10 -4 -8 -14 q-12 4 -14 -8 q-2 -12 10 -14 q-8 -12 4 -22 q6 6 16 -4 z" '
 'fill="#C75B12" stroke="#7E2D1E" stroke-width="2"/>'
 '<path d="M70 34 q6 10 0 18 q-8 -2 -6 -12 q2 -6 6 -6 z" fill="#D98E04"/>'
 '</g>'
 # la guitare : caisse, rosace, manche, tête, chevalet
 '<path d="M62 96 q-16 0 -18 -16 q-2 -12 8 -16 q-8 -6 -4 -16 q4 -10 16 -10 q12 0 16 10 q4 10 -4 16 q10 4 8 16 q-2 16 -22 16 z" '
 'fill="#9C4722" stroke="#2B1E16" stroke-width="3"/>'
 '<circle cx="62" cy="66" r="7" fill="#2B1E16"/>'
 '<circle cx="62" cy="66" r="7" fill="none" stroke="#D98E04" stroke-width="1.6"/>'
 '<rect x="58" y="10" width="8" height="30" fill="#7E2D1E" stroke="#2B1E16" stroke-width="2.4"/>'
 '<rect x="54" y="2" width="16" height="10" fill="#2B1E16"/>'
 '<circle cx="52" cy="5" r="2.2" fill="#D98E04"/><circle cx="52" cy="10" r="2.2" fill="#D98E04"/>'
 '<circle cx="72" cy="5" r="2.2" fill="#D98E04"/><circle cx="72" cy="10" r="2.2" fill="#D98E04"/>'
 '<rect x="52" y="84" width="20" height="4" fill="#2B1E16"/>'
 # les 4 cordes (ids moteur conservés)
 '<g stroke="#F2E3C6" stroke-width="2.5">'
 '<line id="chorde-1" class="chorde" x1="56" y1="12" x2="55" y2="86"/>'
 '<line id="chorde-2" class="chorde" x1="60" y1="12" x2="60" y2="86"/>'
 '<line id="chorde-3" class="chorde" x1="64" y1="12" x2="65" y2="86"/>'
 '<line id="chorde-4" class="chorde" x1="68" y1="12" x2="70" y2="86"/>'
 '</g>'
 '<line x1="10" y1="98" x2="112" y2="98" stroke="#2B1E16" stroke-width="3"/>'
 '</svg></div></div>'
 '<p class="agora-pied"><a href="#pinakas">&Iacute;ndice &mdash; table des mati&egrave;res compl&egrave;te &rarr;</a></p>'
 '<a class="retour-classeur" href="/">&larr; EL ARCHIVADOR &mdash; retour au classeur</a>'
 '</div></section>')

# ---------- LES SECTIONS 1-4 ----------
FICHES_A = []

FICHES_A.append(T("p1-1", 1, 1, 2, "El alma &mdash; la rue comme salon", "la fiesta",
 '<p><span class="lettrine le">V</span>alence vit dehors, tard, et fort. Le vrai culte local, '
 'c&rsquo;est la <strong>fiesta</strong>&nbsp;: p&eacute;tards en toute saison, d&icirc;ners de rue improvis&eacute;s '
 '(la <em lang="es">cena de sobaquillo</em>), terrasses pleines &agrave; minuit. L&rsquo;embl&egrave;me de la ville '
 'est une chauve-souris, <em>Lo Rat Penat</em>, pos&eacute;e sur les armoiries depuis Jaume&nbsp;I.</p>'
 '<p>Deux institutions du quotidien&nbsp;: l&rsquo;<strong lang="es">esmorzaret</strong> de 10h30 '
 '&mdash; gros sandwich, olives, bi&egrave;re ou <em>cremaet</em>, un rite sacr&eacute; &mdash; et la '
 '<strong lang="es">sobremesa</strong>&nbsp;: on reste &agrave; table longtemps apr&egrave;s le dessert, '
 '&agrave; parler. Personne ne t&rsquo;apportera l&rsquo;addition sans qu&rsquo;on la demande&nbsp;: '
 'ce n&rsquo;est pas de la n&eacute;gligence, c&rsquo;est de la politesse.</p>'
 '<div class="merksatz"><p>Le mot le plus dit d&rsquo;Espagne&nbsp;: <em lang="es">vale</em> '
 '(&laquo;&nbsp;d&rsquo;accord&nbsp;&raquo;). Tu l&rsquo;auras adopt&eacute; avant le deuxi&egrave;me jour.</p></div>'))

FICHES_A.append(T("p1-2", 1, 2, 2, "El alma &mdash; l&rsquo;horloge espagnole", "les heures",
 '<p><span class="lettrine le">L</span>&rsquo;horloge locale d&eacute;cale tout de deux heures&nbsp;: '
 'd&eacute;jeuner vers <strong>14h</strong> (le vrai repas du jour), d&icirc;ner &agrave; '
 '<strong>21h&ndash;22h</strong>. Arriver dans un restaurant &agrave; 19h, c&rsquo;est d&icirc;ner seule '
 'avec le personnel. La sieste g&eacute;n&eacute;ralis&eacute;e est un mythe en ville &mdash; mais les '
 'petits commerces ferment souvent en milieu de journ&eacute;e.</p>'
 '<p>On se salue de <strong>deux bises</strong> entre femmes et entre homme et femme&nbsp;; '
 'poign&eacute;e de main entre hommes en contexte formel. Les Valenciens sont chaleureux, directs, '
 'bruyants avec tendresse&nbsp;: parler fort n&rsquo;est pas se f&acirc;cher.</p>'
 '<div class="achtung"><p>Le <em lang="es">men&uacute; del d&iacute;a</em> (midi, ~12&ndash;15&nbsp;&euro;, '
 'trois services + boisson) est le meilleur rapport qualit&eacute;-prix du pays. Le soir, le m&ecirc;me '
 'restaurant co&ucirc;te le double.</p></div>'))

FICHES_A.append(T("p2-1", 2, 1, 2, "Las Fallas &mdash; l&rsquo;art qui na&icirc;t pour br&ucirc;ler", "15&ndash;19 mars",
 '<p><span class="lettrine le">C</span>haque mois de mars, Valence dresse pr&egrave;s de 750 monuments '
 'de carton-p&acirc;te et de polystyr&egrave;ne &mdash; les <strong lang="es">fallas</strong>, jusqu&rsquo;&agrave; '
 'cinq &eacute;tages, peupl&eacute;s de <em lang="es">ninots</em> satiriques qui caricaturent politiciens '
 'et c&eacute;l&eacute;brit&eacute;s. Patrimoine immat&eacute;riel de l&rsquo;<strong>UNESCO</strong> depuis 2016, '
 'port&eacute; par ~200&nbsp;000 membres de commissions de quartier.</p>'
 '<p>Les jours saints&nbsp;: la <em>plant&agrave;</em> (installation, 15 mars), '
 'l&rsquo;<em>Ofrena de Flors</em> (17&ndash;18 mars) o&ugrave; la Vierge des D&eacute;sempar&eacute;s '
 're&ccedil;oit une cape de fleurs haute comme un immeuble, la <em>Nit del Foc</em> (grand feu '
 'd&rsquo;artifice, 18 mars) &mdash; puis le feu.</p>'
 '<div class="merksatz"><p>La nuit du <strong>19 mars</strong>, tout br&ucirc;le&nbsp;: c&rsquo;est la '
 '<em lang="es">Crem&agrave;</em>. Un seul <em>ninot</em> est graci&eacute; chaque ann&eacute;e par le vote '
 'populaire &mdash; l&rsquo;<em>indultat</em> &mdash; et rejoint le Museo Fallero.</p></div>'))

FICHES_A.append(T("p2-2", 2, 2, 2, "Las Fallas &mdash; la mascletà, bouche entrouverte", "survivre au bruit",
 '<p><span class="lettrine le">D</span>u 1<sup>er</sup> au 19 mars, chaque jour &agrave; '
 '<strong>14h</strong> pile, la Plaza del Ayuntamiento explose&nbsp;: la '
 '<strong lang="es">masclet&agrave;</strong>, concert pyrotechnique <em>diurne</em> o&ugrave; '
 'ce qui compte n&rsquo;est pas la lumi&egrave;re mais le <strong>rythme</strong> &mdash; un crescendo '
 'sismique jusqu&rsquo;au <em>terremoto</em> final, autour de 120 d&eacute;cibels.</p>'
 '<p>Les locaux la vivent bouche entrouverte pour &eacute;quilibrer la pression, et jugent '
 'l&rsquo;artificier comme on juge un chef d&rsquo;orchestre. Si tu y es en mars&nbsp;: '
 'bouchons d&rsquo;oreilles dans la poche, h&ocirc;tel r&eacute;serv&eacute; des mois d&rsquo;avance, '
 'et gare aux pickpockets dans la foule.</p>'
 '<div class="achtung"><p>Hors saison, va voir la <strong>Ciutat Fallera</strong> (les ateliers des '
 'artistes falleros) ou le Museo Fallero (~2&nbsp;&euro;)&nbsp;: les ninots graci&eacute;s depuis 1934 '
 'y racontent un si&egrave;cle de satire.</p></div>'))

FICHES_A.append(T("p3-1", 3, 1, 2, "Los c&oacute;digos &mdash; deux langues, une politesse", "valenci&agrave; &amp; castellano",
 '<p><span class="lettrine le">D</span>eux langues co-officielles vivent ici&nbsp;: le '
 '<strong>castillan</strong>, dominant &agrave; l&rsquo;oral en ville, et le '
 '<strong>valencien</strong> (<em lang="es">valenci&agrave;</em>, variante du catalan), tr&egrave;s '
 'pr&eacute;sent &agrave; l&rsquo;&eacute;crit, dans les familles et les villages. Ne dis '
 '<em>jamais</em> que le valencien est un &laquo;&nbsp;dialecte&nbsp;&raquo; &mdash; c&rsquo;est le '
 'seul vrai faux pas linguistique possible.</p>'
 '<p>Cons&eacute;quence pratique&nbsp;: presque tout a <strong>deux noms</strong>. '
 '<em>X&agrave;tiva</em> = <em>J&aacute;tiva</em>, <em>Russafa</em> = <em>Ruzafa</em>, '
 '<em>Pla&ccedil;a de l&rsquo;Ajuntament</em> = <em>Plaza del Ayuntamiento</em>. Les panneaux, '
 'stations et cartes m&eacute;langent les deux&nbsp;: ce n&rsquo;est pas une erreur, c&rsquo;est la ville.</p>'
 '<div class="merksatz"><p>Ouvrir avec <em lang="es">Bon dia</em> puis continuer en castillan '
 '(ou en anglais) d&eacute;clenche des sourires&nbsp;: tu as montr&eacute; que tu sais o&ugrave; tu es.</p></div>'))

FICHES_A.append(T("p3-2", 3, 2, 2, "Los c&oacute;digos &mdash; le pourboire &amp; le tact", "la DANA",
 '<p><span class="lettrine le">L</span>e service est inclus&nbsp;: le pourboire est '
 '<strong>optionnel et modeste</strong> &mdash; arrondir au bar ou au taxi, 5&ndash;10&nbsp;% au '
 'restaurant si le service fut vraiment bon. Personne ne court apr&egrave;s toi pour un pourboire '
 'oubli&eacute;. Pour les &eacute;glises (cath&eacute;drale, San Nicol&aacute;s)&nbsp;: &eacute;paules '
 'et genoux couverts&nbsp;; hors plage, on ne circule pas en maillot.</p>'
 '<p>Un sujet demande du tact&nbsp;: la <strong>DANA d&rsquo;octobre 2024</strong>, ces pluies '
 'torrentielles qui ont fait 229 morts dans la province. Le centre touristique a &eacute;t&eacute; '
 '&eacute;pargn&eacute; &mdash; mais les communes du sud (Paiporta, Catarroja&hellip;) se reconstruisent '
 'encore, dans le deuil et la col&egrave;re politique. On en reparle dans la Cr&oacute;nica.</p>'
 '<div class="achtung"><p>Ces communes ne sont <strong>pas des attractions</strong>&nbsp;: pas de '
 '&laquo;&nbsp;tourisme de catastrophe&nbsp;&raquo;, pas de photos des d&eacute;g&acirc;ts. Si le sujet '
 'vient, &eacute;coute &mdash; ta visite du centre, elle, aide concr&egrave;tement la relance.</p></div>'))

FICHES_A.append(T("p4-1", 4, 1, 2, "La mesa &mdash; la paella, dix ingr&eacute;dients, z&eacute;ro chorizo", "le canon",
 '<p><span class="lettrine le">L</span>a <strong>paella valenciana</strong> est n&eacute;e dans les '
 'rizi&egrave;res de l&rsquo;Albufera, plat d&rsquo;ouvriers agricoles devenu totem. Le canon a m&ecirc;me '
 '&eacute;t&eacute; publi&eacute; dans une revue scientifique (&eacute;tude de l&rsquo;anthropologue '
 'Pablo Vidal, UCV)&nbsp;: riz, poulet, <strong>lapin</strong>, haricot plat vert, '
 '<em lang="es">garrof&oacute;</em>, tomate, paprika, <strong>safran</strong>, huile d&rsquo;olive, eau. '
 'C&rsquo;est tout. <strong>Jamais</strong> de fruits de mer, jamais de chorizo &mdash; sacril&egrave;ge document&eacute;.</p>'
 '<p>Les r&egrave;gles&nbsp;: elle se mange le <strong>midi</strong> (jamais le soir), se '
 '<strong>partage</strong> (minimum deux), cuit <strong>40&ndash;45 minutes</strong> &agrave; la commande '
 '&mdash; d&rsquo;o&ugrave; r&eacute;servation et pr&eacute;-commande. Le tr&eacute;sor est au fond&nbsp;: le '
 '<strong lang="es">socarrat</strong>, cro&ucirc;te de riz caram&eacute;lis&eacute; qu&rsquo;on gratte '
 '&agrave; la cuill&egrave;re, directement dans la po&ecirc;le.</p>'
 '<div class="merksatz"><p>Riz jaune fluo, photos criardes en vitrine, paella servie en 15 minutes ou '
 '&laquo;&nbsp;individuelle&nbsp;&raquo;&nbsp;: quatre drapeaux rouges du pi&egrave;ge &agrave; touristes.</p></div>'))

FICHES_A.append(T("p4-2", 4, 2, 2, "La mesa &mdash; o&ugrave; la manger, vraiment", "les adresses",
 '<p><span class="lettrine le">D</span>eux p&egrave;lerinages s&ucirc;rs. En bord de mer&nbsp;: '
 '<strong>Casa Carmela</strong> (Malvarrosa, depuis 1922), cuisson au feu de bois '
 'd&rsquo;oranger &mdash; r&eacute;server des semaines d&rsquo;avance et pr&eacute;-commander la paella '
 '<em>a le&ntilde;a</em>. Au village d&rsquo;<strong>El Palmar</strong>, dans l&rsquo;Albufera&nbsp;: '
 '<strong>Bon Aire</strong> (titre de &laquo;&nbsp;meilleure paella valenciana du monde&nbsp;&raquo;, '
 'concours de Sueca 2018) ou <strong>Casa Salvador</strong> (1947), au bord de la lagune.</p>'
 '<p>La c&eacute;l&egrave;bre <em>La Pepica</em> (1898, Hemingway en terrasse)&nbsp;? Institution '
 'historique pour les guides, &laquo;&nbsp;pi&egrave;ge&nbsp;&raquo; pour beaucoup de locaux&nbsp;: '
 'vas-y pour l&rsquo;ambiance face &agrave; la mer, pas pour le riz. Explore aussi les cousins&nbsp;: '
 '<em>arr&ograve;s a banda</em>, <em>del senyoret</em> (fruits de mer d&eacute;cortiqu&eacute;s), '
 '<em>negre</em> (encre de seiche), <em>al forn</em> (au four, l&rsquo;hiver) et la '
 '<strong>fideu&agrave;</strong> de Gandia, aux vermicelles.</p>'
 '<div class="achtung"><p>Devant un Valencien, on ne met <strong>rien</strong> sur une paella&nbsp;: '
 'ni ketchup, ni Tabasco, ni citron non demand&eacute;. On complimente le socarrat, et on est adopt&eacute;e.</p></div>'))
