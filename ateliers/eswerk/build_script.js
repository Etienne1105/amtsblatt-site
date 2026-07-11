
/* ============ Moteur sonore DOLCAINA — synthèse pure, timbres valenciens ============ */
const Dolcaina=(function(){
  let ctx=null,muted=false;
  function ensure(){
    if(!ctx){const AC=window.AudioContext||window.webkitAudioContext;if(!AC)return null;ctx=new AC();}
    if(ctx.state==='suspended')ctx.resume();
    return ctx;
  }
  function bruit(c,dur){
    const buf=c.createBuffer(1,Math.max(1,c.sampleRate*dur),c.sampleRate);
    const d=buf.getChannelData(0);
    for(let i=0;i<d.length;i++){d[i]=(Math.random()*2-1)*(1-i/d.length);}
    const s=c.createBufferSource();s.buffer=buf;return s;
  }
  /* frappe : castagnette — claquement de bois sec, très bref */
  function frappe(temps,force){
    const c=ensure();if(!c||muted)return;const t=temps||c.currentTime;const f=force||1;
    const src=bruit(c,0.008);
    const bp=c.createBiquadFilter();bp.type='bandpass';bp.frequency.value=3200;bp.Q.value=7;
    const g=c.createGain();g.gain.setValueAtTime(0.10*f,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.008);
    src.connect(bp).connect(g).connect(c.destination);src.start(t);
    const o=c.createOscillator();o.type='triangle';o.frequency.setValueAtTime(1976,t);
    const g2=c.createGain();g2.gain.setValueAtTime(0.045*f,t);g2.gain.exponentialRampToValueAtTime(0.001,t+0.025);
    o.connect(g2).connect(c.destination);o.start(t);o.stop(t+0.03);
  }
  function tape(){if(Math.random()<0.85)frappe(0,0.55+Math.random()*0.4);}
  /* corde de guitare nylon : fondamentale ronde + octave, détune léger, décroissance longue */
  function corde(freq,t,gain){
    const c=ensure();if(!c)return;
    const o=c.createOscillator();o.type='triangle';o.frequency.setValueAtTime(freq,t);o.detune.setValueAtTime(-4,t);
    const o2=c.createOscillator();o2.type='sine';o2.frequency.setValueAtTime(freq*2,t);o2.detune.setValueAtTime(5,t);
    const g=c.createGain();g.gain.setValueAtTime(0.0001,t);
    g.gain.exponentialRampToValueAtTime(gain,t+0.006);g.gain.exponentialRampToValueAtTime(0.001,t+0.82);
    const g2=c.createGain();g2.gain.setValueAtTime(0.0001,t);
    g2.gain.exponentialRampToValueAtTime(gain*0.35,t+0.006);g2.gain.exponentialRampToValueAtTime(0.001,t+0.42);
    o.connect(g).connect(c.destination);o2.connect(g2).connect(c.destination);
    o.start(t);o.stop(t+0.9);o2.start(t);o2.stop(t+0.5);
  }
  /* rotor/tick : pouce sur la corde grave — Mi 2 (82,41 Hz) */
  function rotor(){const c=ensure();if(!c||muted)return;corde(82.41,c.currentTime,0.13);}
  function tick(){rotor();}
  /* lampe (bonne réponse) : rasgueado phrygien-dominant mi–sol#–si, serré */
  function lampe(){
    const c=ensure();if(!c||muted)return;const t=c.currentTime;
    [[164.81,0],[207.65,0.07],[246.94,0.14]].forEach(function(p){corde(p[0],t+p[1],0.12);});
  }
  /* pluck(freq) : corde nommée — l'easter egg de la guitare au patio */
  function pluck(freq){const c=ensure();if(!c||muted)return;corde(freq||110,c.currentTime,0.16);}
  /* kurzschluss (erreur) : corde étouffée fa-contre-mi (battement) + noria qui grince */
  function kurzschluss(){
    const c=ensure();if(!c||muted)return;const t=c.currentTime;
    corde(174.61,t,0.06);corde(164.81,t,0.06);
    const o=c.createOscillator();o.type='sawtooth';
    o.frequency.setValueAtTime(140,t);o.frequency.exponentialRampToValueAtTime(88,t+0.5);
    const lp=c.createBiquadFilter();lp.type='lowpass';lp.frequency.value=480;lp.Q.value=5;
    const g=c.createGain();g.gain.setValueAtTime(0.0001,t);
    g.gain.exponentialRampToValueAtTime(0.11,t+0.04);
    const trem=c.createOscillator();trem.type='square';trem.frequency.value=9;
    const tg=c.createGain();tg.gain.value=0.05;
    trem.connect(tg).connect(g.gain);
    g.gain.setTargetAtTime(0.001,t+0.42,0.05);
    o.connect(lp).connect(g).connect(c.destination);
    o.start(t);o.stop(t+0.58);trem.start(t);trem.stop(t+0.58);
  }
  /* ding : la cloche du Miguelete — partiels inharmoniques, longue résonance */
  function ding(){
    const c=ensure();if(!c||muted)return;const t=c.currentTime;
    [[165,0.10,2.2],[330,0.12,1.6],[396,0.07,1.1],[495,0.05,0.9],[660,0.04,0.7]].forEach(function(p){
      const o=c.createOscillator();o.type='sine';o.frequency.setValueAtTime(p[0],t);
      const g=c.createGain();g.gain.setValueAtTime(0.0001,t);
      g.gain.exponentialRampToValueAtTime(p[1],t+0.012);g.gain.exponentialRampToValueAtTime(0.001,t+p[2]);
      o.connect(g).connect(c.destination);o.start(t);o.stop(t+p[2]+0.05);
    });
  }
  /* tonnerre : LA MASCLETÀ — détonations en accéléré puis terremoto final */
  function tonnerre(){
    const c=ensure();if(!c||muted)return;const t0=c.currentTime;
    let t=t0,pas=0.17;
    for(let i=0;i<6;i++){
      const s=bruit(c,0.09);
      const lp=c.createBiquadFilter();lp.type='lowpass';lp.frequency.value=900-90*i;
      const g=c.createGain();g.gain.setValueAtTime(0.16+0.02*i,t);
      g.gain.exponentialRampToValueAtTime(0.001,t+0.09);
      s.connect(lp).connect(g).connect(c.destination);s.start(t);
      t+=pas;pas*=0.82;
    }
    const s=bruit(c,1.25);
    const lp=c.createBiquadFilter();lp.type='lowpass';lp.frequency.setValueAtTime(180,t);
    lp.frequency.exponentialRampToValueAtTime(48,t+1.15);
    const g=c.createGain();g.gain.setValueAtTime(0.0001,t);
    g.gain.exponentialRampToValueAtTime(0.32,t+0.06);g.gain.exponentialRampToValueAtTime(0.001,t+1.25);
    s.connect(lp).connect(g).connect(c.destination);s.start(t);
    const o=c.createOscillator();o.type='sine';o.frequency.setValueAtTime(44,t);
    const g2=c.createGain();g2.gain.setValueAtTime(0.0001,t);
    g2.gain.exponentialRampToValueAtTime(0.22,t+0.08);g2.gain.exponentialRampToValueAtTime(0.001,t+1.1);
    o.connect(g2).connect(c.destination);o.start(t);o.stop(t+1.15);
  }
  function toggle(){muted=!muted;return muted;}
  return {frappe,tape,rotor,tick,lampe,pluck,kurzschluss,ding,tonnerre,toggle};
})();
const Lyra=Dolcaina;
const Enigma=Dolcaina;
const Stimme=(function(){
  let voix=null;
  function charger(){
    try{
      const vs=speechSynthesis.getVoices();
      voix=vs.find(v=>v.lang==='es-ES')||vs.find(v=>v.lang&&v.lang.indexOf('es')===0)||null;
    }catch(e){voix=null;}
    document.documentElement.classList.toggle('sans-voix',!voix);
  }
  if('speechSynthesis' in window){
    charger();
    if(speechSynthesis.onvoiceschanged!==undefined)speechSynthesis.onvoiceschanged=charger;
  }else{document.documentElement.classList.add('sans-voix');}
  function dire(txt,btn){
    if(!voix||!txt)return;
    try{
      speechSynthesis.cancel();
      const u=new SpeechSynthesisUtterance(txt);
      u.voice=voix;u.lang=voix.lang;u.rate=0.86;
      if(btn){btn.classList.add('parle');u.onend=u.onerror=()=>btn.classList.remove('parle');}
      speechSynthesis.speak(u);
    }catch(e){}
  }
  return{dire};
})();

/* ============ SPRACHFÜHRER — délégations : écoute, PRÜFEN, Baukasten ============ */
(function(){try{
  document.addEventListener('click',e=>{
    const dire=e.target.closest('button.dire');
    if(dire){Stimme.dire(dire.dataset.de,dire);return;}
    const pt=e.target.closest('button.pruefen-toggle');
    if(pt){
      const table=pt.parentElement.querySelector('table');
      if(table){
        const on=table.classList.toggle('cache-sens');
        table.querySelectorAll('tr.revele').forEach(r=>r.classList.remove('revele'));
        pt.textContent=on?'REVELA \u2014 montre tout':'A PRUEBA \u2014 cache les sens';
        Enigma.tick();
      }return;
    }
    const tr=e.target.closest('table.cache-sens tr');
    if(tr&&!tr.querySelector('th')){tr.classList.add('revele');Enigma.tape();return;}
  });
  /* Satzbaukasten */
  const bk=document.getElementById('baukasten');
  if(bk){
    const de=document.getElementById('bk-de'),fr=document.getElementById('bk-fr');
    let amorce=null,fin=null,timer=0;
    function ecrire(txt){
      clearInterval(timer);let i=0;de.textContent='';
      timer=setInterval(()=>{
        i+=2;de.textContent=txt.slice(0,i);Enigma.tape();
        if(i>=txt.length){clearInterval(timer);de.textContent=txt;Enigma.ding();}
      },34);
    }
    function maj(){
      if(amorce&&fin){
        const phrase=amorce.dataset.de+' '+fin.dataset.de;
        ecrire(phrase);fr.textContent=amorce.dataset.fr+' '+fin.dataset.fr;
      }else if(amorce){de.textContent=amorce.dataset.de+' \u2026';fr.textContent='';}
    }
    bk.addEventListener('click',e=>{
      const a=e.target.closest('.bk-a');
      if(a){
        amorce=a;fin=null;
        bk.querySelectorAll('.bk-a').forEach(b=>b.classList.toggle('choisi',b===a));
        bk.querySelectorAll('.bk-f').forEach(b=>{
          b.classList.toggle('dispo',b.dataset.g===a.dataset.g);
          b.classList.remove('choisi');
        });
        maj();return;
      }
      const f=e.target.closest('.bk-f.dispo');
      if(f){
        fin=f;
        bk.querySelectorAll('.bk-f').forEach(b=>b.classList.toggle('choisi',b===f));
        maj();return;
      }
      if(e.target.closest('#bk-sprechen')&&amorce&&fin){
        Stimme.dire(amorce.dataset.de+' '+fin.dataset.de);
      }
    });
  }
}catch(e){console.error('[sprach]',e);}})();

(function(){try{
  const st=document.querySelector('.stempel-header');
  let taps=[];
  if(st)st.addEventListener('click',function(){
    const t=Date.now();
    taps=taps.filter(function(x){return t-x<1600;});taps.push(t);
    Lyra.frappe();
    if(taps.length>=3){taps=[];Lyra.ding();location.hash='#geheim';}
  });
  /* la lyre : quatre cordes pincées 1->4 déclenchent le foudre */
  const FREQ={1:82.41,2:110.00,3:146.83,4:196.00};
  let suite=[],st2=0;
  document.addEventListener('click',function(e){
    const ch=e.target.closest('.chorde');if(!ch)return;
    const n=parseInt((ch.id||'').replace('chorde-',''),10);
    Lyra.pluck(FREQ[n]||220);
    ch.classList.remove('pincee');void ch.getBoundingClientRect();ch.classList.add('pincee');
    const t=Date.now();
    if(t-st2>4000)suite=[];
    st2=t;suite.push(n);
    const attendu=[1,2,3,4].slice(0,suite.length);
    if(suite.join()!==attendu.join()){suite=(n===1)?[1]:[];return;}
    if(suite.length===4){
      suite=[];
      const lyra=ch.closest('.lyra');if(!lyra)return;
      lyra.classList.add('keravnos');
      Lyra.tonnerre();
      if(!lyra.parentNode.querySelector('.keravnos-tampon')){
        const s=document.createElement('span');
        s.className='keravnos-tampon';
        s.textContent='\u00a1A LA CREM\u00c0!';
        lyra.parentNode.appendChild(s);
        setTimeout(function(){s.remove();},2400);
      }
      setTimeout(function(){lyra.classList.remove('keravnos');},2500);
    }
  });
}catch(e){console.error('[mystika]',e);}})();

/* ============ FRAPPE — la machine dactylographie chaque fiche ============ */
const Frappe=(function(){
  const REDUIT=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const PROFILS=[
    {cps:330,virgule:60,point:120},
    {cps:420,virgule:90,point:180},
    {cps:500,virgule:40,point:90}
  ];
  let enCours=null; /* {actes,raf,curseur,fiche} */

  function collecter(el,actes){
    for(const n of Array.from(el.childNodes)){
      if(n.nodeType===3){
        if(n.textContent.trim())actes.push({t:'txt',n,full:n.textContent});
      }else if(n.nodeType===1){
        if(n.matches('svg'))continue;
        if(n.matches('.achtung,.merksatz,.quiz-cadre,.stempel-inline')){
          actes.push({t:'bloc',n,clac:n.matches('.achtung,.quiz-cadre')});
        }else if(n.matches('table')){
          const cap=n.querySelector('caption');
          if(cap)collecter(cap,actes);
          n.querySelectorAll('tr').forEach(tr=>actes.push({t:'bloc',n:tr}));
        }else collecter(n,actes);
      }
    }
  }
  function toutReveler(e){
    if(!e)return;
    e.actes.forEach(a=>{
      if(a.t==='txt')a.n.textContent=a.full;
      else a.n.classList.remove('cache-frappe');
    });
    if(e.curseur)e.curseur.remove();
    if(e.raf)cancelAnimationFrame(e.raf);
    e.fiche.removeEventListener('pointerdown',e.skip);
  }
  function stop(){toutReveler(enCours);enCours=null;}

  function demarrer(fiche,seed){
    stop();
    const corps=fiche.querySelector('.corps-sec');
    if(!corps)return;
    const actes=[];collecter(corps,actes);
    if(!actes.length)return;
    if(REDUIT)return; /* tout reste visible */
    /* préparer : vider les textes, cacher les blocs */
    actes.forEach(a=>{
      if(a.t==='txt')a.n.textContent='';
      else a.n.classList.add('cache-frappe');
    });
    const curseur=document.createElement('span');curseur.className='curseur';
    const p=PROFILS[Math.abs(seed)%PROFILS.length];
    const e={actes,curseur,fiche,raf:0,skip:null};
    let i=0,pos=0,last=0,lastSon=0,budget=0;
    function pas(now){
      if(!last)last=now;
      budget+=Math.min(60,now-last)/1000*p.cps;last=now;
      while(budget>=1&&i<actes.length){
        const a=actes[i];
        if(a.t==='txt'){
          const take=Math.min(a.full.length-pos,Math.floor(budget));
          if(take>0){
            pos+=take;budget-=take;
            const ch=a.full[pos-1];
            if(ch==='.'||ch==='!'||ch==='?')budget-=p.point/1000*p.cps;
            else if(ch===','||ch===';'||ch===':')budget-=p.virgule/1000*p.cps;
            a.n.textContent=a.full.slice(0,pos);
            if(a.n.parentNode)a.n.parentNode.insertBefore(curseur,a.n.nextSibling);
          }
          if(pos>=a.full.length){i++;pos=0;}
        }else{
          a.n.classList.remove('cache-frappe');
          if(a.clac)Enigma.tick();
          budget-=10;i++;
        }
      }
      if(now-lastSon>85&&i<actes.length){Enigma.tape();lastSon=now;}
      if(i<actes.length){e.raf=requestAnimationFrame(pas);}
      else{curseur.remove();fiche.removeEventListener('pointerdown',e.skip);enCours=null;Enigma.ding();}
    }
    e.skip=function(){toutReveler(e);enCours=null;};
    fiche.addEventListener('pointerdown',e.skip,{once:true});
    enCours=e;
    e.raf=requestAnimationFrame(pas);
  }
  return{demarrer,stop};
})();

/* ============ ROUTEUR v3 — le deck de Karteikarten ============ */
(function(){try{
  const scene=document.getElementById('scene');
  const FICHES=Array.from(document.querySelectorAll('.fiche'));
  const IDS=FICHES.map(f=>f.id);
  const CONTENU=FICHES.filter(f=>f.dataset.par);
  const navbar=document.getElementById('navbar');
  const bPrev=navbar.querySelector('#nav-prev');
  const bHub=navbar.querySelector('#nav-hub');
  const bNext=navbar.querySelector('#nav-next');
  const colD=navbar.querySelector('#col-d');
  const colU=navbar.querySelector('#col-u');
  navbar.querySelector('#rtotal').textContent='\u2044'+CONTENU.length;

  /* colonnes des rotors : 0-9 + cran neutre */
  [colD,colU].forEach(col=>{
    col.innerHTML='';
    '0123456789\u00B7'.split('').forEach(ch=>{
      const s=document.createElement('span');
      s.textContent=ch;s.style.cssText='display:block;height:1.5em;line-height:1.5em;text-align:center';
      col.appendChild(s);
    });
  });
  function setRotor(col,n){col.style.transform='translateY(calc(-'+n+' * 1.5em))';}

  let courantId=null,pendingDir=null,demarre=false,wnAngle=0;
  const NAVIG=IDS.filter(x=>x!=='geheim');
  const idx=id=>IDS.indexOf(id);
  function cible(){
    const h=location.hash.slice(1);
    if(!h)return 'stele';
    return IDS.includes(h)?h:'pinakas';
  }
  function afficher(id,dir){
    const el=document.getElementById(id);if(!el)return;
    scene.dataset.dir=dir||'avant';
    Frappe.stop();
    FICHES.forEach(f=>f.classList.remove('actif'));
    el.classList.add('actif');el.scrollTop=0;
    navbar.classList.toggle('cache',id==='stele');
    const ci=CONTENU.indexOf(el);
    if(ci>-1){const n=ci+1;setRotor(colD,Math.floor(n/10));setRotor(colU,n%10);}
    else{setRotor(colD,10);setRotor(colU,10);}
    const i=NAVIG.indexOf(courantId==='geheim'?'agora':id);
    bPrev.disabled=(i<=0);
    bNext.disabled=(i>=NAVIG.length-1);
    if(demarre&&courantId!==id){Enigma.tick();wnAngle+=90;const wn=document.getElementById('ilios-nav-g');if(wn)wn.style.transform='rotate('+wnAngle+'deg)';}
    if(el.hasAttribute('data-nofrappe')){Frappe.stop();}else{Frappe.demarrer(el,Math.max(0,ci));}
    courantId=id;demarre=true;
  }
  function aller(id){
    if(id===courantId)return;
    pendingDir=(idx(id)>=idx(courantId))?'avant':'arriere';
    if(id==='stele'){
      history.pushState('','',location.pathname+location.search);
      afficher(id,pendingDir);pendingDir=null;
    }else{
      location.hash='#'+id;
    }
  }
  function next(){const i=NAVIG.indexOf(courantId);if(i>-1&&i<NAVIG.length-1)aller(NAVIG[i+1]);}
  function prev(){const i=NAVIG.indexOf(courantId);if(i>0)aller(NAVIG[i-1]);}

  bPrev.addEventListener('click',prev);
  bNext.addEventListener('click',next);
  bHub.addEventListener('click',()=>aller('agora'));
  const be=document.getElementById('btn-anavasi');
  if(be)be.addEventListener('click',()=>{Enigma.frappe();aller('agora');});
  const gr=document.getElementById('geheim-retour');
  if(gr)gr.addEventListener('click',()=>aller('agora'));

  /* balayage tactile */
  let tx=0,ty=0;
  scene.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
  scene.addEventListener('touchend',e=>{
    const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;
    if(Math.abs(dx)>60&&Math.abs(dy)<40){(dx<0)?next():prev();}
  },{passive:true});

  /* mute synchronisé (hub + quiz) */
  document.querySelectorAll('button.mute').forEach(b=>b.addEventListener('click',()=>{
    const m=Enigma.toggle();
    document.querySelectorAll('button.mute').forEach(x=>{
      x.textContent=m?'SFX : AUS':'SFX : AN';
      x.setAttribute('aria-pressed',String(m));
    });
    if(!m)Enigma.frappe();
  }));

  window.addEventListener('hashchange',()=>{
    const c=cible();
    const d=pendingDir||((idx(c)>=idx(courantId))?'avant':'arriere');
    pendingDir=null;afficher(c,d);
  });
  afficher(cible(),'avant');
}catch(e){document.documentElement.classList.add('nojs');console.error('[routeur]',e);}
})();

/* ============ PRÜFUNG — moteur branché sur la machine ============ */

const FRAGEN=[{"sit": "Il est 20h, vous avez faim, et le petit restaurant du coin affiche une belle « paella valenciana ».", "q": "Tu commandes ?", "c": ["Oui, parfait pour souper", "Non — la paella, c'est le midi", "Oui, mais sans riz"], "b": 1, "ex": "Plat du midi, toujours. Un restaurant qui pousse la paella le soir cuisine pour les touristes — et souvent au micro-ondes."}, {"sit": "Le serveur pose la paella. Ta voisine québécoise cherche le chorizo des yeux.", "q": "Dans une paella valenciana, le chorizo…", "c": ["Est indispensable", "Se demande à part", "Est un sacrilège documenté"], "b": 2, "ex": "Le canon tient en dix ingrédients : poulet, lapin, haricots, garrofó, tomate, paprika, safran, huile, riz, eau. Ni chorizo, ni fruits de mer."}, {"sit": "Au fond de la poêle, une croûte de riz doré accroche à la cuillère.", "q": "Tu fais quoi ?", "c": ["Tu la grattes : c'est le trésor", "Tu la laisses : c'est brûlé", "Tu demandes une réduction"], "b": 0, "ex": "C'est le socarrat — la partie la plus convoitée. On la gratte directement dans la poêle, et on complimente la maison."}, {"sit": "Sur le panneau : « Xàtiva ». Sur ton billet de train : « Játiva ».", "q": "Il se passe quoi ?", "c": ["Deux villes différentes", "La même ville, deux langues officielles", "Une faute d'impression"], "b": 1, "ex": "Valencien et castillan coexistent partout : Russafa/Ruzafa, València/Valencia. Ce n'est pas une erreur, c'est la ville."}, {"sit": "Janvier. Une carte affiche des « clòchinas » (moules locales) en vedette.", "q": "Tu en penses quoi ?", "c": ["Méfiance : leur saison, c'est mai-août", "Chouette, c'est la saison", "Les clòchinas n'existent pas"], "b": 0, "ex": "Les vraies clòchinas se pêchent de mai à août. Hors saison, ce sont des moules d'ailleurs déguisées en fierté locale."}, {"sit": "1er mars, 13h55, Plaza del Ayuntamiento. La foule se masse, des locaux entrouvrent la bouche.", "q": "Pourquoi la bouche entrouverte ?", "c": ["Pour crier plus fort", "C'est une prière fallera", "Pour équilibrer la pression des explosions"], "b": 2, "ex": "La mascletà approche : ~120 dB de rythme pyrotechnique. Bouche entrouverte = tympans protégés. Et bouchons d'oreilles dans la poche."}, {"sit": "Addition : 42 €. Le service était impeccable. Ta voisine sort sa calculette à 15 %.", "q": "Le pourboire espagnol…", "c": ["15 % obligatoire, comme au Québec", "Optionnel : on arrondit, 5-10 % si excellent", "Interdit par la loi"], "b": 1, "ex": "Le service est inclus. Arrondir suffit ; 5-10 % récompense un vrai bon moment. Personne ne courra après toi."}, {"sit": "Tu renverses ton verre sur un inconnu. Confuse, tu lances : « ¡Estoy embarazada! »", "q": "Tu viens de dire…", "c": ["« Je suis enceinte »", "« Je suis embarrassée »", "« Je suis désolée »"], "b": 0, "ex": "Le faux ami le plus célèbre de la langue. Pour la gêne : « ¡Qué vergüenza! » — et pour un rhume, evita « constipada »… qui veut dire enrhumée, justement."}, {"sit": "Un chauffeur te propose un « tour photo » des communes touchées par la DANA de 2024.", "q": "Ta réponse ?", "c": ["Pourquoi pas, c'est historique", "Oui, si c'est gratuit", "Non — lieux de deuil, pas d'attraction"], "b": 2, "ex": "Paiporta et ses voisines se reconstruisent dans le deuil. Le vrai geste utile : dépenser dans le centre, dont le tourisme finance la relance."}, {"sit": "Fin du repas depuis 20 minutes. L'addition ne vient toujours pas. Personne ne s'agite.", "q": "Le restaurant…", "c": ["T'a oubliée", "Te laisse la sobremesa : demande-la quand TU veux", "Offre le repas"], "b": 1, "ex": "Apporter l'addition sans qu'on la demande serait pousser dehors. « La cuenta, por favor » — avec le geste de signer dans l'air, ça marche aussi."}, {"sit": "Ton vol atterrit. Tu ouvres Uber : aucun véhicule disponible, nulle part.", "q": "Que se passe-t-il ?", "c": ["Grève surprise", "Ton téléphone est cassé", "Uber n'opère pas à Valence : Cabify/Bolt/métro"], "b": 2, "ex": "Pas d'Uber ici. Cabify est le réflexe local, le métro (lignes 3/5) fait le trajet en ~20 min, et le taxi est à tarif encadré."}, {"sit": "Grosse chaleur. Tu commandes une horchata et réclames « beaucoup de glaçons, por favor ».", "q": "L'horchatero te regarde…", "c": ["Avec une douleur polie : les glaçons la noient", "Avec gratitude", "Sans réaction"], "b": 0, "ex": "L'horchata se sert déjà glacée, souvent mi-granizada. Les glaçons diluent le lait de chufa — demande-la « bien fría », et trempe un farton."}];


(function(){try{
  const zone=document.getElementById('quiz-zone');
  const prog=document.getElementById('quiz-prog');
  if(!zone||!prog)return;
  const rotAt=document.getElementById('rota-t');
  const rotBt=document.getElementById('rotb-t');
  const presse=document.querySelector('#manteion .presse');
  let idx=0,score=0,repondu=false,wAngle=0;

  function setRotA(){if(rotAt)rotAt.textContent=String(idx+1).padStart(2,'0');}
  function setRotB(){if(rotBt)rotBt.textContent=String(score).padStart(2,'0');}
  function tourner(){
    wAngle+=90;
    const w=document.getElementById('meule');
    if(w)w.style.transform='rotate('+wAngle+'deg)';
  }
  function setAmfores(){
    for(let k=1;k<=3;k++){
      const part=Math.max(0,Math.min(1,(score-(k-1)*4)/4));
      const v=document.getElementById('amfora-'+k+'-vul');
      if(v)v.style.transform='scaleY('+part+')';
    }
  }
  function grincer(){
    if(!presse)return;
    presse.classList.add('frein-on');
    setTimeout(function(){presse.classList.remove('frein-on');},560);
  }

  function rendre(){
    repondu=false;
    const f=FRAGEN[idx];
    prog.textContent='PREGUNTA '+(idx+1)+'/12';
    setRotA();
    zone.innerHTML='';
    const sit=document.createElement('p');sit.className='quiz-situation';sit.textContent='Situaci\u00f3n \u2014 '+f.sit;
    const q=document.createElement('p');q.className='quiz-q';q.textContent=f.q;
    const box=document.createElement('div');box.className='quiz-choix';
    f.c.forEach(function(txt,i){
      const b=document.createElement('button');b.type='button';b.className='choix';b.textContent=txt;
      b.addEventListener('click',function(){repondre(i,b,box,f,sit,q);});
      box.appendChild(b);
    });
    zone.append(sit,q,box);
  }

  function repondre(i,btn,box,f,sit,q){
    if(repondu)return;repondu=true;
    if(sit)sit.remove();if(q)q.remove();
    const bonne=(i===f.b);
    if(bonne)score++;
    box.querySelectorAll('button').forEach(function(b,j){
      b.disabled=true;
      if(j===f.b)b.dataset.etat='bonne';
      else if(j===i)b.dataset.etat='mauvaise';
    });
    if(bonne){Lyra.lampe();tourner();setRotB();setAmfores();}
    else{Lyra.kurzschluss();grincer();}
    const rappel=(!bonne)?'<p class="quiz-bonne">\u2192 '+f.c[f.b]+'</p>':'';
    box.remove();
    const verd=document.createElement('div');verd.className='quiz-verdict';
    const st=document.createElement('span');
    st.className='grand-stempel anime '+(bonne?'ok':'non');
    st.textContent=bonne?'\u00a1FET!':'QUEMADO';
    verd.appendChild(st);
    const ex=document.createElement('div');ex.className='quiz-explication';
    ex.innerHTML='<span class="amtston">El veredicto de la noria</span>'+rappel+f.ex;
    const w=document.createElement('button');w.type='button';w.className='weiter';
    w.textContent=(idx<FRAGEN.length-1)?'SIGUIENTE \u2192':'VEREDICTO \u2192';
    w.addEventListener('click',function(){Lyra.rotor();idx++;(idx<FRAGEN.length)?rendre():bilan();});
    zone.append(verd,ex,w);
  }

  function bilan(){
    prog.textContent='LA PAELLA EST\u00c1 SERVIDA';
    let classe,tampon,texte;
    if(score===12){classe='ok';tampon='MATR\u00cdCULA DE HONOR';
      texte="Douze olives press\u00e9es, douze filets d'huile d'or \u2014 la Pythie elle-m\u00eame te c\u00e8derait son tr\u00e9pied. Jeanne, tu lis la Gr\u00e8ce comme un oracle.";}
    else if(score>=9){classe='ok';tampon='NOTABLE';
      texte="Le pressoir a bien coul\u00e9. Tu d\u00e9joues la mo\u00fatza, tu dis \u00ab\u00a0ne\u00a0\u00bb pour oui, tu gardes une journ\u00e9e tampon avant ton vol \u2014 kal\u00f3 tax\u00eddi.";}
    else if(score>=6){classe='ok';tampon='BIEN';
      texte="Admise. Le Manteion conseille une relecture des \u00a7 avant d'affronter un ferry sous melt\u00e9mi.";}
    else{classe='non';tampon='SUSPENSO';
      texte="La meule a plus grinc\u00e9 qu'elle n'a press\u00e9. L'oracle reste muet \u2014 relis la St\u00e8le, puis reviens presser l'olive.";}
    zone.innerHTML='<div class="bilan">'
      +'<span class="score">'+score+'/12</span>'
      +'<span class="grand-stempel '+classe+'" style="position:static;animation:claquer 170ms steps(4,end) both">'+tampon+'</span>'
      +'<p class="verdict-texte">'+texte+'</p>'
      +'</div>';
    const w=document.createElement('button');w.type='button';w.className='weiter';w.textContent='OTRA VEZ (recommencer)';
    w.addEventListener('click',function(){Lyra.rotor();idx=0;score=0;wAngle=0;
      const wk=document.getElementById('meule');if(wk)wk.style.transform='rotate(0deg)';
      setRotB();setAmfores();rendre();});
    zone.querySelector('.bilan').appendChild(w);
    if(score>=9){
      Lyra.ding();
      if(presse&&score===12){presse.classList.remove('storm');void presse.getBoundingClientRect();presse.classList.add('storm');setTimeout(function(){presse.classList.remove('storm');},2500);}
      [0,200,400].forEach(function(dt){setTimeout(function(){Lyra.lampe();},dt);});
    }else if(score>=6){Lyra.ding();}
    else{Lyra.kurzschluss();grincer();}
  }

  rendre();
}catch(e){console.error('[manteion]',e);}
})();

const LEXICON=[{"nl": "Hola", "tts": "Hola", "fr": "salut / bonjour passe-partout", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Buenos días", "tts": "Buenos días", "fr": "bonjour (le matin)", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Buenas tardes", "tts": "Buenas tardes", "fr": "bonjour / bonsoir (après ~14h)", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Buenas noches", "tts": "Buenas noches", "fr": "bonsoir / bonne nuit", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Adiós", "tts": "Adiós", "fr": "au revoir", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Hasta luego", "tts": "Hasta luego", "fr": "à plus tard", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Gracias", "tts": "Gracias", "fr": "merci", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Por favor", "tts": "Por favor", "fr": "s’il vous plaît", "cat": "Le nécessaire absolu", "piege": false}, {"nl": "Sí", "tts": "Sí", "fr": "oui", "cat": "Quatre mots qui décident de tout — et deux mines", "piege": false}, {"nl": "No", "tts": "No", "fr": "non", "cat": "Quatre mots qui décident de tout — et deux mines", "piege": false}, {"nl": "Vale", "tts": "Vale", "fr": "d’accord / OK (le mot le plus dit d’Espagne)", "cat": "Quatre mots qui décident de tout — et deux mines", "piege": false}, {"nl": "Perdón", "tts": "Perdón", "fr": "pardon / excusez-moi", "cat": "Quatre mots qui décident de tout — et deux mines", "piege": false}, {"nl": "No entiendo", "tts": "No entiendo", "fr": "je ne comprends pas", "cat": "Quatre mots qui décident de tout — et deux mines", "piege": false}, {"nl": "Estoy constipada", "tts": "Estoy constipada", "fr": "je suis enrhumée — piège : PAS constipée !", "cat": "Quatre mots qui décident de tout — et deux mines", "piege": true}, {"nl": "Embarazada", "tts": "Embarazada", "fr": "enceinte — piège : PAS embarrassée !", "cat": "Quatre mots qui décident de tout — et deux mines", "piege": true}, {"nl": "Una mesa para dos", "tts": "Una mesa para dos", "fr": "une table pour deux", "cat": "De la table à l’addition", "piege": false}, {"nl": "La carta, por favor", "tts": "La carta, por favor", "fr": "la carte, s’il vous plaît", "cat": "De la table à l’addition", "piege": false}, {"nl": "¿Qué me recomienda?", "tts": "¿Qué me recomienda?", "fr": "que me recommandez-vous ?", "cat": "De la table à l’addition", "piege": false}, {"nl": "Para beber…", "tts": "Para beber…", "fr": "comme boisson…", "cat": "De la table à l’addition", "piege": false}, {"nl": "¡Buenísimo!", "tts": "¡Buenísimo!", "fr": "délicieux !", "cat": "De la table à l’addition", "piege": false}, {"nl": "La cuenta, por favor", "tts": "La cuenta, por favor", "fr": "l’addition (elle ne vient jamais seule)", "cat": "De la table à l’addition", "piege": false}, {"nl": "¿Se puede pagar con tarjeta?", "tts": "¿Se puede pagar con tarjeta?", "fr": "on peut payer par carte ?", "cat": "De la table à l’addition", "piege": false}, {"nl": "El menú del día", "tts": "El menú del día", "fr": "le menu du jour (midi, ~12–15 €)", "cat": "De la table à l’addition", "piege": false}, {"nl": "La paella", "tts": "La paella", "fr": "LE plat — poulet & lapin, midi seulement", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "El socarrat", "tts": "El socarrat", "fr": "la croûte d’or du fond — le trésor", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "Horchata y fartons", "tts": "Horchata y fartons", "fr": "lait de souchet glacé + brioches à tremper", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "El esgarraet", "tts": "El esgarraet", "fr": "poivrons rôtis + morue — l’entrée reine", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "All i pebre", "tts": "All i pebre", "fr": "ragoût d’anguille de l’Albufera", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "Las clóchinas", "tts": "Las clóchinas", "fr": "petites moules locales — mai à août seulement", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "El esmorzaret", "tts": "El esmorzaret", "fr": "le casse-croûte sacré de 10h30", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "Agua de Valencia", "tts": "Agua de Valencia", "fr": "cocktail orange-cava-gin-vodka — traître", "cat": "Ce qui se mange ici, et nulle part ailleurs", "piege": false}, {"nl": "¿Dónde está…?", "tts": "¿Dónde está…?", "fr": "où est… ?", "cat": "La rue, l’arrêt, le billet", "piege": false}, {"nl": "La parada", "tts": "La parada", "fr": "l’arrêt (bus, tram)", "cat": "La rue, l’arrêt, le billet", "piege": false}, {"nl": "Un billete", "tts": "Un billete", "fr": "un billet", "cat": "La rue, l’arrêt, le billet", "piege": false}, {"nl": "La estación", "tts": "La estación", "fr": "la gare / la station", "cat": "La rue, l’arrêt, le billet", "piege": false}, {"nl": "A la derecha", "tts": "A la derecha", "fr": "à droite", "cat": "La rue, l’arrêt, le billet", "piege": false}, {"nl": "A la izquierda", "tts": "A la izquierda", "fr": "à gauche", "cat": "La rue, l’arrêt, le billet", "piege": false}, {"nl": "Todo recto", "tts": "Todo recto", "fr": "tout droit", "cat": "La rue, l’arrêt, le billet", "piege": false}, {"nl": "Uno, dos, tres", "tts": "Uno, dos, tres", "fr": "un, deux, trois", "cat": "Assez pour payer et prendre rendez-vous", "piege": false}, {"nl": "Cuatro, cinco, seis", "tts": "Cuatro, cinco, seis", "fr": "quatre, cinq, six", "cat": "Assez pour payer et prendre rendez-vous", "piege": false}, {"nl": "Siete, ocho, nueve", "tts": "Siete, ocho, nueve", "fr": "sept, huit, neuf", "cat": "Assez pour payer et prendre rendez-vous", "piege": false}, {"nl": "Diez, veinte, cien", "tts": "Diez, veinte, cien", "fr": "dix, vingt, cent", "cat": "Assez pour payer et prendre rendez-vous", "piege": false}, {"nl": "¿A qué hora?", "tts": "¿A qué hora?", "fr": "à quelle heure ?", "cat": "Assez pour payer et prendre rendez-vous", "piege": false}, {"nl": "Son las dos y media", "tts": "Son las dos y media", "fr": "il est deux heures et demie", "cat": "Assez pour payer et prendre rendez-vous", "piege": false}, {"nl": "¡Socorro!", "tts": "¡Socorro!", "fr": "au secours !", "cat": "Les mots qu’on espère ne jamais dire", "piege": false}, {"nl": "La farmacia", "tts": "La farmacia", "fr": "la pharmacie (croix verte)", "cat": "Les mots qu’on espère ne jamais dire", "piege": false}, {"nl": "El médico", "tts": "El médico", "fr": "le médecin", "cat": "Les mots qu’on espère ne jamais dire", "piege": false}, {"nl": "El hospital", "tts": "El hospital", "fr": "l’hôpital", "cat": "Les mots qu’on espère ne jamais dire", "piege": false}, {"nl": "La policía", "tts": "La policía", "fr": "la police", "cat": "Les mots qu’on espère ne jamais dire", "piege": false}, {"nl": "Me duele aquí", "tts": "Me duele aquí", "fr": "j’ai mal ici", "cat": "Les mots qu’on espère ne jamais dire", "piege": false}, {"nl": "¿Habla inglés?", "tts": "¿Habla inglés?", "fr": "parlez-vous anglais ?", "cat": "Les mots qu’on espère ne jamais dire", "piege": false}];

(function(){try{
  if(typeof LEXICON==='undefined'||!LEXICON.length)return;
  var zone=document.getElementById('ex-zone');
  var prog=document.getElementById('ex-prog');
  if(!zone||!prog)return;
  var muteBtn=document.getElementById('ex-mute');
  var NB=14;
  var idx=0,score=0,repondu=false,tirage=[];

  function norm(s){
    s=(s||'').toLowerCase();
    s=s.replace(/[\u00e0\u00e2\u00e4]/g,'a').replace(/[\u00e9\u00e8\u00ea\u00eb]/g,'e')
       .replace(/[\u00ef\u00ee]/g,'i').replace(/[\u00f4\u00f6]/g,'o').replace(/[\u00f9\u00fb\u00fc]/g,'u').replace(/\u00e7/g,'c');
    s=s.replace(/[.!?;,'\u2019\u2018\"]/g,' ');
    s=s.replace(/\s+/g,' ').trim();
    return s;
  }
  // variantes acceptables d'un sens : coupe sur / « ou » « et » virgule ; retire parenthèses et glose après tiret cadratin
  function variantes(fr){
    var base=fr.replace(/\([^)]*\)/g,' ');
    base=base.split(/\u2014/)[0];
    var parts=base.split(/\s*\/\s*|\bou\b|\bet\b|,/);
    var out=[];
    parts.forEach(function(p){var n=norm(p);if(n&&n.length>1)out.push(n);});
    return out.length?out:[norm(base)];
  }

  function melange(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}
  function bati(){
    var pool=melange(LEXICON.slice());
    var choisis=pool.slice(0,Math.min(NB,pool.length));
    tirage=choisis.map(function(item,i){
      var court=!item.piege && variantes(item.fr).some(function(v){return v.split(' ').length<=2;});
      var mode=(i%2===1 && court)?'court':'qcm';
      return {item:item,mode:mode};
    });
  }

  // audio : réutilise Lyra si présent, silencieux sinon
  function bip(ok){try{if(window.Lyra){ok?Lyra.lampe():Lyra.kurzschluss();}}catch(e){}}
  function clic(){try{if(window.Lyra)Lyra.rotor();}catch(e){}}
  function sceau(){try{if(window.Lyra)Lyra.frappe();}catch(e){}}

  function poserCachet(n){
    var c=document.getElementById('cachet-'+n);
    if(c)c.classList.add('appose');
  }

  function rendre(){
    repondu=false;
    var t=tirage[idx],it=t.item;
    prog.textContent='PREGUNTA '+(idx+1)+'/'+tirage.length;
    zone.innerHTML='';
    var tag=document.createElement('p');tag.className='ex-mode';
    tag.textContent=(t.mode==='court')?'Escribe el sentido':'Elige el sentido';
    var q=document.createElement('p');q.className='ex-mot';
    q.innerHTML='<span lang="el">'+it.nl+'</span>';
    var say=document.createElement('button');say.type='button';say.className='ex-dire';
    say.setAttribute('data-de',it.tts||it.nl);say.setAttribute('aria-label','Escucha');
    say.innerHTML='\u25c4';
    q.appendChild(say);
    zone.append(tag,q);

    if(t.mode==='qcm'){
      var opts=[it.fr];
      var autres=melange(LEXICON.filter(function(x){return x.fr!==it.fr;}));
      for(var k=0;k<autres.length&&opts.length<4;k++){opts.push(autres[k].fr);}
      opts=melange(opts);
      var box=document.createElement('div');box.className='ex-choix';
      opts.forEach(function(txt){
        var b=document.createElement('button');b.type='button';b.className='choix';
        b.textContent=txt;
        b.addEventListener('click',function(){jugerQcm(txt===it.fr,it.fr,box,b);});
        box.appendChild(b);
      });
      zone.appendChild(box);
    }else{
      var wrap=document.createElement('div');wrap.className='ex-court';
      var inp=document.createElement('input');inp.type='text';inp.className='ex-input';
      inp.setAttribute('autocomplete','off');inp.setAttribute('autocapitalize','off');
      inp.setAttribute('spellcheck','false');inp.setAttribute('placeholder','tape le sens en fran\u00e7ais\u2026');
      inp.setAttribute('lang','fr');
      var val=document.createElement('button');val.type='button';val.className='ex-valider';val.textContent='COMPROBAR';
      function go(){jugerCourt(inp.value,it,wrap,inp);}
      val.addEventListener('click',go);
      inp.addEventListener('keydown',function(e){if(e.key==='Enter')go();});
      wrap.append(inp,val);zone.appendChild(wrap);
      setTimeout(function(){inp.focus();},60);
    }
    parler(say);
  }

  function verdictNoeud(ok){
    var v=document.createElement('span');
    v.className='grand-stempel anime '+(ok?'ok':'non');
    v.textContent=ok?'\u00a1FET!':'QUEMADO';
    return v;
  }
  function suiteBouton(){
    var w=document.createElement('button');w.type='button';w.className='weiter';
    w.textContent=(idx<tirage.length-1)?'SIGUIENTE \u2192':'VEREDICTO \u2192';
    w.addEventListener('click',function(){clic();idx++;(idx<tirage.length)?rendre():bilan();});
    return w;
  }

  function jugerQcm(ok,bonne,box,btn){
    if(repondu)return;repondu=true;
    box.querySelectorAll('button').forEach(function(b){
      b.disabled=true;
      if(b.textContent===bonne)b.dataset.etat='bonne';
      else if(b===btn&&!ok)b.dataset.etat='mauvaise';
    });
    finir(ok,bonne);
  }
  function jugerCourt(saisie,it,wrap,inp){
    if(repondu)return;repondu=true;
    var v=variantes(it.fr),n=norm(saisie);
    var ok=v.some(function(x){return x===n||(n.length>2&&(x.indexOf(n)===0||n.indexOf(x)===0));});
    inp.disabled=true;inp.classList.add(ok?'bon':'faux');
    wrap.querySelector('.ex-valider').disabled=true;
    finir(ok,it.fr);
  }
  function finir(ok,bonne){
    if(ok){score++;bip(true);sceau();poserCachet(score-1);}
    else{bip(false);}
    var wrapV=document.createElement('div');wrapV.className='ex-verdict';
    wrapV.appendChild(verdictNoeud(ok));
    if(!ok){
      var r=document.createElement('p');r.className='quiz-bonne';
      r.innerHTML='\u2192 '+bonne;wrapV.appendChild(r);
    }
    zone.appendChild(wrapV);
    zone.appendChild(suiteBouton());
  }

  function bilan(){
    prog.textContent='EXAMEN TERMINADO';
    var classe,tampon,texte;
    var p=Math.round(score/tirage.length*100);
    if(score===tirage.length){classe='ok';tampon='MATR\u00cdCULA DE HONOR';
      texte='Couronne compl\u00e8te, pas une feuille manquante. Jeanne, tu portes le laurier \u2014 tu parles le pays.';}
    else if(p>=75){classe='ok';tampon='NOTABLE';
      texte='Laurier accord\u00e9. Tu salues, tu remercies, tu d\u00e9joues le pi\u00e8ge du \u00ab ne \u00bb \u2014 \u00f3la kal\u00e1.';}
    else if(p>=50){classe='ok';tampon='BIEN';
      texte='Admise. Repasse le Gloss\u00e1ri une fois et les mots manquants se logeront vite.';}
    else{classe='non';tampon='SUSPENSO';
      texte='La couronne reste clairsem\u00e9e. Relis le Gloss\u00e1ri \u2014 \u00e9coute chaque \u25c4, puis reviens tresser tes feuilles.';}
    zone.innerHTML='<div class="bilan">'
      +'<span class="score">'+score+'/'+tirage.length+'</span>'
      +'<span class="grand-stempel '+classe+'" style="position:static;animation:claquer 170ms steps(4,end) both">'+tampon+'</span>'
      +'<p class="verdict-texte">'+texte+'</p></div>';
    var again=document.createElement('button');again.type='button';again.className='weiter';
    again.textContent='OTRA VEZ (recommencer)';
    again.addEventListener('click',function(){clic();reset();});
    zone.querySelector('.bilan').appendChild(again);
    if(p>=50){try{if(window.Lyra)Lyra.ding();}catch(e){}}
    else{bip(false);}
  }

  function reset(){
    idx=0;score=0;
    for(var i=0;i<NB;i++){var c=document.getElementById('cachet-'+i);if(c)c.classList.remove('appose');}
    bati();rendre();
  }

  function parler(btn){
    if(!btn)return;
    btn.addEventListener('click',function(){
      try{
        if(!('speechSynthesis'in window))return;
        var u=new SpeechSynthesisUtterance(btn.getAttribute('data-de'));
        u.lang='el-GR';u.rate=0.86;
        speechSynthesis.cancel();speechSynthesis.speak(u);
        btn.classList.add('parle');setTimeout(function(){btn.classList.remove('parle');},700);
      }catch(e){}
    });
  }
  if(muteBtn){muteBtn.addEventListener('click',function(){
    try{var m=window.Lyra&&Lyra.toggle?Lyra.toggle():false;
      muteBtn.textContent='SFX : '+(m?'NO':'S\u00cd');muteBtn.setAttribute('aria-pressed',m?'true':'false');}catch(e){}
  });}

  reset();
}catch(e){console.error('[glossikos-agon]',e);}
})();

