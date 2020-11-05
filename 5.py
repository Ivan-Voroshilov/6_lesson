
class Stationery:

    title = None

    def __init__(self, title=title):
        self.title = title

    def draw(self):
        return 'Starting drawing'


class Pen(Stationery):

    title = 'Pen'

    def draw(self):
        return 'This is pen'


class Pencil(Stationery):

    title = 'Pencil'

    def draw(self):
        return 'This is pencil'


class Handle(Stationery):

    title = 'Handle'

    def draw(self):
        return 'This is handle'


brush = Stationery('Brush')
print(brush.draw())
print(brush.title)

pen = Pen(Pen.title)
print(pen.draw())
print(pen.title)

pencil = Pencil(Pencil.title)
print(pencil.draw())
print(pencil.title)

handle = Handle(Handle.title)
print(handle.draw())
print(handle.title)
