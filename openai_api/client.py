from openai import OpenAI
#Funcionando perfeitamente
#chave: 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
#Função não utilizada no momento, pois a api é paga para utilizar

client = OpenAI(api_key='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')


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content

