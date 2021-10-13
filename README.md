# CURRY Reader For Python
This is an open-source tool which allows to load CURRY data into Python. It supports: raw float (.cdt), ascii (.cdt), legacy raw float (.dat) and legacy ascii (.dat).

# Installation And Dependencies	
This package depends on numpy. If you are new to Python and don't already have numpy, please see https://numpy.org/install/

We recommend using the Miniconda (https://docs.conda.io/en/latest/miniconda.html) distribution of Python.

The complete list of dependencies is contained in the file requirements.txt
	
Having installed a Python distribution, install dependencies for this package in command prompt in Windows or terminal in Linux/MacOs
by navigating to the this project's folder (where requirements.txt is located) and use:

pip install -r requirements.txt --user  
    
# Inputs
    inputfilename:	    if left empty, reader will prompt user with file selection box, otherwise specify filename with path;
                        supported files are: raw float (cdt), ascii (cdt), legacy raw float (dat) and legacy ascii (dat)
    plotdata:           plotdata = 0, don't show plot
                        plotdata = 1, show plot (default)  
                        plotdata = x, with x > 1, shows and automatically closes plot after x seconds
    verbosity:          1 is low, 2 is medium (default) and 3 is high

# Output As Dictionary With Keys
    'data'              functional data matrix (e.g. EEG, MEG) with dimensions (samples, channels)
    'datainfo'          data information with keys: {'samples', 'channels', 'trials/epochs', 'sampling', 'frequency'}
    'labels'            channel labels
    'sensorpos'         channel locations [x,y,z]
    'events'            events matrix where every row corresponds to: [event latency, event type, event start, event stop]
    'annotations'       corresponding annotations to each event
    'epochinfo'         epochs matrix where every row corresponds to: [number of averages, total epochs, type, accept, correct, response, response time]
    'epochlabels'       epoch labels
    'impedancematrix'   impedance matrix with max size (channels, 10), corresponding to last ten impedance measurements
    'hpimatrix'         HPI-coil measurements matrix (Orion-MEG only) where every row is: [measurementsample, dipolefitflag, x, y, z, deviation] 
   
# Usage Examples
	import curryreader as cr

	# 1) Use file selection box, show plot (default), verbosity (default), output in dictionary "currydata"
	currydata = cr.read()

	# 2) Specify file path, avoid plot, minimum verbosity, output in dictionary "currydata"
	currydata = cr.read("test_data\\Float.cdt", plotdata = 0, verbosity = 1)

	# 3) Specify file path, show plot (default), verbosity (default), output in dictionary "currydata", print items
	currydata = cr.read("test_data\\HPI.cdt")
	for key, value in currydata.items(): print(key + ":\n", value)

# Licensing
BSD (3-clause)
