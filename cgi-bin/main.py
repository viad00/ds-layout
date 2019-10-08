#!/home/vlad/PycharmProjects/123/venv/bin/python3
#!/usr/bin/python3
import os,sys
import cgi
import cgitb
import render
cgitb.enable()
from mpl_toolkits import mplot3d
import numpy as np
from stl import mesh
import matplotlib
matplotlib.use('Agg')
os.environ['HOME'] = '/tmp'
import matplotlib.pyplot as plt
render.header()
# Start

fig = plt.figure(figsize=(8, 12))
ax = plt.axes(projection="3d")
your_mesh = mesh.Mesh.from_file('model1.stl')
collection = mplot3d.art3d.Poly3DCollection(your_mesh.vectors)
collection.set_alpha(0.3)
collection.set_sort_zpos(-2)
ax.add_collection3d(collection)
scale = your_mesh.points.flatten(-1)
ax.auto_scale_xyz(np.array([-6, 44]), np.array([-6, 44]), scale)
render.note('Test 3d heat points')
x_values = (17, 13)
y_values = (7, 18)
z_values = (53, 55)
t_values = (65, 45)
c_values = ('red', 'green')
ax.scatter3D(x_values, y_values, z_values, c=t_values, cmap='jet')
for i in range(len(x_values)):
    render.draw_sphere(ax,x_values[i],y_values[i],z_values[i],c_values[i])
render.png_render(plt)

# End
render.footer()
