import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

# im = Image.open('post_card.jpg')
# print(im.size, im.format, im.mode)
# im.show()

#
class PostCardMaker:

    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = 'post_card.jpg' if template is None else template
        if font_path is None:
            self.font_path = os.path.join('fonts', 'ofont_ru_DS Eraser2.ttf')
        else:
            self.font_path = font_path

    def make(self, resize=False):
        im = Image.open('post_card.jpg')
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=30)

        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f'Привет, {self.name}!'
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['red'])

        y = im.size[1] - 20 - font.size
        message = f'С ужастным праздником тебя'
        draw.text((10, y), message, font=font, fill=ImageColor.colormap['red'])

        im.show()

if __name__ == '__main__':
    maker = PostCardMaker(name='Мария')
    maker.make(resize=True)