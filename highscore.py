import shelve
d = shelve.open('gameparameters.csv')
d['gameparameters'] = 'lol'
d.close()

# comment
