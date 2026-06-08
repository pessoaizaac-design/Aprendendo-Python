import os
import shutil

old_path = r'C:\Users\pesso\OneDrive\Desktop\Alg'
new_path = r'C:\Users\pesso\OneDrive\Desktop\python4'

try:
    os.mkdir(new_path)
except FileExistsError as e:
    print(f'{new_path} já existe!')
    
for root, dirs, files in os.walk(old_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)
        
        if '.srt' in file:
            shutil.copy(old_file_path, new_file_path)
            print('Arquivo copiado com sucesso!')
        