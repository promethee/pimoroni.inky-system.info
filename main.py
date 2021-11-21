#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont, ImageColor
from fonts.ttf import RobotoMedium

inky_display = auto(ask_user=True, verbose=True)
WIDTH, HEIGHT = inky_display.resolution
SMALL_DISPLAY = WIDTH == 212

COLOR = inky_display.colour
BLACK = inky_display.BLACK
WHITE = inky_display.WHITE

font_smiley = ImageFont.truetype("CODE2000.TTF", 28 if SMALL_DISPLAY else 72)
font = ImageFont.truetype(RobotoMedium, 16 if SMALL_DISPLAY else 64)

img = Image.new("P", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

inky_display.set_border(inky_display.BLACK)
inky_display.h_flip = os.environ.get('FLIP_H', SMALL_DISPLAY)
inky_display.v_flip = os.environ.get('FLIP_V', SMALL_DISPLAY)

draw.rectangle((0, 0, WIDTH, HEIGHT), fill=WHITE)

def draw_credits(text, h):
  text_w, text_h = draw.textsize(text, font=font)
  x,y = 16, (h - int(text_h * 0.25))
  draw.text((x, y), text, font=font_smiley, fill=BLACK)

draw_credits("¯\_(ツ)_/¯", HEIGHT*(0.05 if SMALL_DISPLAY else 0.1))
draw_credits("promethee", HEIGHT*(0.35 if SMALL_DISPLAY else 0.4))
draw_credits("@github", HEIGHT*(0.65 if SMALL_DISPLAY else 0.7))
inky_display.set_image(img)
inky_display.show(img)

