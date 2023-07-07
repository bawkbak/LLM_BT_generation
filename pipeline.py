import openai
from utils import remove_front_until, find_file, append_tab, subtree_assembly

openai.api_key = "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"

with open('prompt/test.txt', 'r') as file:
    prompt = file.read().rstrip()

response = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    temperature=0,
    max_tokens=500,
    top_p=1,
    presence_penalty=0,
    frequency_penalty=0.2
)

print(response)

completed_text = response['choices'][0]['text']

print("\nHere is the generation tree:")
print(completed_text)

raw_string = remove_front_until(str(completed_text), "->")

raw_text_file = open("result/sample.tree", "wt")
n = raw_text_file.write(raw_string)
raw_text_file.close()

text_file = open("result/execution.tree", "wt")
m = text_file.write(subtree_assembly(raw_string))
text_file.close()