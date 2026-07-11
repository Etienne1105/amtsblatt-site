# Atelier eswerk — la forge d'El Llibret (`/es/`)

Atelier complet ayant produit `es/index.html` (guide Espagne/València du Classeur, forgé pour Stéphanie, juillet 2026). Sert d'exemple canonique au skill **Globetrotter** (`skills/globetrotter.skill`) : la marche à suivre pour ajouter un nouveau pays.

## Contenu

| Fichier | Rôle |
|---|---|
| `pictos_es.py` | Pictogrammes SVG |
| `glosario_es.py` | Glossaire parlant — 51 entrées TTS, faux amis pièges |
| `contenido_a_es.py` | Stèle, patio interactif (13 tuiles + guitare), fiches A |
| `contenido_b_es.py` | Fiches B, despedida, colophon, écran secret Cremà |
| `cronica_es.py` | Chronique — Valentia (−138) → DANA (2024) |
| `preguntas_es.py` | Quiz 12 questions, bonnes réponses redistribuées |
| `examen_es.py` | Examen + corona de azahar (14 fleurs sur Bézier) |
| `dolcaina.js` | Moteur audio — castagnettes, guitare, noria, mascletà |
| `eswerk.py` | Assembleur — substitutions comptées, patches JS, gates zéro-grec |
| `pruebas.js` | Harnais jsdom — 41/41 |
| `build_script.js` | Utilitaire d'extraction du template |

## Reproduire

```bash
npm install jsdom
python3 eswerk.py     # → es_index.html (nécessite gr/index.html du repo à côté)
node pruebas.js       # → exiger 41/41
```

Template source : `gr/index.html`. Sortie de référence : `es/index.html` (sha256 `9087823…f66144`).
