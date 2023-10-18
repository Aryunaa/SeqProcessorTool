def is_dna_or_rna(*args, alphabet_dna={'A', 'T', 'G', 'C', 'a', 't', 'g', 'c'},
                  alphabet_rna={'A', 'U', 'G', 'C', 'a', 'u', 'g', 'c'}) -> list:
    """
    works

    :param args:

    :return:
    """
    seqs = list(*args)
    is_dna_or_rna_list = []
    for seq in seqs:
        unique_chars = set(seq)
        if unique_chars <= alphabet_dna:
            is_dna_or_rna_list.append('dna')  # 1 means dna
        elif unique_chars <= alphabet_rna:
            is_dna_or_rna_list.append('rna')  # 2 means rna
        else:
            is_dna_or_rna_list.append(False)
    return is_dna_or_rna_list


def transcribe(*args, is_dna_or_rna_list) -> list:
    """
    works

    :param args:
    :return:
    """
    seqs = list(*args)
    res_seq = []

    for i in range(len(seqs)):
        if is_dna_or_rna_list[i] is True:
            seq = seqs[i]
            if 'T' in seq:
                temp_seq = seq.replace('T', 'U')
            elif 't' in seq:
                temp_seq = seq.replace('t', 'u')
        else:
            temp_seq = 'Please provide DNA or RNA'
        res_seq.append(temp_seq)
    if len(res_seq) == 1:
        return res_seq[0]
    else:
        return res_seq


def reverse(*args, is_dna_or_rna_list) -> list:
    """"

    works
    :param seqs:
    :return:
    """
    seqs = list(*args)
    rev_seq = []
    for i in range(len(seqs)):
        if is_dna_or_rna_list[i] is True:
            seq = seqs[i]
            rev_seq.append(seq[::-1])
        else:
            rev_seq.append('Please provide DNA or RNA')
    if len(rev_seq) == 1:
        return rev_seq[0]
    else:
        return [rev_seq]


def complement(*args, is_dna_or_rna_list,
               dna_complement_nucl={"A": "T", "G": "C", "C": "G", "T": "A", "a": "t", "g": "c", "c": "g", "t": "a"},
               rna_complement_nucl={"A": "U", "G": "C", "C": "G", "U": "A", "a": "u", "g": "c", "c": "g","u": "a"}) -> list:
    seqs = list(*args)
    comp_seqs = []
    for i in range(len(seqs)):
        if is_dna_or_rna_list[i] == 'dna':  # if seq is dna
            seq = seqs[i]
            comp_seq = ''
            print(seq)
            for nucl in seq:
                comp_seq += dna_complement_nucl[nucl]

        elif is_dna_or_rna_list[i] == 'rna':  # if seq is rna
            print('rna')
            seq = seqs[i]
            comp_seq = ''
            for nucl in seq:
                comp_seq += rna_complement_nucl[nucl]

        else:
            comp_seq = 'Please provide DNA or RNA'

        comp_seqs.append(comp_seq)

    return comp_seqs


def reverse_complement(*args, is_dna_or_rna_list) -> list:
    seqs = list(args)
    comp_seqs = complement(*seqs, is_dna_or_rna_list=is_dna_or_rna_list)
    rev_comp_seqs = reverse(*comp_seqs, is_dna_or_rna_list=is_dna_or_rna_list)

    return rev_comp_seqs


def run_dna_rna_tools(*args, tool='transcribe') -> list:
    """
    Works with dna or rna sequences, has 4 options to work:
        - get transcribed sequence (`transcribe` operation);
        - get reversed sequence (`reverse` operation);
        - get complementary sequence (`complement` operation);
        - get reversed complementary sequence (`reverse_complement` operation);

    Args:
        *args (str): various number of nucleotide sequences
        tool (str): one desired option to work.

    Returns tuple containing two list:
        result (list): list with operation results for each valid sequence;
    """
    seqs = list(args)
    is_dna_or_rna_list = is_dna_or_rna(seqs)
    if any(is_dna_or_rna_list):

        if tool == 'transcribe':
            answer = transcribe(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        elif tool == 'reverse':
            answer = reverse(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        elif tool == 'complement':
            answer = complement(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        elif tool == 'reverse_complement':
            answer = reverse_complement(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        else:
            answer = 'Please enter the proper option'
        return answer

    else:
        return ['Neither DNA nor RNA was found,please provide DNA or RNA']
