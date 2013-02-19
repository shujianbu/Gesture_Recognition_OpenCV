'''
    Constants Module
'''

''' Hue/Intensity Gesture Skin Detector Constants'''
class SkinCons(object):
    HUE_LT = 3
    HUE_UT = 50
    INTENSITY_LT = 15
    INTENSITY_UT = 250

''' Three Gesture Constants - Depth Lowerbound/UppperBound; Area Lowerbound/UppperBound'''
class GesConsAttributes(object):
    pass

class GesCons(object):

#   21.8, 741, 0.173
    FIST = GesConsAttributes()
    FIST.DEPTH_L = 20.0
    FIST.DEPTH_U = 30.0
    FIST.AREA_L = 0.15
    FIST.AREA_U = 0.22

#   15.9, 915, 0.10996
    SCISSORS = GesConsAttributes()
    SCISSORS.DEPTH_L = 15.0
    SCISSORS.DEPTH_U = 20.0
    SCISSORS.AREA_L = 0.02
    SCISSORS.AREA_U = 0.15

#   13.55, 1456, 0.247 ~ 0.634
    PALM = GesConsAttributes()
    PALM.DEPTH_L = 4.0
    PALM.DEPTH_U = 14.5
    PALM.AREA_L = 0.22
    PALM.AREA_U = 0.65
