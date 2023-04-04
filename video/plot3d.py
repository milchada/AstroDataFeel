from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
import pandas as pd
 
#Interactive plot works, but VERY slow.
#May be worth it if you're rendering on supercomputer and can remotely access the graphics display 

# Data
datafile = 'snap50_halo1_stars.csv' #change as needed
moviename = 'figures/stars'
df = pd.read_csv(datafile) 
x = df['X'].values
y = df['Y'].values
z = df['Z'].values
tform = df['tForm'].values
tform -= tform.min() #min = 0
tform /= tform.max() #max = 1

# Creating 3D figure
fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = '3d')
ax.scatter3D(x, y, z, c=cm.RdBu_r(tform))
 
# 360 Degree view
'''
==========   ====  ====
view plane   elev  azim
==========   ====  ====
XY           90    -90
XZ           0     -90
YZ           0     0
-XY          -90   90
-XZ          0     90
-YZ          0     180
'''

amin = -180 
amax = 180
emin = -90
emax = 90
for i in range(360):
   dtheta = i/360.
   elev = emin + dtheta*(emax - emin)
   azim = amin + dtheta*(amax - amin)
   ax.view_init(elev, azim)
   plt.savefig('%s_%d.png' % (moviename, i))

import cv2
import os


def generate_video(image_folder= 'figures/', video_name = 'stars.avi', fps=10, baseDir = '/Users/mila/Documents/Outreach/AstroDataFeel/getData'):
    
    os.chdir(baseDir)
      
    images = [img for img in os.listdir(image_folder)
              if img.endswith("png")]
     
    images.sort()
    frame = cv2.imread(os.path.join(image_folder, images[0]))
  
    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape  
  
    video = cv2.VideoWriter(video_name, 0, fps, (width, height)) #10 frames per second
  
    # Appending the images to the video one by one
    for image in images: 
        video.write(cv2.imread(os.path.join(image_folder, image))) 
      
    # Deallocating memories taken for window creation
    cv2.destroyAllWindows() 
    video.release() 
