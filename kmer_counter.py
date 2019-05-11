import sys
import pandas as pd


def create_dataframe(genome):
    genome_length = len(genome)
    count = 0
    kmer_dict = {}
    k = 1

    for k in range(1, genome_length + 1):
        print(k)
        mini_dict = count_kmers(genome, k, genome_length)
        kmer_dict[k] = mini_dict

    genome_df = pd.DataFrame.from_dict(kmer_dict, orient='index')
    print(genome_df)


def count_kmers(genome, k, genome_length):
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
    print(temp_dict)
    return temp_dict


def create_graph():
    print("Create graph")

def liguistic_proficiency():
    print("Create graph")

# possible kmers
# unique kmers
#

def main():
    # check user input
    if len(sys.argv) > 2:
        print("Usage: kmer_counter.py [FILE] ")
        sys.exit()

    # read input data
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        genome = file.read().replace('\n', '')

    # print(genome)

    # output results
    create_dataframe(genome)

main()
