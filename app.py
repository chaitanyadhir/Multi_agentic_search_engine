from core.google_search import *
from prompts.prompt1 import *
from core.response1 import *
from prompts.prompt2 import *

query="who is prime minister of italy?"
text=""

results = search_and_scrape_duckduckgo(query)

for i,j in enumerate(results):
    text+=j

prompt=build_prompt(text)
KG=get_response(prompt)
print(KG)

prompt2=build_prompt2(KG,query)
result=get_response(prompt2)
print(result)
