import modules.dna_rna_tools as drt
import modules.protein_analyzer_tool as prt
import modules.fastq_tools as ft


# from modules.dna_rna_tools import run_dna_rna_tools as dna_rna
# from modules.protein_analyzer_tool import run_protein_analyzer_tool as prot
# from modules.fastq_tools import run_fastq_tools as fastq


def run_dna_rna_tools(*args, tool='transcribe'):
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
    is_dna_or_rna_list = drt.is_dna_or_rna(seqs)
    if any(is_dna_or_rna_list):

        if tool == 'transcribe':
            answer = drt.transcribe(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        elif tool == 'reverse':
            answer = drt.reverse(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        elif tool == 'complement':
            answer = drt.complement(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        elif tool == 'reverse_complement':
            answer = drt.reverse_complement(seqs, is_dna_or_rna_list=is_dna_or_rna_list)
        else:
            answer = 'Please enter the proper option'
        return answer

    else:
        return 'Neither DNA nor RNA was found,please provide DNA or RNA'


# prot()


# fastq()
