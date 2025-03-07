import curryreader as cr

# 1) Use file selection box, show plot (default), verbosity (default), output in dictionary "currydata"
currydata = cr.read()

# 2) Specify file path, avoid plot, minimum verbosity, output in dictionary "currydata"
# currydata = cr.read("test_data\\Float.cdt", plotdata = 0, verbosity = 1)

# 3) Specify file path, show plot (default), verbosity (default), output in dictionary "currydata", print items
# currydata = cr.read("test_data\\HPI.cdt")

for key, value in currydata.items(): print(key + ":\n", value)
