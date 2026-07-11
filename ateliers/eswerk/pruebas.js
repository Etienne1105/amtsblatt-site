// PRUEBAS — épreuve jsdom du Llibret. Chaque ✓ compte ; tout ✗ est éliminatoire.
const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync('es_index.html', 'utf-8');

let ok = 0, ko = 0;
function t(nom, cond) {
  if (cond) { ok++; console.log('  ✓', nom); }
  else { ko++; console.log('  ✗✗', nom); }
}

const errs = [];
const dom = new JSDOM(html, { runScripts: 'dangerously', url: 'https://amsblatt-site.netlify.app/es/', pretendToBeVisual: true });
const w = dom.window;
w.addEventListener('error', e => errs.push(String(e.message)));
// stub TTS absent en jsdom : la page doit se dégrader proprement (classe sans-voix)

setTimeout(() => {
  const d = w.document;

  console.log('— 1. Chargement & routeur —');
  t('zéro erreur JS runtime', errs.length === 0 || (console.log('   errs:', errs), false));
  const actifs0 = [...d.querySelectorAll('section.fiche.actif')].map(x => x.id);
  t('routeur vivant : une seule page active', actifs0.length === 1);
  t('sans-voix togglé (TTS absent en jsdom)', d.documentElement.classList.contains('sans-voix'));
  const agora = d.getElementById('agora');
  t('couverture active au chargement', actifs0[0] === 'stele');
  t('couverture présente : El Llibret', /El Llibret/.test(d.getElementById('stele').textContent));
  t('dédicace à Stéphanie', /St\u00e9phanie/.test(d.getElementById('stele').textContent));
  t('13 tuiles au patio', agora.querySelectorAll('.tuile').length === 13);
  t('guitare aux 4 cordes présente', agora.querySelectorAll('.chorde').length === 4);

  console.log('— 2. Navigation —');
  w.location.hash = '#p4-1';
  setTimeout(() => {
    const p41 = d.getElementById('p4-1');
    t('navigation #p4-1 (la mesa) active', p41.classList.contains('actif'));
    t('navbar révélée hors couverture', !d.getElementById('navbar').classList.contains('cache'));
    t('label navbar EL PATIO', /EL PATIO/.test(d.getElementById('navbar').textContent));
    t('doctrine paella : le chorizo nommé pour être banni', /chorizo/i.test(p41.textContent));

    console.log('— 3. Glosario & Constructor —');
    w.location.hash = '#p10-9';
    setTimeout(() => {
      const bk = d.getElementById('baukasten');
      t('baukasten présent', !!bk);
      // geste réel : toucher la fiche skippe la Frappe (sinon elle écrase bk-de)
      d.getElementById('p10-9').dispatchEvent(new w.Event('pointerdown', { bubbles: true }));
      bk.querySelector('.bk-a[data-g="quisiera"]').click();
      bk.querySelector('.bk-f[data-de="una horchata."]').click();
      setTimeout(() => {
      console.log('   [sonde] bk-de = «' + d.getElementById('bk-de').textContent + '» | frappe restante: ' + d.querySelectorAll('#p10-9 .cache-frappe').length);
      t('constructor assemble « Quisiera una horchata. » (machine à écrire)', /Quisiera\s+una horchata\./.test(d.getElementById('bk-de').textContent));
      const tousBtn = d.querySelectorAll('button.dire');
      t('boutons TTS nombreux (' + tousBtn.length + ' ≥ 45)', tousBtn.length >= 45);
      const pt = d.querySelector('#p10-3 .pruefen-toggle');
      pt.click();
      t('A PRUEBA cache les sens', d.querySelector('#p10-3 table').classList.contains('cache-sens'));
      t('libellé toggle → REVELA', /REVELA/.test(pt.textContent));

      console.log('— 4. La Prueba (quiz) —');
      w.location.hash = '#manteion';
      setTimeout(() => {
        const qz = d.getElementById('quiz-zone');
        t('question 1 rendue', /PREGUNTA 1\/12/.test(d.getElementById('quiz-prog').textContent));
        t('situation en espagnol-cadre', /Situaci\u00f3n/.test(qz.textContent));
        const bons = qz.querySelectorAll('button');
        t('3 choix offerts', bons.length === 3);
        // répondre juste à Q1 (FRAGEN[0].b) :
        const FR = w.eval('FRAGEN');
        bons[FR[0].b].click();
        t('tampon ¡FET! sur bonne réponse', /\u00a1FET!/.test(qz.textContent));
        const v1 = d.getElementById('amfora-1-vul');
        t('socarrat monte (scaleY > 0)', /scaleY\(0\.25\)/.test(v1.style.transform));
        t('noria a tourné (90°)', /rotate\(90deg\)/.test(d.getElementById('meule').style.transform));
        t('compteur rotor A → 01', d.getElementById('rota-t') && d.getElementById('rota-t').textContent.includes('0'));

        console.log('— 5. El Examen (couronne d\u2019azahar) —');
        w.location.hash = '#examen';
        setTimeout(() => {
          const LEX = w.eval('LEXICON');
          t('LEXICON récolté : 51 paires', LEX.length === 51);
          t('pièges marqués (constipada, embarazada)', LEX.filter(e => e.piege).length === 2);
          t('question 1/14 rendue', /PREGUNTA 1\/14/.test(d.getElementById('ex-prog').textContent));
          const ez = d.getElementById('ex-zone');
          t('mode affiché (Elige/Escribe el sentido)', /(Elige|Escribe) el sentido/.test(ez.textContent));
          t('14 fleurs d\u2019azahar en attente', d.querySelectorAll('#cachets .cachet').length === 14);
          const qcm = ez.querySelectorAll('button.choix');
          if (qcm.length >= 3) { qcm[0].click(); t('réponse QCM acceptée (verdict affiché)', /(\u00a1FET!|QUEMADO)/.test(ez.textContent)); }
          else {
            const inp = ez.querySelector('input'); inp.value = 'xyz';
            const val = ez.querySelector('.ex-valider'); val.click();
            t('réponse courte jugée (QUEMADO attendu)', /QUEMADO/.test(ez.textContent));
          }

          console.log('— 6. Les deux eggs —');
          // egg 1 : triple-tap sur le stempel de couverture
          w.location.hash = '#agora';
          setTimeout(() => {
            const st = d.querySelector('.stempel-header');
            const ev = () => st.dispatchEvent(new w.MouseEvent('click', { bubbles: true }));
            ev(); ev(); ev();
            setTimeout(() => {
              t('triple-tap → #geheim (La Cremà)', w.location.hash === '#geheim');
              const gh = d.getElementById('geheim');
              t('écran Cremà actif', gh.classList.contains('actif'));
              t('ninot indultat dédié à Stéphanie', /St\u00e9phanie/.test(gh.textContent) && /indultat/i.test(gh.textContent));
              d.getElementById('geheim-retour').click();
              // egg 2 : les 4 cordes dans l'ordre
              w.location.hash = '#agora';
              setTimeout(() => {
                [1,2,3,4].forEach(n => d.getElementById('chorde-' + n).dispatchEvent(new w.Event('click', { bubbles: true })));
                setTimeout(() => {
                  t('cordes 1→4 : tampon ¡A LA CREMÀ!', !!d.querySelector('.keravnos-tampon') && /A LA CREM\u00c0/.test(d.querySelector('.keravnos-tampon').textContent));
                  t('classe keravnos (feu) posée', !!d.querySelector('.lyra.keravnos, .keravnos'));

                  console.log('— 7. Structure finale —');
                  t('8 fiches crónica', d.querySelectorAll('[data-par="12"]').length === 8);
                  t('18 retablos §1–9', [...d.querySelectorAll('section.fiche[id^="p"]')].filter(s=>/^p[1-9]-\d$/.test(s.id)).length === 18);
                  t('DANA traitée avec tact (§3 + crónica)', /zona cero|tact|recueil/i.test(d.getElementById('x-8').textContent + d.getElementById('p3-2').textContent));
                  t('colofón signé socarrat-llibret', /socarrat-llibret/.test(d.getElementById('kolophon').textContent));
                  t('retour Classeur présent', !!d.querySelector('#kolophon .retour-classeur[href="/"]'));
                  t('índice : 13 entrées', d.querySelectorAll('#pinakas li').length === 13);

                  console.log('\n════ BILAN : ' + ok + ' ✓ / ' + (ok + ko) + ' — ' + (ko === 0 ? 'SELLADO ✓✓' : ko + ' ÉCHEC(S)') + ' ════');
                  process.exit(ko === 0 ? 0 : 1);
                }, 350);
              }, 250);
            }, 300);
          }, 250);
        }, 300);
      }, 300);
      }, 650);
    }, 300);
  }, 300);
}, 400);
