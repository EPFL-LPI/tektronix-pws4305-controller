#!/usr/bin/env python
# coding: utf-8

# # Power Supply Controller
# ## For use with Tektronix PWS4305

# In[1]:


# standard imports
import os
import sys

# SCPI imports
import usb
import visa

# instrument controller
import instrument_controller as ic


# In[2]:


class PowerSupply( ic.Instrument ):
    
    def __init__( self, timeout = 10, rid = None ):
        ic.Instrument.__init__( self, None, timeout, '\n', '\n' )
        self.rid = 'USB0::0x0699::0x0392::C011451::INSTR' if ( rid is None ) else rid
        
    #--- public methods ---
    
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
        


# In[3]:


# ps = PowerSupply()


# In[4]:


# ps.connect()


# In[5]:


# ps.id


# In[6]:


# del ps


# In[90]:


# ps.off()

