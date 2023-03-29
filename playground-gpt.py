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
parser.add_argument("language", help="The programing language to use in solution.")
parser.add_argument("task", help="Task to send to GPT")
parser.add_argument("filename", help="Output file.")
args = parser.parse_args()

prompt = f"Write a {args.language} script to {args.task}. Provide only code, no text. Include comments.",

##
# Execute request.
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=999,
  n=1,
  stop=None,
  temperature=1,
)

message = response.choices[0].text.strip()

##
# Output to file.
with open(os.path.join("output/", args.filename), "w") as file:
    file.write(message)
