import curryreader as cr
import numpy as np

############
def compose_output(data):
    
    output = ''
    for key, item in data.items():
        output += (key + ': ')
        line = ' '.join(str(item[x]) for x in item) if isinstance(item, dict) else ' '.join(str(x) for x in item)
        output += (line + '\n')

    return output

def create_reference_output(test_file, ref_output_case):
    
    currydata = cr.read(test_folder + test_file, 0)

    f = open(test_ref_folder + 'ref_params_' + ref_output_case + '.txt', 'w')

    np.save(test_ref_folder + 'ref_data_' + ref_output_case, currydata['data'])
    
    currydata.pop('data')
    output = compose_output(currydata)
    
    f.write(output)
    f.close()
#############

test_folder             = "test_data\\"
test_ref_folder         = test_folder + "tests_ref_output\\" 
raw_float_cdt           = "Float.cdt"
legacy_raw_float_dat    = "Legacy.dat"
hpi_cdt                 = "HPI.cdt"

create_reference_output(raw_float_cdt, 'continuos')

create_reference_output(legacy_raw_float_dat, 'epochs')

create_reference_output(hpi_cdt, 'hpi')