from decimal import Decimal
import json
import os
import openai
import boto3

dynamodb = boto3.resource('dynamodb')

def decimal_to_int(obj):
    if isinstance(obj, Decimal):
        return int(obj)

class GetData:
    def __init__(self, value1: str):
        self.Value1 = value1


openai.api_key = os.environ['API_Key']
API_ENDPOINT = 'https://api.openai.com/v1/engine/davinci-codex/completions'

def lambda_handler(event, context):
    data = GetData(event["Value1"])
    output = call_chatGPT(data.Value1)
    print(data.Value1)
    print(output)
    write_dynamoDB(data.Value1,output)
    return output


   
#GPTを呼び出す    
def call_chatGPT(inputText):
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system" , "content": "あなたは山口弁を話す女子大学生です。また回答は250字以内で行ってほしい。"} ,
            # {"role": "system" , "content": "入力された文章が文法的に正しいか、間違えている場合はその理由も合わせて250字以内で日本語で説明して"} ,
            {"role": "user", "content": inputText }
        ]
    )
    print("Received response:" + json.dumps(response,default=decimal_to_int, ensure_ascii=False))
    return response["choices"][0]["message"]["content"]

#DynamoDBに書き込む    
def write_dynamoDB(input , output):
    table = dynamodb.Table('0629-DB')

    table.put_item(
    	Item={
    		"INPUT": input,
    		"OUTPUT": output
    	}
    )
    
    
