#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# helpers - used for verbose mode only
# could have been implemented as static methods in Position
# but we had not seen that at the time
def d_m_s(f):
    """
    make a float readable; e.g. transform 2.5 into 2.30'00'' 
    we avoid using the degree sign to keep things simple
    input is assumed positive
    """
    d = int (f)
    m = int((f-d)*60)
    s = int( (f-d)*3600 - 60*m)
    return "{:02d}.{:02d}'{:02d}''".format(d,m,s)

def lat_d_m_s(f):
    if f>=0:        return "{} N".format(d_m_s(f))
    else:           return "{} S".format(d_m_s(-f))
        
def lon_d_m_s(f):
    if f>=0:        return "{} E".format(d_m_s(f))
    else:           return "{} W".format(d_m_s(-f))


class Position(object):    
    """
    An object that contains latitude, longitude, timestamp
    """
    def __init__(self, latitude, longitude, timestamp):
        """
        constructor
        """
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        
# all these methods are only used when merger.py runs in verbose mode
    def lat_str(self):  return lat_d_m_s(self.latitude)
    def lon_str(self):  return lon_d_m_s(self.longitude)

    def __repr__(self):
        """
        only used when merger.py is in verbose mode
        """
        return "<{} {} @ {}>".format(self.lat_str(),
                                    self.lon_str(), self.timestamp)


class Ship(object):
    """
    An object for the Ships (id, name(options), country(options))
    """    

    def __init__(self, id, name=None, country=None):
        """
        constructor computes references
        """
        self.id = id
        self.name = name
        self.country = country
        # this is where we remember the various positions over time
        self.positions = []

    def add_position(self, position):
        """
        insert a position relating to this ship positions are not kept in 
        order so you need to call 'sort_positions' once you're done
        """
        self.positions.append(position)
    
    def sort_positions(self):
        """
        sort list of positions by chronological order
        """
        self.positions.sort(key=lambda position: position.timestamp)


class ShipDict(dict):
    """
    An object for the dictionnary that contains Ship indexes
    """
    def __init__(self):
        """
        constructor computes reference of Ships in a dict
        """
        dict.__init__(self)        
        #_theDictOfShip = [Ship]
        #self.theDictOfShip =_theDictOfShip 

    def __repr__(self):
        """
        """
        return "<ShipDict instance with {} ships>".format(len(self))  
    
    def add_abbreviated(self, chunk):
        """
        adds an abbreviated data chunk to the repository
        """
        idship, latitude, longitude, _, _, _, timestamp = chunk
        if idship not in self:
            self[idship] = Ship(idship)
        ship = self[idship]
        ship.add_position (Position (latitude, longitude, timestamp))    
    
    def add_extended(self, chunk):
        """
        adds an extended data chunk to the repository
        """
        idship, latitude, longitude = chunk[:3]
        timestamp, name = chunk[5:7]
        country = chunk[10]
        if idship not in self:
            self[idship] = Ship(idship)
        ship = self[idship]
        if not ship.name:
            ship.name = name
            ship.country = country
        self[idship].add_position (Position (latitude, longitude, timestamp))      
  
        
    def all_ships(self):
        """
        returns a list of all ships known to us
        """
        return self.values()
    
    def clean_unnamed(self):
        """
        Because we enter abbreviated and extended data
        in no particular order, and for any time period,
        we might have ship instances with no name attached
        T"his method removes such entries from the dict
        """
        # so let us collect the ids to remove first        
        unamedids =  { id for id, ship in self.iteritems() if ship.name is None }
        # and remove them next        
        for id in unamedids:
            del self[id]
    
    def is_abbreviated(self, chunk):
        """
        depending on the size of the incoming data chunk, 
        guess if it is an abbreviated or extended data
        """
        return len(chunk) <= 7        
    
    def ships_by_name(self, name):
        """
        returns a list of all known ships with name <name>
        """
        return  [ship for ship in self.values() if ship.name == name]

    def sort(self):
        """
        makes sure all the ships have their positions
        sorted in chronological order
        """
        for id, ship in self.iteritems():
            ship.sort_positions()

    def add_chunk(self, chunk):
        """
        chunk is a plain list coming from the JSON data
        and be either extended or abbreviated
        based on the result of is_abbreviated(), 
        gets sent to add_extended or add_abbreviated
        """
        if self.is_abbreviated(chunk):
            self.add_abbreviated(chunk)
        else:
            self.add_extended(chunk)  