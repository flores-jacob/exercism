def to_rna(dna_strand):
    rna_strand = ''

    for nucleotide in dna_strand:
        if nucleotide == 'C':
            rna_strand += 'G'
        elif nucleotide == 'G':
            rna_strand += 'C'
        elif nucleotide == 'T':
            rna_strand += 'A'
        elif nucleotide == 'A':
            rna_strand += 'U'
        else:
            raise ValueError(nucleotide + ' is an invalid input')

    return rna_strand