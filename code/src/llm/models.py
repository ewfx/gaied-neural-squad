import os

from huggingface_hub import login, InferenceClient

class LLMChat:
    def __init__(self, llm: InferenceClient):
        self.llm = llm
        self.chat_history = []
        self.user_message_count = 0
    
    def add_system_message(self, message: str):
        print(f'Adding system message for {self.llm.__dict__}')
        self.chat_history.append({"role": "system", "content": message})
    
    def __add_user_message(self, message: str):
        self.chat_history.append({"role": "user", "content": message})
        
    def __add_assistant_message(self, message: str):
        self.chat_history.append({"role": "assistant", "content": message})
        
    def prompt(self, prompt: str) -> str:
        self.user_message_count += 1
        self.__add_user_message(prompt)
        print(f'prompt type: {type(prompt)}')
        print(f'-   PROMPT #{self.user_message_count}: {self.chat_history[-1]['content'][1:100]}...')
        chat_completion_output = self.llm.chat_completion(
            messages=self.chat_history,
            max_tokens=1024,
            temperature=0.001
        )
        response = chat_completion_output.choices[0].message.content
        print(f'- RESPONSE #{self.user_message_count}: {response}')
        
        self.__add_assistant_message(response)
        
        return response

HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACE_TOKEN')

login(HUGGINGFACEHUB_API_TOKEN)

repo_ids = [
    'mistralai/Mistral-7B-Instruct-v0.2',
    # 'google/flan-t5-small',
    'google/gemma-3-27b-it',
    # 'Qwen/Qwen2.5-7B-Instruct',
]

all_models = [
    (id, InferenceClient(id, token=HUGGINGFACEHUB_API_TOKEN)) for id in repo_ids
]