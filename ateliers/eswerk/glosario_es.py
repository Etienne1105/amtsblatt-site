# -*- coding: utf-8 -*-
# Glosario — 9 fiches parlantes. data-de = texte TTS (clé technique héritée du moteur v5), ici castillan es-ES.
# Affichage : espagnol (· valencien quand il vit) ; .pron = à la québécoise ; récolte examen sur td.de/td.fr.
from pictos_es import PICTOS

SPK = ('<svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true">'
 '<path d="M4 9 h4 l5 -5 v16 l-5 -5 H4 z" fill="currentColor"/>'
 '<path d="M16 9 q3 3 0 6 M18.5 6.5 q5 5.5 0 11" stroke="currentColor" stroke-width="2" fill="none"/></svg>')

def D(es):
    return ('<button class="dire" type="button" data-de="' + es.replace('"', '&quot;') +
            '" aria-label="&Eacute;couter">' + SPK + '</button>')

def T(fid, teil, titre, corps):
    return ('<section class="fiche par-pair" id="' + fid + '" data-par="10">'
            '<header class="fiche-tete"><div><span class="parno">&sect; 10</span>'
            '<h2>' + titre + '</h2><span class="teil">Carreau ' + teil + '</span></div>'
            + PICTOS[10] + '</header><div class="corps-sec">' + corps + '</div></section>')

def rij(es, tl, pron, fr, tts=None):
    tlb = (' <span class="tl">&middot; ' + tl + '</span>') if tl else ''
    return ('<tr><td class="de"><span lang="es">' + es + '</span>' + tlb + ' '
            + D(tts or es) + '</td><td class="pron">' + pron + '</td><td class="fr">' + fr + '</td></tr>')

def tablo(caption, rows, prfx=True):
    btn = ('<button class="pruefen-toggle" type="button">A PRUEBA &mdash; cache les sens</button>' if prfx else '')
    return ('<div class="bloc-tablo"><table class="tablo-sprach"><caption>' + caption + '</caption>'
            '<tr><th>ES</th><th>&agrave; la qu&eacute;b&eacute;coise</th><th>sens</th></tr>'
            + "".join(rows) + '</table>' + btn + '</div>')

# --- prononciation : grille compacte HORS récolte (pas de tablo-sprach) ---
_ALFA = [
 ("J / ge, gi","RRR (Bach)"),("LL","y (paeya)"),("&Ntilde; &ntilde;","gn (Espagne)"),("V v","= B&nbsp;!"),
 ("Z / ce, ci","th (zozote)"),("H h","muette"),("RR rr","r bien roul&eacute;"),("QU qu","k (le u se tait)"),
 ("GU+e/i","gu&egrave; (u muet)","x"),("&iexcl; &iquest;","&agrave; l&rsquo;envers, d&rsquo;abord"),("D final","tr&egrave;s doux"),("accent &#180;","LA syllabe frapp&eacute;e"),
]
ALFA_GRILLE = ('<div class="alfa-grille">' +
 "".join('<span class="al"><b lang="es">' + l[0] + '</b><i>' + l[1] + '</i></span>' for l in _ALFA) + '</div>')

FICHES_TAAL = []

FICHES_TAAL.append(T("p10-1", "1 &middot; 9", "Glosario &mdash; la bouche espagnole",
 '<p><span class="lettrine le">T</span>out se lit comme &ccedil;a s&rsquo;&eacute;crit &mdash; une fois d&eacute;samorc&eacute;s '
 'les douze pi&egrave;ges ci-dessous. L&rsquo;accent aigu (&#180;) marque LA syllabe qu&rsquo;on frappe&nbsp;: '
 '<em lang="es">Val&egrave;ncia</em> = ba-L&Egrave;N-ssia.</p>'
 + ALFA_GRILLE +
 '<div class="achtung"><p>Tra&icirc;tres&nbsp;: <b>V</b> se prononce <strong>B</strong> (Valencia = Balencia), '
 '<b>J</b> racle la gorge, <b>Z</b> et <b>ce/ci</b> zozotent (le fameux <em>ceceo</em> castillan), '
 '<b>H</b> ne se dit jamais.</p></div>'
 '<div class="merksatz"><p>Le bouton (&#9664;) fait parler la voix espagnole de ton appareil. '
 '&Eacute;coute, r&eacute;p&egrave;te, tape A PRUEBA pour te tester.</p></div>'))

FICHES_TAAL.append(T("p10-2", "2 &middot; 9", "Saludos &mdash; saluer &amp; remercier",
 tablo("Le n&eacute;cessaire absolu", [
 rij("Hola", "", "O-la (H muet)", "salut / bonjour passe-partout"),
 rij("Buenos d&iacute;as", "Bon dia", "BOU&Eacute;-noss DI-ass", "bonjour (le matin)"),
 rij("Buenas tardes", "", "BOU&Eacute;-nass TAR-dess", "bonjour / bonsoir (apr&egrave;s ~14h)"),
 rij("Buenas noches", "", "BOU&Eacute;-nass NO-tchess", "bonsoir / bonne nuit"),
 rij("Adi&oacute;s", "", "a-DIOSS", "au revoir"),
 rij("Hasta luego", "", "AS-ta LOU&Eacute;-go", "&agrave; plus tard"),
 rij("Gracias", "Gr&agrave;cies", "GRA-ssiass", "merci"),
 rij("Por favor", "", "por fa-BOR", "s&rsquo;il vous pla&icirc;t"),
 ])
 + '<div class="merksatz"><p>Ouvrir avec un <em>Bon dia</em> valencien fait sourire &mdash; '
 'puis tout le monde bascule en castillan sans fa&ccedil;ons.</p></div>'))

FICHES_TAAL.append(T("p10-3", "3 &middot; 9", "S&iacute;, no &amp; les faux amis",
 tablo("Quatre mots qui d&eacute;cident de tout &mdash; et deux mines", [
 rij("S&iacute;", "", "SI", "oui"),
 rij("No", "", "NO", "non"),
 rij("Vale", "", "BA-l&eacute;", "d&rsquo;accord / OK (le mot le plus dit d&rsquo;Espagne)"),
 rij("Perd&oacute;n", "", "p&egrave;r-DONN", "pardon / excusez-moi"),
 rij("No entiendo", "", "no &egrave;n-TI&Egrave;N-do", "je ne comprends pas"),
 rij("Estoy constipada", "", "&egrave;s-TO&Iuml; conss-ti-PA-da", "je suis enrhum&eacute;e &mdash; pi&egrave;ge&nbsp;: PAS constip&eacute;e&nbsp;!"),
 rij("Embarazada", "", "&egrave;m-ba-ra-SSA-da", "enceinte &mdash; pi&egrave;ge&nbsp;: PAS embarrass&eacute;e&nbsp;!"),
 ])
 + '<div class="achtung"><p>Les deux derniers sont les faux amis les plus c&eacute;l&egrave;bres de la langue&nbsp;: '
 'dire <em>estoy embarazada</em> pour &laquo;&nbsp;je suis g&ecirc;n&eacute;e&nbsp;&raquo; annonce&hellip; une grossesse.</p></div>'))

FICHES_TAAL.append(T("p10-4", "4 &middot; 9", "En el restaurante &mdash; commander",
 tablo("De la table &agrave; l&rsquo;addition", [
 rij("Una mesa para dos", "", "OU-na M&Eacute;-ssa PA-ra DOSS", "une table pour deux"),
 rij("La carta, por favor", "", "la KAR-ta", "la carte, s&rsquo;il vous pla&icirc;t"),
 rij("&iquest;Qu&eacute; me recomienda?", "", "k&eacute; m&eacute; r&eacute;-ko-MI&Egrave;N-da", "que me recommandez-vous&nbsp;?"),
 rij("Para beber&hellip;", "", "PA-ra b&eacute;-B&Egrave;R", "comme boisson&hellip;"),
 rij("&iexcl;Buen&iacute;simo!", "", "boué-NI-ssi-mo", "d&eacute;licieux&nbsp;!"),
 rij("La cuenta, por favor", "", "la KOU&Egrave;N-ta", "l&rsquo;addition (elle ne vient jamais seule)"),
 rij("&iquest;Se puede pagar con tarjeta?", "", "s&eacute; POU&Eacute;-d&eacute; pa-GAR con tar-RH&Eacute;-ta", "on peut payer par carte&nbsp;?"),
 rij("El men&uacute; del d&iacute;a", "", "&egrave;l m&eacute;-NOU d&egrave;l DI-a", "le menu du jour (midi, ~12&ndash;15&nbsp;&euro;)"),
 ])))

FICHES_TAAL.append(T("p10-5", "5 &middot; 9", "La mesa valenciana &mdash; les mots sacr&eacute;s",
 tablo("Ce qui se mange ici, et nulle part ailleurs", [
 rij("La paella", "", "pa-&Eacute;-ya (jamais pa-&eacute;-LA)", "LE plat &mdash; poulet &amp; lapin, midi seulement"),
 rij("El socarrat", "val.", "sso-ka-RRATT", "la cro&ucirc;te d&rsquo;or du fond &mdash; le tr&eacute;sor"),
 rij("Horchata y fartons", "Orxata i fartons", "or-TCHA-ta i far-TONSS", "lait de souchet glac&eacute; + brioches &agrave; tremper"),
 rij("El esgarraet", "val.", "&egrave;s-ga-rra-&Egrave;TT", "poivrons r&ocirc;tis + morue &mdash; l&rsquo;entr&eacute;e reine"),
 rij("All i pebre", "val.", "A&Iuml; i P&Egrave;-br&eacute;", "rago&ucirc;t d&rsquo;anguille de l&rsquo;Albufera"),
 rij("Las cl&oacute;chinas", "val.", "KLO-tchi-nass", "petites moules locales &mdash; mai &agrave; ao&ucirc;t seulement"),
 rij("El esmorzaret", "val.", "&egrave;s-mor-ssa-R&Egrave;TT", "le casse-cro&ucirc;te sacr&eacute; de 10h30"),
 rij("Agua de Valencia", "", "A-goua d&eacute; ba-L&Egrave;N-ssia", "cocktail orange-cava-gin-vodka &mdash; tra&icirc;tre"),
 ])
 + '<div class="merksatz"><p>Les mots marqu&eacute;s <em>val.</em> sont du valencien &mdash; '
 'les prononcer, c&rsquo;est d&eacute;j&agrave; go&ucirc;ter.</p></div>'))

FICHES_TAAL.append(T("p10-6", "6 &middot; 9", "Moverse &mdash; se d&eacute;placer",
 tablo("La rue, l&rsquo;arr&ecirc;t, le billet", [
 rij("&iquest;D&oacute;nde est&aacute;&hellip;?", "", "DONN-d&eacute; &egrave;s-TA", "o&ugrave; est&hellip;&nbsp;?"),
 rij("La parada", "", "la pa-RA-da", "l&rsquo;arr&ecirc;t (bus, tram)"),
 rij("Un billete", "", "oun bi-YÉ-t&eacute;", "un billet"),
 rij("La estaci&oacute;n", "", "la &egrave;s-ta-SSIONN", "la gare / la station"),
 rij("A la derecha", "", "a la d&eacute;-R&Eacute;-tcha", "&agrave; droite"),
 rij("A la izquierda", "", "a la iss-KI&Egrave;R-da", "&agrave; gauche"),
 rij("Todo recto", "", "TO-do R&Egrave;K-to", "tout droit"),
 ])))

FICHES_TAAL.append(T("p10-7", "7 &middot; 9", "N&uacute;meros y horas &mdash; compter",
 tablo("Assez pour payer et prendre rendez-vous", [
 rij("Uno, dos, tres", "", "OU-no, DOSS, TR&Egrave;SS", "un, deux, trois"),
 rij("Cuatro, cinco, seis", "", "KOUA-tro, SSIN-ko, S&Egrave;&Iuml;SS", "quatre, cinq, six"),
 rij("Siete, ocho, nueve", "", "SI&Egrave;-t&eacute;, O-tcho, NOU&Egrave;-b&eacute;", "sept, huit, neuf"),
 rij("Diez, veinte, cien", "", "DI&Egrave;SS, B&Eacute;&Iuml;N-t&eacute;, SSI&Egrave;NN", "dix, vingt, cent"),
 rij("&iquest;A qu&eacute; hora?", "", "a k&eacute; O-ra", "&agrave; quelle heure&nbsp;?"),
 rij("Son las dos y media", "", "sonn lass DOSS i M&Eacute;-dia", "il est deux heures et demie"),
 ])))

FICHES_TAAL.append(T("p10-8", "8 &middot; 9", "Urgencias &mdash; sant&eacute; &amp; secours",
 tablo("Les mots qu&rsquo;on esp&egrave;re ne jamais dire", [
 rij("&iexcl;Socorro!", "", "sso-KO-rro", "au secours&nbsp;!"),
 rij("La farmacia", "", "la far-MA-ssia", "la pharmacie (croix verte)"),
 rij("El m&eacute;dico", "", "&egrave;l M&Eacute;-di-ko", "le m&eacute;decin"),
 rij("El hospital", "", "&egrave;l oss-pi-TAL", "l&rsquo;h&ocirc;pital"),
 rij("La polic&iacute;a", "", "la po-li-SSI-a", "la police"),
 rij("Me duele aqu&iacute;", "", "m&eacute; DOU&Egrave;-l&eacute; a-KI", "j&rsquo;ai mal ici"),
 rij("&iquest;Habla ingl&eacute;s?", "", "A-bla inn-GL&Egrave;SS", "parlez-vous anglais&nbsp;?"),
 ])
 + '<div class="achtung"><p>Le <strong>112</strong> fonctionne partout, en anglais. '
 'Les pharmaciens espagnols conseillent volontiers &mdash; premier r&eacute;flexe pour les petits bobos.</p></div>'))

FICHES_TAAL.append(T("p10-9", "9 &middot; 9", "El Constructor &mdash; fabrique &agrave; phrases",
 '<p>Assemble&nbsp;: une amorce, une brique. Le carreau imprime, puis parle. '
 '(Rappel&nbsp;: le &iquest; ouvre la question, &agrave; l&rsquo;envers, d&egrave;s le d&eacute;but.)</p>'
 '<div id="baukasten">'
 '<div class="bk-rang">'
 '<button type="button" class="bk-a" data-g="donde" data-de="&iquest;D&oacute;nde est&aacute;" data-fr="O&ugrave; est">&iquest;D&oacute;nde est&aacute;&hellip;</button>'
 '<button type="button" class="bk-a" data-g="quisiera" data-de="Quisiera" data-fr="Je voudrais">Quisiera&hellip;</button>'
 '<button type="button" class="bk-a" data-g="tiene" data-de="&iquest;Tiene" data-fr="Avez-vous">&iquest;Tiene&hellip;</button>'
 '<button type="button" class="bk-a" data-g="puedo" data-de="&iquest;Puedo" data-fr="Puis-je">&iquest;Puedo&hellip;</button>'
 '</div>'
 '<div class="bk-rang">'
 '<button type="button" class="bk-f" data-g="donde" data-de="el ba&ntilde;o?" data-fr="les toilettes&nbsp;?">el ba&ntilde;o?</button>'
 '<button type="button" class="bk-f" data-g="donde" data-de="el Mercado Central?" data-fr="le Mercado Central&nbsp;?">el Mercado Central?</button>'
 '<button type="button" class="bk-f" data-g="donde" data-de="la parada del metro?" data-fr="l&rsquo;arr&ecirc;t de m&eacute;tro&nbsp;?">la parada del metro?</button>'
 '<button type="button" class="bk-f" data-g="donde" data-de="la Lonja?" data-fr="la Lonja&nbsp;?">la Lonja?</button>'
 '<button type="button" class="bk-f" data-g="quisiera" data-de="una horchata." data-fr="une horchata.">una horchata.</button>'
 '<button type="button" class="bk-f" data-g="quisiera" data-de="una paella para dos." data-fr="une paella pour deux.">una paella para dos.</button>'
 '<button type="button" class="bk-f" data-g="quisiera" data-de="la cuenta." data-fr="l&rsquo;addition.">la cuenta.</button>'
 '<button type="button" class="bk-f" data-g="quisiera" data-de="dos billetes." data-fr="deux billets.">dos billetes.</button>'
 '<button type="button" class="bk-f" data-g="tiene" data-de="agua?" data-fr="de l&rsquo;eau&nbsp;?">agua?</button>'
 '<button type="button" class="bk-f" data-g="tiene" data-de="mesa para dos?" data-fr="une table pour deux&nbsp;?">mesa para dos?</button>'
 '<button type="button" class="bk-f" data-g="tiene" data-de="un plano?" data-fr="un plan&nbsp;?">un plano?</button>'
 '<button type="button" class="bk-f" data-g="tiene" data-de="fartons?" data-fr="des fartons&nbsp;?">fartons?</button>'
 '<button type="button" class="bk-f" data-g="puedo" data-de="sentarme aqu&iacute;?" data-fr="m&rsquo;asseoir ici&nbsp;?">sentarme aqu&iacute;?</button>'
 '<button type="button" class="bk-f" data-g="puedo" data-de="hacer una foto?" data-fr="prendre une photo&nbsp;?">hacer una foto?</button>'
 '<button type="button" class="bk-f" data-g="puedo" data-de="pedir?" data-fr="commander&nbsp;?">pedir?</button>'
 '<button type="button" class="bk-f" data-g="puedo" data-de="pagar con tarjeta?" data-fr="payer par carte&nbsp;?">pagar con tarjeta?</button>'
 '</div>'
 '<div class="bk-sortie"><p id="bk-de" lang="es">&nbsp;</p><p id="bk-fr">&nbsp;</p></div>'
 '<button type="button" class="bk-sprechen">HABLA &mdash; faire parler</button>'
 '</div>'))
