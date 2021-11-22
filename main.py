#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import shutil
from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont, ImageColor
from fonts.ttf import RobotoMedium

inky_display = auto(ask_user=True, verbose=True)
WIDTH, HEIGHT = inky_display.resolution
SMALL_DISPLAY = WIDTH == 212

COLOR = inky_display.colour
BLACK = inky_display.BLACK
WHITE = inky_display.WHITE

font_size = 24 if SMALL_DISPLAY else 64
font_smiley = ImageFont.truetype("CODE2000.TTF", 28 if SMALL_DISPLAY else 72)
font = ImageFont.truetype(RobotoMedium, font_size)

img = Image.new("P", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

inky_display.set_border(inky_display.BLACK)
inky_display.h_flip = os.environ.get('FLIP_H', SMALL_DISPLAY)
inky_display.v_flip = os.environ.get('FLIP_V', SMALL_DISPLAY)

def get_ratio(part, total):
  return (part / total)

def draw_credits(text, h):
  text_w, text_h = draw.textsize(text, font=font)
  x,y = 16, (h - int(text_h * 0.25))
  draw.text((x, y), text, font=font_smiley, fill=BLACK)

def draw_system_info_bg(margin):
  bg_margin = 8
  x = bg_margin
  w = WIDTH - (bg_margin*2)
  y = (HEIGHT*0.7) + bg_margin
  h = (HEIGHT*0.1) + bg_margin
  draw.rectangle((x, y, x+w, y+h), fill=BLACK)
  return x,y,w,h

def draw_system_info_ratio(x,y,w,h,ratio, margin):
  draw.rectangle((x+margin, y+margin, x+(round(w * ratio))-margin, y+h-margin), fill=WHITE)

def draw_system_info(total, used, free, ratio_used, ratio_free):
  draw.rectangle((0, 0, WIDTH, HEIGHT), fill=WHITE)
  margin = 4
  x,y,w,h = draw_system_info_bg(margin)
  draw_system_info_ratio(x,y,w,h,ratio_free, margin)
  draw.text((8, (font_size * 0)), f'SIZE {total // (2**30)} Go', BLACK, font)
  draw.text((8, (font_size * 1)), f'FREE {free // (2**30)} Go | {round(ratio_free*100)} %', BLACK, font)
  draw.text((8, (font_size * 2)), f'USED {used // (2**30)} Go | {round(ratio_used*100)} %', BLACK, font)

draw.rectangle((0, 0, WIDTH, HEIGHT), fill=WHITE)
draw_credits("¯\_(ツ)_/¯", HEIGHT*(0.05 if SMALL_DISPLAY else 0.1))
draw_credits("promethee", HEIGHT*(0.35 if SMALL_DISPLAY else 0.4))
draw_credits("@github", HEIGHT*(0.65 if SMALL_DISPLAY else 0.7))
inky_display.set_image(img)
inky_display.show(img)
time.sleep(1)

while True:
  total, used, free = shutil.disk_usage("/")
  ratio_used = used / total
  ratio_free = free / total

  draw_system_info(total, used, free, ratio_used, ratio_free)
  inky_display.set_image(img)
  inky_display.show(img)

  time.sleep(60)

