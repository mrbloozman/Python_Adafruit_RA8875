import pygame
import pygame.gfxdraw
import sys

# port of Adafruit_RA8875.cpp
from adafruit_gfx import *
from adafruit_ra8875_sim.Adafruit_RA8875_h import *


######################################################################
# Constructor for a new RA8875 instance
# @args CS[in]  Location of the SPI chip select pin
# @args RST[in] Location of the reset pin
######################################################################

class Adafruit_RA8875(GFX):
	def __init__(self, CS, RST):
		GFX.__init__(self, 800, 480)
		self._cs = CS
		self._rst = RST

	######################################################################
	# Initialises the LCD driver and any HW required by the display

	# @args s[in] The display size, which can be either:
	#           'RA8875_480x272' (4.3" displays) r
	#           'RA8875_800x480' (5" and 7" displays)
	######################################################################

	def begin(self,s):
		self._size = s

		if self._size == RA8875sizes.RA8875_480x272:
			self._width = 480
			self._height = 272
		elif self._size == RA8875sizes.RA8875_800x480:
			self._width = 800
			self._height = 480
		else:
			return False

		self.initialize()
		return True

	######################################################################
	# Performs a SW-based reset of the RA8875
	######################################################################

	def softReset(self):
		# self.writeCommand(RA8875_PWRR)
		# self.writeData(RA8875_PWRR_SOFTRESET)
		# self.writeData(RA8875_PWRR_NORMAL)
		pass

	def initialize(self):
		self._screen = pygame.display.set_mode([self.width(), self.height()])
		pygame.display.flip()



	######################################################################
	# Returns the display width in pixels
	######################################################################

	def width(self):
		return self._width

	######################################################################
	# Returns the display height in pixels
	######################################################################

	def height(self):
		return self._height

	######################################################################
	# Sets the display in text mode (as opposed to graphics mode)
	######################################################################

	def textMode(self):
		# Set text mode
		# self.writeCommand(RA8875_MWCR0)
		# temp = self.readData()
		# temp |= RA8875_MWCR0_TXTMODE # Set bit 7
		# self.writeData(temp)

		# Select the internal (ROM) font
		# self.writeCommand(0x21)
		# temp = self.readData()
		# temp &= ~((1<<7) | (1<<5)) # Clear bits 7 and 5
		# self.writeData(temp)
		pass

	######################################################################
	# Sets the display in text mode (as opposed to graphics mode)

	# @args x[in] The x position of the cursor (in pixels, 0..1023)
	# @args y[in] The y position of the cursor (in pixels, 0..511)
	######################################################################

	def textSetCursor(self, x, y):
		self._cursor = (x,y)

	######################################################################
	# Sets the fore and background color when rendering text

	# @args foreColor[in] The RGB565 color to use when rendering the text
	# @args bgColor[in]   The RGB565 colot to use for the background
	######################################################################

	def rgb(self,color):
		return ((color & 0xFF0000)>>16,(color & 0xFF00)>>8,(color & 0xFF))

	def textColor(self, foreColor, bgColor):
		# Set Fore Color

		self._fg = self.rgb(foreColor)
		self._bg = self.rgb(bgColor)

	######################################################################
	# Sets the fore color when rendering text with a transparent bg

	# @args foreColor[in] The RGB565 color to use when rendering the text
	######################################################################

	def textTransparent(self, foreColor):
		# Set Fore Color
		# self.writeCommand(0x63)
		# self.writeData((foreColor & 0xf800) >> 11)
		# self.writeCommand(0x64)
		# self.writeData((foreColor & 0x07e0) >> 5)
		# self.writeCommand(0x65)
		# self.writeData((foreColor & 0x001f))

		# Set transparency flag
		# self.writeCommand(0x22)
		# temp = self.readData()
		# temp |= (1<<6) # Set bit 6
		# self.writeData(temp)
		# ToDo
		pass

	######################################################################
	# Sets the text enlarge settings, using one of the following values:

	# 0 = 1x zoom
	# 1 = 2x zoom
	# 2 = 3x zoom
	# 3 = 4x zoom

	# @args scale[in]   The zoom factor (0..3 for 1-4x zoom)
	######################################################################

	def textEnlarge(self, scale):
		if scale > 3:
			scale = 3

		# Set font size flags
		# self.writeCommand(0x22)
		# temp = self.readData()
		# temp &= ~(0xF) # Clears bits 0..3
		# temp |= scale << 2
		# temp |= scale
		# self.writeData(temp)

		self._textScale = scale

	######################################################################
	# Renders some text on the screen when in text mode

	# @args buffer[in]    The buffer containing the characters to render
	# @args len[in]       The size of the buffer in bytes
	######################################################################

	def textWrite(self, buffer, ln):
		# if ln == 0:
		# 	ln = len(buffer)
		# self.writeCommand(RA8875_MRWC)

		# for i in range(ln):
		# 	self.writeData(ord(buffer[i]))

		font = pygame.font.SysFont(None,8*self._textScale)
		font_surface = font.render(buffer, False, self._fg, self._bg)
		self._screen.blit(font_surface,self._cursor)
		pygame.display.flip()

		######################################################################
		# Sets the display in graphics mode (as opposed to text mode)
		######################################################################

	def graphicsMode(self):
		# self.writeCommand(RA8875_MWCR0)
		# temp = self.readData()
		# temp &= ~RA8875_MWCR0_TXTMODE # bit #7
		# self.writeData(temp)
		pass

	######################################################################
	# Waits for screen to finish by polling the status!
	######################################################################

	def waitPoll(self, regname, waitflag):
		# Wait for the command to finish
		# while True:
		# 	temp = self.readReg(regname)
			# print 'waitPoll(' + hex(regname) + ','+hex(waitflag)+'): '+hex(temp)
			# if not (temp & waitflag):
			# 	return True
		# return false # MEMEFIX: yeah i know, unreached! - add timeout?
		return True
	######################################################################
	# Sets the current X/Y position on the display before drawing

	# @args x[in] The 0-based x location
	# @args y[in] The 0-base y location
	######################################################################

	def setXY(self, x, y):
		# self.writeReg(RA8875_CURH0, x)
		# self.writeReg(RA8875_CURH1, x >> 8)
		# self.writeReg(RA8875_CURV0, y)
		# self.writeReg(RA8875_CURV1, y >> 8)
		self._cursor = (x,y)

	######################################################################
	# HW accelerated function to push a chunk of raw pixel data

	# @args num[in] The number of pixels to push
	# @args p[in]   The pixel color to use
	######################################################################

	def pushPixels(self, num, p):
		# digitalWrite(_cs, LOW);
		# GPIO.output(self._cs, GPIO.LOW)
		# self.spi.xfer2([RA8875_DATAWRITE])
		# while num > 0:
		# 	self.spi.xfer2([(p >> 8),p])
		# 	num = num-1
		# digitalWrite(_cs, HIGH);
		# GPIO.output(self._cs, GPIO.HIGH)
		pass
		# ToDo

	######################################################################

	######################################################################

	def fillRect(self):
		# self.writeCommand(RA8875_DCR)
		# self.writeData(RA8875_DCR_LINESQUTRI_STOP | RA8875_DCR_DRAWSQUARE)
		# self.writeData(RA8875_DCR_LINESQUTRI_START | RA8875_DCR_FILL | RA8875_DCR_DRAWSQUARE)
		pass
		# ToDo


	######################################################################
	# Draws a single pixel at the specified location

	# @args x[in]     The 0-based x location
	# @args y[in]     The 0-base y location
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def drawPixel(self, x, y, color):
		pygame.gfxdraw.pixel(self._screen, x, y, self.rgb(color))
		pygame.display.flip()

	######################################################################
	# Draws a HW accelerated line on the display

	# @args x0[in]    The 0-based starting x location
	# @args y0[in]    The 0-base starting y location
	# @args x1[in]    The 0-based ending x location
	# @args y1[in]    The 0-base ending y location
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def drawLine(self, x0, y0, x1, y1, color):
		pygame.gfxdraw.line(self._screen,x0,y0,x1,y1,self.rgb(color))
		pygame.display.flip()

	######################################################################

	######################################################################

	def drawFastVLine(self, x, y, h, color):
		pygame.gfxdraw.line(self._screen,x, y, x, y+h, self.rgb(color))
		pygame.display.flip()

	######################################################################

	######################################################################

	def drawFastHLine(self, x, y, w, color):
		pygame.gfxdraw.line(self._screen,x, y, x+w, y, self.rgb(color))
		pygame.display.flip()

	######################################################################
	# Draws a HW accelerated rectangle on the display

	# @args x[in]     The 0-based x location of the top-right corner
	# @args y[in]     The 0-based y location of the top-right corner
	# @args w[in]     The rectangle width
	# @args h[in]     The rectangle height
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def drawRect(self, x, y, w, h, color):
		self.rectHelper(x, y, x+w, y+h, color, False)
		pygame.display.flip()

	######################################################################
	# Draws a HW accelerated filled rectangle on the display

	# @args x[in]     The 0-based x location of the top-right corner
	# @args y[in]     The 0-based y location of the top-right corner
	# @args w[in]     The rectangle width
	# @args h[in]     The rectangle height
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def fillRect(self, x, y, w, h, color):
		self.rectHelper(x, y, x+w, y+h, color, True)
		pygame.display.flip()

	######################################################################
	# Fills the screen with the spefied RGB565 color

	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def fillScreen(self, color):
		self.rectHelper(0, 0, self._width-1, self._height-1, color, True)
		pygame.display.flip()

	######################################################################
	# Draws a HW accelerated circle on the display

	# @args x[in]     The 0-based x location of the center of the circle
	# @args y[in]     The 0-based y location of the center of the circle
	# @args w[in]     The circle's radius
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def drawCircle(self, x0, y0, r, color):
		self.circleHelper(x0, y0, r, color, False)

	######################################################################
	# Draws a HW accelerated filled circle on the display

	# @args x[in]     The 0-based x location of the center of the circle
	# @args y[in]     The 0-based y location of the center of the circle
	# @args w[in]     The circle's radius
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def fillCircle(self, x0, y0, r, color):
		self.circleHelper(x0, y0, r, color, True)

	######################################################################
	# Draws a HW accelerated triangle on the display

	# @args x0[in]    The 0-based x location of point 0 on the triangle
	# @args y0[in]    The 0-based y location of point 0 on the triangle
	# @args x1[in]    The 0-based x location of point 1 on the triangle
	# @args y1[in]    The 0-based y location of point 1 on the triangle
	# @args x2[in]    The 0-based x location of point 2 on the triangle
	# @args y2[in]    The 0-based y location of point 2 on the triangle
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def drawTriangle(self, x0, y0, x1, y1, x2, y2, color):
		self.triangleHelper(x0, y0, x1, y1, x2, y2, color, False)

	######################################################################
	# Draws a HW accelerated filled triangle on the display

	# @args x0[in]    The 0-based x location of point 0 on the triangle
	# @args y0[in]    The 0-based y location of point 0 on the triangle
	# @args x1[in]    The 0-based x location of point 1 on the triangle
	# @args y1[in]    The 0-based y location of point 1 on the triangle
	# @args x2[in]    The 0-based x location of point 2 on the triangle
	# @args y2[in]    The 0-based y location of point 2 on the triangle
	# @args color[in] The RGB565 color to use when drawing the pixel
	######################################################################

	def fillTriangle(self, x0, y0, x1, y1, x2, y2, color):
		self.triangleHelper(x0, y0, x1, y1, x2, y2, color, True)

	######################################################################
	# Draws a HW accelerated ellipse on the display

	# @args xCenter[in]   The 0-based x location of the ellipse's center
	# @args yCenter[in]   The 0-based y location of the ellipse's center
	# @args longAxis[in]  The size in pixels of the ellipse's long axis
	# @args shortAxis[in] The size in pixels of the ellipse's short axis
	# @args color[in]     The RGB565 color to use when drawing the pixel
	######################################################################

	def drawEllipse(self, xCenter, yCenter, longAxis, shortAxis, color):
		self.ellipseHelper(xCenter, yCenter, longAxis, shortAxis, color, False)

	######################################################################
	# Draws a HW accelerated filled ellipse on the display

	# @args xCenter[in]   The 0-based x location of the ellipse's center
	# @args yCenter[in]   The 0-based y location of the ellipse's center
	# @args longAxis[in]  The size in pixels of the ellipse's long axis
	# @args shortAxis[in] The size in pixels of the ellipse's short axis
	# @args color[in]     The RGB565 color to use when drawing the pixel
	######################################################################

	def fillEllipse(self, xCenter, yCenter, longAxis, shortAxis, color):
		self.ellipseHelper(xCenter, yCenter, longAxis, shortAxis, color, True)

	######################################################################
	# Draws a HW accelerated curve on the display

	# @args xCenter[in]   The 0-based x location of the ellipse's center
	# @args yCenter[in]   The 0-based y location of the ellipse's center
	# @args longAxis[in]  The size in pixels of the ellipse's long axis
	# @args shortAxis[in] The size in pixels of the ellipse's short axis
	# @args curvePart[in] The corner to draw, where in clock-wise motion:
	#                     0 = 180-270
	#                     1 = 270-0
	#                     2 = 0-90
	#                     3 = 90-180
	# @args color[in]     The RGB565 color to use when drawing the pixel
	######################################################################

	def drawCurve(self, xCenter, yCenter, longAxis, shortAxis, curvePart, color):
		self.curveHelper(xCenter, yCenter, longAxis, shortAxis, curvePart, color, False)

	######################################################################
	# Draws a HW accelerated filled curve on the display

	# @args xCenter[in]   The 0-based x location of the ellipse's center
	# @args yCenter[in]   The 0-based y location of the ellipse's center
	# @args longAxis[in]  The size in pixels of the ellipse's long axis
	# @args shortAxis[in] The size in pixels of the ellipse's short axis
	# @args curvePart[in] The corner to draw, where in clock-wise motion:
	#                     0 = 180-270
	#                     1 = 270-0
	#                     2 = 0-90
	#                     3 = 90-180
	# @args color[in]     The RGB565 color to use when drawing the pixel
	######################################################################

	def fillCurve(self, xCenter, yCenter, longAxis, shortAxis, curvePart, color):
		self.curveHelper(xCenter, yCenter, longAxis, shortAxis, curvePart, color, True)

	######################################################################
	# Helper function for higher level circle drawing code
	######################################################################

	def circleHelper(self, x0, y0, r, color, filled):

		if filled:
			pygame.gfxdraw.filled_circle(self._screen, x0, y0, r, self.rgb(color))
		else:
			pygame.gfxdraw.circle(self._screen, x0, y0, r, self.rgb(color))

	######################################################################
	# Helper function for higher level rectangle drawing code
	######################################################################

	def rectHelper(self, x, y, w, h, color, filled):
		if filled:
			pygame.gfxdraw.rectangle(self._screen,(x,y,w,h),self.rgb(color))
		else:
			pygame.gfxdraw.box(self._screen,(x,y,w,h),self.rgb(color))

	######################################################################
	# Helper function for higher level triangle drawing code
	######################################################################

	def triangleHelper(self, x0, y0, x1, y1, x2, y2, color, filled):
		if filled:
			pygame.gfxdraw.filled_trigon(self._screen,x0,y0,x1,y1,x2,y2,self.rgb(color))
		else:
			pygame.gfxdraw.trigon(self._screen,x0,y0,x1,y1,x2,y2,self.rgb(color))

	######################################################################
	# Helper function for higher level ellipse drawing code
	######################################################################

	def ellipseHelper(self, xCenter, yCenter, longAxis, shortAxis, color, filled):
		if filled:
			pygame.gfxdraw.filled_ellipse(self._screen,xCenter, yCenter, longAxis, shortAxis, self.rgb(color))
		else:
			pygame.gfxdraw.ellipse(self._screen,xCenter, yCenter, longAxis, shortAxis, self.rgb(color))

	######################################################################
	# Helper function for higher level curve drawing code
	######################################################################

	def curveHelper(self, xCenter, yCenter, longAxis, shortAxis, curvePart, color, filled):
		pass
		# ToDo

	######################################################################
	# Mid Level
	######################################################################

	def GPIOX(self, on):
		pass

		######################################################################

		######################################################################

	def PWM1out(self, p):
		pass

	######################################################################

	######################################################################

	def PWM2out(self, p):
		pass

	######################################################################

	######################################################################

	def PWM1config(self, on, clock):
		pass

		######################################################################

		######################################################################

	def PWM2config(self, on, clock):
		pass

		######################################################################
		# Enables or disables the on-chip touch screen controller
		######################################################################

	def touchEnable(self, on):
		#ToDo

		if on:
			return
		else:
			return

		######################################################################
		# Checks if a touch event has occured

		# @returns  True is a touch event has occured (reading it via
		#         touchRead() will clear the interrupt in memory)
		######################################################################

	def touched(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				self._tx = event.pos[0]
				self._ty = event.pos[1]
				return True
		return False

	######################################################################
	# Reads the last touch event

	# @args x[out]  Pointer to the uint16_t field to assign the raw X value
	# @args y[out]  Pointer to the uint16_t field to assign the raw Y value

	# @note Calling this function will clear the touch panel interrupt on
	#     the RA8875, resetting the flag used by the 'touched' function
	######################################################################

	def touchRead(self):
		# tx = self.readReg(RA8875_TPXH)
		# ty = self.readReg(RA8875_TPYH)
		# temp = self.readReg(RA8875_TPXYL)
		# tx <<= 2
		# ty <<= 2
		# tx |= temp & 0x03        # get the bottom x bits
		# ty |= (temp >> 2) & 0x03 # get the bottom y bits

		# /* Clear TP INT Status */
		# self.writeReg(RA8875_INTC2, RA8875_INTC2_TP)

		xScale = 1024.0/self.width()
		yScale = 1024.0/self.height()


		return {'x':int(self._tx*xScale),'y':int(self._ty*yScale)}
	######################################################################
	# Turns the display on or off
	######################################################################

	def displayOn(self, on):
		if on:
			pygame.display.flip()
		else:
			self._screen.get_surface().fill((0,0,0))

		######################################################################
		# Puts the display in sleep mode, or disables sleep mode if enabled
		######################################################################

	def sleep(self, sleep):
		pass

		######################################################################
		# Low Level
		######################################################################

	def writeReg(self, reg, val):
		pass

	######################################################################

	######################################################################

	def readReg(self, reg):
		# self.writeCommand(reg)
		return 255
	# return 255

	######################################################################

	######################################################################

	def writeData(self, d):
		pass

	######################################################################

	######################################################################

	def readData(self):

		return 0

	######################################################################

	######################################################################

	def writeCommand(self, d):
		pass

	######################################################################

	######################################################################

	def readStatus(self):

		return 0

######################################################################

######################################################################



