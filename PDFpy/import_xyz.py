class XYZFilter:
    @staticmethod
    def filter_xyz(input_filename: str, output_filename: str, elements: list) -> None:
        """
        Filters an .xyz file by removing lines that do not contain specific elements and saves the result to a temporary file.
        """
        # Read input file
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        
        # Header contains the number of atoms
        header = lines[:2]
        atom_lines = lines[2:]
        
        # Filter lines according to the desired elements
        filtered_lines = [line for line in atom_lines if line.split()[0] in elements]
        
        # Update the atom count in the header
        header[0] = str(len(filtered_lines)) + '\n'
        
        # Write the temporary file with only the desired elements
        with open(output_filename, 'w') as outfile:
            outfile.writelines(header + filtered_lines)
        print(f"The temporary file {output_filename} has been created with the desired elements {elements}.")
