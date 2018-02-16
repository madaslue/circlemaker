import scipy as sp
import matplotlib.pyplot as plt

#first 5 bragg condition meeting vectors for the 4 structures of interest
braggSC =  sp.array([[1,0,0],[1,1,0],[1,1,1],[2,0,0],[2,1,0]])
braggFCC = sp.array([[1,1,1],[2,0,0],[2,2,0],[3,1,1],[2,2,2]])
braggBCC = sp.array([[1,1,0],[2,0,0],[2,1,1],[2,2,0],[3,1,0]])
braggDia = sp.array([[1,1,1],[2,2,0],[3,1,1],[4,0,0],[3,3,1]])

cuKAlpha = 1.542
unitCella = 5.0

def makecircles(peakArray, wavelength, cellSize,name):
	circlePlot, ax= plt.subplots()
	filename = name + '.png'
	f.write( "--------------------- \n" )
	f.write( name + ':\n' )
	f.write(' Index   2Theta \n')
	datalimit = sp.array([0])
	for peak in peakArray:
		dhkl = cubicDSpacing(cellSize, peak)
		angle = sp.arcsin( wavelength / ( 2 * dhkl ) )
		radius = sp.tan(2 * angle)
		f.write( str(peak) + str( 2 * sp.rad2deg(angle) ) + '\n' )
		circle = plt.Circle((0,0), radius, fill=False)
		ax.add_artist(circle)
		if radius > datalimit:
			datalimit = radius
	ax.set_aspect('equal', adjustable='datalim')
	graphLimits = datalimit * 1.3 # this magic number is just a format thing
	plt.xlim(-graphLimits, graphLimits)
	plt.ylim(-graphLimits, graphLimits)
	circlePlot.savefig(filename)
	f.write( "--------------------- \n\n" )


def cubicDSpacing(cellSize, millerIndex):
	h,k,l = millerIndex[[0]], millerIndex[[1]], millerIndex[[2]]
	dSpacing = cellSize/( sp.sqrt( h**2 + k**2 + l**2 ) )
	return dSpacing


f = open('Circles','w')
f.write( 'Assumptions made: \n' )
f.write( 'Cu Kalpha = ' + str(cuKAlpha) + ' Angstroms \n' )
f.write( 'Distance to detector = 1 (arbitrary unit)\n' )
makecircles(braggSC,  cuKAlpha, unitCella, 'Simple Cubic')
makecircles(braggFCC, cuKAlpha, unitCella, 'Face Centered Cubic')
makecircles(braggBCC, cuKAlpha, unitCella, 'Body Centered Cubic')
makecircles(braggDia, cuKAlpha, unitCella, 'Diamond')
f.close()
