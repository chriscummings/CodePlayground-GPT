import os
import argparse
import dotenv
import openai


##
# Load in secret/environment variables.
dotenv_file = os.path.join("./", ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
else:
    raise Exception("Unable to find .env file.")

openai.api_key = os.environ['OPENAI_KEY']

##
# Handle parameters.
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save Python script")
args = parser.parse_args()

prompt = f"Write python script to {args.prompt}. Provide only code, no text",

##
# Execute request.
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=60,
  n=1,
  stop=None,
  temperature=0.1,
)

message = response.choices[0].text.strip()

##
# Output to file.
with open(os.path.join("output/", args.file_name), "w") as file:
    file.write(message)
