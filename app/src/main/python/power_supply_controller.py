#!/usr/bin/env python
# coding: utf-8

# # Power Source Controller
# ## For use with Tektronix PWS4305

# In[2]:


# standard imports
import os
import sys

# SCPI imports
import usb
import visa

# instrument controller
import instrument_controller as ic


# In[85]:


class PowerSource( ic.Instrument ):
    
    def __init__( self, timeout = 10 ):
        ic.Instrument.__init__( self, timeout = timeout, backend = '' )
        self.rid = 'USB0::0x0699::0x0392::C011451::INSTR'
        self.isnt = self.__inst
        
    #--- public methods ---
    
    def connect( self ):
        # need to set termination characters
        set_termination = ( self.instrument is None ) 
        
        # connect
        ic.Instrument.connect( self )
        
        # set termination characters if needed
        if set_termination:
            self.instrument.write_termination = '\n'
            self.instrument.read_termination = '\n'
            
    @property        
    def voltage( self ):
        """
        Returns the voltage setting
        """
        return self.source.volt.level()
    
    
    @voltage.setter
    def voltage( self, volts ):
        """
        Sets the voltage of the instrument
        """
        self.source.volt.level( volts )
        
    
    @property
    def current( self ):
        """
        Returns the current setting in Amps
        """
        return self.source.current.level()
        
        
    @current.setter
    def current( self, amps ):
        """
        Set the current of the instrument
        """
        self.source.current.level( amps )
        
    
    def on( self ):
        """
        Turns the output on
        """
        self.output.state( 'on' )
        
        
    def off( self):
        """
        Turns the output off
        """
        self.output.state( 'off' )
        


# In[87]:


# ps = PowerSource()


# In[88]:


# ps.connect()


# In[55]:


# ps.id


# In[86]:


# del ps


# In[90]:


# ps.off()

