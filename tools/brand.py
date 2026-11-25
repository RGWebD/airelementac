"""Air Element AC & Heating — vector brand kit (RGWebD). Text converted to paths with fontTools."""
import math, os, io
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import cairosvg
from PIL import Image, ImageDraw, ImageFont
G='/usr/share/fonts/truetype/sand-box/google/'
O=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','brand'); os.makedirs(O,exist_ok=True)
def vf(path,w):
    f=TTFont(path); return instancer.instantiateVariableFont(f,{'wght':w})
UNB=vf(G+'Unbounded/Unbounded-VariableFont_wght.ttf',800)
UNB6=vf(G+'Unbounded/Unbounded-VariableFont_wght.ttf',600)
MONO=TTFont(G+'IBM Plex Mono/IBMPlexMono-SemiBold.ttf')
ICE='#7DD8FF'; ICE2='#2FA8E6'; EMB='#FF6A2B'; EMB2='#FF9A3C'; SLATE='#0B1118'; FROST='#EAF6FF'
def text_path(font,s,size,x,y,track=0):
    gs=font.getGlyphSet(); cmap=font.getBestCmap(); upm=font['head'].unitsPerEm; sc=size/upm
    pen=SVGPathPen(gs); cx=0
    for ch in s:
        g=cmap.get(ord(ch))
        if g is None: continue
        tp=TransformPen(pen,(sc,0,0,-sc,x+cx,y)); gs[g].draw(tp)
        cx+=gs[g].width*sc+track
    return pen.getCommands(), cx-track
def width(font,s,size,track=0): return text_path(font,s,size,0,0,track)[1]
def arc(cx,cy,r,a0,a1):
    p=lambda a:(cx+r*math.sin(math.radians(a)),cy-r*math.cos(math.radians(a)))
    x0,y0=p(a0);x1,y1=p(a1);large=1 if abs(a1-a0)>180 else 0
    return f'M{x0:.2f} {y0:.2f}A{r} {r} 0 {large} 1 {x1:.2f} {y1:.2f}'
def emblem(mode='color',fav=False,disc=True):
    """200x200 thermostat-dial emblem with the 'ae' monogram from their sign."""
    a_col,e_col,ring_l,ring_r,bg=ICE,EMB,ICE,EMB,SLATE
    if mode=='white': a_col=e_col=ring_l=ring_r='#FFFFFF'
    if mode=='slate': a_col=e_col=ring_l=ring_r=SLATE
    sw=20 if fav else 13; r=78 if fav else 80
    parts=[]
    if disc and mode=='color': parts.append(f'<circle cx="100" cy="100" r="99" fill="{bg}"/>')
    parts.append(f'<path d="{arc(100,100,r,-138,-7)}" fill="none" stroke="{ring_l}" stroke-width="{sw}" stroke-linecap="round"/>')
    parts.append(f'<path d="{arc(100,100,r,7,138)}" fill="none" stroke="{ring_r}" stroke-width="{sw}" stroke-linecap="round"/>')
    if not fav:  # dial ticks
        for i in range(-120,121,20):
            if abs(i)<10: continue
            a=math.radians(i); r1,r2=60,66
            c=ring_l if i<0 else ring_r
            parts.append(f'<line x1="{100+r1*math.sin(a):.2f}" y1="{100-r1*math.cos(a):.2f}" x2="{100+r2*math.sin(a):.2f}" y2="{100-r2*math.cos(a):.2f}" stroke="{c}" stroke-width="3" stroke-linecap="round" opacity=".75"/>')
        parts.append(f'<circle cx="100" cy="{100-r}" r="5" fill="{"#fff" if mode=="color" else ring_l}"/>')
    size=92 if fav else 78
    wa=width(UNB,'a',size); we=width(UNB,'e',size); ov=size*0.16
    tot=wa+we-ov; x0=100-tot/2; base=100+size*0.36
    pa,_=text_path(UNB,'a',size,x0,base); pe,_=text_path(UNB,'e',size,x0+wa-ov,base)
    parts.append(f'<path d="{pa}" fill="{a_col}"/>')
    if mode=='color':  # knock-out seam where e overlaps a
        parts.append(f'<path d="{pe}" fill="none" stroke="{SLATE}" stroke-width="7" stroke-linejoin="round"/>')
    parts.append(f'<path d="{pe}" fill="{e_col}"/>')
    return ''.join(parts)
def svg(w,h,body,bg=None):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{b}{body}</svg>'
def wordmark(x,y,col_main,col_sub,col_accent,big=58,center=False,total_w=None):
    t1='AIR ELEMENT'; t2='AC & HEATING, LLC'
    tr1=big*0.02; w1=width(UNB,t1,big,tr1)
    sub=big*0.34; tr2=sub*0.42; w2=width(MONO,t2,sub,tr2)
    ox=x-(w1/2 if center else 0)
    p1,_=text_path(UNB,t1,big,ox,y,tr1)
    ox2=x-(w2/2 if center else 0)
    p2,_=text_path(MONO,t2,sub,ox2,y+sub*1.9,tr2)
    lx=ox2-(0 if center else 0)
    bar=''
    if not center: bar=f'<rect x="{ox+w2+sub*.6:.1f}" y="{y+sub*1.9-sub*.42:.1f}" width="{max(0,w1-w2-sub*.6):.1f}" height="{sub*.16:.1f}" rx="{sub*.08:.1f}" fill="url(#g)"/>'
    return f'<path d="{p1}" fill="{col_main}"/><path d="{p2}" fill="{col_sub}"/>{bar}', w1
GRAD=f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{ICE}"/><stop offset="1" stop-color="{EMB}"/></linearGradient></defs>'
def horizontal(theme='dark'):
    main={'dark':'#FFFFFF','light':SLATE,'white':'#FFFFFF','slate':SLATE}[theme]
    sub={'dark':'#9FB3C8','light':'#4A5B6E','white':'#FFFFFF','slate':SLATE}[theme]
    em_mode='color' if theme in('dark','light') else theme
    wm,w1=wordmark(230,108,main,sub,EMB,58)
    W=int(230+w1+20)
    body=GRAD+f'<g transform="translate(10,10)">{emblem(em_mode)}</g>'+wm
    if theme in('white','slate'): body=body.replace('url(#g)',main)
    return svg(W,220,body)
def stacked(theme='dark'):
    main={'dark':'#FFFFFF','light':SLATE,'white':'#FFFFFF','slate':SLATE}[theme]
    sub={'dark':'#9FB3C8','light':'#4A5B6E','white':'#FFFFFF','slate':SLATE}[theme]
    em_mode='color' if theme in('dark','light') else theme
    wm,w1=wordmark(0,0,main,sub,EMB,50,center=True)
    W=int(w1+40)
    body=GRAD+f'<g transform="translate({W/2-100:.1f},10)">{emblem(em_mode)}</g><g transform="translate({W/2:.1f},280)">{wm}</g>'
    return svg(W,340,body)
def write(name,s): open(os.path.join(O,name),'w').write(s)
def png(s,name,w):
    cairosvg.svg2png(bytestring=s.encode(),write_to=os.path.join(O,name),output_width=w)
if __name__=='__main__':
    for t in ['dark','light','white','slate']:
        write(f'logo-horizontal-{t}.svg',horizontal(t)); write(f'logo-stacked-{t}.svg',stacked(t))
    write('emblem.svg',svg(200,200,emblem('color')))
    write('emblem-white.svg',svg(200,200,emblem('white')))
    write('emblem-slate.svg',svg(200,200,emblem('slate')))
    fav=svg(200,200,emblem('color',fav=True)); write('favicon.svg',fav)
    for s in [16,32,48,180,192,512]: png(fav if s<=48 else svg(200,200,emblem('color')),f'favicon-{s}.png',s)
    Image.open(os.path.join(O,'favicon-48.png')).save(os.path.join(O,'favicon.ico'),sizes=[(16,16),(32,32),(48,48)])
    png(horizontal('dark'),'logo-horizontal-dark-1200.png',1200); png(horizontal('light'),'logo-horizontal-light-1200.png',1200)
    png(svg(200,200,emblem('color')),'emblem-1024.png',1024)
    # presentation sheet
    S=Image.new('RGB',(2000,1500),'#EEF3F7'); d=ImageDraw.Draw(S)
    def paste(svgs,w,xy,bg=None):
        b=io.BytesIO(cairosvg.svg2png(bytestring=svgs.encode(),output_width=w)); im=Image.open(b).convert('RGBA')
        if bg: box=Image.new('RGBA',(bg[2],bg[3]),bg[4]); S.paste(box,(bg[0],bg[1]))
        S.paste(im,xy,im)
    paste(horizontal('dark'),900,(80,110),(40,60,1000,380,SLATE))
    paste(horizontal('light'),900,(1060,110),(1040,60,1000,380,'#FFFFFF'))
    paste(stacked('dark'),420,(110,500),(40,460,560,520,SLATE))
    paste(stacked('light'),420,(630,500),(580,460,520,520,'#FFFFFF'))
    paste(svg(200,200,emblem('color')),210,(1205,480),(1120,460,380,250,'#1A2633'))
    paste(svg(200,200,emblem('white')),220,(1200,740),(1120,720,380,260,EMB))
    paste(svg(200,200,emblem('slate')),220,(1590,740),(1520,720,440,260,'#FFFFFF'))
    for i,s in enumerate([16,32,48,180]):
        im=Image.open(os.path.join(O,f'favicon-{s}.png')).convert('RGBA'); S.paste(im,(1560+[0,40,100,170][i],560-s//2+40),im)
    try:
        F=ImageFont.truetype(G+'IBM Plex Mono/IBMPlexMono-SemiBold.ttf',26); FT=ImageFont.truetype(G+'IBM Plex Mono/IBMPlexMono-Bold.ttf',34)
    except Exception: F=FT=ImageFont.load_default()
    d.text((40,14),'AIR ELEMENT AC & HEATING — BRAND SHEET (RGWebD redraw of the “ae” sign mark)',font=FT,fill=SLATE)
    sw=[('Deep Slate',SLATE),('Frost',FROST),('Ice',ICE),('Ice Deep',ICE2),('Ember',EMB),('Ember Glow',EMB2)]
    for i,(n,c) in enumerate(sw):
        x=40+i*325; d.rounded_rectangle((x,1020,x+300,1250),18,fill=c,outline='#C9D4DE',width=2)
        d.text((x+10,1265),n,font=F,fill=SLATE); d.text((x+10,1300),c,font=F,fill='#4A5B6E')
    d.text((40,1380),'Type: Unbounded 800 (display) · Manrope (body) · IBM Plex Mono (readouts)   Favicons 16/32/48/180/192/512 + .ico',font=F,fill=SLATE)
    S.save(os.path.join(O,'brand-sheet.png')); print('ok')
