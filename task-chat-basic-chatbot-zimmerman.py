#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:34:19 2023

@author: fzimmerman
"""
#%% global
import openai
openai.api_key = "YOUR-API-KEY"

#%% set up
prompt = "YOUR-PROMPT"
#Temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random,
#while lower values like 0.2 will make it more focused and deterministic.
temperature = 0.8

class ChatBot:

    def __init__(self, prompt, temperature):
        self.messages = [
            { "role": "system", "content": prompt }
        ]
        self.temperature = temperature
    
    
    def chat(self):
        userMessage = input("You: ")
        
        self.messages.append(
            { "role": "user", "content": userMessage}
        )
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = self.messages,
            temperature = self.temperature
        )
        
        answer = response.choices[0]['message']['content']
        
        print("Bot:", answer)
        
        self.messages.append(
           { "role": "assistant", "content": answer} 
        )

#%% run
if __name__ == "__main__":
    bot = ChatBot(prompt, temperature)
    while True:
        bot.chat()