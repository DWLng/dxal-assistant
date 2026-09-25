from PIL import Image, ImageDraw
import math
def make(size, path):
    im = Image.new("RGB", (size, size), (31, 77, 58))  # 深绿
    d = ImageDraw.Draw(im)
    # 白色指北针星（四芒+细十字）
    cx = cy = size/2
    R = size*0.34
    r = size*0.09
    pts_n = [(cx, cy-R), (cx+r, cy-r), (cx, cy-r*0.2), (cx-r, cy-r)]
    pts_s = [(cx, cy+R), (cx+r, cy+r), (cx, cy+r*0.2), (cx-r, cy+r)]
    pts_e = [(cx+R, cy), (cx+r, cy-r), (cx+r*0.2, cy), (cx+r, cy+r)]
    pts_w = [(cx-R, cy), (cx-r, cy-r), (cx-r*0.2, cy), (cx-r, cy+r)]
    for pts in (pts_n, pts_s, pts_e, pts_w):
        d.polygon(pts, fill=(245, 239, 224))
    d.ellipse([cx-size*0.045, cy-size*0.045, cx+size*0.045, cy+size*0.045], fill=(224, 123, 26))
    # 上下文字带
    fs = int(size*0.13)
    d.text((cx, size*0.115), "北纬53°", anchor="mm", fill=(216, 207, 180), font_size=fs)
    d.text((cx, size*0.885), "找北之旅", anchor="mm", fill=(216, 207, 180), font_size=fs)
    im.save(path)
make(192, "/tmp/dxal_app/icon-192.png")
make(512, "/tmp/dxal_app/icon-512.png")
print("icons ok")
