'''
Download DNA and protein file from NCBI
NM_207618.2 from Nucleotide of NCBI, download FASTA file save as dna.txt
'''

#Import DNA to Python
inputfile = ("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_3/dna.txt")
f = open(inputfile, "r")
seq = f.read()

# be careful, there are \N in the text, which cause problem to translation
print(seq)

# remove \N
seq = seq.replace("\n", "")

print(seq)
#remove other character hidding in the string
seq = seq.replace("\r", "")

'''
Learn how to translate the DNA sequence using a dictionary lookup
Learn how to check the length of the sequence using the modulo operator
'''
#DNA and corresponding amino acid
def translate(seq):
    '''Translate a string containing a nucleotide sequence into a string
    containing the corresponding sequence of amino acids. Nucleotides are
    translated in triplets using the table dictionary; each amino acid
    is encoded with a string of length 1.'''
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    print(table['GCC'])

    protein = ""
    # step 1: check that length of sequence is divisible by 3
    if len(seq) % 3 == 0:
        # loop over the sequence
        for i in range(0, len(seq), 3):
            # extract a single codon
            codon = seq[i : i+3]
            # look up the codon and store result
            protein += table[codon]

    return protein

print(translate("ATA"))
#help(translate) # check the documentation (docstring) of the new funtion "translate"

print(seq[0:3]) # slide the string
print(seq[3:6])
print(seq[6:9])
list(range(0, 11, 3)) # loop over string with a step of 3
print(138%13)
print(seq[40:50])


'''
Learn how to use the with statement to read in an entire file
Learn how to compare your translation to the protein sequence you downloaded
'''

def read_seq(inputfile):
    """Reads and returns the input sequence with special characters removed."""
    with open (inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq

prt = read_seq("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_3/protein.txt")
dna = read_seq("/Users/tp10/Sanger_work/Developer101/python_for_research_edXcourse/Week_3/dna.txt")

print(translate(dna)) # empty because length of seq is not divisible by 3

print(translate(dna[20:938])) # will include _ which is a stop codon
print(prt)

print(translate(dna[20:935]))

print (prt == translate(dna[20:935]))

# exclude the last character of the translated seq
print (prt == translate(dna[20:938])[:-1]) # exclude the last char  

