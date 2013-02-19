'''
    Gesture Recognition Module
'''

from constants import GesCons
import imgproc

''' SkinDetector Class and Its Functions'''

class Gesture(object):
    def __init__(self, type_):
        self.type_ = type_

    def __repr__(self):
        return self.type_ 

    def hasMeaning(self):
        return self.type_ != 'Uncertain'

''' Gesture Analyzer Class and Its Functions'''

class GestureAnalyzer(object):
    def __init__(self):
        pass
        
    # using maximal area and convexity defect depths to recognize between palm and fist.    
    def recognize(self, contours): 
        x, y, r, b, isCenter = imgproc.find_max_rectangle(contours)
        max_area, contours = imgproc.max_area(contours)
        max_area_n = float(max_area)/((r-x)*(b-y))
        # print 'Normalized Area: ', max_area_n 
        # print 'Actual Area: ', float(max_area)
        hull = imgproc.find_convex_hull(contours)
        mean_depth = 0
        if hull:
          cds = imgproc.find_convex_defects(contours, hull)
          if len(cds) != 0:
              mean_depth = sum([cd[3] for cd in cds])/len(cds)
        # print 'Depth: ', mean_depth      
        if self.isFist(max_area_n, mean_depth, isCenter): 
            ges = 'Fist' 
        elif self.isPalm(max_area_n, mean_depth, isCenter): 
            ges = 'Palm'
        elif self.isScissors(max_area_n, mean_depth, isCenter):
            ges = 'Scissors'    
        else: 
            ges = 'Uncertain'
        return Gesture(ges), max_area, mean_depth    

    def isFist(self, area, depth, center):
        return GesCons.FIST.DEPTH_L < depth < GesCons.FIST.DEPTH_U and \
               GesCons.FIST.AREA_L  < area  < GesCons.FIST.AREA_U and \
               center == 0

    def isPalm(self, area, depth, center):
        return GesCons.PALM.DEPTH_L < depth < GesCons.PALM.DEPTH_U and \
               GesCons.PALM.AREA_L  < area  < GesCons.PALM.AREA_U and \
               center == 1

    def isScissors(self, area, depth, center):
        return GesCons.SCISSORS.DEPTH_L < depth < GesCons.SCISSORS.DEPTH_U and \
               GesCons.SCISSORS.AREA_L  < area  < GesCons.SCISSORS.AREA_U and \
               center == 1
