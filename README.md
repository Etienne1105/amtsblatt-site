# Amtsblatt — Guide des usages allemands

Guide culturel de voyage (Rhénanie) en un seul fichier HTML autonome, forgé dans la vibe **BETON-SCRIPTORIUM** — brutalisme béton coffrage 1972 × enluminures gothiques.

> *« Un règlement municipal coulé dans le béton en 1972, enluminé la nuit par un moine copiste. »*

## Contenu

- **§ 1–10** — le contrat social, le rituel Kölsch/Köbes, l'argent, le Pfand, la Rettungsgasse, les pièges sociaux, la table rhénane, le lexique de survie.
- **§ 11 — Prüfung** : 12 mises en situation, tamponnées `GENEHMIGT` / `ABGELEHNT`, sonorisées à la machine Enigma (synthèse Web Audio, zéro dépendance).

## Structure

| Fichier | Rôle |
|---|---|
| `index.html` | Le guide complet — HTML/CSS/JS autonome, mobile-first |
| `beton-scriptorium.vibe.json` | La vibe forgée (itération 5 — Conseils des 6-8 juillet 2026) — palette 4 pigments, deck, typo, SFX, gate anti-slop |

## Déploiement

Site statique pur : Netlify (Drop ou import Git), GitHub Pages, ou n'importe quel hébergeur. Seule dépendance externe : Google Fonts (`Grenze Gotisch`, `IBM Plex Sans/Mono`).

## Journal des itérations

### v5 — 2026-07-08 · Der Sprachführer
- **EMPFANG** : page d'accueil à 11 tuiles bristol (pictos animés en chœur), tuile Sprachführer pleine largeur, avant l'Inhaltsverzeichnis conservé.
- **Sprachführer professionnel (§ 10, 11 fiches)** : voix allemande native (SpeechSynthesis de-DE) sur chaque entrée, prononciation en deux volets avec l'avantage francophone assumé, six lexiques thématiques (survie, Brauhaus, ville-santé, Bahn, Freizeitpark, chiffres-temps), mode **PRÜFEN** par table (sens voilés, tap pour révéler), **Satzbaukasten** — 16 phrases calibrées, dactylographiées puis prononcées —, faux amis enrichis.
- **Deux œufs de Pâques** : une Annexe 7 classifiée quelque part sous un tampon, et une séquence de clavier sur le Lampenfeld.
- **Quiz** : le verdict remplace désormais situation, question et choix (hauteur constante) ; machine compactée à 280 px.
- `beton-scriptorium.vibe.json` → `iteration: 5`.

### v4 — 2026-07-07 · La fiche bristol dactylographiée
- **Cartes Karteikarten** : chaque fiche devient une carte bristol posée sur le béton — papier ligné bleu pâle, marge rouge, liseré de classement pigmenté, ombre dure ; pictogrammes repassés à l'encre.
- **Zéro défilement** : 35 fiches calibrées ≤ 1250 caractères, § 11 scindé (intro / examen), verdict du quiz remplaçant les choix (hauteur constante). `overflow:hidden` — filet automatique sous 640 px de hauteur seulement.
- **Dactylographie** : chaque fiche se tape à l'ouverture — trois profils de frappe (330/420/500 c/s) avec pauses à la ponctuation, curseur bloc clignotant, encadrés et rangées de tables révélés en blocs, frappes sonores échantillonnées et *ding* de chariot en fin de carte. Un tap révèle tout.
- **Animations accélérées ~40 %** ; le picto § 4 refondu — la pièce tombe dans la fente de la caisse `BAR`.
- `beton-scriptorium.vibe.json` → `iteration: 4`.

### v3 — 2026-07-07 · Le deck mécanique
Conseil de Recette v3 (trois décisions d'Étienne) : le défilement cesse d'être le mode principal de navigation.
- **Deck de Karteikarten** : 29 fiches de contenu plein écran (découpe aux frontières `h3`, lexique scindé en Blocs A/B/C), plus couverture, hub et colophon. Navigation par boutons, balayage tactile et liens profonds (`#p6-2`).
- **Enigma omniprésente** : compteur à rotors dans la barre de navigation (chiffres roulants, tic sonore par fiche) + machine complète au § 11 — trois rotors crantés, Lampenfeld QWERTZUIOP, câblage de Steckerbrett. Bonne réponse : lampe jaune Autobahn + rotor qui avance ; mauvaise : court-circuit sur un câble.
- **11 pictogrammes Plakatstil** animés en `steps()`, un par § : le tampon frappe, les traits du Deckel se comptent, la Rettungsgasse s'ouvre, l'Ampelmännchen passe au vert, le Kranz tourne…
- **Enluminures 4 pigments** : lettrines bichromes à rehaut d'or, pilcrows ¶ cyclant bleu tampon / rouge oxyde / **Patinagrün** (`#3E7A63`, vert-de-gris des toits de cuivre rhénans).
- Contenu §1–§11 déplacé programmatiquement (asserts d'intégrité texte) — zéro régénération.
- `beton-scriptorium.vibe.json` → `iteration: 3`.

### v2.1 — 2026-07-07 · Correctif d'affichage
La règle de masquage `html.js .imprimable` (spécificité 0,2,1) écrasait la révélation `.est-imprime` (0,1,0) : contenu chargé mais bloqué à `opacity:0` — seuls le fronton et l'impressum s'affichaient. Corrigé par le sélecteur `html.js .imprimable.est-imprime` (0,3,1), plus un filet de sécurité : si le routeur échoue, la classe `js` est retirée et le document redevient un mur intégralement lisible.

### v2 — 2026-07-07 · Navigation dossier à fiches
Le mur monolithique (tous les § déroulés sur une seule page) devient un **dossier navigable** :
- **Hub d'accueil** : le sommaire (*Inhaltsverzeichnis*) est l'écran d'entrée ; un tap ouvre la fiche § voulue en plein écran.
- **Barre sticky** `‹ ZURÜCK · INHALT n/11 · WEITER ›`, calée dans la zone du pouce (respect du `safe-area-inset` iOS).
- **Hash-routing** : les boutons précédent/suivant de Safari fonctionnent, et les liens profonds sont partageables (`…/#p6` ouvre directement la Rettungsgasse).
- **Amélioration progressive** : sans JavaScript, le document complet reste lisible en un seul flux — rien ne casse.
- `beton-scriptorium.vibe.json` → `iteration: 2`, justification *layout* révisée.

### v1 — 2026-07-06 · Mur monolithique
Première coulée. Guide complet §1–§11 en page unique, vibe **BETON-SCRIPTORIUM** forgée au Conseil de Recette (palette béton + rubrication, typo Grenze Gotisch × IBM Plex, SFX Enigma, gate anti-slop).

---
*Forge : vibe-forge · Scribe : Claudi-brimbor · Az. 2026/07-EM · GÜLTIG AB SOFORT*

## NL v1 — « Het Logboek » (2026-07-09)
Guide néerlandais complet dans /nl/ : vibe DELFT-LOGBOEK (faïence, Hollandais Volant), 29 fiches (§1-9 + Taalgids 9 fiches TTS nl-NL + Toets 12 vragen sur moulin à sacs de grain), moteur v5 transplanté (Frappe/routeur), sons refondus bois/moulin, 2 œufs (spook, tempête). Épreuve jsdom 27/27.
