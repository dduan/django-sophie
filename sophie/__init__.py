VERSION = (0, 0, 1, 'alpha', 0)

# meaning =  (major, minor, micro, stage, release)

def get_version():
    ''' 
    Version Schema agrees to PEP 386. 

    'stage' and 'release' are only reserved for special occasions. 
    At least the former will remain being 'alpha' before version 1.0.
    '''
    
    v = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        v = '%s.%s' % (v, VERSION[2])
    if VERSION[3] != 'final' and VERSION[4] != 0:
            v = '%s%s%s' % (v, VERSION[3][0], VERSION[4])
    return v

