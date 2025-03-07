import os
import curryreader as cr
import numpy as np
import pytest
from numpy.testing import assert_allclose
from create_ref_results import compose_output

plot = 0
tol = 1e-4

test_folder             = "test_data"
test_ref_folder         = os.path.join(test_folder, "tests_ref_output") 
raw_float_cdt           = os.path.join(test_folder, "Float.cdt")
ascii_cdt               = os.path.join(test_folder, "ASCII.cdt")
legacy_raw_float_dat    = os.path.join(test_folder, "Legacy.dat")
ascii_dat               = os.path.join(test_folder, "Legacy ASCII.dat")
hpi_cdt                 = os.path.join(test_folder, "HPI.cdt")
meg_eeg_cdt             = os.path.join(test_folder, "MEG2085.cdt")
missing_params_cdt      = os.path.join(test_folder, "Missing Parameters.cdt")
missing_data_cdt        = os.path.join(test_folder, "Missing Data.cdt")
compressed_cdt          = os.path.join(test_folder, "Compressed.cdt")

# reference outputs
ref_data_continuos      =  os.path.join(test_ref_folder, "ref_data_continuos.npy")
ref_params_continuos    =  os.path.join(test_ref_folder, "ref_params_continuos.txt")
ref_data_epochs         =  os.path.join(test_ref_folder, "ref_data_epochs.npy")
ref_params_epochs       =  os.path.join(test_ref_folder, "ref_params_epochs.txt")
ref_data_hpi            =  os.path.join(test_ref_folder, "ref_data_hpi.npy")
ref_params_hpi          =  os.path.join(test_ref_folder, "ref_params_hpi.txt")
ref_data_meg_eeg        =  os.path.join(test_ref_folder, "ref_data_meg_eeg.npy")
ref_params_meg_eeg      =  os.path.join(test_ref_folder, "ref_params_meg_eeg.txt")

# Tests raw-float-cdt format with continuos data, alternative parameter file (dpo), 
# data-info, labels, events, annotations, sensor locations and impedance check
def test_raw_float_cdt():
    
    currydata = cr.read(raw_float_cdt, plot)
    ref_data = np.load(ref_data_continuos)
    assert_allclose(currydata['data'], ref_data)
    
    currydata.pop('data')
    params_output = compose_output(currydata)
    ref_params = open(ref_params_continuos).read()
    assert(params_output == ref_params)
    

# Tests ascii-cdt format with continuos data
def test_ascii_cdt():
    
    currydata = cr.read(ascii_cdt, plot)   
    ref_data = np.load(ref_data_continuos)
    assert_allclose(currydata['data'], ref_data, rtol = tol)

# Tests raw-float-dat format with epochs, data-info, labels, sensor locations
def test_legacy_raw_float_dat():
    
    currydata = cr.read(legacy_raw_float_dat, plot)
    ref_data = np.load(ref_data_epochs)
    assert_allclose(currydata['data'], ref_data)
    
    currydata.pop('data')
    params_output = compose_output(currydata)
    ref_params = open(ref_params_epochs).read()  
    assert(params_output == ref_params)
    

# Tests ascii-dat-format with epochs, data-info, labels, sensor locations 
def test_ascii_dat():
    
    currydata = cr.read(ascii_dat, plot)
    ref_data = np.load(ref_data_epochs)
    assert_allclose(currydata['data'], ref_data)
    
    currydata.pop('data')
    params_output = compose_output(currydata)
    ref_params = open(ref_params_epochs).read()
    assert(params_output == ref_params)
    

# Tests raw-float-cdt format with continuos data, data-info, labels, 
# events, annotations, sensor locations, landmarks and HPI matrix
def test_hpi():
    
    currydata = cr.read(hpi_cdt, plot)   
    ref_data = np.load(ref_data_hpi)
    assert_allclose(currydata['data'], ref_data)
    
    currydata.pop('data')
    params_output = compose_output(currydata)
    ref_params = open(ref_params_hpi).read()  
    assert(params_output == ref_params)
    
# Tests raw-float-cdt format with continuos data, multiple groups, 
# data-info, labels, sensor locations, landmarks and headshape points
def test_meg_eeg():
    
    currydata = cr.read(meg_eeg_cdt, plot)   
    ref_data = np.load(ref_data_meg_eeg)
    assert_allclose(currydata['data'], ref_data)
    
    currydata.pop('data')
    params_output = compose_output(currydata)
    ref_params = open(ref_params_meg_eeg).read()  
    assert(params_output == ref_params)
    
# Test compressed format
def test_compressed():

    with pytest.raises(Exception, match="Unsupported compressed data format, use Curry to convert file to raw float format"):
        cr.read(compressed_cdt)

# Test file extension
def test_file_extension():

    with pytest.raises(Exception, match='Unsupported file, choose a cdt or dat file'):
        cr.read("file")

    with pytest.raises(Exception, match='Unsupported extension, choose a cdt or dat file'):
        cr.read("file.xy")

# Test missing parameters
def test_missing_params():

    with pytest.raises(FileNotFoundError, match="Parameter file not found"):
        cr.read(missing_params_cdt)

# Test missing data
def test_missing_data():

    with pytest.raises(FileNotFoundError, match="Data file not found"):
        cr.read(missing_data_cdt)
