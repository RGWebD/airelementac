(()=>{
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,HOV=matchMedia('(hover:hover)').matches;
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const root=document.documentElement;root.classList.remove('no-js');
// split headings into words
$$('.split').forEach(h=>{let k=0;const walk=n=>{[...n.childNodes].forEach(c=>{if(c.nodeType===3){const parts=c.textContent.split(/(\s+)/);const f=document.createDocumentFragment();parts.forEach(p=>{if(!p)return;if(/^\s+$/.test(p)){f.appendChild(document.createTextNode(p));return}const w=document.createElement('span');w.className='w';const i=document.createElement('span');i.textContent=p;i.style.setProperty('--k',k++);w.appendChild(i);f.appendChild(w)});c.replaceWith(f)}else if(c.nodeType===1)walk(c)})};walk(h)});
// mode (cool / heat)
const dial=$('.dial'),dn=$('.d-n'),dm=$('.d-mode');const SET={cool:70,heat:76};let cur=null,auto=true;
function tweenTemp(to){if(!dn)return;const from=+dn.textContent||72;if(RM){dn.textContent=to;return}const t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/900),e=1-Math.pow(1-p,3);dn.textContent=Math.round(from+(to-from)*e);if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}
function setMode(m,save){root.dataset.mode=m;if(save){try{localStorage.setItem('ae-mode',m)}catch(e){}}
  $$('[data-set]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.set===m));
  if(dial){const t=SET[m];dial.style.setProperty('--dv',(75*(t-60)/30).toFixed(1));dm.textContent=m==='cool'?'Cooling':'Heating';tweenTemp(t)}cur=m}
let stored=null;try{stored=localStorage.getItem('ae-mode')}catch(e){}
setMode(stored||'cool',false);
$$('[data-set]').forEach(b=>b.addEventListener('click',()=>{auto=false;setMode(b.dataset.set,true)}));
// loader
const ld=$('.loader');const ready=()=>{document.body.classList.add('ready');
  if(dial&&!RM&&!stored){setTimeout(()=>{if(auto)setMode('heat')},3000);setTimeout(()=>{if(auto)setMode('cool')},6400)}};
if(ld){let seen=false;try{seen=sessionStorage.getItem('ae-intro')}catch(e){}
  if(RM||seen){ld.remove();ready()}else{try{sessionStorage.setItem('ae-intro','1')}catch(e){}
    const n=$('.ld-n',ld),t0=performance.now();const f=t=>{const p=Math.min(1,(t-t0)/1200);n.textContent=Math.round(88-16*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f);
    setTimeout(()=>{ld.classList.add('done');ready();setTimeout(()=>ld.remove(),1000)},1450)}}else ready();
// nav, progress, mobile bar
const nav=$('.nav'),prog=$('.prog'),mbar=$('.mbar');
const onS=()=>{const y=scrollY,h=root.scrollHeight-innerHeight;nav&&nav.classList.toggle('solid',y>30);if(prog)prog.style.transform=`scaleX(${h>0?Math.min(1,y/h):0})`;if(mbar)mbar.classList.toggle('show',y>innerHeight*.45)};
addEventListener('scroll',onS,{passive:true});onS();
const bg=$('.burger'),mm=$('.mmenu');
if(bg&&mm){const t=o=>{bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu');mm.classList.toggle('open',o);mm.setAttribute('aria-hidden',!o);document.body.style.overflow=o?'hidden':''};
  bg.addEventListener('click',()=>t(bg.getAttribute('aria-expanded')!=='true'));$$('a',mm).forEach(a=>a.addEventListener('click',()=>t(false)));addEventListener('keydown',e=>{if(e.key==='Escape')t(false)})}
// demo pill
const pill=$('.demo');if(pill){try{if(sessionStorage.getItem('ae-pill'))pill.classList.add('gone')}catch(e){}
  $('button',pill).addEventListener('click',()=>{pill.classList.add('gone');try{sessionStorage.setItem('ae-pill','1')}catch(e){}})}
// reveals + counters
function count(el){const to=+el.dataset.count,dec=+(el.dataset.dec||0);if(RM){el.textContent=to.toFixed(dec);return}
  const t0=performance.now(),d=1600;const f=t=>{const p=Math.min(1,(t-t0)/d),e=1-Math.pow(1-p,3);el.textContent=(to*e).toFixed(dec);if(p<1)requestAnimationFrame(f);else el.textContent=to.toFixed(dec)};requestAnimationFrame(f)}
const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const el=e.target;const grp=el.parentElement&&el.parentElement.matches('.why-g,.svc-g')?[...el.parentElement.children]:[el];grp.forEach(x=>{x.classList.add('in');io.unobserve(x);$$('.lv',x).forEach(l=>l.classList.add('in'))});
  $$('[data-count]',el).forEach(count)}),{threshold:.15,rootMargin:'0px 0px -5% 0px'});
$$('.rv,.split,.lv').forEach(el=>io.observe(el));
// timeline
const tl=$('.tl');if(tl&&!RM){const line=$('.tl-line i',tl);const u=()=>{const r=tl.getBoundingClientRect();const p=Math.min(1,Math.max(0,(innerHeight*.8-r.top)/(r.height*.9)));line.style.setProperty('--t',p.toFixed(3))};addEventListener('scroll',u,{passive:true});u()}
// compare slider
$$('.ba').forEach(ba=>{const r=$('input',ba);const set=v=>{ba.style.setProperty('--p',v+'%');r.value=v;r.setAttribute('aria-valuetext',Math.round(v)+'% blueprint shown')};
  r.addEventListener('input',()=>set(+r.value));let demo=!RM;['pointerdown','keydown','touchstart'].forEach(ev=>ba.addEventListener(ev,()=>demo=false,{passive:true}));
  if(demo){const o=new IntersectionObserver(es=>{if(es[0].isIntersecting){o.disconnect();const t0=performance.now();const f=t=>{if(!demo)return;const p=Math.min(1,(t-t0)/2800);set(50+38*Math.sin(p*2*Math.PI));if(p<1)requestAnimationFrame(f);else set(50)};requestAnimationFrame(f)}},{threshold:.5});o.observe(ba)}});
// tilt + magnetic
if(!RM&&HOV){$$('.tilt').forEach(c=>{c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(900px) rotateY(${x*7}deg) rotateX(${-y*7}deg) translateY(-4px)`});c.addEventListener('pointerleave',()=>c.style.transform='')});
  $$('.mag').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.16}px,${(e.clientY-r.top-r.height/2)*.24}px)`});b.addEventListener('pointerleave',()=>b.style.transform='')})}
// open/closed (8 AM–10 PM daily, America/New_York)
(()=>{const now=new Date(new Date().toLocaleString('en-US',{timeZone:'America/New_York'}));const m=now.getHours()*60+now.getMinutes(),O=480,C=1320;
  const y=now.getFullYear(),nov1=new Date(y,10,1).getDay(),thx=1+((4-nov1+7)%7)+21;const hol=now.getMonth()===10&&(now.getDate()===thx||now.getDate()===thx+1);
  let txt,open=false;if(m>=O&&m<C){open=true;txt='Open now · until 10 PM'}else if(m<O)txt='Closed · opens 8 AM today';else txt='Closed · opens 8 AM tomorrow';
  if(hol)txt+=' · holiday hours may differ';
  $$('[data-live]').forEach(el=>{el.classList.add(open?'open':'closed');$('.t',el).textContent=txt});
  const keys=['su','mo','tu','we','th','fr','sa'];const tr=$(`.hours tr[data-d="${keys[now.getDay()]}"]`);if(tr)tr.classList.add('today')})();
// reviews carousel
$$('.rc').forEach(rc=>{const tr=$('.rc-tr',rc),sl=$$('.rc-s',rc),dots=$('.rc-dots',rc);let i=0,tm=null,hold=false;
  sl.forEach((s,k)=>{const b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Show review '+(k+1));b.addEventListener('click',()=>go(k));dots.appendChild(b)});
  const go=k=>{i=(k+sl.length)%sl.length;tr.style.transform=`translateX(${-100*i}%)`;sl.forEach((s,j)=>{s.setAttribute('aria-hidden',j!==i);s.inert=j!==i});$$('button',dots).forEach((b,j)=>b.setAttribute('aria-current',j===i))};
  $('.rc-p',rc).addEventListener('click',()=>go(i-1));$('.rc-n',rc).addEventListener('click',()=>go(i+1));
  ['mouseenter','focusin'].forEach(ev=>rc.addEventListener(ev,()=>hold=true));['mouseleave','focusout'].forEach(ev=>rc.addEventListener(ev,()=>hold=false));
  let sx=null;rc.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});rc.addEventListener('touchend',e=>{if(sx===null)return;const dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>45)go(i+(dx<0?1:-1));sx=null});
  go(0);if(!RM)tm=setInterval(()=>{if(!hold&&!document.hidden)go(i+1)},6500)});
// gallery + lightbox
const gal=$('.gal'),lb=$('.lbx');
if(gal&&lb){const btns=$$('.filters button');btns.forEach(b=>b.addEventListener('click',()=>{btns.forEach(x=>x.setAttribute('aria-pressed',x===b));const f=b.dataset.f;$$('.gi',gal).forEach(g=>g.classList.toggle('hide',f!=='all'&&!g.dataset.tags.split(' ').includes(f)))}));
  const im=$('img',lb),cap=$('figcaption',lb);let items=[],i=0,last=null;
  const show=()=>{const g=items[i],a=$('img',g).alt;im.src=g.dataset.full;im.alt=a;cap.textContent=`${i+1} / ${items.length} — ${a}`};
  const open=g=>{items=$$('.gi:not(.hide)',gal);i=items.indexOf(g);last=g;show();lb.classList.add('open');document.body.style.overflow='hidden';$('.lbx-x',lb).focus()};
  const close=()=>{lb.classList.remove('open');document.body.style.overflow='';im.removeAttribute('src');last&&last.focus()};
  $$('.gi',gal).forEach(g=>g.addEventListener('click',()=>open(g)));
  $('.lbx-x',lb).addEventListener('click',close);$('.lbx-p',lb).addEventListener('click',()=>{i=(i-1+items.length)%items.length;show()});$('.lbx-n',lb).addEventListener('click',()=>{i=(i+1)%items.length;show()});
  lb.addEventListener('click',e=>{if(e.target===lb)close()});
  addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='Escape')close();if(e.key==='ArrowRight')$('.lbx-n',lb).click();if(e.key==='ArrowLeft')$('.lbx-p',lb).click();
    if(e.key==='Tab'){const f=$$('button',lb);const a=f.indexOf(document.activeElement);e.preventDefault();f[(a+(e.shiftKey?-1:1)+f.length)%f.length].focus()}});
  let sx=null;lb.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});lb.addEventListener('touchend',e=>{if(sx===null)return;const dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)$(dx<0?'.lbx-n':'.lbx-p',lb).click();sx=null})}
// service request -> SMS
const qf=$('.qf');if(qf){qf.addEventListener('submit',e=>{e.preventDefault();const v=n=>(qf.elements[n]&&qf.elements[n].value||'').trim();
  const body=`Hi Air Element, I'd like to request service.\nName: ${v('name')}\nPhone: ${v('phone')}\nService: ${v('service')}\nArea: ${v('area')}\nDetails: ${v('details')}`;
  location.href=`sms:+19044403389?&body=${encodeURIComponent(body)}`})}
})();
