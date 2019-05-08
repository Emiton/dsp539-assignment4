def create_dataframe(genome):
    genome_length = len(genome)
    count = 0
    kmer_dict = {}
    k = 1

    for k in range(1, genome_length + 1):
        # change mini_dict logic to extract kmers
        mini_dict = count_kmers(genome, k, genome_length)
        print(k)


def count_kmers(genome, k, genome_length):
    unique_kmers = []
    count = 0

    for i in range(genome_length):
        if (i + k) > genome_length:
            break
        else:
            count += 1
            current_kmer = genome[i:k]
            if unique_kmers.count(current_kmer) == 0:
                unique_kmers.append(current_kmer)

    return unique_kmers, count





def create_graph():
    print("Create graph")

def liguistic_proficiency():
    print("Create graph")

# possible kmers
# unique kmers
#

def main():
    print("Hello, world!")
    # read in data
    # output results
    create_dataframe("ATTTGGATT")

main()
