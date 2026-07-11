
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
