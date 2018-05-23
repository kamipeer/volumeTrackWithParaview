#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'CSV Reader'
particles_200csv = CSVReader(FileName=['/home/eric/RemoteCluster/Simulations/20180514SmallerVentricle/particleFolder1/particles_200.csv'])
particles_200csv.DetectNumericColumns = 1
particles_200csv.UseStringDelimiter = 1
particles_200csv.HaveHeaders = 1
particles_200csv.FieldDelimiterCharacters = ','
particles_200csv.MergeConsecutiveDelimiters = 0

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.UseCache = 0
spreadSheetView1.ViewSize = [400, 400]
spreadSheetView1.CellFontSize = 9
spreadSheetView1.HeaderFontSize = 9
spreadSheetView1.SelectionOnly = 0
spreadSheetView1.GenerateCellConnectivity = 0
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.SelectedComponent = -1
spreadSheetView1.InvertOrder = 0
spreadSheetView1.BlockSize = 1024L
spreadSheetView1.ColumnVisibility = []

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, spreadSheetView1)

# show data in view
particles_200csvDisplay = Show(particles_200csv, spreadSheetView1)
# trace defaults for the display properties.
particles_200csvDisplay.FieldAssociation = 'Row Data'
particles_200csvDisplay.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=particles_200csv)
tableToPoints1.XColumn = 'APD'
tableToPoints1.YColumn = 'APD'
tableToPoints1.ZColumn = 'APD'
tableToPoints1.a2DPoints = 0
tableToPoints1.KeepAllDataArrays = 0

# Properties modified on tableToPoints1
tableToPoints1.XColumn = 'x'
tableToPoints1.YColumn = 'y'
tableToPoints1.ZColumn = 'z'

# show data in view
tableToPoints1Display = Show(tableToPoints1, spreadSheetView1)
# trace defaults for the display properties.
tableToPoints1Display.FieldAssociation = 'Point Data'
tableToPoints1Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(particles_200csv, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(Input=tableToPoints1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'APD']
glyph1.Vectors = ['POINTS', 'None']
glyph1.Orient = 1
glyph1.ScaleMode = 'off'
glyph1.ScaleFactor = 0.0009695249999999999
glyph1.GlyphMode = 'Uniform Spatial Distribution'
glyph1.MaximumNumberOfSamplePoints = 5000
glyph1.Seed = 10339
glyph1.Stride = 1
glyph1.GlyphTransform = 'Transform2'

# init the 'Arrow' selected for 'GlyphType'
glyph1.GlyphType.TipResolution = 6
glyph1.GlyphType.TipRadius = 0.1
glyph1.GlyphType.TipLength = 0.35
glyph1.GlyphType.ShaftResolution = 6
glyph1.GlyphType.ShaftRadius = 0.03
glyph1.GlyphType.Invert = 0

# init the 'Transform2' selected for 'GlyphTransform'
glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]

# Properties modified on glyph1.GlyphType
glyph1.GlyphType.Radius = 0.1

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.GlyphMode = 'All Points'

# Properties modified on glyph1.GlyphType
glyph1.GlyphType.Radius = 0.1

# show data in view
glyph1Display = Show(glyph1, spreadSheetView1)
# trace defaults for the display properties.
glyph1Display.FieldAssociation = 'Point Data'
glyph1Display.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Threshold'
threshold1 = Threshold(Input=glyph1)
threshold1.Scalars = ['POINTS', 'GlyphScale']
threshold1.ThresholdRange = [0.2804499864578247, 0.29482001066207886]
threshold1.AllScalars = 1
threshold1.UseContinuousCellRange = 0

# Properties modified on threshold1
threshold1.Scalars = ['POINTS', 'particleCategory']
threshold1.ThresholdRange = [98.0, 98.0]

# show data in view
threshold1Display = Show(threshold1, spreadSheetView1)
# trace defaults for the display properties.
threshold1Display.FieldAssociation = 'Point Data'
threshold1Display.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Delaunay 3D'
delaunay3D1 = Delaunay3D(Input=threshold1)
delaunay3D1.Alpha = 0.0
delaunay3D1.Tolerance = 0.001
delaunay3D1.Offset = 2.5
delaunay3D1.BoundingTriangulation = 0
delaunay3D1.AlphaTets = 1
delaunay3D1.AlphaTris = 1
delaunay3D1.AlphaLines = 0
delaunay3D1.AlphaVerts = 0

# show data in view
delaunay3D1Display = Show(delaunay3D1, spreadSheetView1)
# trace defaults for the display properties.
delaunay3D1Display.FieldAssociation = 'Point Data'
delaunay3D1Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(threshold1, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(Input=delaunay3D1)
integrateVariables1.DivideCellDataByVolume = 0

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1)
# trace defaults for the display properties.
integrateVariables1Display.FieldAssociation = 'Point Data'
integrateVariables1Display.CompositeDataSetIndex = [0]

# update the view to ensure updated data information
spreadSheetView1.Update()

# set active source
SetActiveSource(integrateVariables1)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
