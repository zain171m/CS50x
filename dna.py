import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(0)

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as tablefile:
        data = csv.DictReader(tablefile)
        subsequences = list(data)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as samplefile:
        sampledata = samplefile.read()

    # TODO: Find longest match of each STR in DNA sequence
    subsequence = list(subsequences[0].keys())
    subsequence.pop(0)
    checklist = []
    for name in subsequence:
        longest_run = longest_match(sampledata, name)
        checklist.append(longest_run)

    # TODO: Check database for matching profiles
    for j in range(len(subsequences)):
        sliced_dict = {key: subsequences[j][key] for key in subsequence}
        for index, (key, value) in enumerate(sliced_dict.items()):
            if sliced_dict[key] == str(checklist[index]):
                continue
            else:
                index = index - 1
                break  
   
        counter = index + 1
        if counter == len(sliced_dict):
            print(subsequences[j]["name"])
            sys.exit(0)
        else:
            continue
    print("No match")
    sys.exit(0)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
