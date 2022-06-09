# Prerequisite

pip install screed



# Run
```console
python swap.py [input_fq] [new_bases_for_ATCG]  > [output_fq]
```

As to  \[new_bases_for_ATCG\], you need to write down the new base for A, then for T, then for C and finally for G. For example, your A should be T and T be A, C should be G and G be C. Then your \[new_bases_for_ATCG\] should be TAGC. Let's say if you have a file input.fq in /app/, and you want your result in /app/output.fq, you should run:


```console
python swap.py /app/input.fq TAGC  > /app/output.fq
```
