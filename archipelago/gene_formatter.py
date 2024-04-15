def format_bits(data):
    formatted_data = ""
    for sublist in data:
        for i in range(0, len(sublist), 8):  # Process every 8 elements
            # Get next slice of 8 bits or fewer if not enough elements left
            chunk = sublist[i:i+8]
            line = ' '.join(str(bit) for bit in chunk[:4]) + "     " + ' '.join(str(bit) for bit in chunk[4:])
            formatted_data += line + "\n"
        formatted_data += "\n\n\n\n\n"  # Add 5 empty lines after each list
    return formatted_data

def process_file(input_filepath, output_filepath):
    with open(input_filepath, 'r') as file:
        data_string = file.read().strip()
    
    # Assume data is in the correct format as a list of lists
    data = eval(data_string)

    # Format the data
    formatted_data = format_bits(data)

    # Write to output file
    with open(output_filepath, 'w') as file:
        file.write(formatted_data)

# Example usage:
process_file('genes.txt', 'genes_with_formatting.txt')
