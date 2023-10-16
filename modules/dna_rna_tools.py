
def is_dna_or_rna(*seqs,alphabet_dna={'A', 'T', 'G', 'C','a','t','g','c'}, alphabet_rna = {'A', 'U', 'G', 'C','a','u','g','c'}):
    seqs = list(*seqs)
    is_dna_or_rna_list = []
    for seq in seqs:
        unique_chars = set(seq)
        if(unique_chars<=alphabet_dna):
            is_dna_or_rna_list.append(1) # 1 means dna
        elif(unique_chars<=alphabet_rna):
            is_dna_or_rna_list.append(2) # 2 means rna
        else:
            is_dna_or_rna_list.append(0)
    return (is_dna_or_rna_list)

def transcribe(*seqs,is_dna_or_rna_list):
    '''
    works

    :param seqs:
    :return:
    '''
    seqs = list(*seqs)
    res_seq = []
    for i in range(len(seqs)):
        if(is_dna_or_rna_list[i]==True):
            seq = seqs[i]
            if ('T' in seq):
                temp_seq= seq.replace('T', 'U')
            elif ('t' in seq):
                temp_seq = seq.replace('t','u')
        else:
            temp_seq='Please provide DNA or RNA'
        res_seq.append(temp_seq)
    if len(res_seq) == 1:
        return res_seq[0]
    else:
        return res_seq

def reverse(*seqs,is_dna_or_rna_list):
    '''

    works
    :param seqs:
    :return:
    '''
    seqs = list(*seqs)
    rev_seq = []
    for i in range(len(seqs)):
        if (is_dna_or_rna_list[i] == True):
            seq = seqs[i]
            rev_seq.append(seq[::-1])
        else:
            rev_seq.append('Please provide DNA or RNA')
    if len(rev_seq) == 1:
        return rev_seq[0]
    else:
        return rev_seq

def complement(*seqs,is_dna_or_rna_list):
    seqs = list(*seqs)
    comp_seqs = []
    for i in range(len(seqs)):
        if (is_dna_or_rna_list[i] == 1): # if seq is dna
            seq = seqs[i]
            comp_seq = ''
            print(seq)
            for j in seq:
                if(j == 'A'):
                    comp_seq += 'T'
                elif(j == 'T'):
                    comp_seq += 'A'
                elif(j == 'G'):
                    comp_seq += 'C'
                elif(j == 'C'):
                    comp_seq += 'G'

                if(j == 'a'):
                    comp_seq += 't'
                elif(j == 't'):
                    comp_seq += 'a'
                elif(j == 'g'):
                    comp_seq += 'c'
                elif(j == 'c'):
                    comp_seq += 'g'

        elif (is_dna_or_rna_list[i] == 2): # if seq is rna
            print('rna')
            seq = seqs[i]
            comp_seq = ''
            for j in seq:
                if (j == 'A'):
                    comp_seq += 'U'
                elif (j == 'U'):
                    comp_seq += 'A'
                elif (j == 'G'):
                    comp_seq += 'C'
                elif (j == 'C'):
                    comp_seq += 'G'

                if (j == 'a'):
                    comp_seq += 'u'
                elif (j == 'u'):
                    comp_seq += 'a'
                elif (j == 'g'):
                    comp_seq += 'c'
                elif (j == 'c'):
                    comp_seq += 'g'

        else:
            comp_seq='Please provide DNA or RNA'

        comp_seqs.append(comp_seq)
    if len(comp_seqs) == 1:
        return comp_seqs[0]
    else:
        return comp_seqs

def reverse_complement(*seqs,is_dna_or_rna_list):
    #################################################
    seqs = list(*seqs)
    comp_seqs = []
    for i in range(len(seqs)):
        if (is_dna_or_rna_list[i] == 1):  # if seq is dna
            seq = seqs[i]
            comp_seq = ''
            print(seq)
            for j in seq:
                if (j == 'A'):
                    comp_seq += 'T'
                elif (j == 'T'):
                    comp_seq += 'A'
                elif (j == 'G'):
                    comp_seq += 'C'
                elif (j == 'C'):
                    comp_seq += 'G'

                if (j == 'a'):
                    comp_seq += 't'
                elif (j == 't'):
                    comp_seq += 'a'
                elif (j == 'g'):
                    comp_seq += 'c'
                elif (j == 'c'):
                    comp_seq += 'g'

        elif (is_dna_or_rna_list[i] == 2):  # if seq is rna
            print('rna')
            seq = seqs[i]
            comp_seq = ''
            for j in seq:
                if (j == 'A'):
                    comp_seq += 'U'
                elif (j == 'U'):
                    comp_seq += 'A'
                elif (j == 'G'):
                    comp_seq += 'C'
                elif (j == 'C'):
                    comp_seq += 'G'

                if (j == 'a'):
                    comp_seq += 'u'
                elif (j == 'u'):
                    comp_seq += 'a'
                elif (j == 'g'):
                    comp_seq += 'c'
                elif (j == 'c'):
                    comp_seq += 'g'

        else:
            comp_seq = 'Please provide DNA or RNA'

        comp_seqs.append(comp_seq)
    #######################################S

    rev_comp_seqs = []
    for i in range(len(comp_seqs)):
        if (is_dna_or_rna_list[i] == True):
            seq = comp_seqs[i]
            rev_comp_seqs.append(seq[::-1])
        else:
            rev_comp_seqs.append('Please provide DNA or RNA')

    if len(rev_comp_seqs) == 1:
        return rev_comp_seqs[0]
    else:
        return rev_comp_seqs








#my_test()
#коммит для автотеста