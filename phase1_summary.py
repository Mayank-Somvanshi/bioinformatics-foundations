# Define a custom function to open, read, and parse FASTA-formatted sequence files from disk
def read_fasta(filename):
    # Initialize an empty dictionary to map sequence headers (keys) to their assembled DNA sequences (values)
    sequences = {}
    # Create a string tracker variable to remember the most recently encountered FASTA header
    current_header = ""
    # Safely open the target file in read-only mode, guaranteeing automatic closure when finished
    with open(filename, "r") as file:
        # Step through the open file stream line-by-line using a for-in loop
        for line in file:
            # Strip trailing newline characters (\n) and whitespace from both ends of the line
            line = line.strip()
            # Inspect whether the line starts with '>' to identify a FASTA identifier/header line
            if line.startswith(">"):
                # Slice the string from index 1 to the end to remove the leading '>' character
                current_header = line[1:]
                # Create a new key in the dictionary with this header and set its initial value to an empty string
                sequences[current_header] = ""
            # Handle lines containing nucleotide sequence characters rather than header metadata
            else:
                # Concatenate the current sequence line onto the ongoing string stored under the active header
                sequences[current_header] += line
    # Return the completed dictionary containing all headers and their corresponding full sequence strings
    return sequences


# Define a validation function to verify that a strand contains strictly canonical DNA bases
def is_valid_dna(sequence):
    # Iterate through the sequence string character-by-character
    for base in sequence:
        # Check if the current nucleotide is absent from the valid canonical alphabet "ATCG"
        if base not in "ATCG":
            # Immediately terminate the function and return False if an illegal or ambiguous character is found
            return False
    # Return True only after all characters have passed inspection without triggering an early return
    return True


# Define a quantitative function to calculate the percentage of Guanine and Cytosine in a sequence
def calculate_gc(sequence):
    # Count the total number of Guanine ('G') bases present in the sequence
    g = sequence.count("G")
    # Count the total number of Cytosine ('C') bases present in the sequence
    c = sequence.count("C")
    # Add G and C counts, divide by total sequence length, and multiply by 100 to compute the GC percentage
    return (g + c) / len(sequence) * 100


# Define an optimization function to locate the single longest sequence in the parsed dataset
def find_longest(sequences):
    # Initialize an empty string variable to hold the header of the longest sequence discovered
    longest_header = ""
    # Initialize an empty string variable to track the sequence with the greatest character length
    longest_seq = ""
    # Unpack the dictionary into its corresponding header and sequence pairs simultaneously
    for header, sequence in sequences.items():
        # Compare the length of the current sequence against the length of the longest sequence recorded so far
        if len(sequence) > len(longest_seq):
            # Overwrite the longest sequence variable with the newly found larger sequence
            longest_seq = sequence
            # Update the longest header variable to match the identifier of this new longest sequence
            longest_header = header
    # Return both the header and the sequence string of the longest record as a two-item tuple
    return longest_header, longest_seq


# Define the master coordinator function that manages the end-to-end analysis workflow
def analyze_fasta(filename):
    # Call our file parser function to convert the FASTA text file into a populated Python dictionary
    sequences = read_fasta(filename)
    # Print the total count of distinct sequence entries found by checking the dictionary's length
    print(f"Total sequences found: {len(sequences)}")
    # Print a decorative terminal separator consisting of 40 equal signs
    print("=" * 40)

    # Loop through each individual header and sequence entry in the dictionary
    for header, sequence in sequences.items():
        # Standardize all letters to uppercase to prevent case-sensitivity mismatches during validation and counting
        sequence = sequence.upper()
        # Print the current sequence identifier to the terminal
        print(f"Header: {header}")

        # Pass the sequence to the validator function using a boolean NOT guard clause
        if not is_valid_dna(sequence):
            # Alert the console that non-canonical bases were detected
            print("Status: INVALID sequence")
            # Print a lightweight section divider
            print("___")
            # Immediately skip the rest of this loop iteration and move directly to the next sequence
            continue

        # Calculate the GC percentage using our dedicated calculation function
        gc = calculate_gc(sequence)
        # Print the total nucleotide base count using the len() function
        print(f"Length: {len(sequence)} bases")
        # Print the calculated GC content formatted cleanly to exactly two decimal places (.2f)
        print(f"GC Content: {gc:.2f}%")
        # Confirm that the sequence successfully passed quality checks
        print("Status: VALID")
        # Print a lightweight section divider
        print("___")

    # Unpack the two values returned by find_longest into two distinct variables
    longest_header, longest_seq = find_longest(sequences)
    # Output the header name of the longest sequence in the file
    print(f"Longest sequence: {longest_header}")
    # Output the total length in base pairs of that longest sequence
    print(f"Length: {len(longest_seq)} bases")


# Trigger the master analysis function with the absolute file path to your practice FASTA file
analyze_fasta("/home/mayank/python_practice/sample.fasta")
