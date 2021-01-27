import curryreader as cr

# 1) Use file selection box, get all outputs separately :
#(data, datainfo, labels, events, annotations, sensorpos, impedancematrix, hpimatrix) = cr.read()

# 2) Specify file path, avoid plot, set minimum verbosity, get all outputs in tuple "data":
#data = cr.read("test_data\\Float.cdt", 0, 1)

# 3) Get only first x outputs:
data, datainfo, labels, *_ = cr.read("test_data\\Float.cdt")
print("Info (samples, channels, trials/epochs, sampling frequency):\n", datainfo) 
