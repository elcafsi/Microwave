import numpy as np 

class CoaxialCable:
    def __init__(self,innerDiameter,outDiameter,relativepermittivity,dielectricConductivity,metalConductivity):
        self.innerDiameter=innerDiameter
        self.outDiameter=outDiameter
        self.relativepermittivity=relativepermittivity
        self.dielectricConductivity=dielectricConductivity
        self.metalConductivity=metalConductivity
    
    def getCapacitance(self):
        capacitance=7.354*self.relativepermittivity/np.log10(self.outDiameter/self.innerDiameter)
        return capacitance

    def getInductance(self):
        inductance=140.4*np.log10(self.outDiameter/self.innerDiameter)
        return inductance

    def getConductance(self):
        conductance=(2*np.pi*self.dielectricConductivity)/(np.log(self.outDiameter/self.innerDiameter))
        return conductance

    def getResistance(self,frequency):
        skinEffect=1/np.sqrt(np.pi*frequency*self.metalConductivity)
        surfaceResistance=1/(self.metalConductivity*skinEffect)
        resistance=(surfaceResistance/np.pi)*(1/self.innerDiameter+1/self.outDiameter)
        return resistance

    def getImpedance(self):
        impedance=138*np.log10(self.outDiameter/self.innerDiameter)/np.sqrt(self.relativepermittivity)    
        return impedance
    
    def getCutOffFrequency(self):
        cutOffFrequency=11.8/(np.sqrt(self.relativepermittivity)*np.pi*((self.innerDiameter+self.outDiameter)/2))
        return cutOffFrequency
    
    def getPropagationConstant(self,frequency,C,L,R,G):
        gamma= np.sqrt((R+1j*2*np.pi*frequency*L)*(C+1j*2*np.pi*frequency*C))
        return gamma

    def getWavelentgh(self,frequency,C,L):
        wavelength=1/frequency*np.sqrt(C*L)
        return wavelength
    
    
    def getPropagationVelocity(self,frequency,C,L):
        propagationVelocity=1/np.sqrt(C*L)
        return propagationVelocity

    
   
  
