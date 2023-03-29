# CodePlayground-GPT
Generate scripts for any language with gpt and work with them inside the docker container.

## Usage

* Create a `.env` file (or rename `.env.example` to `.env`)
* Add your OpenAI key. [(Link to keys page)](https://platform.openai.com/account/api-keys)
* Build the image. 
  * `docker build -t playground-gpt .` 
* Run the container with a mounted volume. 
  * `docker run -it -v $(pwd):/code playground-gpt /bin/bash`
* Start generating code. It will be saved to the output directory. 
  * `python playground-gpt.py python3 "count to 10" ten.py`
* Run your output (may need clean up first). 
  * `python output/ten.py`

### How do I add dependencies?

Quick and dirty:

* Just add via pip. `pip install some-library`

More long term:

* Stop your running container.
* Add to the `requirements.txt` file.
* Rebuild your image and go from there.

