from astroquery.mast import Catalogs

#https://mast.stsci.edu/api/v0/pages.html

catalog_data = Catalogs.query_region("158.47924 -7.30962", radius=1, catalog="Gaia", version=2)
keys = ['ra', 'dec', 'pmra', 'pmdec', 'parallax']
#distance_pc = 1/parallax_arcsec

import sdss
ra = 179.689293428354
dec = -0.454379056007667
reg = sdss.Region(ra, dec, fov=300, opt='')
df_sp = reg.nearest_spects()
df_sp = df_sp[df_sp['class']=='GALAXY']
