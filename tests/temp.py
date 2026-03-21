from sys import argv
import os
import re

from google import genai
from google.genai import types

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyC0d3tOcjgARiuUvBtPVkkVz5O1NW18Yh4")

FERROR = 1
ARGERROR = 2

def generate_task_filename(task:str) -> str:
    prompt = (
        f"Translate this algorithmic task to English and return a short, "
        f"lowercase kebab-case filename (max 3 words). "
        f"Output ONLY the filename, no extension: {task}"
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    filename = response.text.strip().lower()
    filename = re.sub(r'[^a-z0-9\-]', '', filename)
    
    return filename



def generator():
    args = argv
    if len(args) <= 1:
        print("Too few arguments given, expected one 'filename' ")
        return ARGERROR

    fname = args[1]
    if not os.path.isfile(fname):
        print(f"File {fname}, doesnt exist")
        return FERROR

    with open(fname, 'r') as f:
        content = f.read()
        f.close()

    if len(content.strip("\n\t ")) == 0:
        print(f"File {fname} is empty")
        return FERROR

    blocks = content.split('\n\n')
    num_files = len(blocks)
    print(f"CREATING {num_files} taks files...")

    unfound_numbers = 0
    for i, block in enumerate(blocks):
        find_ob = re.search(r'[0-9]+\.', block)
        if not find_ob: 
            print(f"couldnt find the task num for task {i+1}")
            task_num_ind = f"?{unfound_numbers}."
            unfound_numbers += 1
        else:
            task_num_ind = find_ob.group()

        desc = generate_task_filename(block)
        nfname = f"{task_num_ind}{desc}.py"
        print(f"creating {nfname}")
        template = f'''"""
        {block}
        """

        def solution():
            # TODO: Implement algorithm logic here
            pass

        if __name__ == "__main__":
            solution()
        '''
        with open(f"{fname}", "w") as f:
            f.write(template)
            f.close()


    




if __name__ == "__main__":
    ret = generator()
