#
# Created : 2018-03-22
#
# @author: Eric Lapouyade
#

from .svgparts import *
import hashlib


def make_robot_svg(string, width=300, height=300):
    hash = str(int(hashlib.md5(string.encode()).hexdigest(),16))
    accessory,body,eyes,face,mouth,r,g,b,br,bg,bb = tuple(map(int,hash))[:11]
    color = '{:02X}{:02X}{:02X}'.format(r*25+5, g*25+5, b*25+5)
    bgcolor = '{:02X}{:02X}{:02X}'.format(br*25+5, bg*25+5, bb*25+5)
    accessory = parts['accessory'][accessory]
    body = parts['body'][body]
    eyes = parts['eyes'][eyes]
    face = parts['face'][face]
    mouth = parts['mouth'][mouth]
    return template.format(**locals())
