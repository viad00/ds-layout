import io
import base64
import numpy as np

def header():
    print("Content-type: text/html")
    print()
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Plot test</title>
            </head>
            <body>""")
def note(out):
    print("<h1>{}</h1>".format(out))
def png_render(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    print("""<img src="data:image/png;base64,{}">""".format(base64.b64encode(buf.read()).decode('ascii')))
    buf.close()
def svg_render(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format='svg')
    buf.seek(0)
    print(buf.read().decode('utf-8'))
    buf.close()
def draw_sphere(ax,x,y,z,c,r=5):
    u = np.linspace(0, np.pi, 15)
    v = np.linspace(0, 2 * np.pi, 15)
    xc = r*np.outer(np.sin(u), np.sin(v))+x
    yc = r*np.outer(np.sin(u), np.cos(v))+y
    zc = r*np.outer(np.cos(u), np.ones_like(v))+z
    ax.plot_wireframe(xc, yc, zc, color=c, alpha=0.1)
def footer():
    print("""</body>
            </html>""")
