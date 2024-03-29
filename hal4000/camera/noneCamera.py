#!/usr/bin/python
#
## @file
#
# Camera for the none setup.
#
# Hazen 12/13
#

import sc_library.hdebug as hdebug

import camera.classicSingleCamera as classicSingleCamera
#import camera.detachedSingleCamera as detachedSingleCamera

class ACamera(classicSingleCamera.ClassicSingleCamera):
#class ACamera(detachedSingleCamera.DetachedSingleCamera):

    @hdebug.debug
    def __init__(self, hardware, parameters, camera_frame, camera_params_frame, parent = None):
        classicSingleCamera.ClassicSingleCamera.__init__(self, hardware, parameters, camera_frame, camera_params_frame, parent)

#    @hdebug.debug
#    def __init__(self, parameters, parent = None):
#        detachedSingleCamera.DetachedSingleCamera.__init__(self, parameters, parent)

def getMode():
    return "single"

#
# The MIT License
#
# Copyright (c) 2013 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

