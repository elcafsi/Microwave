import numpy as np 

class CoaxialCable:
    def __init__(self,innerDiameter,outDiameter,relativepermittivity):
        self.innerDiameter=innerDiameter
        self.outDiameter=outDiameter
        self.relativepermittivity=relativepermittivity
    
    def getCapacitance(self):
        capacitance=7.354*self.relativepermittivity/np.log10(self.outDiameter/self.innerDiameter)
        return capacitance

    def getInductance(self):
        inductance=140.4*np.log10(self.outDiameter/self.innerDiameter)
        return inductance

    def getImpedance(self):
        impedance=138*np.log10(self.outDiameter/self.innerDiameter)/np.sqrt(self.relativepermittivity)    
        return impedance
    
    def getCutOffFrequency(self):
        cutOffFrequency=11.8/(np.sqrt(self.relativepermittivity)*np.pi*((self.innerDiameter+self.outDiameter)/2))
        return cutOffFrequency
   
  
