import subprocess

class FortranExecutor:
    @staticmethod
    def run_pdf(name: str, path: str, nhis: int, dr: float) -> None:
        """
        Modifies a Fortran file, compiles and runs the modified file.
        """
        new_filename = path + '\\' + name
        with open('..\\..\\PDF\\rdf.f90', 'r') as f:
            lines = f.readlines()
        with open('temp_rdf.f90', 'w') as f:
            for line in lines:
                if "file='shell.xyz'" in line:
                    line = line.replace("file='shell.xyz'", f"file='{new_filename}'")
                if "nhis=2600" in line:
                    line = line.replace("nhis=2600", f"nhis={nhis}")
                if "file='rdf.txt'" in line:
                    line = line.replace("file='rdf.txt'", f"file='{name[:-4] + '.txt'}'")
                if "delr = 0.02" in line:
                    line = line.replace("delr = 0.02", f"delr = {dr}")
                f.write(line)
        result = subprocess.run(['gfortran', 'temp_rdf.f90', '-o', 'rdf'], capture_output=True)
        print(result.stdout.decode())
        result2 = subprocess.run(['./rdf.exe'], capture_output=True)
        print(result2.stdout.decode())
    
    @staticmethod
    def run_pdf_noMD(name: str, path: str, nhis: int, dr: float, smooth1: float, smooth2: float) -> None:
        """
        Modifies a Fortran file, compiles and runs the modified file with specific parameters for smoothing.
        """
        new_filename = path + '\\' + name
        with open('..\\..\\PDF\\rdf_noMD.f90', 'r') as f:
            lines = f.readlines()
        with open('temp_rdf.f90', 'w') as f:
            for line in lines:
                if "file='shell.xyz'" in line:
                    line = line.replace("file='shell.xyz'", f"file='{new_filename}'")
                if "nhis=2600" in line:
                    line = line.replace("nhis=2600", f"nhis={nhis}")
                if 'call smooth(hs1,5,hs2)' in line:
                    line = line.replace('call smooth(hs1,5,hs2)', f'call smooth(hs1,{smooth1},hs2)')
                if 'call smooth(hs2,5,hs1)' in line:
                    line = line.replace('call smooth(hs2,5,hs1)', f'call smooth(hs2,{smooth2},hs1)')
                if "file='rdf.txt'" in line:
                    line = line.replace("file='rdf.txt'", f"file='{name[:-4] + '.txt'}'")
                if "delr = 0.02" in line:
                    line = line.replace("delr = 0.02", f"delr = {dr}")
                f.write(line)
        result = subprocess.run(['gfortran', 'temp_rdf.f90', '-o', 'rdf'], capture_output=True)
        print(result.stdout.decode())
        result2 = subprocess.run(['./rdf.exe'], capture_output=True)
        print(result2.stdout.decode())
    
    @staticmethod
    def process_all_files_in_folder(folder: str) -> None:
        """
        Processes all files in a specified folder using the `run_pdf` function.
        """
        file_list = FileManager.list_files(folder)
        for file in file_list:
            print(file)
            FortranExecutor.run_pdf(file, folder)
            print('\n')
