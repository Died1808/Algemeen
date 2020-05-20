import os
import sys
sys.stdout = open('s02.csv', 'a')

class GEF:
    def __init__(self):
        
        
        self._data_seperator = ' '
        self._columns = {}
            
    def readFile(self, filename):
        lines = open(filename, 'r').readlines()
        for line in lines:
            reading_header = True


        for line in lines:            
            if reading_header:
                self._parseHeaderLine(line)
            else:
                self._parseDataLine(line)
            if line.find('#EOH') >-1:
                if self._check_header():
                    reading_header = False
                else:

                    return
            
    def _check_header(self):
        if not 1 in self._columns:
            return False
        if not 2 in self._columns:
            return False
        if not 3 in self._columns:
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

        if len(line.split()) == 0:
            return
        
        keyword, argline = line.split('=')             
      
        keyword = keyword.strip()
        argline = argline.strip()
        args = argline.split(',')

        if '#XYID' in line:
            argline = argline.replace('.',',')        
        
        if keyword=='#XYID':
            args[1]=args[1].replace('.','')
            args[2]=args[2].replace('.','')
            
            self.x = float(args[1])

            if 1e0 < self.x < 3e5:
                self.x = int(round(self.x,0))
            elif 3e5 < self.x <3e6:
                self.x = int(round(self.x/1e1))                
            elif 3e6 < self.x <3e7:
                self.x = int(round(self.x/1e2))
            elif 3e7< self.x <3e8:
                self.x = int(round(self.x/1e3))
            elif 3e8 < self.x <3e9:
                self.x = int(round(self.x/1e4))
            elif 3e9< self.x <3e10:
                self.x = int(round(self.x/1e5))
            elif 3e10 < self.x <3e11:
                self.x = int(round(self.x/1e6))
            elif 3e11< self.x <3e12:
                self.x = int(round(self.x/1e7))
            elif 3e12< self.x <3e13:
                self.x = int(round(self.x/1e8))
            elif 3e13< self.x <3e14:
                self.x = int(round(self.x/1e9))
                
               
            self.y = float(args[2])

            if 1e0 < self.y < 1e6:
                self.y = int(round(self.y,0))
            elif 1e6 < self.y <1e7:
                self.y = int(round(self.y/1e1))
            elif 1e7 < self.y <1e8:
                self.y = int(round(self.y/1e2))
            elif 1e8 < self.y <1e9:
                self.y = int(round(self.y/1e3))
            elif 1e9 < self.y <1e10:
                self.y = int(round(self.y/1e4))
            elif 1e10 < self.y <1e11:
                self.y = int(round(self.y/1e5))                
            elif 1e11 < self.y <1e12:
                self.y = int(round(self.y/1e6))                  
            elif 1e12 < self.y <1e13:
                self.y = int(round(self.y/1e7))   
            elif 1e13 < self.y <1e14:
                self.y = int(round(self.y/1e8))   




            Val=[]
            Val.append(filename)
            Val.append(self.x)
            Val.append(self.y)  
            Val[0] = Val[0].replace('.gef','')
            Val[0] = Val[0].replace('.GEF','')
            
            print(*Val)
        
for filename in os.listdir(os.getcwd()):
    if filename.endswith ('.GEF') or filename.endswith ('.gef'):
        filesize= os.path.getsize(filename)
        if filesize/1024 < 1:
            pass
        else:
            if __name__=="__main__":
                g=GEF()
                g.readFile(filename)


            

    

    

