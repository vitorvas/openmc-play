#!/usr/bin/env python3

import openmc

triga = openmc.data.IncidentNeutron.from_ace('../xsdata/sssth1-TRIGA.ace')
triga.export_to_hdf5('../xsdata/TRIGA.h5')

library = openmc.data.DataLibrary()
library.register_file('../xsdata/TRIGA.h5')
library.export_to_xml()


