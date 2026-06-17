import os
import sys
from pathlib import Path

def main():
    # print( Path.cwd() )
    path_files = sys.argv[1]
    # names_files = os.listdir(path_files)
    
    p = Path(path_files)
    for file in p.glob('*mkv'):
        print(file)


    # print(os.listdir(path_files))
    


    # print(sys.argv[1])
 

if __name__ == "__main__":
    main()
