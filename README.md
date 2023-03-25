# PyGen-GPT
Generate scripts with gpt. Based on [https://gitlab.com/nanuchi/python-automation-chatgpt](https://gitlab.com/nanuchi/python-automation-chatgpt)

## Usage

Build the image. 

`docker build -t pygen-gpt .`

Run the container with a mounted volume.

`docker run -it -v $(pwd):/code pygen-gpt /bin/bash`

Start generating code. It will be saved to the output directory.

`python pygen-gpt.py "count to 10" ten.py`

Run your output (may need clean up first).

`python output/ten.py`


