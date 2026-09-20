"""assets/templates/*.png -> *.webp（同名）。サイズ上限を超えたら品質を下げる。"""
import glob, os
from PIL import Image
D = os.path.join(os.path.dirname(__file__), "templates")
for png in sorted(glob.glob(os.path.join(D, "*.png"))):
    if png.endswith("-2k.png"):
        continue
    hi = png[:-4] + "-2k.png"
    if os.path.exists(hi):
        png = hi                      # 縦長は2K版を優先（A4印刷向け）
    out = png.replace("-2k.png", ".png")[:-4] + ".webp"
    im = Image.open(png).convert("RGB")
    for q in (84, 78, 72, 66, 60):
        im.save(out, "WEBP", quality=q, method=6)
        if os.path.getsize(out) <= 600 * 1024:
            break
    print(os.path.basename(out), im.size, f"{os.path.getsize(out)//1024}KB q={q}")
