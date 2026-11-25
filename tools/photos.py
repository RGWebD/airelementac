from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import os
P='/workspace/lead3/photos/'; O=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','img')+'/'
def save(im,name,w,q=80):
    im=ImageOps.exif_transpose(im).convert('RGB')
    if im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    im.save(O+name+'.webp','WEBP',quality=q,method=6); print(name,im.size)
# hero: rooftop service call (g06, 1125x2000) — tall frame
save(Image.open(P+'g06.jpg'),'hero-rooftop',1100,80)
save(Image.open(P+'g06.jpg').crop((0,250,1125,1650)),'hero-rooftop-m',900,78)
names={'g01':'trane-condenser','g02':'attic-ducts','g03':'air-handler-ductboard','g04':'garage-air-handler','g05':'minisplit-patio',
 'g07':'commercial-ductwork','g10':'minisplit-porch','g11':'twin-condensers','g12':'condenser-stand','g13':'heat-pump-tall',
 'g14':'package-unit','g15':'closet-air-handler','g16':'attic-flex','g17':'minisplit-outdoor','g18':'package-unit-2',
 'g19':'air-handler-closet','g20':'commercial-condenser'}
for k,n in names.items(): save(Image.open(P+k+'.jpg'),n,1400 if k in('g05','g07','g02') else 1100)
for k,n in {'f03':'trane-air-handler','f05':'attic-air-handler','f06':'minisplit-yard','f08':'condenser-brick'}.items(): save(Image.open(P+k+'.jpg'),n,900,82)
# blueprint (same-photo line drawing) for the compare slider — g04 garage install
im=ImageOps.exif_transpose(Image.open(P+'g04.jpg')).convert('RGB'); im=im.resize((900,round(im.height*900/im.width)),Image.LANCZOS)
im.save(O+'bp-real.webp','WEBP',quality=80,method=6)
g=im.convert('L').filter(ImageFilter.GaussianBlur(1.4)).filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(.8))
mask=g.point(lambda v:255 if v>9 else 0).filter(ImageFilter.MaxFilter(3))
from PIL import ImageDraw
bp=Image.new('RGB',im.size,(10,34,58)); d=ImageDraw.Draw(bp)
for x in range(0,im.width,30): d.line([(x,0),(x,im.height)],fill=(22,58,90),width=1)
for y in range(0,im.height,30): d.line([(0,y),(im.width,y)],fill=(22,58,90),width=1)
bp.paste(Image.new('RGB',im.size,(170,228,255)),(0,0),mask)
bp.save(O+'bp-lines.webp','WEBP',quality=82,method=6); print('bp',im.size)
