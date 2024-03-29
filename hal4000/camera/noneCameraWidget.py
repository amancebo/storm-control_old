#!/usr/bin/python
#
## @file
#
# qtCameraWidget specialized for displaying data from the
# emulated camera.
#
# Hazen 10/13
#

import numpy
from PyQt4 import QtCore, QtGui

import qtWidgets.qtCameraWidget as qtCameraWidget

## ACameraWidget
#
# The UI for displaying the "data" from the emulated camera.
#
class ACameraWidget(qtCameraWidget.QCameraWidget):

    ## __init__
    #
    # Create a emulated camera widget.
    #
    # @param parameters A camera parameters object.
    # @param parent (Optional) The PyQt parent of this object.
    #
    def __init__(self, parameters, parent = None):
        qtCameraWidget.QCameraWidget.__init__(self, parameters, parent)

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
# The above copyright notice and this permission notice shall be included 
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
