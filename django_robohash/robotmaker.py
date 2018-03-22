from .svgparts import parts
import hashlib

def make_robot_svg(string):
    hash = str(int(hashlib.md5(string.encode()).hexdigest(),16))
    accessory, body, eyes, face, mouth, r, g, b = tuple(map(int,hash))[:8]

    color = '{:02X}{:02X}{:02X}'.format(r*25+5, g*25+5, b*25+5)