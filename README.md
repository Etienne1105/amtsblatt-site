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
| `beton-scriptorium.vibe.json` | La vibe forgée (Conseil de Recette, 2026-07-06) — palette, typo, SFX, gate anti-slop |

## Déploiement

Site statique pur : Netlify (Drop ou import Git), GitHub Pages, ou n'importe quel hébergeur. Seule dépendance externe : Google Fonts (`Grenze Gotisch`, `IBM Plex Sans/Mono`).

## Journal des itérations

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
