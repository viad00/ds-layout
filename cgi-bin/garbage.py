plt.plot([1,2,3])
render.note('Test PNG')
render.png_render(plt)
render.note('Test SVG')
render.svg_render(plt)
render.note('Test 3d SVG')

render.svg_render(plt)
render.note('Test 3d model of box')
render.svg_render(plt)