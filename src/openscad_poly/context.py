"""
Contributors:
Copyright (c) 2016 Benedict Endemann
Copyright (c) 2011 Marty McGuire
"""

class OSCADPolyContext:
    def __init__(self, svg_file):
        self.file = svg_file
        self.polygons = []

    def generate(self):
        generatedScad = ''
        # generate list of all modules at top for easy control
        for polygon in self.polygons:
            if polygon['color']:
                generatedScad += "\ncolor([{:0.4f}, {:0.4f}, {:0.4f}, {:0.4f}]) {}();".format(
                    polygon['color'][0],
                    polygon['color'][1],
                    polygon['color'][2],
                    polygon['color'][3],
                    polygon['id'])
            else:
                generatedScad += "\n{}();".format(polygon['id'])

        # generate actual modules from polygons
        for polygon in self.polygons:
            generatedScad += '\n'
            generatedScad += '\nmodule {}()'.format(polygon['id'])
            generatedScad += '\n  polygon('
            generatedScad += '\n    points='
            generatedScad += '\n      {},'.format(polygon['points'])
            generatedScad += '\n    paths='
            generatedScad += '\n      {}'.format(polygon['paths'])
            generatedScad += '\n  );'

        return generatedScad

    def add_poly(self, poly_id, points, paths, color = None):
        shortened_points = [[round(x, 3),round(y, 3)] for x, y in points]
        self.polygons.append({ 'id': poly_id, 'points':shortened_points, 'paths':paths, 'color':color})
