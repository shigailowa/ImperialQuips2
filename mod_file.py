def mod_file(input_file, output_file):

    input = open(input_file,'r')
    output = open(output_file, 'w')

    for i, line in enumerate(input):
        if not line.startswith('#'):
            output.write(line)

    input.close()
    output.close()


if __name__ == '__main__':
    
    mod_file('ru_syntagrus-ud-test.conllu','russ_test_new.conll')