'''
    Image Processing Module
'''
import numpy
import cv

''' Color '''
class Color(object):
    pass

color=Color()
color.RED=(0,0,255,0)
color.GREEN=(0,255,0,0)
color.BLUE=(255,0,0,0)

''' Font '''
class Font(object):
    pass

font = Font()
font.default = cv.InitFont(cv.CV_FONT_HERSHEY_DUPLEX, 1.0, 1.0, thickness=2)

''' Functions For Image Processing'''

def cvimg2numpy(cvimg):
  return numpy.asarray(cv.GetMat(cvimg))
  
def bgr2hsv(cvimg):
  size = (cvimg.width, cvimg.height)
  depth = cvimg.depth
  channels = cvimg.nChannels
  hsvimg = cv.CreateImage(size, depth, channels)
  cv.CvtColor(cvimg, hsvimg, cv.CV_BGR2HSV)
  return hsvimg
  
def bgr2gray(cvimg):
  size = (cvimg.width, cvimg.height)
  depth = cvimg.depth
  channels = cvimg.nChannels
  grayimg = cv.CreateImage(size, depth, 1)
  cv.CvtColor(cvimg, grayimg, cv.CV_BGR2GRAY)
  return grayimg
  
def bgr2rgb(cvimg):
  size = (cvimg.width, cvimg.height)
  depth = cvimg.depth
  channels = cvimg.nChannels
  rgbimg = cv.CreateImage(size, depth, channels)
  cv.CvtColor(cvimg, rgbimg, cv.CV_BGR2RGB)
  return rgbimg

def rgb2bgr(cvimg):
  size = (cvimg.width, cvimg.height)
  depth = cvimg.depth
  channels = cvimg.nChannels
  bgrimg = cv.CreateImage(size, depth, channels)
  cv.CvtColor(cvimg, bgrimg, cv.CV_RGB2BGR)
  return bgrimg

def split3(cvimg):
  size = (cvimg.width, cvimg.height)
  c1 = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
  c2 = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)  
  c3 = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
  cv.Split(cvimg, c1, c2, c3, None)
  return c1,c2,c3

def merge3(b,g,r):
  size = (r.width, r.height)
  img = cv.CreateImage(size, cv.IPL_DEPTH_8U, 3)
  cv.Merge(b,g,r,None,img)
  return img
  
def size(cvimg):
  return (cvimg.width, cvimg.height)

''' Functions For Calculation'''

def find_contours(im):
    storage = cv.CreateMemStorage(0)
    try:
      contours = cv.FindContours(im, 
                               storage,
                               cv.CV_RETR_TREE,
                               cv.CV_CHAIN_APPROX_SIMPLE)
      contours = cv.ApproxPoly(contours,
                             storage,
                             cv.CV_POLY_APPROX_DP, 3, 1)
    except cv.error, e:
      print e
      return None
    return contours

def find_convex_hull(cvseq):
    storage = cv.CreateMemStorage(0)
    try:
      hull = cv.ConvexHull2(cvseq, storage, cv.CV_CLOCKWISE, 0)
    except TypeError, e:
      return None
    return hull

def find_convex_defects(contour, hull):
    storage = cv.CreateMemStorage(0)
    return cv.ConvexityDefects(contour, hull, storage)

def max_area(contours):
    max_area = 0
    max_contours = contours
    try:
      while True:
          area = cv.ContourArea(contours)
          if area > max_area:
              max_area = area
              max_contours = contours
          contours = contours.h_next()
    except TypeError, e:
      return max_area, max_contours
    return max_area, max_contours

def find_max_rectangle(contours):
    max_a, contours = max_area(contours)
    left, top, w, h = cv.BoundingRect(contours)
    right = left + w
    bottom = top + h
    center_x = left + w/2
    center_y = top + h/2 
    if (center_x > 270) and (center_x < 810) and (center_y > 180) and (center_y < 540): 
      isCenter = 1
    elif ((center_x > 0) and (center_x < 270)) or ((center_x > 810) and (center_x < 1080)): 
      isCenter = 0
    else: 
      isCenter = None
    return left, top, right, bottom, isCenter

''' Plot Functions '''

def plot_contours(contours, shape):
    img = cv.CreateImage(shape, 8, 3)
    cv.NamedWindow('Controus', 1)
    cv.SetZero(img)
    cv.DrawContours(img, contours, color.RED, color.GREEN, 1)
    cv.ShowImage('Controus', img)

''' Test Functions '''
# def test_funcs():
#   import matplotlib.pyplot as pyplot
#   im = cv.LoadImage('test.png')
#   im = bgr2hsv(im)
#   h,s,v = split3(im)
#   h = cvimg2numpy(h)
#   s = cvimg2numpy(s)
#   v = cvimg2numpy(v)
#   print h.shape
#   pyplot.figure(1)
#   pyplot.imshow(h, cmap=pyplot.cm.gray) 
#   pyplot.figure(2)
#   pyplot.imshow(s, cmap=pyplot.cm.gray)
#   pyplot.figure(3)
#   pyplot.imshow(v, cmap=pyplot.cm.gray)
#   # pyplot.show() To Show Image
#   pyplot.figure(4)
#   (n, bins) = numpy.histogram(h.flatten(), bins=30)
#   binc = .5*(bins[1:]+bins[:-1])
#   print binc[n.argmax()]

''' Self Test Functions '''
# if __name__=='__main__': 
#   im = cv.LoadImage('test_1/2.png')
#   b,g,r = split3(im)
#   im2 = merge3(b,g,r)
#   # cv.SaveImage('out.png', im2)
#   # test_funcs() # test
#   # exit(0)
#   im3 = bgr2gray(im2)
#   contours = find_contours(im3)
#   test_rectangle = find_max_rectangle(contours)
#   print 'test_rectangle: '
#   print test_rectangle
#   area = cv.ContourArea(contours)
#   print 'area: '
#   print area
#   hull = find_convex_hull(contours)
#   defects = find_convex_defects(contours, hull)
#   print 'defects: '
#   print defects
#   plot_contours(contours, (im.width, im.height))