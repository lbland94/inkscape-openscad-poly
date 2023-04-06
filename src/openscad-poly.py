#!/usr/bin/env python
"""
Copyright (c) 2011 MakerBot(r) Industries

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

Contributors:
Copyright (c) 2016 Benedict Endemann
Copyright (c) 2011 Marty McGuire
"""
import inkex, sys
from openscad_poly.context import OSCADPolyContext
from openscad_poly.svg_parser import SvgParser

class MyEffect(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.context = None
        self.arg_parser.add_argument("--tab", type=str, dest="tab")

    def effect(self):
        self.context = OSCADPolyContext(self.options.input_file)
        parser = SvgParser(self.document.getroot())
        parser.parse()
        for entity in parser.entities:
            entity.make_poly(self.context)

    def save(self, stream):
        """Save the svg document to the given stream"""
        generatedScad = self.context.generate()
        try:
            stream.write(generatedScad)
        except TypeError:
            stream.write(generatedScad.encode('utf-8'))

if __name__ == '__main__':   #pragma: no cover
    e = MyEffect()
    e.run()
