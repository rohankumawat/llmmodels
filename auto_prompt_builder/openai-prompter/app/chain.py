from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOpenAI

with open("prompt-guide.txt") as f:
    text = f.read()

template = """{text}
----------------------------

----------------------------

----------------------------
Based on above intructions, help me write a good prompt TEMPLATE.

This template should be a string that can be formatted as python f-string. It can take in any number of variables depending on my objectives.

Return your answer in the following format:

```prompt
...
```

This is my objective:

{objective}"""

prompt = PromptTemplate.from_template(template)
prompt = prompt.partial(text = text)
chain = prompt | ChatOpenAI(model="gpt-4-1106-preview") | StrOutputParser()