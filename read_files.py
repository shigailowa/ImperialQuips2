def read_rg_file():

    input = open('RG_word.txt','r')

    rg_words = {}

    for i, line in enumerate(input):
    	entries = line.split()
    	if float(entries[2]) >= 2:
            rg_words[entries[0]] = entries[1]

    input.close()
    return(rg_words)

def read_wordsim_file():

	input = open('WordSim_sense.txt','r')

	ws_words = {}

	for i, line in enumerate(input):
		entries = line.split()
		if float(entries[2]) >= 6:
			ws_words[entries[0].split("#")[0]] = entries[1].split("#")[0]

	input.close()
	return(ws_words)

def read_scws_file():

	input = open('ratings.txt','r')

	sc_words = {}
	sc_words['n'] = {}
	sc_words['v'] = {}
	sc_words['a'] = {}

	for i,line in enumerate(input):
		entries = line.split('\t')
		if float(entries[7]) >= 5 and entries[2] == entries[4] and entries[1]!=entries[3]:
			sc_words[entries[2]][entries[1]] = entries[3]

	input.close()
	return(sc_words)


def read_rw_file():

	input = open('rw.txt','r')

	rw_words={}

	for i,line in enumerate(input):
		entries = line.split()
		if float(entries[2]) >= 6:
			rw_words[entries[0]] = entries[1]

	input.close()
	return(rw_words)


def read_simlex_file():
	
	input = open('SimLex-999.txt','r')

	sl_words = {}
	sl_words['n'] = {}
	sl_words['v'] = {}
	sl_words['a'] = {}

	itersim = iter(input)
	next(itersim)
 
	for line in itersim:
		entries = line.split()
		if float(entries[3]) >= 5:
			sl_words[entries[2].lower()][entries[0]] = entries[1] 

	input.close()
	return(sl_words)


def read_simlex_rus_file():

	input = open('MSimLex999_Russian.txt')

	itersim = iter(input)
	next(itersim)

	sim_words = {} 

	for line in itersim:
		entries = line.split(',')
		if float(entries[15]) >= 5:
			sim_words[entries[0]] = entries[1]

	input.close()
	return(sim_words)

def read_wordsim_rus_file():

	input = open('WS353-russian-sim.txt')

	itersim = iter(input)
	next(itersim)

	sim_words = {} 

	for line in itersim:
		entries = line.split(',')
		if float(entries[2]) >= 5:
			sim_words[entries[0]] = entries[1]

	input.close()
	return(sim_words)


if __name__ == '__main__':
    
    print((read_simlex_rus_file()))

