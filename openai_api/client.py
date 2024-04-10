import openai
import os
#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

def get_car_ai_description(model, brand, year):
    openai.api_key = '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'

    prompt =f'Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas especificas desse modelo'
    
    response = openai.completions.create(
        model='text',
        prompt=prompt,
        max_tokens=500,
    )
    return response['choices'][0]['text']

