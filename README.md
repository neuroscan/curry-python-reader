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
    inputfilename:	if left empty, reader will prompt user with file selection box, otherwise specify filename with path;
                    supported files are: raw float (cdt), ascii (cdt), legacy raw float (dat) and legacy ascii (dat)
    plotdata:       plotdata = 0, don't show plot
                    plotdata = 1, show plot (default)  
                    plotdata = x, with x > 1, shows and automatically closes plot after x seconds
    verbosity:      1 is low, 2 is medium (default) and 3 is high

# Outputs
    data            functional data (e.g. EEG, MEG)
    datainfo        data information: [samples, channels, trials/epochs, sampling frequency]
    labels          channel labels
    events          events matrix where every row is: [event latency, event type, event start, event stop]
    annontations    corresponding annotations to each event
    sensorpos       channel locations (x,y,z)
    impedancematrix impedance matrix with max size = (channels, 10), corresponding to last ten impedance measurements
    hpimatrix       HPI-coil measurements matrix (Orion-MEG only) where every row is: [measurementsample, dipolefitflag, x, y, z, deviation]
    
# Usage
    import curryreader as cr
    
    # Use file selection box, get all outputs separately :
    (data, datainfo, labels, events, annotations, sensorpos, impedancematrix, hpimatrix) = cr.read()
  
    # Specify file path, avoid plot, set minimum verbosity, get all outputs in tuple "data":
    data = cr.read("test.cdt", 0, 1)
  
    # Get only first x outputs:
    data, datainfo, labels, *_ = cr.read("test.cdt")

# Licensing
BSD (3-clause)
