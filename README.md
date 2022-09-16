[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8392808&assignment_repo_type=AssignmentRepo)
# Basic exact pattern matching

This project is about exact pattern matching. You should implement the naive quadratic time algorithm and a linear time algorithm of your cheice, e.g. the border-array or the KMP-algorithm. The naive algorithm has the worst-case running time O(nm) and the other algorithms we have seen have worst-case running time O(n+m).

The algorithms should be implemented in two programs, `naive` and `lin`. Both programs should take two arguments (no more and no less): the first should be a Simple-FASTA file and the second a Simple-FASTQ file. The programs should output all matches in the Simple-SAM format to stdout (i.e., they should write to the terminal). Since we are only doing exact matching, the CIGAR strings in the output should consist of M’s only, since all the characters in the read will match the reference at the reported position.

For example, with this Simple-FASTA file

```
> chr1
mississippi
> chr2
mississippimississippi
```

and this Simple-FASTQ file

```
@read1
iss
@read2
mis
@read3
ssi
@read4
ssippi
```

your output should be

```
read1	chr1	2	3M	iss
read1	chr1	5	3M	iss
read1	chr2	2	3M	iss
read1	chr2	5	3M	iss
read1	chr2	13	3M	iss
read1	chr2	16	3M	iss
read2	chr1	1	3M	mis
read2	chr2	1	3M	mis
read2	chr2	12	3M	mis
read3	chr1	3	3M	ssi
read3	chr1	6	3M	ssi
read3	chr2	3	3M	ssi
read3	chr2	6	3M	ssi
read3	chr2	14	3M	ssi
read3	chr2	17	3M	ssi
read4	chr1	6	6M	ssippi
read4	chr2	6	6M	ssippi
read4	chr2	17	6M	ssippi
```

assuming you iterate over reads in an outer loop and FASTA records in an inner loop. If you order your loops differently, of course, the output will be different.

The project should be in groups of 2–3 students. It will not be graded.

## Part 1: parsers 

Write parsers for Simple-FASTA and Simple-FASTQ if you have not done so already.

ANSWER:
They are part of both the lin.py and naive.py scripts (read_fasta; read_fastq)

## Part 2: simulating data for evaluation

For testing the running time as functions of n and m, you should also write code for generating Simple-FASTA and Simple-FASTQ files (with appropriate properties for your tests).

ANSWER:
See src/runtime_comparison.py (and figure in the bottumn (red=naive;blue=lin))

## Part 2: mappers

Now write the tools for exact pattern matching. You can use the naive algorithm to test your linear time algorithm; the result of the two programs that you write should be identical after you sort the output.

```sh
> ./naive fasta.fa fastq.fq | sort > naive.sam
> ./lin fasta.fa fastq.fq | sort > lin.sam
> diff naive.sam lin.sam
```

You might not have to sort the output, if you run through reads

ANSWER:
See src/naive.py and src/lin.py

## Evaluation

Implement the two algorithms in two tools, `naive` and `lin`, that must be present at the root of the repository once they are built. The test setup checks that they give the correct output on selected data, but you should still carefully test them.

Once you have implemented the tools, fill out the report below. 

ANSWER:
See src/naive.py and src/lin.py

## Report

### Insights you may have had while implementing and comparing the algorithms. 

ANSWER:
Finally understood how border-arrays enables efficient string-searching.

### Problems encountered if any. 

ANSWER:
I had some trouble jumping backwards (or rather figuring out that i had to repetitively jump back until i reached match) in my border-array (finally fixed it with a while-loop).

### Experiments that verifies the correctness of your implementations.

ANSWER:
I simulate a bunch of random DNA sequences of varying lengths (representing ref seqs), and from these sequence sampled random intervals of length 1-20 representing read seqs. These samples were then used to test if my implentations returned the exact intervals/positions correctly (compared to the builtin find() method; see src/runtime_comparison.py).
Similarily, i sampled ref/reads as described above while feeding these samples to both algorithms simultaneously. The algorithms returned the same result for all iterations (500000; see src/runtime_comparison.py).
Furthermore both algorithms were tested for varius empty input cases (e.g. empty/empty and non-empty/empty). A coverage test was performed using coverage.py (https://coverage.readthedocs.io/en/6.4.4/). For this purpuse a fasta file containing 5 sequences and a corresponding simple fastq file containing 100 reads were generated. The naive and lin algorithms had respectivly 95% and 94% coverage where all missing lines (naive: 15, 17, 21, 23; lin: 16, 32, 42, 44, 48, 50) was involved in early returnings as response to empty/incompatable inputs. 


### Experiments validating the running time.

For this section, you should address the following:

* An experiment that verifies that your implementation of `naive` uses no more time than O(nm) to find all occurrences of a given pattern in a text. Remember to explain your choice of test data. What are “best” and “worst” case inputs? 

* An experiment that verifies that your implementations of `lin` use no more time than O(n+m) to find all occurrences of a given pattern in a text. Remember to explain your choice of test data. What are “best” and “worst” case inputs?

![](figs/runtimes.png)


