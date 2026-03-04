from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)


## This loads the environment variables from a .env file, which is commonly used to store sensitive information like API keys. 
# The OpenAI class is then instantiated with the specified model, and the invoke method is called with a prompt
#  to get the response from the language model. 
# Finally, the result is printed to the console.

## The capital of India is New Delhi. = result will be this answer.
