import sys
import screed


input_file = sys.argv[1]
new_text = sys.argv[2]



with screed.open(input_file) as seqfile:
    for read in seqfile:
        asci_symbols = read.sequence.maketrans("ATCG", new_text)
        new_read = read.sequence.translate(asci_symbols)
        print (f"@{read.name}\n{new_read}\n+\n{read.quality}")

