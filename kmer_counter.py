import matplotlib.pyplot as plt
import pandas as pd
import sys


def create_dataframe(genome):
    """
    Summary line: Creates a dataframe from k-mer data

    Extended description: This function accepts a genomic sequence and creates
         a dataframe. The dataframe consists of k-mer data extracted from the
         genome sequence

    Parameters:
    genome (string): A string of characters representing a genomic sequence

    Return:
    genome_df: a dataframe which consists of one row for every possible k-mer
        length from 1 to the length of the genome sequence. Each row will
        consist of one column of the count of observed k-mers, one column for
        the count of possible k-mers, and one column which holds a list of
        strings of the unique k-mers observed
    """
    genome_length = len(genome)
    kmer_dict = {}

    for k in range(1, genome_length + 1):
        mini_dict = count_kmers(genome, k, genome_length)
        kmer_dict[k] = mini_dict

    genome_df = pd.DataFrame.from_dict(kmer_dict, orient='index')
    return genome_df


def count_kmers(genome, k, genome_length):
    """
    Summary line: Count all possible and observed k-mers for a given k-mer length

    Extended description: This function will count all possible k-mers and all
    unique k-mers within a genome sequence for a k-mer length k. It will find
    and save all unique k-mers

    Parameters:
    genome (string): a genomic sequence
    k (int): length of the k-mer sequences being looked for
    genome_length (int): length of the genomic sequence

    Return:
    temp_dict: a dictionary which consists of the count of all possible k-mers,
        the count of all unique k-mers, and a list of strings of all unique
        k-mers

    """
    assert(genome_length > 0)
    unique_kmers = []
    count = 0
    temp_dict = {}

    for i in range(genome_length):
        if (i + k) > genome_length:
            break
        else:
            count += 1
            current_kmer = genome[i:i+k]
            if unique_kmers.count(current_kmer) == 0:
                unique_kmers.append(current_kmer)

    if count > 4**k:
        count = 4**k

    temp_dict['observed_kmers'] = unique_kmers
    temp_dict['observed_count'] = len(unique_kmers)
    temp_dict['possible_count'] = count
    return temp_dict


def create_graph(kmer_data):
    """
    Summary line: A function which takes a dataframe and creates a graph

    Extended description: This function will plot the differences between the
    observed k-mers and the unique k-mers within a given genomic sequence

    Parameters:
    kmer_data (dataframe): A dataframe consisting of all k-mer information for
        all lengths k from 1 to the length of the genomic sequence

    Return:
    No return value
    """
    kmer_graph = kmer_data[['possible_count', 'observed_count']]\
        .plot(kind='bar', title='Observed kmers vs Possible kmers', legend=True)
    kmer_graph.set_xlabel("K (kmer length)")
    kmer_graph.set_ylabel("Count")
    plt.show()


def linguistic_complexity(kmer_data):
    """
    Summary line: Determines the linguistic complexity of genomic sequence

    Extended description: This function determines the linguistic complexity of
        a genome sequence by determining the observed k-mers and the possible
        k-mers and then calculating the linguistic complexity using these values

    Parameters:
    kmer_data (dataframe): A dataframe consisting of all k-mer information for
        all lengths k from 1 to the length of the genomic sequence

    Return:
    complexity: A floating point value of the linguistic complexity of a language
    """
    observed_kmers = kmer_data['observed_count'].sum()
    possible_kmers = kmer_data['possible_count'].sum()
    complexity = observed_kmers / possible_kmers
    return complexity


def main():
    # check user input
    if len(sys.argv) > 2:
        print("Usage: kmer_counter.py [FILE] ")
        sys.exit()

    # read input data
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        genome = file.read().replace('\n', '')

    # output results
    kmer_data = create_dataframe(genome)
    create_graph(kmer_data)
    complexity = linguistic_complexity(kmer_data)
    print(complexity)


main()
