import illustris_python as il
import pandas as pd
import numpy as np
import gc

basePath = '/n/holystore01/LABS/hernquist_lab/Lab/IllustrisTNG/Runs/L205n2500TNG/output/'

snap = 50
halo = 1

stars = il.snapshot.loadHalo(basePath,snap,halo,'stars')
df = pd.DataFrame(data=stars['Coordinates'], columns=['X','Y','Z'])
df.insert(3, 'Masses', stars['Masses'])
df.insert(4, 'tForm', stars['GFM_StellarFormationTime'])
df.to_csv('snap%d_halo%d_stars.csv' % (snap, halo), index=False)

del(stars, df)
gc.collect()

dm = il.snapshot.loadHalo(basePath,snap,halo,'dm')
df = pd.DataFrame(data=np.hstack((dm['Coordinates'], dm['Velocities'])), columns=['X','Y','Z','Vx','Vy','Vz'])
df.to_csv('snap%d_halo%d_dm.csv' % (snap, halo), index=False)

del(dm, df)
gc.collect()

gas = il.snapshot.loadHalo(basePath,snap,halo,'gas')
df = pd.DataFrame(data=np.hstack((gas['Coordinates'], gas['Velocities'])), columns=['X','Y','Z','Vx','Vy','Vz'])
df.insert(6, 'Eint', gas['InternalEnergy'])
df.to_csv('snap%d_halo%d_gas.csv' (snap, halo), index=False)

del(gas, df)
gc.collect()
