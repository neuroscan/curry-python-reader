import os
import curryreader as cr
import numpy as np

test_folder             = "test_data"
test_ref_folder         = os.path.join(test_folder, "tests_ref_output") 
raw_float_cdt           = "Float.cdt"
legacy_raw_float_dat    = "Legacy.dat"
hpi_cdt                 = "HPI.cdt"
meg_eeg_cdt             = "MEG2085.cdt"

############
def compose_output(data):
    
    output = ''
    for key, item in data.items():
        output += (key + ': ')
        line = ' '.join(str(item[x]) for x in item) if isinstance(item, dict) else ' '.join(str(x) for x in item)
        output += (line + '\n')

    return output

def create_reference_output(test_file, ref_output_case):
    
    currydata = cr.read(os.path.join(test_folder, test_file), 0)

    f = open(os.path.join(test_ref_folder, 'ref_params_' + ref_output_case + '.txt'), 'w')

    np.save(os.path.join(test_ref_folder, 'ref_data_' + ref_output_case), currydata['data'])
    
    currydata.pop('data')
    output = compose_output(currydata)
    
    f.write(output)
    f.close()
#############

def create_all():

    create_reference_output(raw_float_cdt, 'continuos')

    create_reference_output(legacy_raw_float_dat, 'epochs')

    create_reference_output(hpi_cdt, 'hpi')

    create_reference_output(meg_eeg_cdt, 'meg_eeg')

#############
#create_all(); # Uncomment to create/update reference outputs