#!/usr/bin/env python3
"""Air Element AC & Heating LLC — demo site generator (RGWebD). Writes static site to ./docs"""
import json, os, shutil, html, datetime, sys
from PIL import Image
ROOT=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(ROOT,'docs')
BASE=os.environ.get('BASE','https://rgwebd.github.io/airelementac/')
E=lambda s: html.escape(str(s),quote=True)
YEAR=datetime.date.today().year
BOOK='https://book.housecallpro.com/book/Air-Element-AC-and-Heating-LLC/9239cfc3335f4d33ab65185a114bcb70?v2=true&lead_source=google&merchant_id=20476f79-8d79-4615-bec2-31c5933843bd'
MAPS='https://www.google.com/maps/place/Air+Element+Ac+and+Heating+LLC/@30.1834703,-81.5734384,17z/data=!4m6!3m5!1s0x22697d220e0d5129:0xb6f4c285adef97dc!8m2!3d30.1834703!4d-81.5734384!16s%2Fg%2F11l32k4dxx'
BBB='https://www.bbb.org/us/fl/jacksonville/profile/air-conditioning-contractor/air-element-ac-and-heating-llc-0403-236020389'
YELP='https://www.yelp.com/biz/air-element-ac-and-heating-jacksonville'
D=dict(name='Air Element AC and Heating LLC', short='Air Element AC & Heating',
  phone='(904) 440-3389', tel='tel:+19044403389', sms='sms:+19044403389',
  street='10702 Hood Rd Ste 3', city='Jacksonville', region='FL', zip='32257', hood='Mandarin',
  lic='CAC1822512', counties=['Duval','Clay','St. Johns','Nassau'],
  desc='Professional HVAC contractor providing efficient heating and cooling repairs and installations.',
  open=480, close=1320)
DAYS=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
ADDR=f"{D['street']}, {D['city']}, {D['region']} {D['zip']}"
REVIEWS=[
 dict(n='Annalise DeBoef',a='4 months ago',k='Same-day repair',t='Couldn’t be happier with their work. I was originally on a maintenance plan with another company and contacted them when out AC wasn’t working and only reached a robot. Reached out to Air Element and heard back immediately. Robert came out on a Sunday within half an hour. He identified an electrical issue near immediately and provided us a temporary fix until he could get all supplies to get our AC set. We had also injured one of our copper lines with a shovel and he got the lines replaced and the electrical issue fixed with ease. We will certainly continue to use him for all of our AC needs in the future.',
   reply='Thank you, Annalise! We’re so glad to hear about your positive experience with Robert and our team. Your satisfaction means a lot to us, and we appreciate your trust in us for your AC needs.'),
 dict(n='Michael Toenies II',a='6 months ago',k='Condo AC replacement',t='I recently had Robert from Air Element AC and Heating LLC replace an AC unit in my condo, and I could not be more impressed with the experience. From start to finish, he was extremely professional, on time, and excellent with communication. He was very transparent about the different options available and took the time to explain everything clearly without any pressure.\n\nHis pricing was very affordable and fair, especially considering the quality of work and level of service provided. What stood out the most was how much pride he took in his work..he made sure the installation was done right, took the time to teach me about the new unit, and cleaned up thoroughly afterward.\n\nAs an active duty military member of 18 years at the time of this writing, transparency and professionalism are qualities I value highly, and Robert absolutely delivered on both. I strongly recommend Air Element AC and Heating LLC for any HVAC needs around Jacksonville, Florida.',
   reply='Thank you, Michael, for your wonderful review! We appreciate your kind words about Robert’s professionalism and dedication to quality work. It’s great to hear that you had such a positive experience with us. Your recommendation means a lot!'),
 dict(n='Lieth Quffa',a='4 months ago',k='Heating + AC install',t='Great family owned local business. Had the best price, expedient, responsive, and seamless job. Did not try to oversale, or pressure us into more expensive units or extra products. Highly recommend.',
   reply='Thank you, Lieth! We truly appreciate your kind words and support for our family-owned business. It’s wonderful to hear that you had a positive experience with us and felt no pressure during your visit. Your recommendation means a lot to us!'),
 dict(n='Austin Williamson',a='8 months ago',k='Whole-home AC install',t='I needed an entire AC unit for my home. They quoted me a reasonable price for the unit including the labor and were able to get it installed the next day. I really appreciated how fast they had everything installed, and were very kind people. It’s family business and would recommend their services for any A/C related concerns!'),
 dict(n='Roy T',a='8 months ago',k='Repeat customer',t='I’ve used him for multiple AC jobs and I can honestly say he’s outstanding. Extremely reliable, always on time, and very transparent about what actually needs to be done without trying to upsell unnecessary work.\n\nHis pricing is very fair compared to the market, and the quality of his work speaks for itself. He works efficiently, gets the job done fast, and does everything with true professionalism.\n\nIf you’re looking for someone trustworthy, skilled, and easy to work with, I highly recommend him. I’ll definitely continue using his services.'),
 dict(n='Marilou Chyna Brown',a='2 months ago',k='Clogged AC',t='Anton came out to fix my AC that was clogged. Did a great job. Professional and fast. Highly recommend!!!'),
 dict(n='Dany Turk',a='2 years ago',k='AC check & fix',t='Very professional people! Their service and prices are excellent! I called them to come and check out my AC, and they came immediately. They fixed the issue, and they made sure the AC is working well before they left. I will use their service when I need it in the future. I highly recommend them.'),
 dict(n='Marleine Sakr',a='2 months ago',k='Service call',t='Wonderful and friendly service. So grateful to Antonin for his patience and for explaining everything thoroughly. Would highly recommend'),
 dict(n='Mine Can',a='a year ago',k='Install + follow-up',t='I can’t say enough good things about Robert! He installed our A/C unit two years ago, and when we recently ran into an issue, he came through once again with outstanding service. He responded to my call right away and had the problem fixed by the very next day. It’s incredibly reassuring to have someone so dependable, professional, and efficient to count on—especially when dealing with summer heat. Highly recommend his services to anyone looking for quality work done with care!'),
 dict(n='Judy Batson',a='a year ago',k='Mini-split install',t='Air Element AC and Heating is a top notch company owned by Robert K. We needed a mini-split system installed in our recently enclosed patio/spa room. Robert was prompt to reply, courteous and attentive to the needs and resources of the client, thorough and efficient with everyone’s time. Robert and his team is highly recommended!'),
]
SERVICES=[
 dict(id='ac-repair',name='A/C Repair',ico='snow',blurb='Fast diagnosis when the cooling quits — electrical faults, line sets, clogs.',
   body='When the house is heating up, you want a real person to answer. Customers describe calls returned right away, Sunday visits and fixes by the next day — from electrical issues and damaged copper lines to a clogged system.',
   pts=['A/C system repair & maintenance','Electrical issues & replaced copper lines','Clogged systems cleared','Checked running before we leave'],
   q=('Robert came out on a Sunday within half an hour.','Annalise DeBoef'),img='condenser-stand',alt='Outdoor A/C condenser on a raised metal stand beside a sided home'),
 dict(id='ac-installation',name='A/C & Heat Pump Installation',ico='fan',blurb='Whole-system replacements, quoted with the labor included.',
   body='Replacing a worn-out system? You’ll get the options laid out plainly, a price that includes the labor, and a clean, by-the-book install — reviewers mention next-day installs and being shown how the new unit works.',
   pts=['Complete A/C system replacement','Heat pump & condenser installs','Options explained, no pressure','Install done right, cleaned up after'],
   q=('They quoted me a reasonable price for the unit including the labor and were able to get it installed the next day.','Austin Williamson'),img='twin-condensers',alt='Two new matching condensers installed on pads along the side of a townhome'),
 dict(id='heating',name='Heating & Air Handlers',ico='flame',blurb='Heating installs and air handlers in closets, garages and attics.',
   body='Jacksonville winters are short, but a cold snap still finds a weak system. Air Element installs heating systems and air handlers — sealed, strapped and plumbed neatly in closets, garages and attics.',
   pts=['Heating system installation','Air handler replacement','Closet, garage & attic setups','Condensate lines plumbed clean'],
   q=('Did not try to oversale, or pressure us into more expensive units or extra products.','Lieth Quffa'),img='air-handler-ductboard',alt='Newly installed air handler with sealed duct-board plenums in a utility room'),
 dict(id='ductwork',name='Duct Work',ico='duct',blurb='New runs, replacements and duct systems — residential to commercial.',
   body='Comfort only reaches the room if the air does. From attic flex runs to open-truss commercial builds, Air Element lays out and installs duct systems that move air where it’s needed.',
   pts=['Attic flex duct runs','Duct systems for new builds','Commercial open-truss ductwork','Plenums & returns sealed'],
   q=('Great family owned local business. Had the best price, expedient, responsive, and seamless job.','Lieth Quffa'),img='attic-ducts',alt='Attic with new insulated flex duct runs branching from a central trunk'),
 dict(id='mini-splits',name='Ductless Mini-Splits',ico='split',blurb='Cooling for enclosed patios, additions and rooms without ducts.',
   body='Enclosed a patio, added a room or finished a space the ducts don’t reach? A ductless mini-split adds quiet, independent comfort — wall head inside, compact condenser outside.',
   pts=['Mini-split system installation','Enclosed patios & sunrooms','Additions and garages','Wall-mounted heads, neat line sets'],
   q=('We needed a mini-split system installed in our recently enclosed patio/spa room.','Judy Batson'),img='minisplit-porch',alt='White ductless mini-split head mounted high on a porch wall above a window'),
 dict(id='commercial',name='Commercial & Rooftop',ico='roof',blurb='Residential and commercial — packaged and rooftop units too.',
   body='Their business card says it plainly: residential and commercial. That includes packaged units, rooftop equipment and commercial condensers serviced up on the roof or out back.',
   pts=['Rooftop unit service','Packaged units','Commercial condensers','Commercial A/C contractors (BBB category)'],
   q=('Very professional people! Their service and prices are excellent!','Dany Turk'),img='commercial-condenser',alt='Commercial condenser on a pad behind yellow safety bollards beside a block wall'),
]
GALLERY=[ # (img, tags, alt)
 ('trane-condenser','cooling','New Trane condenser on a fresh pad beside a gray-sided home'),
 ('minisplit-patio','minisplit','Mini-split head above sliding glass doors in a screened patio room'),
 ('garage-air-handler','heating','Garage air handler with sealed plenums next to the water heater'),
 ('heat-pump-tall','cooling','Tall two-fan outdoor unit set on a concrete pad'),
 ('attic-flex','ducts','Insulated flex duct running through an attic between rafters'),
 ('package-unit','cooling','Packaged A/C unit on a pad alongside a sided home'),
 ('closet-air-handler','heating','Air handler in a closet with an insulated supply duct'),
 ('commercial-ductwork','ducts commercial','Open-truss commercial space with new ductwork overhead'),
 ('minisplit-outdoor','minisplit','Compact mini-split condenser on a pad in a mulch bed'),
 ('package-unit-2','cooling','Packaged unit with disconnect box beside a home'),
 ('air-handler-closet','heating','Slim air handler installed in a utility closet'),
 ('trane-air-handler','heating','Trane air handler with new duct-board plenums in a garage'),
 ('attic-air-handler','heating ducts','Horizontal air handler in an attic surrounded by new flex ducts'),
 ('condenser-brick','cooling','Condenser on a pad beside a brick home'),
 ('minisplit-yard','minisplit','Mini-split outdoor unit against a garden building'),
 ('hero-rooftop-m','commercial','Technician beside an opened rooftop unit on a commercial roof'),
 ('commercial-condenser','cooling commercial','Commercial condenser behind yellow safety bollards'),
 ('attic-ducts','ducts','Attic with new insulated flex duct runs branching from a trunk'),
 ('condenser-stand','cooling','Condenser on a raised metal stand beside a sided home'),
 ('air-handler-ductboard','heating','Air handler with sealed duct-board plenums in a utility room'),
 ('minisplit-porch','minisplit','Mini-split head on a porch wall above a window'),
]
GALLERY=[g for g in GALLERY if g[1]!='skip']
PAGES=[('index.html','Home'),('services.html','Services'),('work.html','Our Work'),('reviews.html','Reviews'),('about.html','About & FAQ'),('contact.html','Contact')]
FAQ=[
 ('What areas does Air Element serve?','Duval, Clay, St. Johns and Nassau counties — Jacksonville and the surrounding area. The office is at 10702 Hood Rd Ste 3 in Mandarin.'),
 ('What are your hours?','8 AM to 10 PM, seven days a week, per the Google Business Profile. Holiday hours may differ — call to confirm.'),
 ('Can I book online?','Yes. Use the “Book online” button to request a visit through Housecall Pro, or call (904) 440-3389.'),
 ('Do you work on homes and businesses?','Yes — residential and commercial, including packaged and rooftop units.'),
 ('Are you licensed?','Yes. Florida license CAC1822512 (listed on the company’s BBB profile).'),
 ('Are you BBB accredited?','Yes — BBB Accredited since January 31, 2024, with an A+ rating.'),
 ('What HVAC services do you offer?','A/C repair and maintenance, A/C and heat pump installation, heating and air handler installation, duct work, ductless mini-splits, and commercial / rooftop equipment.'),
]
# ------------------------------------------------------------------ helpers
_dims={}
def dims(n):
    if n not in _dims: _dims[n]=Image.open(os.path.join(ROOT,'img',n+'.webp')).size
    return _dims[n]
def img(n,alt,cls='',lazy=True,extra=''):
    w,h=dims(n)
    return f'<img src="img/{n}.webp" width="{w}" height="{h}" alt="{E(alt)}"{" loading=\"lazy\" decoding=\"async\"" if lazy else " fetchpriority=\"high\""}{f" class=\"{cls}\"" if cls else ""}{extra}>'
def louver(inner,cls=''):
    return f'<div class="lv {cls}">{inner}<span class="lv-s" aria-hidden="true">{"<i></i>"*7}</span></div>'
ICO={
 'phone':'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 'cal':'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M8 15h3"/>',
 'sms':'<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 'pin':'<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 'clock':'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'snow':'<path d="M12 2v20M4.9 6.5l14.2 11M19.1 6.5 4.9 17.5M9 3.5l3 2.5 3-2.5M9 20.5l3-2.5 3 2.5M2.6 9.6l3.7.9-1.2 3.6M21.4 14.4l-3.7-.9 1.2-3.6"/>',
 'flame':'<path d="M12 22c4.4 0 7-3 7-7 0-4.5-4-7-4-11-2.5 1.5-4 4-4 6-1-1-1.6-2.4-1.6-3.6C7 8 5 10.8 5 15c0 4 2.6 7 7 7z"/><path d="M12 22c-1.7 0-3-1.3-3-3.2 0-2 1.7-3 3-5 1.3 2 3 3 3 5 0 1.9-1.3 3.2-3 3.2z"/>',
 'fan':'<circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 1-7 4-7s3 4 0 6l-2 1M14 12c4 0 7 1 7 4s-4 3-6 0l-1-2M12 14c0 4-1 7-4 7s-3-4 0-6l2-1M10 12c-4 0-7-1-7-4s4-3 6 0l1 2"/>',
 'duct':'<path d="M3 8h10a4 4 0 0 1 4 4v9M3 13h7a2 2 0 0 1 2 2v6M3 4h10a8 8 0 0 1 8 8v9"/>',
 'split':'<rect x="2" y="5" width="20" height="8" rx="2"/><path d="M6 10h12M7 17c0 1.5-1 2-1 3M12 17c0 1.5-1 2-1 3M17 17c0 1.5-1 2-1 3"/>',
 'roof':'<path d="M3 11 12 4l9 7"/><rect x="7" y="13" width="10" height="7" rx="1"/><circle cx="12" cy="16.5" r="1.6"/>',
 'star':'<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 'shield':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 'arrow':'<path d="M5 12h14M13 6l6 6-6 6"/>',
}
def ic(n,fill=False): return f'<svg class="ic" viewBox="0 0 24 24" {"fill=\"currentColor\" stroke=\"none\"" if fill else "fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\""} aria-hidden="true">{ICO[n]}</svg>'
EMBLEM=open(os.path.join(ROOT,'brand','emblem.svg')).read()
def flow_svg(cls='flow'):
    paths=['M-50 120 C 200 60, 380 200, 620 120 S 1000 40, 1500 140','M-50 220 C 240 160, 420 300, 700 210 S 1100 150, 1500 250',
           'M-50 330 C 180 290, 460 400, 760 320 S 1150 260, 1500 360','M-50 450 C 260 400, 520 520, 820 430 S 1200 380, 1500 480',
           'M-50 560 C 220 520, 500 640, 800 560 S 1180 500, 1500 600']
    ps=''.join(f'<path d="{p}" style="--d:{i*0.7:.1f}s"/>' for i,p in enumerate(paths))
    return f'<svg class="{cls}" viewBox="0 0 1440 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><g class="f-a">{ps}</g><g class="f-b">{ps}</g></svg>'
def biz_schema():
    return {'@context':'https://schema.org','@type':'HVACBusiness','@id':BASE+'#business','name':D['name'],'alternateName':['Air Element AC & Heating','Air Element AC'],
      'description':D['desc'],'url':BASE,'telephone':'+1-904-440-3389','image':BASE+'og.jpg','logo':BASE+'brand/logo-horizontal-light-1200.png',
      'address':{'@type':'PostalAddress','streetAddress':D['street'],'addressLocality':D['city'],'addressRegion':'FL','postalCode':D['zip'],'addressCountry':'US'},
      'geo':{'@type':'GeoCoordinates','latitude':30.1834703,'longitude':-81.5734384},'hasMap':MAPS,
      'areaServed':[{'@type':'AdministrativeArea','name':c+' County, FL'} for c in D['counties']],
      'openingHoursSpecification':[{'@type':'OpeningHoursSpecification','dayOfWeek':DAYS,'opens':'08:00','closes':'22:00'}],
      'sameAs':[MAPS,BBB,YELP],
      'hasCredential':{'@type':'EducationalOccupationalCredential','credentialCategory':'license','name':'Florida DBPR Certified Air Conditioning Contractor license CAC1822512'},
      'potentialAction':{'@type':'ReserveAction','target':BOOK,'name':'Book online'},
      'aggregateRating':{'@type':'AggregateRating','ratingValue':'5.0','reviewCount':82,'bestRating':'5','worstRating':'1'},
      'hasOfferCatalog':{'@type':'OfferCatalog','name':'HVAC services','itemListElement':[{'@type':'Offer','itemOffered':{'@type':'Service','name':s['name'],'description':s['body']}} for s in SERVICES]},
      'review':[{'@type':'Review','author':{'@type':'Person','name':r['n']},'reviewBody':r['t'],'publisher':{'@type':'Organization','name':'Google'}} for r in REVIEWS]}
def crumbs(path,title):
    it=[{'@type':'ListItem','position':1,'name':'Home','item':BASE}]
    if path!='index.html': it.append({'@type':'ListItem','position':2,'name':title,'item':BASE+path})
    return {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':it}
def head(path,title,desc,schemas,home=False):
    canon=BASE+('' if path=='index.html' else path)
    ld=''.join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in schemas)
    pre='<link rel="preload" as="image" href="img/hero-rooftop.webp" media="(min-width:861px)"><link rel="preload" as="image" href="img/hero-rooftop-m.webp" media="(max-width:860px)">' if home else ''
    return f'''<!doctype html><html lang="en" class="no-js" data-mode="cool"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}"><meta name="theme-color" content="#0b1118">
<meta property="og:type" content="website"><meta property="og:site_name" content="{E(D['short'])}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE}og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{BASE}og.jpg">
<link rel="icon" href="brand/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="brand/favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="brand/favicon-32.png"><link rel="apple-touch-icon" href="brand/favicon-180.png">
<script>try{{var m=localStorage.getItem('ae-mode');if(m)document.documentElement.dataset.mode=m}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800;900&family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
{pre}<link rel="stylesheet" href="assets/site.css?v=3">{ld}
</head><body class="pg-{path[:-5]}">
<a class="skip" href="#main">Skip to content</a><div class="prog" aria-hidden="true"></div>
'''
def nav(path):
    li=''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==path else ""}>{t}</a></li>' for h,t in PAGES)
    ml=''.join(f'<a class="ml" href="{h}"{" aria-current=\"page\"" if h==path else ""}>{t}</a>' for h,t in PAGES)
    return f'''<header class="nav" role="banner">
<a class="brand" href="index.html" aria-label="Air Element AC &amp; Heating — home"><span class="b-em">{EMBLEM}</span><span class="b-tx">Air Element<small>AC &amp; Heating, LLC</small></span></a>
<nav aria-label="Main"><ul>{li}</ul></nav>
<div class="n-cta"><a class="btn ghost sm" href="{D['tel']}">{ic('phone')}<span>{D['phone']}</span></a><a class="btn sm mag" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}Book online</a></div>
<button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mmenu"><i></i><i></i><i></i></button>
</header>
<div class="mmenu" id="mmenu" aria-hidden="true">{ml}<div class="mm-row"><a class="btn" href="{D['tel']}">{ic('phone')}Call {D['phone']}</a><a class="btn ghost" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}Book online</a></div><p class="mm-note">8 AM – 10 PM · 7 days</p></div>
<main id="main">'''
def live(cls=''): return f'<span class="live {cls}" data-live><b></b><span class="t">8 AM – 10 PM daily</span></span>'
def cta_band(h='Too hot? Too cold? <em>Call&nbsp;now.</em>',p='Real people answer from 8 AM to 10 PM, seven days a week — or grab a time online.'):
    return f'''<section class="ctab"><div class="ctab-bg" aria-hidden="true">{flow_svg('flow flow-c')}</div><div class="wrap ctab-in rv">
<h2>{h}</h2><p>{p}</p><div class="ctas"><a class="btn lg mag" href="{D['tel']}">{ic('phone')}Call {D['phone']}</a><a class="btn lg ghost" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}Book online</a></div>{live('lg')}</div></section>'''
def footer():
    links=''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in PAGES)
    svc=''.join(f'<li><a href="services.html#{s["id"]}">{s["name"]}</a></li>' for s in SERVICES)
    return f'''</main>
<footer class="foot"><div class="wrap"><div class="fgrid">
<div class="f-brand"><img src="brand/logo-horizontal-dark.svg" width="460" height="104" alt="Air Element AC &amp; Heating, LLC logo" loading="lazy"><p>Family-owned heating &amp; air conditioning for homes and businesses across Duval, Clay, St. Johns &amp; Nassau counties.</p><p class="f-cred">{ic('shield')}FL Lic. {D['lic']} · BBB A+ Accredited</p></div>
<div><h3>Pages</h3><ul>{links}</ul></div>
<div><h3>Services</h3><ul>{svc}</ul></div>
<div><h3>Visit &amp; call</h3><address><a href="{MAPS}" target="_blank" rel="noopener">{D['name']}<br>{D['street']}<br>{D['city']}, FL {D['zip']}</a></address><p><a class="f-ph" href="{D['tel']}">{D['phone']}</a></p><p>Open 8 AM – 10 PM, 7 days a week</p>{live()}</div>
</div><div class="f-base"><span>© {YEAR} {D['name']}</span><span><a href="{MAPS}" target="_blank" rel="noopener">Google</a> · <a href="{BBB}" target="_blank" rel="noopener">BBB</a> · <a href="{YELP}" target="_blank" rel="noopener">Yelp</a></span></div></div></footer>
<div class="mbar"><a href="{D['tel']}">{ic('phone')}Call</a><a class="mb-b" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}Book online</a></div>
<div class="demo" role="note"><span>Design preview by <b>RGWebD</b></span><button type="button" aria-label="Dismiss design preview note">×</button></div>
<div class="lbx" role="dialog" aria-modal="true" aria-label="Photo viewer"><button class="lbx-x" type="button" aria-label="Close">×</button><button class="lbx-p" type="button" aria-label="Previous photo">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lbx-n" type="button" aria-label="Next photo">›</button></div>
<script src="assets/site.js?v=3" defer></script>
</body></html>'''
def phero(path,eyebrow,h1,lede,image,alt,extra=''):
    return f'''<section class="phero"><div class="phero-bg" aria-hidden="true">{flow_svg()}</div><div class="wrap phero-in">
<div class="phero-tx"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">{dict(PAGES)[path]}</span></nav>
<p class="eyebrow">{eyebrow}</p><h1 class="split">{h1}</h1><p class="lede">{lede}</p>{extra}</div>
<figure class="phero-ph">{img(image,alt,lazy=False)}<span class="ph-tag">{E(alt)}</span></figure></div></section>'''
def gauge(val,dec,label,sub,maxv,mode='ice'):
    pct=min(1,float(val)/maxv)
    return f'''<div class="gauge g-{mode} rv"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="g-tr" cx="60" cy="60" r="50" pathLength="100"/><circle class="g-v" cx="60" cy="60" r="50" pathLength="100" style="--p:{pct*75:.2f}"/></svg>
<div class="g-n"><span data-count="{val}" data-dec="{dec}">{float(val):.{dec}f}</span></div><p class="g-l">{label}</p><p class="g-s">{sub}</p></div>'''
def rcard(r,full=True,cls=''):
    t=r['t'] if full else (r['t'][:210].rsplit(' ',1)[0]+'…' if len(r['t'])>220 else r['t'])
    paras=''.join(f'<p>{E(p)}</p>' for p in t.split('\n\n'))
    rep=f'<div class="r-rep"><b>Owner reply</b><p>{E(r["reply"])}</p></div>' if full and r.get('reply') else ''
    return f'''<figure class="rcard {cls}"><div class="r-top"><span class="r-av" aria-hidden="true">{E(r["n"][0])}</span><div><figcaption class="r-n">{E(r["n"])}</figcaption><span class="r-m">Google review · {E(r["a"])}</span></div><span class="r-k">{E(r["k"])}</span></div><blockquote>{paras}</blockquote>{rep}</figure>'''
# ------------------------------------------------------------------ pages
def page_home():
    p='index.html'; t='Air Element AC & Heating | HVAC Repair & Installation in Jacksonville, FL'
    desc='Family-owned A/C and heating repair, installation, duct work and mini-splits in Jacksonville (Mandarin). 5.0★ from 82 Google reviews. Open 8 AM–10 PM, 7 days. Call (904) 440-3389.'
    s=head(p,t,desc,[biz_schema(),crumbs(p,'Home')],home=True)
    s+='<div class="loader" aria-hidden="true"><div class="ld-in"><div class="ld-em">'+EMBLEM+'</div><div class="ld-temp"><span class="ld-n">88</span>°</div><p class="ld-l">Setting your comfort…</p></div></div>'
    s+=nav(p)
    mq=''.join(f'<span>{x}</span><i aria-hidden="true">✳</i>' for x in ['A/C repair','A/C installation','Heat pumps','Heating installation','Air handlers','Duct work','Ductless mini-splits','Rooftop units','Residential','Commercial','HVAC maintenance'])
    s+=f'''<section class="hero" aria-label="Introduction">
<div class="h-bg" aria-hidden="true"><i class="h-cool"></i><i class="h-heat"></i>{flow_svg()}</div>
<div class="h-out" aria-hidden="true">AIR</div>
<div class="wrap h-grid">
<div class="h-tx">
<p class="eyebrow"><span class="dot"></span>HVAC · Mandarin · Jacksonville, FL</p>
<h1 class="h-h"><span class="h-l1">Cool when it’s <em class="c">blazing.</em></span><span class="h-l2">Warm when it <em class="h">drops.</em></span></h1>
<p class="h-p">Family-owned A/C &amp; heating repair and installation for homes and businesses across Duval, Clay, St.&nbsp;Johns &amp; Nassau&nbsp;counties.</p>
<div class="ctas"><a class="btn lg mag" href="{D['tel']}">{ic('phone')}Call {D['phone']}</a><a class="btn lg ghost" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}Book online</a></div>
<div class="trust"><a class="t-rate" href="reviews.html"><span class="stars" aria-hidden="true">{ic('star',1)*5}</span><b>5.0</b><span>82 Google reviews</span></a>{live()}<span class="t-bbb">{ic('shield')}BBB A+</span></div>
</div>
<div class="h-vis">
<figure class="h-ph"><picture><source media="(max-width:860px)" srcset="img/hero-rooftop-m.webp" width="900" height="1120"><img src="img/hero-rooftop.webp" width="1100" height="1956" alt="Air Element technician beside an opened rooftop HVAC unit on a commercial roof" fetchpriority="high"></picture><i class="h-tint" aria-hidden="true"></i>
<span class="pin pin-a" style="--x:47%;--y:56%"><b></b><em>Rooftop unit · opened for service</em></span></figure>
<div class="dial" role="group" aria-label="Cool or heat mode — re-tints the page">
<svg viewBox="0 0 200 200" aria-hidden="true"><circle class="d-tr" cx="100" cy="100" r="82" pathLength="100"/><circle class="d-v" cx="100" cy="100" r="82" pathLength="100"/>{''.join(f'<line class="d-tk" x1="100" y1="10" x2="100" y2="{17 if i%5 else 22}" transform="rotate({-135+i*9} 100 100)"/>' for i in range(31))}</svg>
<div class="d-rd"><span class="d-mode">Cooling</span><span class="d-t"><span class="d-n">72</span>°</span><span class="d-s">Set&nbsp;·&nbsp;Jacksonville</span></div>
<div class="d-sw"><button type="button" data-set="cool" aria-pressed="true">{ic('snow')}Cool</button><button type="button" data-set="heat" aria-pressed="false">{ic('flame')}Heat</button></div>
</div>
</div></div>
<div class="mq" aria-label="Services"><div class="mq-t">{mq}{mq}</div></div>
</section>'''
    # why
    why=[('snow','Fast, human response','Calls returned immediately — even Sunday visits.','Robert came out on a Sunday within half an hour.','Annalise DeBoef'),
         ('shield','No upselling','Straight answers about what actually needs doing.','Did not try to oversale, or pressure us into more expensive units or extra products.','Lieth Quffa'),
         ('fan','Options, explained','You see the choices and the price — then decide.','He was very transparent about the different options available and took the time to explain everything clearly without any pressure.','Michael Toenies II'),
         ('flame','Clean, careful installs','Done right, walked through, cleaned up after.','He made sure the installation was done right, took the time to teach me about the new unit, and cleaned up thoroughly afterward.','Michael Toenies II')]
    wc=''.join(f'<article class="why-c tilt rv" style="--i:{i}"><span class="why-i">{ic(a)}</span><h3>{b}</h3><p>{c}</p><blockquote>“{E(q)}”<cite>— {E(n)}</cite></blockquote></article>' for i,(a,b,c,q,n) in enumerate(why))
    s+=f'''<section class="sec why"><div class="wrap"><div class="sh rv"><p class="eyebrow">Why Jacksonville calls Air Element</p><h2>Family-owned. <em>Straight-talking.</em> Fast.</h2><p>Every reason below comes straight from their customers’ Google reviews.</p></div><div class="why-g">{wc}</div></div></section>'''
    # gauges
    s+=f'''<section class="sec gauges"><div class="g-bg" aria-hidden="true"></div><div class="wrap"><div class="sh rv"><p class="eyebrow">The readout</p><h2>Numbers that <em>hold steady.</em></h2></div><div class="g-g">
{gauge('5.0',1,'Google rating','Average across 82 reviews',5,'ice')}{gauge(82,0,'Google reviews','And counting',100,'ember')}{gauge(7,0,'Days a week','Open every day',7,'ice')}{gauge(14,0,'Hours a day','8 AM – 10 PM',24,'ember')}{gauge(4,0,'Counties served','Duval · Clay · St. Johns · Nassau',4,'ice')}
</div></div></section>'''
    # services teaser
    feat=[SERVICES[0],SERVICES[1],SERVICES[3],SERVICES[4]]
    alt_imgs={'ac-repair':('trane-condenser','New Trane condenser on a fresh pad beside a gray-sided home'),'ac-installation':('heat-pump-tall','Tall two-fan outdoor unit set on a concrete pad'),'ductwork':('attic-flex','Insulated flex duct running through an attic between rafters'),'mini-splits':('minisplit-patio','Mini-split head above sliding glass doors in a screened patio room')}
    sc=''.join(f'<a class="svc-c rv" style="--i:{i}" href="services.html#{x["id"]}">{louver(img(alt_imgs[x["id"]][0],alt_imgs[x["id"]][1]))}<div class="svc-b"><span class="svc-i">{ic(x["ico"])}</span><h3>{x["name"]}</h3><p>{x["blurb"]}</p><span class="more">Learn more {ic("arrow")}</span></div></a>' for i,x in enumerate(feat))
    s+=f'''<section class="sec svc"><div class="wrap"><div class="sh sh-row rv"><div><p class="eyebrow">What they do</p><h2>Cooling, heating &amp; <em>everything the air moves through.</em></h2></div><a class="btn ghost" href="services.html">All services {ic('arrow')}</a></div><div class="svc-g">{sc}</div></div></section>'''
    # reviews carousel
    pick=[REVIEWS[i] for i in (2,3,5,8,9,6)]
    sl=''.join(f'<div class="rc-s" role="group" aria-roledescription="slide" aria-label="{i+1} of {len(pick)}">{rcard(r,False)}</div>' for i,r in enumerate(pick))
    s+=f'''<section class="sec rv-band"><div class="wrap rvb-g"><div class="rvb-l rv"><p class="eyebrow">Google reviews</p><p class="big5">5.0</p><span class="stars lg" aria-hidden="true">{ic('star',1)*5}</span><p>from <b>82</b> reviews on Google</p><a class="btn ghost" href="reviews.html">Read the reviews {ic('arrow')}</a></div>
<div class="rc rv" aria-roledescription="carousel" aria-label="Customer reviews"><div class="rc-tr">{sl}</div><div class="rc-nav"><button type="button" class="rc-p" aria-label="Previous review">‹</button><div class="rc-dots"></div><button type="button" class="rc-n" aria-label="Next review">›</button></div></div></div></section>'''
    # teasers
    tz=[('work.html','commercial-ductwork','Open-truss commercial space with new ductwork overhead','Our work','Installs, attics, rooftops — a gallery of real jobs.'),
        ('about.html','garage-air-handler','Garage air handler with sealed plenums next to the water heater','About & FAQ','Licensed, BBB A+ accredited, family-owned in Mandarin.'),
        ('contact.html','minisplit-porch','White ductless mini-split head mounted high on a porch wall above a window','Contact','Call, text or book online — 8 AM to 10 PM daily.')]
    tc=''.join(f'<a class="tz tilt rv" style="--i:{i}" href="{h}">{img(m,a)}<div class="tz-b"><h3>{t_}</h3><p>{d_}</p><span class="more">Open {ic("arrow")}</span></div></a>' for i,(h,m,a,t_,d_) in enumerate(tz))
    s+=f'<section class="sec tzs"><div class="wrap"><div class="tz-g">{tc}</div></div></section>'
    s+=cta_band()+footer(); return s
def page_services():
    p='services.html'; t='HVAC Services in Jacksonville — A/C Repair, Installs, Ducts & Mini-Splits | Air Element'
    desc='A/C repair and maintenance, A/C & heat pump installation, heating and air handlers, duct work, ductless mini-splits and commercial rooftop units across Duval, Clay, St. Johns & Nassau.'
    s=head(p,t,desc,[biz_schema(),crumbs(p,'Services')])+nav(p)
    chips=''.join(f'<a class="chip" href="#{x["id"]}">{ic(x["ico"])}{x["name"]}</a>' for x in SERVICES)
    s+=phero(p,'Services','Every part of <em>the system.</em>','From a clogged A/C on a Sunday to a full replacement, a new duct layout or a rooftop unit — residential and commercial.','minisplit-patio','Mini-split head above sliding glass doors in a screened patio room',f'<div class="chips">{chips}</div>')
    for i,x in enumerate(SERVICES):
        pts=''.join(f'<li>{E(z)}</li>' for z in x['pts'])
        s+=f'''<section class="sec srv {'flip' if i%2 else ''}" id="{x['id']}"><div class="wrap srv-g">
<div class="srv-ph rv" data-r="{'right' if i%2 else 'left'}">{louver(img(x['img'],x['alt']))}<span class="srv-no">0{i+1}</span></div>
<div class="srv-tx rv"><span class="svc-i">{ic(x['ico'])}</span><h2>{x['name']}</h2><p class="lede">{x['body']}</p><ul class="ticks">{pts}</ul>
<blockquote class="pull">“{E(x['q'][0])}”<cite>— {E(x['q'][1])}, Google review</cite></blockquote>
<div class="ctas"><a class="btn mag" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}Book {x['name'].split(' &')[0]}</a><a class="btn ghost" href="{D['tel']}">{ic('phone')}{D['phone']}</a></div></div></div></section>'''
    # blueprint compare
    s+=f'''<section class="sec bp"><div class="wrap bp-g"><div class="bp-tx rv"><p class="eyebrow">Drag to compare</p><h2>Drawn like a plan. <em>Built like one.</em></h2><p>One real Air Element garage install, shown two ways: a line-drawn blueprint traced from the photo, and the finished equipment — air handler, sealed supply and return plenums, and a neatly run condensate line.</p><p class="note">Same photo, two views — not a before/after.</p></div>
<div class="ba rv" style="--p:50%"><img class="ba-a" src="img/bp-real.webp" width="900" height="1180" alt="Finished air handler install in a garage with sealed plenums and condensate line" loading="lazy"><div class="ba-b">{img('bp-lines','Blueprint-style line drawing traced from the same garage install')}</div><span class="ba-h" aria-hidden="true"><b>{ic('arrow')}</b></span><span class="ba-lb ba-l1">Blueprint</span><span class="ba-lb ba-l2">Installed</span><input type="range" min="0" max="100" value="50" aria-label="Compare blueprint and installed photo"></div></div></section>'''
    steps=[('Call or book online','Call (904) 440-3389 or request a time through the online booking page — 8 AM to 10 PM, every day.','Reached out to Air Element and heard back immediately.','Annalise DeBoef'),
           ('A real diagnosis','A technician finds what’s actually wrong — and tells you plainly what does and doesn’t need doing.','Very transparent about what actually needs to be done without trying to upsell unnecessary work.','Roy T'),
           ('Clear options & price','You get the options side by side with the price, labor included — no pressure.','They quoted me a reasonable price for the unit including the labor.','Austin Williamson'),
           ('Fixed, tested, tidy','The work gets done, the system is checked running, and the space is cleaned up.','They made sure the AC is working well before they left.','Dany Turk')]
    st=''.join(f'<li class="tl-s rv"><span class="tl-n">0{i+1}</span><h3>{a}</h3><p>{b}</p><blockquote>“{E(q)}” <cite>— {E(n)}</cite></blockquote></li>' for i,(a,b,q,n) in enumerate(steps))
    s+=f'<section class="sec how" id="process"><div class="wrap"><div class="sh rv"><p class="eyebrow">How a visit works</p><h2>Four steps. <em>No runaround.</em></h2></div><ol class="tl"><span class="tl-line" aria-hidden="true"><i></i></span>{st}</ol></div></section>'
    s+=cta_band()+footer(); return s
def page_work():
    p='work.html'; t='Our Work — HVAC Installs & Ductwork Photos | Air Element AC & Heating'
    desc='Real Air Element AC & Heating jobs around Jacksonville: condensers, heat pumps, air handlers, attic ductwork, mini-splits and commercial equipment.'
    s=head(p,t,desc,[biz_schema(),crumbs(p,'Our Work')])+nav(p)
    s+=phero(p,'Our work','Real jobs. <em>Real equipment.</em>','Every photo here is from Air Element’s own Google and Yelp listings — installs, attics, closets and rooftops around Jacksonville.','twin-condensers','Two new matching condensers installed on pads along the side of a townhome')
    f=[('all','All'),('cooling','Cooling'),('heating','Air handlers & heat'),('ducts','Ductwork'),('minisplit','Mini-splits'),('commercial','Commercial')]
    fb=''.join(f'<button type="button" data-f="{a}" aria-pressed="{"true" if a=="all" else "false"}">{b}</button>' for a,b in f)
    gl=''.join(f'<button type="button" class="gi rv" data-tags="{tg}" data-full="img/{m}.webp" aria-label="Open photo: {E(a)}">{img(m,a)}<span class="gi-c">{E(a)}</span></button>' for m,tg,a in GALLERY)
    s+=f'<section class="sec gal-s"><div class="wrap"><div class="filters" role="group" aria-label="Filter photos">{fb}</div><div class="gal">{gl}</div></div></section>'
    s+=cta_band('Want yours <em>done this clean?</em>','Book online or call — repairs, replacements, ducts and mini-splits.')+footer(); return s
def page_reviews():
    p='reviews.html'; t='Reviews — 5.0 Stars from 82 Google Reviews | Air Element AC & Heating'
    desc='Read what Jacksonville customers say about Air Element AC & Heating: 5.0 stars from 82 Google reviews — fast response, fair prices, no upselling.'
    s=head(p,t,desc,[biz_schema(),crumbs(p,'Reviews')])+nav(p)
    s+=phero(p,'Reviews','5.0 stars. <em>82 reviews.</em>','Fast response, fair prices and no upselling — in their customers’ own words, quoted exactly as posted on Google.','heat-pump-tall','Tall two-fan outdoor unit set on a concrete pad',f'<div class="trust"><a class="t-rate" href="{MAPS}" target="_blank" rel="noopener"><span class="stars" aria-hidden="true">{ic("star",1)*5}</span><b>5.0</b><span>82 Google reviews</span></a></div>')
    cards=''.join(f'<div class="rv rg-i">{rcard(r)}</div>' for r in REVIEWS)
    s+=f'<section class="sec rgrid-s"><div class="wrap"><div class="rgrid">{cards}</div><p class="r-more"><a class="btn ghost" href="{MAPS}" target="_blank" rel="noopener">See all 82 reviews on Google {ic("arrow")}</a></p></div></section>'
    s+=cta_band('Be the next <em>five-star</em> story.','Call or book online — 8 AM to 10 PM, seven days a week.')+footer(); return s
def page_about():
    p='about.html'; t='About Air Element AC & Heating — Family-Owned HVAC in Mandarin, Jacksonville'
    desc='Family-owned HVAC contractor at 10702 Hood Rd in Mandarin, Jacksonville. FL license CAC1822512, BBB A+ accredited, serving Duval, Clay, St. Johns & Nassau counties.'
    faq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]}
    s=head(p,t,desc,[biz_schema(),crumbs(p,'About & FAQ'),faq])+nav(p)
    s+=phero(p,'About & FAQ','Local. Licensed. <em>Family-owned.</em>','A Mandarin-based heating and air conditioning company keeping homes and businesses comfortable across four Northeast Florida counties.','air-handler-closet','Slim air handler installed in a utility closet')
    cred=[('shield','FL Lic. CAC1822512','Florida-licensed air conditioning contractor (license listed on BBB).'),('star','BBB A+ Accredited','BBB Accredited Business since January 31, 2024.'),('pin','Based in Mandarin','Office at 10702 Hood Rd Ste 3, Jacksonville, FL 32257.'),('clock','Open 7 days','8 AM – 10 PM, every day of the week.')]
    cc=''.join(f'<div class="cred tilt rv" style="--i:{i}">{ic(a)}<h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate(cred))
    s+=f'''<section class="sec story"><div class="wrap st-g"><div class="st-tx rv"><p class="eyebrow">The company</p><h2>“Great family owned <em>local business.”</em></h2>
<p>That’s how customer Lieth Quffa put it — and the company’s own reply says the same: “our family-owned business.” Air Element AC and Heating LLC works out of a Mandarin office on Hood Road and handles residential and commercial heating and cooling: repairs, replacements, duct systems, mini-splits and rooftop equipment.</p>
<p>In their own words: <i>“Don’t wait until the sun starts blazing or the weather drops to freezing temperatures to call for HVAC assistance. Let us keep your home or business at the temperatures you find most comfortable.”</i></p>
<p>Reviewers keep coming back to the same things — technicians like Robert and Anton who show up fast, explain the options, don’t upsell and leave the place clean.</p></div>
<div class="st-ph rv">{louver(img('commercial-ductwork','Open-truss commercial space with new ductwork overhead'))}{img('trane-air-handler','Trane air handler with new duct-board plenums in a garage','st-ph2')}</div></div></section>'''
    s+=f'<section class="sec creds"><div class="wrap"><div class="cred-g">{cc}</div></div></section>'
    cz=''.join(f'<li class="cty rv" style="--i:{i}"><span>{c}</span><small>County</small></li>' for i,c in enumerate(D['counties']))
    s+=f'''<section class="sec area"><div class="wrap ar-g"><div class="rv"><p class="eyebrow">Service area</p><h2>Four counties. <em>One call.</em></h2><p>Per the company’s BBB profile, Air Element serves Duval, Clay, St. Johns and Nassau counties — Jacksonville and its neighbors on every side.</p></div><ul class="ctys">{cz}</ul></div></section>'''
    fq=''.join(f'<details class="fq rv"><summary>{E(q)}<span aria-hidden="true">+</span></summary><p>{E(a)}</p></details>' for q,a in FAQ)
    s+=f'<section class="sec faq"><div class="wrap fq-w"><div class="sh rv"><p class="eyebrow">FAQ</p><h2>Quick <em>answers.</em></h2></div>{fq}</div></section>'
    s+=cta_band()+footer(); return s
def page_contact():
    p='contact.html'; t='Contact Air Element AC & Heating — Call (904) 440-3389 or Book Online'
    desc='Call (904) 440-3389, text, or book online with Air Element AC & Heating. 10702 Hood Rd Ste 3, Jacksonville, FL 32257. Open 8 AM–10 PM, 7 days a week.'
    s=head(p,t,desc,[biz_schema(),crumbs(p,'Contact')])+nav(p)
    s+=phero(p,'Contact','Let’s get you <em>comfortable.</em>','Call, text or book a visit online. Open 8 AM to 10 PM, seven days a week.','condenser-brick','Condenser on a pad beside a brick home',f'<div class="ctas"><a class="btn lg mag" href="{D["tel"]}">{ic("phone")}Call {D["phone"]}</a><a class="btn lg ghost" href="{BOOK}" target="_blank" rel="noopener">{ic("cal")}Book online</a></div>')
    hrs=''.join(f'<tr data-d="{d[:2].lower()}"><th scope="row">{d}</th><td>8:00 AM – 10:00 PM</td></tr>' for d in DAYS)
    opts=''.join(f'<option>{x["name"]}</option>' for x in SERVICES)
    s+=f'''<section class="sec ct"><div class="wrap ct-g">
<div class="ct-c rv"><h2>Reach us</h2>
<a class="ct-row" href="{D['tel']}">{ic('phone')}<span><b>{D['phone']}</b><small>Tap to call</small></span></a>
<a class="ct-row" href="{D['sms']}">{ic('sms')}<span><b>Text us</b><small>{D['phone']}</small></span></a>
<a class="ct-row" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}<span><b>Book online</b><small>Request a time via Housecall Pro</small></span></a>
<a class="ct-row" href="{MAPS}" target="_blank" rel="noopener">{ic('pin')}<span><b>{D['street']}</b><small>{D['city']}, FL {D['zip']} · Mandarin</small></span></a>
<h3>Hours {live()}</h3><table class="hours"><tbody>{hrs}</tbody></table><p class="note">Holiday hours may differ — Google notes this for Thanksgiving and Black Friday.</p></div>
<form class="qf rv" novalidate><h2>Send a service request</h2><p>Fill this in and it opens a text to Air Element with your details — nothing is sent until you hit send on your phone.</p>
<label>Name<input name="name" autocomplete="name" required></label><label>Phone<input name="phone" type="tel" autocomplete="tel"></label>
<label>Service<select name="service"><option value="">Choose one…</option>{opts}<option>Not sure</option></select></label>
<label>County / area<select name="area"><option value="">Choose…</option>{''.join(f'<option>{c} County</option>' for c in D['counties'])}</select></label>
<label class="full">What’s going on?<textarea name="details" rows="4" placeholder="e.g. A/C running but not cooling, upstairs unit"></textarea></label>
<div class="ctas full"><button class="btn mag" type="submit">{ic('sms')}Text this request</button><a class="btn ghost" href="{BOOK}" target="_blank" rel="noopener">{ic('cal')}Book online instead</a></div></form>
</div></section>
<section class="map-s"><iframe title="Map: Air Element AC and Heating LLC, 10702 Hood Rd Ste 3, Jacksonville FL" src="https://www.google.com/maps?q=Air+Element+Ac+and+Heating+LLC,+10702+Hood+Rd+Ste+3,+Jacksonville,+FL+32257&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></section>'''
    s+=footer(); return s
def page_404():
    s=head('404.html','Page not found | Air Element AC & Heating','This page could not be found.',[]).replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="canonical"')
    s=s.replace('href="assets/','href="/airelementac/assets/').replace('href="brand/','href="/airelementac/brand/')
    n=nav('404.html').replace('href="','href="/airelementac/').replace('/airelementac/tel:','tel:').replace('/airelementac/https://','https://').replace('src="','src="/airelementac/')
    s+=n+f'<section class="phero nf"><div class="wrap"><p class="eyebrow">Error 404</p><h1>This vent <em>leads nowhere.</em></h1><p class="lede">The page you’re after isn’t here. Head home or give us a call.</p><div class="ctas"><a class="btn lg" href="/airelementac/">Back to home</a><a class="btn lg ghost" href="{D["tel"]}">{ic("phone")}{D["phone"]}</a></div></div></section>'
    f=footer().replace('href="','href="/airelementac/').replace('/airelementac/tel:','tel:').replace('/airelementac/https://','https://').replace('/airelementac/services.html#','/airelementac/services.html#').replace('src="','src="/airelementac/')
    return s+f
def llms():
    svc='\n'.join(f'- {x["name"]}: {x["body"]}' for x in SERVICES)
    pg='\n'.join(f'- [{t}]({BASE}{"" if h=="index.html" else h})' for h,t in PAGES)
    rv='\n'.join(f'- {r["n"]} ({r["a"]}): "{r["t"][:240]}{"…" if len(r["t"])>240 else ""}"' for r in REVIEWS[:6])
    return f'''# {D['name']}
> Family-owned HVAC contractor in Mandarin, Jacksonville, Florida: A/C and heating repair, installation, duct work, ductless mini-splits and commercial/rooftop equipment.

- Address: {ADDR} (Mandarin)
- Phone: {D['phone']}
- Book online: {BOOK}
- Hours: 8 AM – 10 PM, Monday through Sunday (holiday hours may differ)
- Service area: Duval, Clay, St. Johns and Nassau counties, FL
- Rating: 5.0 stars from 82 Google reviews
- Florida license: CAC1822512 · BBB Accredited (A+) since 2024-01-31
- Residential and commercial
- Google: {MAPS}
- BBB: {BBB}

## Services
{svc}

## Pages
{pg}

## What customers say (Google reviews, verbatim excerpts)
{rv}
'''
def og():
    from PIL import ImageDraw, ImageFont, ImageFilter
    G='/usr/share/fonts/truetype/sand-box/google/'
    im=Image.new('RGB',(1200,630),(11,17,24))
    ph=Image.open(os.path.join(ROOT,'img','hero-rooftop-m.webp')).convert('RGB'); ph=ph.resize((506,630)); im.paste(ph,(694,0))
    ov=Image.new('RGBA',(1200,630),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for x in range(694,820): d.line([(x,0),(x,630)],fill=(11,17,24,int(255*(1-(x-694)/126))))
    im=Image.alpha_composite(im.convert('RGBA'),ov)
    import cairosvg, io
    lg=Image.open(io.BytesIO(cairosvg.svg2png(url=os.path.join(ROOT,'brand','logo-horizontal-dark.svg'),output_width=560))).convert('RGBA')
    im.alpha_composite(lg,(56,60))
    d=ImageDraw.Draw(im)
    f1=ImageFont.truetype(G+'Unbounded/Unbounded-VariableFont_wght.ttf',50); f1.set_variation_by_axes([800])
    f2=ImageFont.truetype(G+'IBM Plex Mono/IBMPlexMono-SemiBold.ttf',26)
    d.text((60,250),"Cool when it's",font=f1,fill='white'); d.text((60,310),'blazing.',font=f1,fill=(125,216,255))
    d.text((60,370),'Warm when it',font=f1,fill='white'); d.text((60,430),'drops.',font=f1,fill=(255,106,43))
    d.text((60,530),'Jacksonville HVAC · 5.0★ · (904) 440-3389',font=f2,fill=(190,210,228))
    im.convert('RGB').save(os.path.join(OUT,'og.jpg'),quality=86)
def main():
    if os.path.isdir(OUT):
        for n in os.listdir(OUT):
            pth=os.path.join(OUT,n); shutil.rmtree(pth) if os.path.isdir(pth) else os.remove(pth)
    os.makedirs(OUT+'/assets',exist_ok=True)
    shutil.copytree(os.path.join(ROOT,'img'),os.path.join(OUT,'img'))
    os.makedirs(OUT+'/brand'); 
    for f in os.listdir(os.path.join(ROOT,'brand')):
        if f!='brand-sheet.png': shutil.copy(os.path.join(ROOT,'brand',f),os.path.join(OUT,'brand',f))
    for f in ('site.css','site.js'): shutil.copy(os.path.join(ROOT,'src',f),os.path.join(OUT,'assets',f))
    pages={'index.html':page_home(),'services.html':page_services(),'work.html':page_work(),'reviews.html':page_reviews(),'about.html':page_about(),'contact.html':page_contact(),'404.html':page_404()}
    for n,h in pages.items(): open(os.path.join(OUT,n),'w').write(h)
    open(os.path.join(OUT,'llms.txt'),'w').write(llms())
    open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
    today=datetime.date.today().isoformat()
    open(os.path.join(OUT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{"" if h=="index.html" else h}</loc><lastmod>{today}</lastmod></url>' for h,_ in PAGES)+'</urlset>\n')
    open(os.path.join(OUT,'.nojekyll'),'w').write('')
    og(); print('built',list(pages))
if __name__=='__main__': main()
