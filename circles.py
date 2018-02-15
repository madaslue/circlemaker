import scipy as sp
import matplotlib.pyplot as plt

#first 5 bragg condition meeting vectors for the 4 structures of interest
braggSC =  sp.array([[1,0,0],[1,1,0],[1,1,1],[2,0,0],[2,1,0]])
braggFCC = sp.array([[1,1,1],[2,0,0],[2,2,0],[2,2,1],[3,1,1]])
braggBCC = sp.array([[1,1,0],[2,0,0],[2,1,1],[2,2,0],[3,1,0]])
braggDia = sp.array([[1,1,1],[2,2,0],[3,1,1],[4,0,0],[3,3,1]])

lamb = 1 # lambda is a keyword, and I'm too lazy for wavelength as a name

def makecircles(peakArray, name):
	circlePlot, ax= plt.subplots()
	filename = name + '.png' 
	print( name )
	for peak in peakArray:
		dhkl = cubicDSpacing(5, peak)
		angle = sp.arcsin((lamb/ (2 * dhkl)))
		radius = sp.tan(2 * angle)
		print( 'Relative radius: ' + str(radius) )
		circle = plt.Circle((0,0), radius, fill=False)
		ax.add_artist(circle)
	ax.set_aspect('equal', adjustable='datalim')
	plt.ylim(-1.5,1.5)
	plt.xlim(-1.5,1.5)
	circlePlot.savefig(filename)
	print( 'Saved as ' + filename )
	print( "---------------" )

def cubicDSpacing(unitcell, millerIndex):
	h,k,l = millerIndex[[0]], millerIndex[[1]], millerIndex[[2]]
	dSpacing = unitcell/(( h**2 + k**2 + l**2 )**(1/2))
	return dSpacing



makecircles(braggSC, 'Simple Cubic')
makecircles(braggFCC, 'Face Centered Cubic')
makecircles(braggBCC, 'Body Centered Cubic')
makecircles(braggDia, 'Diamond')
