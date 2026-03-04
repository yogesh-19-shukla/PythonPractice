from langchain_openai import ChatOpenAI  # LangChain's wrapper for OpenAI chat models
from dotenv import load_dotenv           # loads your API key from .env file

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=100)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)


# temperature=1.5 — controls creativity (0 = robotic, 2 = very random)
# max_completion_tokens=100 — limits response to only 100 tokens (~75-80 words)