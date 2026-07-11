# -*- coding: utf-8 -*-
# Crónica ES — 8 fiches x-1..x-8, data-par=12. Pictos inline dédiés par époque.

def X(n, roman, teil, titre, picto, corps):
    return ('<section class="fiche par-chroniko" id="x-' + str(n) + '" data-par="12">'
            '<header class="fiche-tete"><div><span class="parno">CR&Oacute;NICA &middot; ' + roman + '</span>'
            '<h2>' + titre + '</h2><span class="teil">' + teil + '</span></div>'
            '<svg class="picto" viewBox="0 0 96 96" role="img" aria-label="' + titre.replace('"','') + '">'
            + picto + '</svg></header><div class="corps-sec">' + corps + '</div></section>')

FICHES_X = []

FICHES_X.append(X(1, "I", "VALENTIA &middot; &minus;138", "Une prime de retraite romaine",
 '<path class="plein" d="M20 78 v-30 h8 v30 z M44 78 v-30 h8 v30 z M68 78 v-30 h8 v30 z"/>'
 '<path class="jaune" d="M14 44 h68 v-8 h-68 z"/>'
 '<path class="trait" d="M12 36 l36 -18 l36 18" fill="none"/>'
 '<g class="gr-cligne"><circle class="oranj" cx="48" cy="26" r="4"/></g>'
 '<line class="trait" x1="12" y1="82" x2="84" y2="82"/>',
 '<p><span class="lettrine le">V</span>alence est n&eacute;e fonctionnaire&nbsp;: en '
 '<strong>138 av. J.-C.</strong>, le consul Junius Brutus installe ~2&nbsp;000 v&eacute;t&eacute;rans '
 'des guerres lusitaniennes sur une &icirc;le du Turia. <em>Valentia</em> &mdash; &laquo;&nbsp;la '
 'vaillance&nbsp;&raquo; &mdash; comme solde de d&eacute;part. C&rsquo;est l&rsquo;une des plus vieilles '
 'villes d&rsquo;Espagne.</p>'
 '<p>Fid&egrave;le au mauvais camp dans la guerre civile, elle est ras&eacute;e par '
 '<strong>Pomp&eacute;e</strong> en &minus;75, renaît, prosp&egrave;re &mdash; forum, cirque, voies. '
 'Ses fondations dorment sous la place de la Vierge&nbsp;: le mus&eacute;e de '
 'l&rsquo;<strong>Almoina</strong> les montre, sous une dalle de verre.</p>'
 '<div class="merksatz"><p>Le nom n&rsquo;a jamais chang&eacute;&nbsp;: Valentia &rarr; Balansiya '
 '&rarr; Val&egrave;ncia. 2&nbsp;164 ans de continuit&eacute; &mdash; et toujours entre deux bras '
 'd&rsquo;un m&ecirc;me fleuve.</p></div>'))

FICHES_X.append(X(2, "II", "BALANSIYA &middot; 714&ndash;1238", "L&rsquo;eau des Maures, mille ans d&rsquo;avance",
 '<g class="gr-tourne" style="transform-origin:48px 44px">'
 '<circle class="trait" cx="48" cy="44" r="24" fill="none" stroke-width="4"/>'
 '<line class="trait" x1="48" y1="20" x2="48" y2="68"/><line class="trait" x1="24" y1="44" x2="72" y2="44"/>'
 '<line class="trait" x1="31" y1="27" x2="65" y2="61"/><line class="trait" x1="65" y1="27" x2="31" y2="61"/>'
 '<rect class="jaune" x="44" y="16" width="8" height="8"/></g>'
 '<circle class="oranj" cx="48" cy="44" r="5"/>'
 '<path class="trait" d="M12 82 q10 5 20 0 q10 -5 20 0 q10 5 24 0" fill="none"/>',
 '<p><span class="lettrine le">E</span>n <strong>714</strong>, la ville se rend sans combat aux '
 'Berb&egrave;res et Arabes&nbsp;: <em>Balansiya</em> devient un jardin. Les Maures tracent le '
 'r&eacute;seau d&rsquo;irrigation de la huerta &mdash; canaux, norias, tours de partage &mdash; '
 '<strong>encore en service aujourd&rsquo;hui</strong>, et fondent le '
 '<strong>Tribunal de las Aguas</strong> qui si&egrave;ge toujours le jeudi.</p>'
 '<p>Interm&egrave;de de l&eacute;gende&nbsp;: <strong>El Cid</strong> prend la ville en 1094 et y '
 'r&egrave;gne en prince mercenaire&nbsp;; &agrave; sa mort, sa veuve Chim&egrave;ne tient le si&egrave;ge '
 'trois ans. Puis Almoravides et Almohades reprennent la main, jusqu&rsquo;au si&egrave;cle suivant.</p>'
 '<div class="achtung"><p>Quand tu bois ton horchata&nbsp;: la <em>chufa</em> est arriv&eacute;e avec '
 'eux. Ton verre a mille ans d&rsquo;histoire agricole dedans.</p></div>'))

FICHES_X.append(X(3, "III", "JAUME I &middot; 1238", "Le roi, la chauve-souris, le royaume",
 '<path class="plein" d="M28 40 h40 l-6 34 h-28 z"/>'
 '<path class="jaune" d="M24 40 v-10 h6 v6 h8 v-8 h6 v8 h8 v-8 h6 v8 h8 v-6 h6 v10 z"/>'
 '<g class="gr-cligne">'
 '<path class="trait" d="M32 22 q8 -12 16 -4 q8 -8 16 4 q-8 -2 -10 4 q-6 -6 -6 -6 q0 0 -6 6 q-2 -6 -10 -4 z" '
 'fill="#2B1E16"/></g>'
 '<line class="trait" x1="20" y1="82" x2="76" y2="82"/>',
 '<p><span class="lettrine le">L</span>e <strong>9 octobre 1238</strong>, Jaume&nbsp;I '
 'd&rsquo;Aragon entre dans Balansiya et fonde le <strong>Royaume de Valence</strong>, avec ses '
 'propres lois &mdash; les <em>furs</em> &mdash; et sa langue, le valencien. Le 9 octobre est '
 'rest&eacute; LA f&ecirc;te r&eacute;gionale&nbsp;: on y offre des massepains en forme de&hellip; '
 'fruits et l&eacute;gumes de la huerta.</p>'
 '<p>La l&eacute;gende de l&rsquo;embl&egrave;me date du si&egrave;ge&nbsp;: une '
 '<strong>chauve-souris</strong> se serait pos&eacute;e sur le heaume du roi &mdash; bon augure. '
 '<em>Lo Rat Penat</em> couronne depuis les armoiries de la ville, les maillots du Valencia CF, '
 'et les plaques d&rsquo;&eacute;gout que tu photographieras sans t&rsquo;en rendre compte.</p>'
 '<div class="merksatz"><p>Cherche-la partout&nbsp;: lampadaires, fontaines, blasons. '
 'C&rsquo;est le Pok&eacute;mon officiel du voyage.</p></div>'))

FICHES_X.append(X(4, "IV", "SIGLO DE ORO &middot; XV&#7497;", "La soie, la banque &amp; deux papes",
 '<path class="plein" d="M22 78 v-36 q0 -8 8 -8 h36 q8 0 8 8 v36 z"/>'
 '<path class="trait" d="M32 78 v-30 q8 -10 16 0 v30 M48 78 v-30 q8 -10 16 0 v30" fill="none"/>'
 '<path class="jaune" d="M40 22 q8 -14 16 0 q-8 6 -16 0 z"/>'
 '<g class="gr-onde"><path class="trait" d="M76 30 q6 6 0 14" fill="none"/></g>'
 '<line class="trait" x1="16" y1="82" x2="80" y2="82"/>',
 '<p><span class="lettrine le">A</span>u XV&#7497; si&egrave;cle, Valence est la ville la plus '
 'peupl&eacute;e de la Couronne d&rsquo;Aragon, riche du commerce de la <strong>soie</strong>. '
 'Elle invente une banque municipale (la <em>Taula de canvi</em>) &mdash; dont les banquiers '
 'pr&ecirc;teront &agrave; Isabelle la Catholique pour financer&hellip; le voyage de '
 '<strong>Colomb</strong>, 1492.</p>'
 '<p>Le monument de l&rsquo;&eacute;poque est ta visite &agrave; 2&nbsp;&euro;&nbsp;: la '
 '<strong>Lonja de la Seda</strong> (1482&ndash;1533), for&ecirc;t de colonnes torsad&eacute;es '
 'class&eacute;e UNESCO. Et la ville donne deux papes &agrave; Rome, les <strong>Borgia</strong> '
 'de X&agrave;tiva &mdash; Calixte&nbsp;III et Alexandre&nbsp;VI, le p&egrave;re de Lucr&egrave;ce.</p>'
 '<div class="achtung"><p>Dans la salle des colonnes de la Lonja, l&egrave;ve les yeux&nbsp;: les '
 'gargouilles ext&eacute;rieures sont d&rsquo;une paillardise assum&eacute;e. Le gothique avait '
 'de l&rsquo;humour.</p></div>'))

FICHES_X.append(X(5, "V", "LA CA&Iacute;DA &middot; 1609&ndash;1707", "L&rsquo;expulsion &amp; les fueros perdus",
 '<path class="plein" d="M48 16 q22 8 22 34 q0 20 -22 28 q-22 -8 -22 -28 q0 -26 22 -34 z"/>'
 '<path class="trait" d="M48 16 v62 M30 40 h36" fill="none"/>'
 '<path class="oranj" d="M62 60 l14 14 l-5 5 l-14 -14 z"/>'
 '<line class="trait" x1="20" y1="84" x2="76" y2="84"/>',
 '<p><span class="lettrine le">L</span>e d&eacute;clin vient par d&eacute;crets. En '
 '<strong>1609</strong>, l&rsquo;expulsion des <strong>morisques</strong> &mdash; les descendants '
 'des musulmans convertis &mdash; vide un tiers du royaume et saigne la huerta de ses meilleurs '
 'bras. La piraterie barbaresque ronge la c&ocirc;te, le commerce bascule vers '
 'l&rsquo;Atlantique&nbsp;: la M&eacute;diterran&eacute;e n&rsquo;est plus le centre du monde.</p>'
 '<p>Le coup de gr&acirc;ce est politique&nbsp;: apr&egrave;s la guerre de Succession, le d&eacute;cret '
 'de <strong>1707</strong> abolit les <em>furs</em> &mdash; les lois propres du royaume. '
 'Trois si&egrave;cles plus tard, la m&eacute;moire de cette perte nourrit encore '
 'l&rsquo;attachement f&eacute;roce des Valenciens &agrave; leur langue et &agrave; leurs '
 'institutions &mdash; Tribunal des Eaux en t&ecirc;te.</p>'
 '<div class="merksatz"><p>Retiens la m&eacute;canique&nbsp;: ce que Valence a perdu par d&eacute;cret, '
 'elle l&rsquo;a reconstruit par la f&ecirc;te, la table et la langue. Les Fallas sont aussi '
 '&ccedil;a&nbsp;: une revanche annuelle.</p></div>'))

FICHES_X.append(X(6, "VI", "LA RIADA &middot; 1957", "Le fleuve puni, le parc gagn&eacute;",
 '<path class="trait" d="M12 34 q12 -10 24 0 q12 10 24 0 q12 -10 24 0" fill="none" stroke-width="4"/>'
 '<path class="trait" d="M12 46 q12 -10 24 0 q12 10 24 0 q12 -10 24 0" fill="none" stroke-width="4" style="stroke:#9C4722"/>'
 '<path class="plein" d="M20 82 v-18 q28 -14 56 0 v18 z" style="fill:#5C7345"/>'
 '<g class="gr-pousse"><circle class="oranj" cx="38" cy="60" r="4"/><circle class="jaune" cx="58" cy="58" r="4"/></g>'
 '<line class="trait" x1="14" y1="84" x2="82" y2="84"/>',
 '<p><span class="lettrine le">E</span>n octobre <strong>1957</strong>, le Turia noie sa ville&nbsp;: '
 'des dizaines de morts, le centre sous les eaux. La r&eacute;ponse est radicale &mdash; la '
 '&laquo;&nbsp;Solution Sud&nbsp;&raquo;&nbsp;: on <strong>d&eacute;place le fleuve</strong> entier '
 'dans un canal de 12&nbsp;km contournant la ville par le sud.</p>'
 '<p>Restait un lit vide de 9&nbsp;km en plein centre. Les ing&eacute;nieurs y voyaient une '
 'autoroute&nbsp;; les Valenciens ont exig&eacute; &mdash; et obtenu &mdash; un <strong>parc</strong>. '
 'Les <strong>Jardins du Turia</strong> sont n&eacute;s de cette bataille citoyenne&nbsp;: '
 'aujourd&rsquo;hui tu y p&eacute;dales entre les ponts anciens qui enjambent&hellip; des orangers.</p>'
 '<div class="achtung"><p>Garde cette date en t&ecirc;te&nbsp;: c&rsquo;est ce d&eacute;tournement '
 'de 1957 qui, en octobre 2024, a sauv&eacute; le centre-ville. La suite &agrave; la derni&egrave;re fiche.</p></div>'))

FICHES_X.append(X(7, "VII", "EL FUTURO BLANCO &middot; 1982&ndash;2007", "Calatrava &amp; le si&egrave;cle blanc",
 '<path class="oranj" d="M14 66 q34 -30 68 0 q-34 14 -68 0 z"/>'
 '<g class="gr-cligne"><ellipse class="plein" cx="48" cy="62" rx="10" ry="7"/></g>'
 '<path class="trait" d="M20 40 q28 -22 56 0" fill="none" stroke-width="4"/>'
 '<path class="trait" d="M26 40 v8 M36 34 v12 M48 31 v14 M60 34 v12 M70 40 v8" fill="none"/>'
 '<line class="trait" x1="12" y1="84" x2="84" y2="84"/>',
 '<p><span class="lettrine le">L</span>&rsquo;autonomie revient en <strong>1982</strong> '
 '(Communaut&eacute; valencienne, statut, Generalitat), et la ville se r&ecirc;ve un futur. '
 'Elle le confie &agrave; un enfant du pays&nbsp;: <strong>Santiago Calatrava</strong>, qui '
 'plante dans le lit du Turia une <strong>Cit&eacute; des Arts et des Sciences</strong> '
 'blanche comme un squelette de baleine &mdash; Hemisf&egrave;ric (1998), mus&eacute;e des '
 'Sciences, Oceanogr&agrave;fic de F&eacute;lix Candela.</p>'
 '<p>En <strong>2007</strong>, l&rsquo;America&rsquo;s Cup am&egrave;ne le monde dans la marina&nbsp;; '
 'la F1 suivra quelques ann&eacute;es en circuit urbain. Co&ucirc;teux, discut&eacute;, '
 'photog&eacute;nique&nbsp;: le &laquo;&nbsp;si&egrave;cle blanc&nbsp;&raquo; divise les Valenciens '
 '&mdash; et remplit tes cartes m&eacute;moire.</p>'
 '<div class="merksatz"><p>Meilleure heure &agrave; la Cit&eacute;&nbsp;: la dor&eacute;e, quand le '
 'blanc de Calatrava vire &agrave; l&rsquo;orange et se double dans les bassins.</p></div>'))

FICHES_X.append(X(8, "VIII", "LA DANA &middot; 2024&ndash;2026", "La goutte froide &amp; la reconstruction",
 '<path class="plein" d="M48 14 q20 26 20 42 q0 16 -20 24 q-20 -8 -20 -24 q0 -16 20 -42 z" style="fill:#7E2D1E"/>'
 '<path class="jaune" d="M42 52 l6 6 l12 -14 l-4 -4 l-8 10 l-2 -2 z"/>'
 '<g class="gr-pousse"><path class="trait" d="M76 74 q2 -12 8 -16" fill="none" style="stroke:#5C7345"/>'
 '<circle cx="84" cy="56" r="3.4" fill="#5C7345"/></g>'
 '<line class="trait" x1="16" y1="84" x2="80" y2="84"/>',
 '<p><span class="lettrine le">L</span>e <strong>29 octobre 2024</strong>, une DANA &mdash; la '
 '&laquo;&nbsp;goutte froide&nbsp;&raquo; m&eacute;diterran&eacute;enne &mdash; d&eacute;verse plus de '
 '770&nbsp;L/m&sup2; en amont&nbsp;: <strong>229 morts</strong> dans la province, des communes '
 'enti&egrave;res du sud (Paiporta, Catarroja&hellip;) d&eacute;vast&eacute;es. Le centre de Valence, '
 'lui, est &eacute;pargn&eacute; &mdash; prot&eacute;g&eacute; par le canal de <strong>1957</strong>. '
 'L&rsquo;histoire s&rsquo;est referm&eacute;e comme une parenth&egrave;se.</p>'
 '<p>Depuis&nbsp;: col&egrave;re politique (d&eacute;mission du pr&eacute;sident r&eacute;gional fin '
 '2025, enqu&ecirc;te judiciaire en cours), et une reconstruction lente mais r&eacute;elle &mdash; '
 'm&eacute;tro du sud enti&egrave;rement rouvert en juin 2025, chantiers massifs en 2026. Les '
 'communes touch&eacute;es restent des lieux de deuil&nbsp;: on n&rsquo;y va pas en visite.</p>'
 '<div class="achtung"><p>Visit Val&egrave;ncia le dit sans d&eacute;tour&nbsp;: le tourisme du '
 'centre <strong>finance la relance</strong>. Voyager ici en 2026, c&rsquo;est aider &mdash; '
 'avec le tact de la fiche &sect;&nbsp;3.</p></div>'))
