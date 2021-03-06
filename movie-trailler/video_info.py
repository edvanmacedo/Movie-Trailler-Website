# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:32:52 2016

@author: edvan.macedo.jr@gmail.com
"""

class VideoInfo():

    """ This class provides a way to store comum information about video
    Attributes:
        duration (str): This should inform the media duration
        ratings (str): This should inform the valid ratings of media
        genre (str): This should inform the genre of media
        date(str): This should inform the date of release of media
    """    

    def __init__(self, duration, ratings, genre, date):        
        self.duration = duration
        self.ratings = ratings
        self.genre = genre
        self.date = date