import curryreader as cr
import numpy as np

############ 
def create_reference_output(test_file, ref_output_case):
    
    data = cr.read(test_folder + test_file, 0)

    f = open(test_ref_folder + 'ref_params_' + ref_output_case + '.txt', 'w')

    np.save(test_ref_folder + 'ref_data_' + ref_output_case, data[0])

    for t in data[1:]:
        line = ' '.join(str(x) for x in t)
        f.write(line + '\n')
    
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