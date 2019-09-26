def to_rna(dna_strand):
    conv = {'G':'C','C':'G','T':'A','A':'U'}

    valid = dna_strand.count('G') + dna_strand.count('C') + dna_strand.count('T') + dna_strand.count('A')

    if valid != len(dna_strand):
        raise Exception("The imput you provided is not a valid DNA nucleotide. Please use only G,C,T or A.")
    else:
        rna_strand = ''.join([conv[x] for x in dna_strand])

    return rna_strand
