
import modules.dna_rna_tools as drt
import modules.protein_analyzer_tool as prt
import modules.fastq_tools as ft

#from modules.dna_rna_tools import run_dna_rna_tools as dna_rna
#from modules.protein_analyzer_tool import run_protein_analyzer_tool as prot
#from modules.fastq_tools import run_fastq_tools as fastq


def run_dna_rna_tools(*seqs,tool='transcribe'):
    """
    Works with dna or rna sequences, has 4 options to work:
        - get transcribed sequence (`transcribe` operation);
        - get reversed sequence (`reverse` operation);
        - get complementary sequence (`complement` operation);
        - get reversed complementary sequence (`reverse_complement` operation);

    Args:
        *seqs (str): various number of nucleotide sequences
        tool (str): one desired option to work.

    Returns tuple containing two list:
        result (list): list with operation results for each valid sequence;
    """

    is_dna_or_rna_list = drt.is_dna_or_rna(seqs)
    if(True in is_dna_or_rna_list):

        if (tool == 'transcribe'):
            answer = drt.transcribe(seqs,is_dna_or_rna_list = is_dna_or_rna_list)
        elif (tool == 'reverse'):
            answer = drt.reverse(seqs,is_dna_or_rna_list = is_dna_or_rna_list)
        elif (tool == 'complement'):
            answer = drt.complement(seqs,is_dna_or_rna_list = is_dna_or_rna_list)
        elif (tool == 'reverse_complement'):
            answer = drt.reverse_complement(seqs, is_dna_or_rna_list = is_dna_or_rna_list)
        print(answer)
    else:
        print('Neither DNA nor RNA was found,please provide DNA or RNA')

#prot()



#fastq()



def my_test():
    #run_dna_rna_tools('aTgcatgCaUgcatgc','atgc','aTgc',tool='transcribe')
    #run_dna_rna_tools('aTgcatgCaUgcatgc',tool='transcribe')
    #run_dna_rna_tools('aTgcatgCaUgcatgc','atgc','aTgc',tool='reverse')
    #run_dna_rna_tools('aTgcatgCaUgcatgc',tool='reverse')

    run_dna_rna_tools('aTgcatgCaUgcatgc','atgc','aTgc',tool='complement')
    run_dna_rna_tools('aTgcatgCaUgcatgc',tool='complement')
    run_dna_rna_tools('aTgcatgCaUgcatgc','atgc','aTgc',tool='reverse_complement')
    run_dna_rna_tools('aTgcatgCaUgcatgc',tool='reverse_complement')
