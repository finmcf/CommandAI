import openai
import click
import re
import subprocess

import prompt_toolkit

# Set up OpenAI API credentials
openai.api_key = "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"


# Define the OpenAI API call as a function
def generate_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
    )

    # Get the generated text from the response
    matches = re.findall(r"`(.*?)`", response["choices"][0]["text"])
    
    return matches
    

# Define the Click command
@click.command()
@click.option('--prompt', prompt='Enter a prompt to generate a response', help='Prompt for the OpenAI API call')
def chat(prompt):
    response = generate_text(prompt)
    print(response)

    

    if len(response) > 0:
        while True:
            BUFFER = prompt_toolkit.prompt("", default=response[0])
            

            # Run the command entered by the user
            try:
                result = subprocess.run(BUFFER, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                print(result.stdout.decode())
            except Exception as e:
                print(str(e))
 

# Run the Click command
if __name__ == '__main__':
    chat()
