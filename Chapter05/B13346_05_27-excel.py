"""Convert a spreadsheet to a shapefile"""

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.xls

import xlrd
import shapefile

# Open the spreadsheet reader
xls = xlrd.open_workbook("NYC_MUSEUMS_GEO.xls")
sheet = xls.sheet_by_index(0)

# Open the shapefile writer
with shapefile.Writer("NYC_MUSEUMS_XLS2SHP", shapefile.POINT) as w:
    # Move data from spreadsheet to shapefile
    for i in range(sheet.ncols):
        w.field(str(sheet.cell(0, i).value), "C", 40)
    for i in range(1, sheet.nrows):
        values = []
        for j in range(sheet.ncols):
            values.append(sheet.cell(i, j).value)
        w.record(*values)
        w.point(float(values[-2]), float(values[-1]))
