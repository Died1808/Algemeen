import os
import math
import numpy as np
import pandas as pd
import peakutils
import matplotlib.pyplot as plt
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point

params = {'font.family': 'sans-serif',
          'font.sans-serif': 'arial',
          'axes.labelsize': 10,
          'axes.facecolor': '#ffffff', 
          'axes.labelcolor': 'black',
          'legend.fontsize': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'lines.linewidth': 1,
          'grid.color': 'grey',
          'grid.linestyle': 'dashed',
          'grid.linewidth': 0.5,
          'text.usetex': False,
          'font.style': 'normal',
          'font.variant':'normal',
          'figure.facecolor': 'white',
          'font.size':8,
          'figure.autolayout': True,
          'figure.figsize': (3,8),
          'figure.dpi': 100,
          }
plt.rcParams.update(params)
#
Rg = Polygon([(0.01,11),(0.01,70),(0.31,70),(0.41,48),(0.42,45),(0.41,21),(0.41,11)])
Rm = Polygon([(0.01,11),(0.01,3.4),(0.58,3.4),(0.77,3.9),(0.41,11)])
Rl = Polygon([(2.1,1.2),(1.7,1.7),(1,2.2),(0.77,3.9),(0.58,3.4),(0.01,3.4),(0.01,1.2)])
Xg = Polygon([(0.41,48),(0.42,45),(0.41,21),(0.41,11),(0.7,13),(0.88,19),(0.72,30)])
Xm = Polygon([(0.41,11),(0.77,3.9),(1.4,5.4),(1,10),(0.9,14),(0.88,19),(0.7,13)])
Xl = Polygon([(1.4,5.4),(1.9,2.8),(3.2,1.4),(2.1,1.2),(1.7,1.7),(1,2.2),(0.77,3.9)])
Og = Polygon([(0.88,19),(0.72,30),(0.41,48),(0.31,70),(0.69,75),(1,71),(1.4,76),(1.5,50),(1.5,42),(1.4,32),(1.4,21)])
Om = Polygon([(1.4,5.4),(1,10),(0.9,14),(0.88,19),(1.4,21),(1.6,14),(2,6)])
Ol = Polygon([(4.1,1.4),(2.2,2.8),(2.1,4.1),(2,6),(1.4,5.4),(1.9,2.8),(3.2,1.4)])
Glag = Polygon([(1.4,76),(1.5,50),(1.5,42),(1.4,32),(1.4,21),(1.6,14),(2,16),(2.4,18),(3.1,17),(3.4,22),(3.1,32),(3.2,40),(3.1,60),(1.8,78)])
Glaug = Polygon([(3.1,17),(3.4,22),(3.1,32),(3.2,40),(3.1,60),(4.2,47),(5,40),(5.2,12)])
Tert = Polygon([(5,40),(8,20),(15,8),(5.2,12)])
Glam = Polygon([(2,6),(1.6,14),(2,16),(2.2,10),(3.8,6),(4.1,4.6)])
Glauz = Polygon([(2,16),(2.2,10),(3.8,6),(4.1,4.6),(5,7),(5.2,12),(3.1,17),(2.4,18)])
Conk = Polygon([(4.1,4.6),(5,7),(5.2,12),(15,8),(30,1.4),(15,1.4),(7.2,2.5),(6.3,3.2)])
Glal = Polygon([(2,6),(4.1,4.6),(6.3,3.2),(7.2,2.5),(15,1.4),(4.1,1.4),(2.2,2.8),(2.1,4.1)])
Xkl = Polygon([(2.1,1.2),(3.2,1.4),(4.1,1.4),(7,1.05),(10,0.7),(4.7,1.05),(4,1.05),(3.5,0.8)])
KV = Polygon([(2.1,0.3),(3,0.6),(3.5,0.8),(4,1.05),(4.7,1.05), (10,0.7),(4.92,0.3)])
XVkl = Polygon([(1.0,0.3),(1.6,0.6),(2.1,1.2),(3.5,0.8),(2.1,0.3)])
Rkl = Polygon([(0.01,1.2),(0.1,1.2),(0.2,1.0),(1.0,0.3),(1.6,0.6),(2.1,1.2)])
Vkl = Polygon([(7,1.05),(4.1,1.4),(7,1.4),(30,1.4),(40,0.70),(10,0.70)])
V = Polygon([(1.0,0.30),(3,0.1),(10,0.01), (40,0.01),(40,0.70),(10,0.70),(4.92,0.3)])
Los= Polygon([(0.01,1.2),(0.1,1.2),(0.2,1.0),(0.5,0.5),(1,0.3),(3,0.1),(10,0.01), (0.01,0.01)])
#

class GEF:
    def __init__(self):
        self._data_seperator = ' '
        self._columns = {}
        self.x = 0.
        self.y = 0.
        self.z = 0.
        self.dz = []
        self.qc = []
        self.pw = []
        self.wg = []
        self.c  = []
        self.kb = []
        self.grof  = []
        self.matig = []
        self.matigfijn=[]
        self.fijn  = []
        self.leem  = []
        self.klei  = []
        self.veen  = []
#
        self.Rgc   = []
        self.Xgc   = []
        self.Ogc   = []
        self.Glagc = []
        self.Glaugc =[]
        self.Rmc   = []
        self.Xmc   = []
        self.Omc   = []
        self.Glamc = []
        self.Glauzc= []
        self.Conkc = []
        self.Glalc = []
        self.Olc   = []
        self.Xlc   = []
        self.Rlc   = []
        self.Xklc  = []
        self.Rklc  = []
        self.Vklc  = []
        self.Vc    = []
        self.Tertc = []
        self.Losc  = []
        self.XVklc = []
        self.KVc   = []
#        
        
    def readFile(self, filename):
        lines = open(filename, 'r').readlines()
        for line in lines:
            reading_header = True
        for line in lines:            
            if reading_header:
                self._parseHeaderLine(line)
            else:
                self._parseDataLine(line)
            if line.find('#EOH') > -1:
                if self._check_header():
                    reading_header = False
                else:
                    print(filename,'fout in GEF')
                    return
            
    def _check_header(self):
        if not 1 in self._columns:
            return False
        if not 2 in self._columns:
            return False
        return True
    
    def _parseHeaderLine(self, line):
        if '#COMMENT'in line:
            return
        if 'Peil='in line:
            return        
        if 'uitvoerder'in line:
            return                
        if 'materieel'in line:
            return                
        if 'WATERSTAND'in line:
            return  
        if 'opmerkingen#MEASUREMENTTEXT'in line:
            return    
        if '==' in line:
            return        
        if '= NAP' in line:
            return      
        if '/' in line:
            return     

        if len(line.split()) == 0:
            return
        
        
        keyword, argline = line.split('=')             
      
        keyword = keyword.strip()
        argline = argline.strip()
        if '#XYID' in line:
            argline = argline.replace('.','')        
                
        args = argline.split(',')
        if keyword=='#XYID':
            self.x = float(args[1])
            self.y = float(args[2])
        elif keyword=='#ZID':
            self.z = round(float(args[1]),3)
            
        elif keyword=='#COLUMNINFO':
            column = int(args[0])
            dtype = int(args[-1])
            if dtype==11:
                dtype = 10
            self._columns[dtype] = column - 1    
       
    def _parseDataLine(self, line):
        line=line.strip()
        line = line.replace('|',' ')
        line = line.replace(';',' ')
        line = line.replace('!',' ')
        line = line.replace(':',' ')
        args=line.split()
        for n, i in enumerate(args):
            if i == '9.9990e+003':
                args[n] = '0.'
        for n, i in enumerate(args):
            if i == '-9999.9900':
                args[n] = '0.'
        for n, i in enumerate(args):
            if i == '-1.0000e+007':
                args[n] = '0.'
        for n, i in enumerate(args):
            if i == '-99999':
                args[n] = '0.'
        for n, i in enumerate(args):
            if i == '-99999.0':
                args[n] = '0.'                
        for n, i in enumerate(args):
            if i == '-99999.00':
                args[n] = '0.' 
        for n, i in enumerate(args):
            if i == '-99999.000':
                args[n] = '0.'                
        for n, i in enumerate(args):
            if i == '-9.9990e+003':
                args[n] = '0.'
        for n, i in enumerate(args):
            if i == '999.000':
                args[n] = '0.' 
        for n, i in enumerate(args):
            if i == '-9999.99':
                args[n] = '0.'        
        for n, i in enumerate(args):
            if i == '999.999':
                args[n] = '0.'        

        if len(line.split()) == 0:
            return
        z  = abs(float(args[self._columns[1]]))
        dz = self.z - z
        qc = float(args[self._columns[2]])

        slope    =  0.0104
        intercept=  0.0190
                         
        try:
            pw = float(args[self._columns[3]])
            if pw < 1e-3:
                pw=0.003
            elif pw>20:
                pw=slope*qc+intercept   
        except IndexError:
            return                
        except KeyError: #Deze regel maakt van een tweekolommer een driekolommer
            pw=slope*qc+intercept

        self.dz.append(dz)
        self.qc.append(qc)
        self.pw.append(pw)
        
        if qc<=0.001:
            qc=0.1
            self.wg.append(10.)
        else:
            wg = abs((pw / qc) * 100.)

        wg = abs((pw / qc) * 100.)
        
        
#
        point=Point(wg,qc)
#
        if Xm.contains(point) ==True:
            Xmc=1.
        else:
            Xmc=-1.
        self.Xmc.append(Xmc)
#            
        if Rg.contains(point) ==True:
            Rgc=1.
        else:
            Rgc=-1.
        self.Rgc.append(Rgc)
#
        if Xg.contains(point) ==True:
            Xgc=1.
        else:
            Xgc=-1.
        self.Xgc.append(Xgc)
#
        if Og.contains(point) ==True:
            Ogc=1.
        else:
            Ogc=-1.
        self.Ogc.append(Ogc)
#            
        if Glag.contains(point) ==True:
            Glagc=1.
        else:
            Glagc=-1.
        self.Glagc.append(Glagc)
#
        if Glaug.contains(point) ==True:
            Glaugc=1.
        else:
            Glaugc=-1.
        self.Glaugc.append(Glaugc)
#            
        if Rm.contains(point) ==True:
            Rmc=1.
        else:
            Rmc=-1.
        self.Rmc.append(Rmc)
#
        if Om.contains(point) ==True:
            Omc=1.
        else:
            Omc=-1.
        self.Omc.append(Omc)
#
        if Glam.contains(point) ==True:
            Glamc=1.
        else:
            Glamc=-1.
        self.Glamc.append(Glamc)
#            
        if Glauz.contains(point) ==True:
            Glauzc=1.
        else:
            Glauzc=-1.
        self.Glauzc.append(Glauzc)
#
        if Conk.contains(point) ==True:
            Conkc=1.
        else:
            Conkc=-1.
        self.Conkc.append(Conkc)
#
        if Ol.contains(point) ==True:
            Olc=1.
        else:
            Olc=-1.
        self.Olc.append(Olc)
#            
        if Glal.contains(point) ==True:
            Glalc=1.
        else:
            Glalc=-1.
        self.Glalc.append(Glalc)
#
        if Xl.contains(point) ==True:
            Xlc=1.
        else:
            Xlc=-1.
        self.Xlc.append(Xlc)
#            
        if Rl.contains(point) ==True:
            Rlc=1.
        else:
            Rlc=-1.
        self.Rlc.append(Rlc)
#
        if Xkl.contains(point) ==True:
            Xklc=1.
        else:
            Xklc=-1.
        self.Xklc.append(Xklc)
#
        if Rkl.contains(point) ==True:
            Rklc=1.
        else:
            Rklc=-1.
        self.Rklc.append(Rklc)
#            
        if Vkl.contains(point) ==True:
            Vklc=1.
        else:
            Vklc=-1.
        self.Vklc.append(Vklc)
#
        if V.contains(point) ==True:
            Vc=1.
        if V.intersects(point) ==True:
            Vc=1.
        else:
            Vc=-1.
        self.Vc.append(Vc)
#
        if Tert.contains(point) ==True:
            Tertc=1.
        else:
            Tertc=-1.
        self.Tertc.append(Tertc)
#
        if Los.contains(point) ==True:
            Losc=1.
        else:
            Losc=-1.
        self.Losc.append(Losc)
#
        if XVkl.contains(point) ==True:
            XVklc=1.
        else:
            XVklc=-1.
        self.XVklc.append(XVklc)
#
        if KV.contains(point) ==True:
            KVc=1.
        else:
            KVc=-1.
        self.KVc.append(KVc)
##########        
        if wg>=0.0:
            if wg >20:
                wg=20
            ke=math.exp(wg)
        if ke <=0:
            ke=1
        else:
            kb  = (qc / ke)*1.45 
            if kb > 40:
                kb=40.
            self.kb.append(kb)

            c=1/(kb)
            if c > 15:
                c=15.
            if wg>4:
                c=c/10
            else:
                c=c*2
            self.c.append(c)       

        if wg > 2.7 and qc<0.32:
            veen = 50*kb
        else:
            veen = -kb
            
        if kb > 20.:
            grof = 0
        else:
            grof = -kb
        self.grof.append(grof)

        if  kb <= 20. and kb > 10.:
            matig = 0
        else:
            matig = -kb
        self.matig.append(matig)

        if  kb <= 10. and kb >5. :
            matigfijn = 0
        else:
            matigfijn = -kb
        self.matigfijn.append(matigfijn)
        
        if  kb <= 5. and kb >1 :
            fijn = 0
        else:
            fijn = -kb
        self.fijn.append(fijn)
        
        if kb<=1 and kb>0.1:
            leem = kb
        else:
            leem=-kb
        self.leem.append(leem)
        
        if veen== 0:
            klei = -kb
        else:
            if  kb <= 0.1 and kb > 0: 
                klei = kb
            else:
                klei = -kb
        self.veen.append(veen)   
        self.klei.append(klei)

    def asNumpy(self):
        return np.transpose(np.array([self.dz, self.c, self.kb, self.grof, self.matig, self.matigfijn, self.fijn, self.leem, self.klei, self.veen,
                                      self.Xmc, self.Rgc, self.Xgc, self.Ogc, self.Glagc, self.Glaugc, 
                                      self.Rmc, self.Omc, self.Glamc, self.Glauzc, self.Conkc, self.Olc, self.Glalc,
                                      self.Xlc, self.Rlc, self.Xklc, self.Rklc, self.Vklc, self.Vc, self.Tertc, self.Losc, 
                                      self.XVklc, self.KVc]))


    def asDataFrame(self):
        a = self.asNumpy()
        return pd.DataFrame(data=a, columns=['depth','c', 'k', 'g','m','mf', 'f', 'le','kl','v',
                                             'Xm','Rg','Xg', 'Og', 'Glag','Glaug','Rm','Om','Glam',
                                             'Glauz','Conk','Ol', 'Glal', 'Xl','Rl','Xkl','Rkl','Vkl',
                                             'V', 'Tert', 'Los', 'XVkl','KV'])
        
    def plt(self, filename):
        df = self.asDataFrame()
        df = df.sort_values('depth', ascending=False)
        if df.empty:
            print(filename,'fout in GEF')
            return df
        dzend=round(df.loc[df.index[-1],'depth'],1)
        df.at[df.index[-1],'k']= 'nan'
        ymax=int((round(self.z,-1))+10)
#        ymax=5
        ymin=ymax-60
        ds=5 #dit bepaalt de afstand op de y-as in de grafiek
# 
        df=df[df.depth <=ymax]
        df=df[df.depth >=ymin]
        if dzend <= ymin:
            dzend = ymin
        if df.empty:
            print(filename,'fout in GEF')
            return
            
        try:
            dist=df.iloc[4,0]-df.iloc[5,0]
            dataq=np.array(np.arange(ymax,dzend,dist))
        except (IndexError, ValueError):
            print(filename,'fout in GEF')
            return
        
        dfq=pd.DataFrame(data=dataq, columns=['depth'])
        dfq=dfq.assign(k=np.nan) 
        dfq=dfq.sort_values(by=['depth'], ascending=False)
#        
        dfnew=pd.merge(df,dfq,on='depth', how='outer')
        dfnew=dfnew.sort_values(by=['depth'], ascending=False)
        dfnew=dfnew.drop(columns=['k_y'])
        dfnew=dfnew.rename(index=str, columns={"k_x": "k"})
#
        dfnew.iloc[[0], np.r_[1:31:1]] = -1
#        
        dfnew['k']   = dfnew['k'].ffill()
        dfnew['c']   = dfnew['c'].ffill()
        dfnew['g']   = dfnew['g'].ffill()
        dfnew['m']   = dfnew['m'].ffill()
        dfnew['mf']  = dfnew['mf'].ffill()
        dfnew['f']   = dfnew['f'].ffill()
        dfnew['le']  = dfnew['le'].ffill()
        dfnew['kl']  = dfnew['kl'].ffill()
        dfnew['v']   = dfnew['v'].ffill()
        dfnew['Xm']  = dfnew['Xm'].ffill()
        dfnew['Rg']  = dfnew['Rg'].ffill()
        dfnew['Xg']  = dfnew['Xg'].ffill()
        dfnew['Og']  = dfnew['Og'].ffill()
        dfnew['Glag']= dfnew['Glag'].ffill()
        dfnew['Glaug']= dfnew['Glaug'].ffill()
        dfnew['Rm']  = dfnew['Rm'].ffill()
        dfnew['Om']  = dfnew['Om'].ffill()
        dfnew['Glam']= dfnew['Glam'].ffill()
        dfnew['Glauz']= dfnew['Glauz'].ffill()
        dfnew['Conk']= dfnew['Conk'].ffill()
        dfnew['Ol']  = dfnew['Ol'].ffill()
        dfnew['Glal']= dfnew['Glal'].ffill()
        dfnew['Xl']  = dfnew['Xl'].ffill()
        dfnew['Rl']  = dfnew['Rl'].ffill()
        dfnew['Xkl'] = dfnew['Xkl'].ffill()
        dfnew['Rkl'] = dfnew['Rkl'].ffill()
        dfnew['Vkl'] = dfnew['Vkl'].ffill()
        dfnew['V']   = dfnew['V'].ffill()
        dfnew['Tert']= dfnew['Tert'].ffill()
        dfnew['Los'] = dfnew['Los'].ffill()
        dfnew['XVkl'] = dfnew['XVkl'].ffill()
        dfnew['KV'] = dfnew['KV'].ffill()

#
        df = dfnew
        df = df.reset_index(drop=True)
        df2 = df.set_index("depth", drop = False)
#
        KD_fact=1.0   #Deze waarde is om de KD-waarde in lijn te brengen met de output. Door het samenvoegen van dataframes ontstaat deze correctie
#                   In de Reeshof is de gemiddelde afwijking pompproef-sondering 1.5, De bovenstaande factor 1.5 is doorvermenigvuldigd  
        #Top_klei1
        if self.z > ymax:
            self.z=ymax #hier wordt voorkomen dat de Top_zand1 boven de grafiek ligt als ymax < self.z is
        sudf=df2.query('depth < @self.z')
        subdf=sudf.query('0<k<0.1')

        try:
            Top_klei1 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei1=self.z
            sudf=df2.query('@dzend < depth < @Top_klei1')
            subdf=sudf.query('k>1')
            KD_zand1= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei1 - self.z)),0)

        sudf=df2.query('@Top_klei1 < depth < @self.z')
        subdf=sudf.query('k>0.1')
        KD_zand1= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei1 - self.z)),0)

        
        #OZ_klei1
        sudf=df2.query('depth < @Top_klei1')
        subdf=sudf.query('k>1')

        try:
            OZ_klei1=round((subdf.iloc[0,0]),3) 
        except IndexError:
            OZ_klei1= dzend
            sudf=df2.query('@OZ_klei1 < depth < @Top_klei1')
            subdf=sudf.query('c>1')
            w_klei1=round((subdf['c'].sum()/3),0)
            pass
        
        #c waarde klei1   
        sudf=df2.query('@OZ_klei1 < depth < @Top_klei1')
        subdf=sudf.query('c>1')
        w_klei1=round((subdf['c'].sum()/3),0)
        if Top_klei1==self.z:
            sudf=df2.query('@OZ_klei1 < depth < @self.z')
            subdf=sudf.query('c>1')
            w_klei1=round((subdf['c'].sum()/3),0)
       #Top klei2
        sudf=df2.query('depth < @OZ_klei1')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei2 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei2=dzend        
            sudf=df2.query('@dzend < depth < @OZ_klei1')
            subdf=sudf.query('k>1')

            KD_zand2= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei2 - OZ_klei1)),0)
            Spr_pakket1=round(math.sqrt(KD_zand1*w_klei1),0)
            pass
        
        sudf=df2.query('@Top_klei2 < depth < @OZ_klei1') 
        subdf=sudf.query('k>0')
        KD_zand2= KD_fact*round(((subdf['k'].mean()))*(abs(OZ_klei1 - Top_klei2)),0)
        Spr_pakket1=round(math.sqrt(KD_zand1*w_klei1),0)
        
        #OZ_klei2
        sudf=df2.query('depth < @Top_klei2')
        subdf=sudf.query('k>1')
        try:
            OZ_klei2=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei2= dzend
            sudf=df2.query('@OZ_klei2 < depth < @Top_klei2')
            subdf=sudf.query('c>1')
            w_klei2=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei2   
        sudf=df2.query('@OZ_klei2 < depth < @Top_klei2')
        subdf=sudf.query('c>1')
        w_klei2=round((subdf['c'].sum()/3),0)

       #Top klei3
        sudf=df2.query('depth < @OZ_klei2')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei3 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei3=dzend        
            sudf=df2.query('@dzend < depth < @OZ_klei2')
            subdf=sudf.query('k>1')
            KD_zand3= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei3 - OZ_klei2)),0)
            Spr_pakket2=round(math.sqrt(KD_zand1*w_klei2),0)
            pass
        
        sudf=df2.query('@Top_klei3 < depth < @OZ_klei2') 
        subdf=sudf.query('k>1')
        KD_zand3= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei3- OZ_klei2)),0)
        Spr_pakket2=round(math.sqrt(KD_zand1*w_klei2),0)
        
        #OZ_klei3
        sudf=df2.query('depth < @Top_klei3')
        subdf=sudf.query('k>1')
        try:
            OZ_klei3=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei3= dzend
            sudf=df2.query('@OZ_klei3 < depth < @Top_klei3')
            subdf=sudf.query('c>1')
            w_klei3=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei3   
        sudf=df2.query('@OZ_klei3 < depth < @Top_klei3')
        subdf=sudf.query('c>1')
        w_klei3=round((subdf['c'].sum()/3),0)

       #Top klei4
        sudf=df2.query('depth < @OZ_klei3')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei4 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei4=dzend        
            sudf=df2.query('@dzend < depth < @OZ_klei3')
            subdf=sudf.query('k>1')
            KD_zand4= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei4 - OZ_klei3)),0)
            Spr_pakket3=round(math.sqrt(KD_zand4*w_klei3),0)
            pass
        
        sudf=df2.query('@Top_klei4 < depth < @OZ_klei3') 
        subdf=sudf.query('k>1')
        KD_zand4= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei4 - OZ_klei3)),0)
        Spr_pakket3=round(math.sqrt(KD_zand4*w_klei3),0)
        
        #OZ_klei4
        sudf=df2.query('depth < @Top_klei4')
        subdf=sudf.query('k>1')
        try:
            OZ_klei4=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei4= dzend
            sudf=df2.query('@OZ_klei4 < depth < @Top_klei4') 
            subdf=sudf.query('c>1')
            w_klei4=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei4   
        sudf=df2.query('@OZ_klei4 < depth < @Top_klei4')
        subdf=sudf.query('c>1')
        w_klei4=round((subdf['c'].sum()/3),0)

       #Top klei5
        sudf=df2.query('depth < @OZ_klei4')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei5 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei5=dzend        
            sudf=df2.query('@Top_klei5 < depth < @OZ_klei4')
            subdf=sudf.query('k>1')
            KD_zand5= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei5 - OZ_klei4)),0)
            Spr_pakket4=round(math.sqrt(KD_zand5*w_klei4),0)
            pass
        
        sudf=df2.query('@Top_klei5 < depth < @OZ_klei4') 
        subdf=sudf.query('k>1')
        KD_zand5= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei5 - OZ_klei4)),0)
        Spr_pakket4=round(math.sqrt(KD_zand5*w_klei4),0)
        
        #OZ_klei5
        sudf=df2.query('depth < @Top_klei5')
        subdf=sudf.query('k>1')
        try:
            OZ_klei5=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei5= dzend
            sudf=df2.query('@OZ_klei5 < depth < @Top_klei5') 
            subdf=sudf.query('0<k<0.1')
            w_klei5=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei5   
        sudf=df2.query('@OZ_klei5 < depth < @Top_klei5')
        subdf=sudf.query('0<k<0.1')
        w_klei5=round((subdf['c'].sum()/3),0)


       #Top klei6
        sudf=df2.query('depth < @OZ_klei5')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei6 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei6=dzend        
            sudf=df2.query('@Top_klei6 < depth < @OZ_klei5')
            subdf=sudf.query('k>1')
            KD_zand6= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei6 - OZ_klei5)),0)
            Spr_pakket5=round(math.sqrt(KD_zand6*w_klei5),0)
            pass
        
        sudf=df2.query('@Top_klei6 < depth < @OZ_klei5') 
        subdf=sudf.query('k>1')
        KD_zand6= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei6 - OZ_klei5)),0)
        Spr_pakket5=round(math.sqrt(KD_zand6*w_klei5),0)
        
        #OZ_klei6
        sudf=df2.query('depth < @Top_klei6')
        subdf=sudf.query('k>1')
        try:
            OZ_klei6=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei6= dzend
            sudf=df2.query('@OZ_klei6 < depth < @Top_klei6') 
            subdf=sudf.query('0<k<0.1')
            w_klei6=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei6   
        sudf=df2.query('@OZ_klei6 < depth < @Top_klei6')
        subdf=sudf.query('0<k<0.1')
        w_klei6=round((subdf['c'].sum()/3),0)
 
       #Top klei7
        sudf=df2.query('depth < @OZ_klei6')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei7 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei7=dzend        
            sudf=df2.query('@Top_klei7 < depth < @OZ_klei6')
            subdf=sudf.query('k>1')
            KD_zand7= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei7 - OZ_klei6)),0)
            Spr_pakket6=round(math.sqrt(KD_zand7*w_klei6),0)
            pass
        
        sudf=df2.query('@Top_klei7 < depth < @OZ_klei6') 
        subdf=sudf.query('k>1')
        KD_zand7= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei7 - OZ_klei6)),0)
        Spr_pakket6=round(math.sqrt(KD_zand7*w_klei6),0)
        
        #OZ_klei7
        sudf=df2.query('depth < @Top_klei7')
        subdf=sudf.query('k>1')
        try:
            OZ_klei7=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei7= dzend
            sudf=df2.query('@OZ_klei7 < depth < @Top_klei7') 
            subdf=sudf.query('0<k<0.1')
            w_klei7=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei7   
        sudf=df2.query('@OZ_klei7 < depth < @Top_klei7')
        subdf=sudf.query('0<k<0.1')
        w_klei7=round((subdf['c'].sum()/3),0)
       
       #Top klei8
        sudf=df2.query('depth < @OZ_klei7')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei8 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei8=dzend        
            sudf=df2.query('@Top_klei8 < depth < @OZ_klei7')
            subdf=sudf.query('k>1')
            KD_zand8= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei8 - OZ_klei7)),0)
            Spr_pakket7=round(math.sqrt(KD_zand8*w_klei7),0)
            pass
        
        sudf=df2.query('@Top_klei8 < depth < @OZ_klei7') 
        subdf=sudf.query('k>1')
        KD_zand8= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei8 - OZ_klei7)),0)
        Spr_pakket7=round(math.sqrt(KD_zand8*w_klei7),0)
        
        #OZ_klei8
        sudf=df2.query('depth < @Top_klei8')
        subdf=sudf.query('k>1')
        try:
            OZ_klei8=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei8= dzend
            sudf=df2.query('@OZ_klei8 < depth < @Top_klei8') 
            subdf=sudf.query('0<k<0.1')
            w_klei8=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei8   
        sudf=df2.query('@OZ_klei8 < depth < @Top_klei8')
        subdf=sudf.query('0<k<0.1')
        w_klei8=round((subdf['c'].sum()/3),0)

       #Top klei9
        sudf=df2.query('depth < @OZ_klei8')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei9 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei9=dzend        
            sudf=df2.query('@Top_klei9 < depth < @OZ_klei8')
            subdf=sudf.query('k>1')
            KD_zand9= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei9 - OZ_klei8)),0)
            Spr_pakket8=round(math.sqrt(KD_zand9*w_klei8),0)
            pass
        
        sudf=df2.query('@Top_klei9 < depth < @OZ_klei8') 
        subdf=sudf.query('k>1')
        KD_zand9= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei9 - OZ_klei8)),0)
        Spr_pakket8=round(math.sqrt(KD_zand9*w_klei8),0)
        
        #OZ_klei9
        sudf=df2.query('depth < @Top_klei9')
        subdf=sudf.query('k>1')
        try:
            OZ_klei9=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei9= dzend
            sudf=df2.query('@OZ_klei9 < depth < @Top_klei9') 
            subdf=sudf.query('0<k<0.1')
            w_klei9=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei9   
        sudf=df2.query('@OZ_klei9 < depth < @Top_klei9')
        subdf=sudf.query('0<k<0.1')
        w_klei9=round((subdf['c'].sum()/3),0)

       #Top klei10
        sudf=df2.query('depth < @OZ_klei9')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei10 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei10=dzend        
            sudf=df2.query('@Top_klei10 < depth < @OZ_klei9')
            subdf=sudf.query('k>1')
            KD_zand10= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei10 - OZ_klei9)),0)
            Spr_pakket9=round(math.sqrt(KD_zand10*w_klei9),0)
            pass
        
        sudf=df2.query('@Top_klei10 < depth < @OZ_klei9') 
        subdf=sudf.query('k>1')
        KD_zand10= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei10 - OZ_klei9)),0)
        Spr_pakket9=round(math.sqrt(KD_zand10*w_klei9),0)

        #OZ_klei10
        sudf=df2.query('depth < @Top_klei10')
        subdf=sudf.query('k>1')
        try:
            OZ_klei10=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei10= dzend
            sudf=df2.query('@OZ_klei10 < depth < @Top_klei10') 
            subdf=sudf.query('0<k<0.1')
            w_klei10=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei10   
        sudf=df2.query('@OZ_klei10 < depth < @Top_klei10')
        subdf=sudf.query('0<k<0.1')
        w_klei10=round((subdf['c'].sum()/3),0)
 
       #Top klei11
        sudf=df2.query('depth < @OZ_klei10')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei11 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei11=dzend        
            sudf=df2.query('@Top_klei11 < depth < @OZ_klei10')
            subdf=sudf.query('k>1')
            KD_zand11= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei11 - OZ_klei10)),0)
            Spr_pakket10=round(math.sqrt(KD_zand11*w_klei10),0)
            pass
        
        sudf=df2.query('@Top_klei11 < depth < @OZ_klei10') 
        subdf=sudf.query('k>1')
        KD_zand11= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei11 - OZ_klei10)),0)
        Spr_pakket10=round(math.sqrt(KD_zand11*w_klei10),0)
        
        #OZ_klei11
        sudf=df2.query('depth < @Top_klei11')
        subdf=sudf.query('k>1')
        try:
            OZ_klei11=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei11= dzend
            sudf=df2.query('@OZ_klei11 < depth < @Top_klei11') 
            subdf=sudf.query('0<k<0.1')
            w_klei11=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei11   
        sudf=df2.query('@OZ_klei11 < depth < @Top_klei11')
        subdf=sudf.query('0<k<0.1')
        w_klei11=round((subdf['c'].sum()/3),0)
       
       #Top klei12
        sudf=df2.query('depth < @OZ_klei11')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei12 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei12=dzend        
            sudf=df2.query('@Top_klei12 < depth < @OZ_klei11')
            subdf=sudf.query('k>1')
            KD_zand12= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei12 - OZ_klei11)),0)
            Spr_pakket11=round(math.sqrt(KD_zand12*w_klei11),0)
            pass
        
        sudf=df2.query('@Top_klei12 < depth < @OZ_klei11') 
        subdf=sudf.query('k>1')
        KD_zand12= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei12 - OZ_klei11)),0)
        Spr_pakket11=round(math.sqrt(KD_zand12*w_klei11),0)
        
        #OZ_klei12
        sudf=df2.query('depth < @Top_klei12')
        subdf=sudf.query('k>1')
        try:
            OZ_klei12=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei12= dzend
            sudf=df2.query('@OZ_klei12 < depth < @Top_klei12') 
            subdf=sudf.query('0<k<0.1')
            w_klei12=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei12   
        sudf=df2.query('@OZ_klei12 < depth < @Top_klei12')
        subdf=sudf.query('0<k<0.1')
        w_klei12=round((subdf['c'].sum()/3),0)

       #Top klei13
        sudf=df2.query('depth < @OZ_klei12')
        subdf=sudf.query('0<k<0.1')
        try:
            Top_klei13 = round((subdf.iloc[0,0]),3) 
        except IndexError:
            Top_klei13=dzend        
            sudf=df2.query('@Top_klei13 < depth < @OZ_klei12')
            subdf=sudf.query('k>1')
            KD_zand13= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei13 - OZ_klei12)),0)
            Spr_pakket12=round(math.sqrt(KD_zand13*w_klei12),0)
            pass
        
        sudf=df2.query('@Top_klei13 < depth < @OZ_klei12') 
        subdf=sudf.query('k>1')
        KD_zand13= KD_fact*round(((subdf['k'].mean()))*(abs(Top_klei13 - OZ_klei12)),0)
        Spr_pakket12=round(math.sqrt(KD_zand13*w_klei12),0)
        
        #OZ_klei13
        sudf=df2.query('depth < @Top_klei13')
        subdf=sudf.query('k>1')
        try:
            OZ_klei13=round((subdf.iloc[0,0]),3)
        except IndexError:
            OZ_klei13= dzend
            sudf=df2.query('@OZ_klei13 < depth < @Top_klei13') 
            subdf=sudf.query('0<k<0.1')
            w_klei13=round((subdf['c'].sum()/3),0)
            pass

        #c waarde klei13   
        sudf=df2.query('@OZ_klei13 < depth < @Top_klei13')
        subdf=sudf.query('0<k<0.1')
        w_klei13=round((subdf['c'].sum()/3),0)
#        
        d_klei1=Top_klei1-OZ_klei1
        d_klei2=Top_klei2-OZ_klei2
        d_klei3=Top_klei3-OZ_klei3
        d_klei4=Top_klei4-OZ_klei4
        d_klei5=Top_klei5-OZ_klei5
        d_klei6=Top_klei6-OZ_klei6
        d_klei7=Top_klei7-OZ_klei7
        d_klei8=Top_klei8-OZ_klei8
        d_klei9=Top_klei9-OZ_klei9
        d_klei10=Top_klei10-OZ_klei10
        d_klei11=Top_klei11-OZ_klei11
        d_klei12=Top_klei12-OZ_klei12
        d_klei13=Top_klei13-OZ_klei13
#
        d_zand1=self.z-Top_klei1
        d_zand2=OZ_klei1-Top_klei2
        d_zand3=OZ_klei2-Top_klei3
        d_zand4=OZ_klei3-Top_klei4
        d_zand5=OZ_klei4-Top_klei5
        d_zand6=OZ_klei5-Top_klei6
        d_zand7=OZ_klei6-Top_klei7
        d_zand8=OZ_klei7-Top_klei8
        d_zand9=OZ_klei8-Top_klei9
        d_zand10=OZ_klei9-Top_klei10
        d_zand11=OZ_klei10-Top_klei11
        d_zand12=OZ_klei11-Top_klei12
        d_zand13=OZ_klei12-Top_klei13
#
        varia=[
              [Top_klei1, Top_klei2, Top_klei3, Top_klei4, Top_klei5, Top_klei6, Top_klei7, Top_klei8, Top_klei9, Top_klei10, Top_klei11, Top_klei12, Top_klei13],
              [OZ_klei1, OZ_klei2, OZ_klei3, OZ_klei4, OZ_klei5, OZ_klei6, OZ_klei7, OZ_klei8, OZ_klei9, OZ_klei10, OZ_klei11, OZ_klei12, OZ_klei13],
              [w_klei1, w_klei2, w_klei3, w_klei4, w_klei5, w_klei6, w_klei7, w_klei8, w_klei9, w_klei10, w_klei11, w_klei12, w_klei13],
              [d_klei1,d_klei2, d_klei3, d_klei4, d_klei5, d_klei6, d_klei7, d_klei8, d_klei9, d_klei10, d_klei11, d_klei12, d_klei13],
              [self.z ,OZ_klei1, OZ_klei2, OZ_klei3, OZ_klei4, OZ_klei5, OZ_klei6, OZ_klei7, OZ_klei8, OZ_klei9, OZ_klei10, OZ_klei11, OZ_klei12],
              [Top_klei1, Top_klei2, Top_klei3, Top_klei4, Top_klei5, Top_klei6, Top_klei7, Top_klei8, Top_klei9, Top_klei10, Top_klei11, Top_klei12, Top_klei13],
              [d_zand1,d_zand2, d_zand3, d_zand4, d_zand5, d_zand6, d_zand7, d_zand8, d_zand9, d_zand10, d_zand11, d_zand12, d_zand13],
              [KD_zand1, KD_zand2, KD_zand3, KD_zand4, KD_zand5, KD_zand6, KD_zand7, KD_zand8, KD_zand9, KD_zand10, KD_zand11, KD_zand12, KD_zand13],
              ['NaN', Spr_pakket1, Spr_pakket2, Spr_pakket3, Spr_pakket4, Spr_pakket5, Spr_pakket6,  Spr_pakket7, Spr_pakket8, Spr_pakket9, Spr_pakket10,  Spr_pakket11, Spr_pakket12 ]  
              ]
        columns = ['P1','P2','P3', 'P4','P5', 'P6', 'P7', 'P8','P9', 'P10', 'P11', 'P12','P13' ]
        index   = ['Top_klei', 'OZ_klei', 'c-waarde','Dikte_klei', 'Top_zand','OZ_zand','Dikte zand','KD_WVP', 'Spreidingslengte']
        a=pd.DataFrame(varia, columns=columns, index=index)
#
        filename=filename.replace('.gef', '')
        filename=filename.replace('.GEF', '')

        pd.set_option('display.max_columns', None) 
        pd.set_option('display.max_rows', None) 
        pd.set_option('display.expand_frame_repr', True)
        pd.options.display.float_format = '{:,.1f}'.format
        df = df.reset_index(drop=True)
        df["Kg"] = df[["Rg", "Rm"]].max(axis=1)        
        df["Km"] = df[["Xg", "Xm"]].max(axis=1)        
        df["Ks"] = df[["Og", "Om"]].max(axis=1)        
        df["Kl"] = df[["Rl", "Xl", "Ol"]].max(axis=1)        


####Peakutils#################################################################
        xp=df['depth']
        yp=df['c']
        yq=df['k']
        min_dist=round(3/dist,-2)
        if min_dist < 20:
            min_dist=20
        indexes = peakutils.indexes(yp, thres=0.75, min_dist=min_dist)
        indexes2 = peakutils.indexes(yq, thres=0.3, min_dist=min_dist)
        x_ind=round(xp[indexes],2).tolist()
        x2_ind=round(xp[indexes2],2).tolist()
        x_ind=sorted(x_ind+x2_ind)
        y_ind=np.ones(len(x_ind))
##########SDataset sequences        
        dataset = pd.DataFrame({'depth':x_ind,'y_Value':y_ind})
        dataset=dataset.sort_values('depth', ascending=False)
        dataset=dataset.reset_index(drop=True)
        if dataset.empty:
            return dataset
        x_ind=dataset['depth'].tolist()
        
        sx=[]    
        sx.append('0')
        X=df['k']
        Y=df['depth']
        
        for xs,nextxs in zip(x_ind, x_ind[1 : ] + x_ind[ : 1]):
            if xs<nextxs:
                continue
            Xx=df.loc[(df.depth <= xs) & (df.depth >= nextxs)]
            sxa = str(np.where(round(np.polyfit(Xx['depth'],Xx['k'],1)[0],1)<0,-1,1))
            sx.append(sxa)

        try:
            dataset['slope'] = pd.Series(sx, index=dataset.index)
        except (ValueError,KeyError):
            return
        dataset['lengte']=dataset['depth'].diff()
        dataset['depth3']=dataset['depth'].shift(1)
        dataset['slope']= dataset['slope'].astype(float)
        dataset['v']=dataset['slope']*dataset['lengte']
        dataset['u'] = 0
        dataset['color']=np.where(dataset['slope']==1,'blue','red')
        dataset['depth4']=np.where(dataset['slope']<0,dataset['depth'], dataset['depth3'])
###############################################################################        
        
        
#
        fig, ax = plt.subplots(nrows=1, ncols=3, gridspec_kw = {'width_ratios':[2.4, 0.4,0.5]})
        fig.subplots_adjust(wspace=0, hspace=0)
#
        df.plot(x='kl',  y='depth', ylim = (ymin, ymax), xlim = (0,40), yticks=range (ymin, ymax, ds), xticks=range (0,40,5), xerr='k', elinewidth=0.5, ax=ax[0], legend=False, color='green');
        df.plot(x='v',   y='depth', ylim = (ymin, ymax), xlim = (0,40), yticks=range (ymin, ymax, ds), xticks=range (0,40,5), xerr='k', elinewidth=0.5, ax=ax[0], legend=False, color='mediumorchid');
        df.plot(x='le',  y='depth', ylim = (ymin, ymax), xlim = (0,40), yticks=range (ymin, ymax, ds), xticks=range (0,40,5), xerr='k', elinewidth=0.5, ax=ax[0], legend=False, color='darkgreen');
        df.plot(x='f',   y='depth', ylim = (ymin, ymax), xlim = (0,40), yticks=range (ymin, ymax, ds), xticks=range (0,40,5), xerr='k', elinewidth=0.5, ax=ax[0], legend=False, color='gold');
        df.plot(x='mf',  y='depth', ylim = (ymin, ymax), xlim = (0,40), yticks=range (ymin, ymax, ds), xticks=range (0,40,5), xerr='k', elinewidth=0.5, ax=ax[0], legend=False, color='orange');
        df.plot(x='m',   y='depth', ylim = (ymin, ymax), xlim = (0,40), yticks=range (ymin, ymax, ds), xticks=range (0,40,5), xerr='k', elinewidth=0.5, ax=ax[0], legend=False, color='darkgoldenrod');
        df.plot(x='g',   y='depth', ylim = (ymin, ymax), xlim = (0,40), yticks=range (ymin, ymax, ds), xticks=range (0,40,5), xerr='k', elinewidth=0.5, ax=ax[0], legend=False, grid=True, color='brown',  title=filename);       

        dataset.plot(x='y_Value', y='depth', ylim = (ymin, ymax), xlim = (0,2), xerr=1.0, elinewidth=1, ax=ax[2], legend=False, color='lightgrey', grid=False,  zorder=-1);
        Q=ax[2].quiver(dataset['y_Value'],dataset['depth4'],dataset['u'],dataset['v'], scale_units='xy', scale=1,
                     color=dataset['color'], width=0.06, headwidth=7,headlength=8, zorder=1)
        ax[2].quiverkey(Q, 0.85, 0.9, 1.5, r'Fine-up', labelpos='E',coordinates='figure',color='red', angle=90)
        ax[2].quiverkey(Q, 0.85, 0.85, 1.5, r'Coarse-up', labelpos='E',coordinates='figure',color='blue', angle=-90)

        ax[2].set_xlabel('')
        ax[2].set_xticklabels([])
        ax[2].set_yticklabels([])
        plt.axis('off')

        df.plot(x='Kg',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='navajowhite');
#        df.plot(x='Rm',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='navajowhite');
#        df.plot(x='Rl',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='darkseagreen');
        df.plot(x='Km',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='orange');
#        df.plot(x='Xm',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='orange');
#        df.plot(x='Xl',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='darkseagreen');
        df.plot(x='Ks',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='peru');
#        df.plot(x='Om',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='peru');
        df.plot(x='Kl',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='darkseagreen');
        df.plot(x='Rkl',  y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='darkcyan');
        df.plot(x='Glag', y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='red');
        df.plot(x='Glam', y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='dodgerblue');
        df.plot(x='Glal', y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='xkcd:chartreuse');
        df.plot(x='Glaug',y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='lightgrey');
        df.plot(x='Glauz',y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='firebrick');
        df.plot(x='Conk', y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='pink');
        df.plot(x='Tert', y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='yellow');
        df.plot(x='Vkl',  y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='plum');
        df.plot(x='V',    y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='hotpink')
        df.plot(x='XVkl', y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='indigo');
        df.plot(x='KV',   y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='slateblue');
        df.plot(x='Xkl',  y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='rosybrown');
        df.plot(x='Los',  y='depth', ylim = (ymin, ymax), xlim = (0,1), yticks=range (ymin, ymax, ds), xticks=range (0, 1, 1), xerr=1.0, elinewidth=0.5,  ax=ax[1], legend=False, color='powderblue', grid=True, title='T');
        ax[1].set_yticklabels([])
        ax[1].set_xticklabels([])
        ax[1].set_xlabel('')

# Bepaling bijschrift met alleen de grotere lagen           
        try:
            c1=int(a.iloc[2,0])
            if float(a.iloc[3,0])<0.4:
                c1=''
            else:
                c1=str(c1)+ ' dag'
        except ValueError:
            c1=''
        try:
            KD1=int(a.iloc[7,0])
            if KD1<1 or float(a.iloc[6,0])<2:
                KD1=''
            else:
                KD1=str(KD1)+' m2/dag'
        except ValueError:
            KD1=''
        try:
            c2=int(a.iloc[2,1])
            if float(a.iloc[3,1])<0.4:
                c2=''
            else:
                c2=str(c2)+ ' dag'
        except ValueError:
            c2=''
        try:
            KD2=int(a.iloc[7,1])
            if KD2<1 or float(a.iloc[6,1])<2:
                KD2=''
            else:
                KD2=str(KD2)+' m2/dag'
        except ValueError:
            KD2=''
        try:
            c3=int(a.iloc[2,2])
            if float(a.iloc[3,2])<0.4:
                c3=''
            else:
                c3=str(c3)+ ' dag'
        except ValueError:
            c3=''
        try:
            KD3=int(a.iloc[7,2])
            if KD3<1 or float(a.iloc[6,2])<2:
                KD3=''
            else:
                KD3=str(KD3)+' m2/dag'
        except ValueError:
            KD3=''
        try:
            c4=int(a.iloc[2,3])
            if float(a.iloc[3,3])<0.4:
                c4=''
            else:
                c4=str(c4)+ ' dag'
        except ValueError:
            c4=''
        try:
            KD4=int(a.iloc[7,3])
            if KD4<1 or float(a.iloc[6,3])<2:
                KD4=''
            else:
                KD4=str(KD4)+' m2/dag'
        except ValueError:
            KD4=''
        try:
            c5=int(a.iloc[2,4])
            if float(a.iloc[3,4])<0.4:
                c5=''
            else:
                c5=str(c5)+ ' dag'
        except ValueError:
            c5=''
        try:
            KD5=int(a.iloc[7,4])
            if KD5<1 or float(a.iloc[6,4])<2:

                KD5=''
            else:
                KD5=str(KD5)+' m2/dag'
        except ValueError:
            KD5=''
        try:
            c6=int(a.iloc[2,5])
            if float(a.iloc[3,5])<0.4:
                c6=''
            else:
                c6=str(c6)+ ' dag'
        except ValueError:
            c6=''
        try:
            KD6=int(a.iloc[7,5])
            if KD6<1 or float(a.iloc[6,5])<2:
                KD6=''
            else:
                KD6=str(KD6)+' m2/dag'
        except ValueError:
            KD6=''
        try:
            c7=int(a.iloc[2,6])
            if float(a.iloc[3,6])<0.4:
                c7=''
            else:
                c7=str(c7)+ ' dag'
        except ValueError:
            c7=''
        try:
            KD7=int(a.iloc[7,6])
            if KD7<1 or float(a.iloc[6,6])<2:
                KD7=''
            else:
                KD7=str(KD7)+' m2/dag'
        except ValueError:
            KD7=''
        try:
            c8=int(a.iloc[2,7])
            if float(a.iloc[3,7])<0.4:
                c8=''
            else:
                c8=str(c8)+ ' dag'
        except ValueError:
            c8=''
        try:
            KD8=int(a.iloc[7,7])
            if KD8<1 or float(a.iloc[6,7])<2:
                KD8=''
            else:
                KD8=str(KD8)+' m2/dag'
        except ValueError:
            KD8=''
        try:
            c9=int(a.iloc[2,8])
            if float(a.iloc[3,8])<0.4:
                c9=''
            else:
                c9=str(c9)+ ' dag'
        except ValueError:
            c9=''
        try:
            KD9=int(a.iloc[7,8])
            if KD9<1 or float(a.iloc[6,8])<2:
                KD9=''
            else:
                KD9=str(KD9)+' m2/dag'
        except ValueError:
            KD9=''
        try:
            c10=int(a.iloc[2,9])
            if float(a.iloc[3,9])<0.4:
                c10=''
            else:
                c10=str(c10)+ ' dag'
        except ValueError:
            c10=''
        try:
            KD10=int(a.iloc[7,9])
            if KD10<1 or float(a.iloc[6,9])<2:
                KD10=''
            else:
                KD10=str(KD10)+' m2/dag'
        except ValueError:
            KD10=''
        try:
            c11=int(a.iloc[2,10])
            if float(a.iloc[3,10])<0.4:
                c11=''
            else:
                c11=str(c11)+ ' dag'
        except ValueError:
            c11=''
        try:
            KD11=int(a.iloc[7,10])
            if KD11<1 or float(a.iloc[6,10])<2:
                KD11=''
            else:
                KD11=str(KD11)+' m2/dag'
        except ValueError:
            KD11=''
        try:
            c12=int(a.iloc[2,11])
            if float(a.iloc[3,11])<0.4:
                c12=''
            else:
                c12=str(c12)+ ' dag'
        except ValueError:
            c12=''
        try:
            KD12=int(a.iloc[7,11])
            if KD12<1 or float(a.iloc[6,11])<2:
                KD12=''
            else:
                KD12=str(KD12)+' m2/dag'
        except ValueError:
            KD12=''
        try:
            c13=int(a.iloc[2,12])
            if float(a.iloc[3,12])<0.4:
                c13=''
            else:
                c13=str(c13)+ ' dag'
        except ValueError:
            c13=''
        try:
            KD13=int(a.iloc[7,12])
            if KD13<1 or float(a.iloc[6,12])<2:
                KD13=''
            else:
                KD13=str(KD13)+' m2/dag'
        except ValueError:
            KD13=''
#
        if c1 =='0 dag':
            c1=''
        if c2 =='0 dag':
            c2=''
        if c3 == '0 dag':
            c3=''
        if c4 == '0 dag':
            c4=''
        if c5 == '0 dag':
            c5=''
        if c6 == '0 dag':
            c6=''
        if c7 == '0 dag':
            c7=''
        if c8 == '0 dag':
            c8=''
        if c9 == '0 dag':
            c9=''
        if c10 == '0 dag':
            c10=''
        if c11 == '0 dag':
            c11=''
        if c12 == '0 dag':
            c12=''
        if c13 == '0 dag':
            c13=''
        ax[0].text(60,((a.iloc[0,0]+a.iloc[1,0])/2),c1)
        ax[0].text(60,((a.iloc[0,1]+a.iloc[1,1])/2),c2)
        ax[0].text(60,((a.iloc[0,2]+a.iloc[1,2])/2),c3)
        ax[0].text(60,((a.iloc[0,3]+a.iloc[1,3])/2),c4)
        ax[0].text(60,((a.iloc[0,4]+a.iloc[1,4])/2),c5)
        ax[0].text(60,((a.iloc[0,5]+a.iloc[1,5])/2),c6)
        ax[0].text(60,((a.iloc[0,6]+a.iloc[1,6])/2),c7)
        ax[0].text(60,((a.iloc[0,7]+a.iloc[1,7])/2),c8)
        ax[0].text(60,((a.iloc[0,8]+a.iloc[1,8])/2),c9)
        ax[0].text(60,((a.iloc[0,9]+a.iloc[1,9])/2),c10)
        ax[0].text(60,((a.iloc[0,10]+a.iloc[1,10])/2),c11)
        ax[0].text(60,((a.iloc[0,11]+a.iloc[1,11])/2),c12)
        ax[0].text(60,((a.iloc[0,12]+a.iloc[1,12])/2),c13)

        ax[0].text(70,((a.iloc[4,0]+a.iloc[5,0])/2),KD1)
        ax[0].text(70,((a.iloc[4,1]+a.iloc[5,1])/2),KD2)
        ax[0].text(70,((a.iloc[4,2]+a.iloc[5,2])/2),KD3)
        ax[0].text(70,((a.iloc[4,3]+a.iloc[5,3])/2),KD4)
        ax[0].text(70,((a.iloc[4,4]+a.iloc[5,4])/2),KD5)
        ax[0].text(70,((a.iloc[4,5]+a.iloc[5,5])/2),KD6)
        ax[0].text(70,((a.iloc[4,6]+a.iloc[5,6])/2),KD7)
        ax[0].text(70,((a.iloc[4,7]+a.iloc[5,7])/2),KD8)
        ax[0].text(70,((a.iloc[4,8]+a.iloc[5,8])/2),KD9)
        ax[0].text(70,((a.iloc[4,9]+a.iloc[5,9])/2),KD10)
        ax[0].text(70,((a.iloc[4,10]+a.iloc[5,10])/2),KD11)
        ax[0].text(70,((a.iloc[4,11]+a.iloc[5,11])/2),KD12)
        ax[0].text(70,((a.iloc[4,12]+a.iloc[5,12])/2),KD13)

        leg=ax[1].legend(['Zand, sortering = goed',
                        'Zand, sortering = matig',
                        'Zand, sortering = slecht',
                        'Zandige klei tot leem', 
                        'Klei',
                        'Grof Boxtel, Peelo-afzettingen, Matig grof Di/T',
                        'Boxtel, Matig fijn Di/T',
                        'Lemig Boxtel, Potklei, Keileem, Lemig Di/T',
                        'Grof Glauconietzand, Grof Di/T',
                        'Glauconietzand, Diestienzand, T4',
                        'Geconsolideerde klei, Boomse klei, Topklei T3', 
                        'Tertiaire afzettingen, Tongrien', 
                        'Venige klei, Löss',
                        'Mineraalarm veen',
                        'Humeuze klei',
                        'Kleiig veen',
                        'Compact kleiig veen',
                        'Cohesiearm',
                        ], 
    bbox_to_anchor=(7.5, 1.0), loc='upper left',fontsize=10, frameon=1, title='T (Bodemtype)', 
    title_fontsize=14, labelspacing=0.5, borderpad=1, handlelength=2, handletextpad=2);
        leg._legend_box.sep = 30
        for legobj in leg.legendHandles:
            legobj.set_linewidth(12.0)


        ax[0].hlines(self.z, xmin=0, xmax=40, linestyle='solid', color='grey')
        ax[0].text(1, self.z+0.3, 'Mv', weight='bold')
        ax[1].hlines(self.z, xmin=0, xmax=1, linestyle='solid', color='grey')
        
        ax=ax[0].set(xlabel="k [m/dag]", ylabel="[m NAP]") 

        
        
        plt.savefig(filename + ".png", bbox_inches = "tight")
        
for filename in os.listdir(os.getcwd()):
    if filename.endswith ('.GEF') or filename.endswith ('.gef'):
        if __name__=="__main__":
            g=GEF()
            g.readFile(filename)
            g.plt(filename)
        plt.show()    
        plt.close()