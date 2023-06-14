
import os
import openai
from configparser import ConfigParser

# Read in OpenAI API token
# NOTE: Make sure this file is in your .gitignore!
OPENAI_CRED_FILE = "../openai_creds.cfg"
config = ConfigParser()
config.read(OPENAI_CRED_FILE)
openai.api_key = config["OPENAI_API_KEY"]["openai_api_key"]


def call_openapi(text):
    response = openai.Completion.create(
      engine="davinci",
      prompt="""Ini adalah program pengalih bahasa
      
                 Kau buat apa ni?:Mung wak mende ning? ###
                 Tak faham bahasa sungguh kau ni:Dok pahang bahase goh mung ning ###
                 telefon berbunyi tu:Talipung bunying tu ###
                 Kenapa jadi macam tu?:Bakpe jadi gitu? ###
                 Ikut suka aku la:Ikut panda aku ar ###
                 Sedapnya bercakap:Sedak teh cakak ###
                 Nak pergi mana tu bro?:Nok gi mane tu boh? ###
                 Cuba kau tengok:Ce mung tengok ###
                 Malas aku nak tengok:Malah aku nok tengok ###
                 Kau tak nak makan ke?:Mung takboh makang ke? ###
                 Lauk tak sedap:Lauk dok sedak ###
                 Sedap ni:Sedak ning ###
                 Cuba kau rasa:Ce mung rase ###
                 Tawar sangat lauk ni:Tawo heber lauk ning ###
                 Tak boleh makan masin sangat:Dokleh makang maseng sangak ###
                 Nanti kena penyakit darah tinggi:Kekgi kene nyakek daroh tinggi ###
                 Kau jangan nak tipu:Mung jangang nok pelawok ###
                 Aku tak tipu pun:Aku dok pelawok pung ###
                 Jangan buat macam tu..tak baik:Jangang wak gitu..dok baik ###
                 Ikut suka aku la nak buat apa pun:Ikut panda aku ar nok wak gane-gane pung ###
                 Kenapa kau degil sangat?:Bakpe mung keghah keng ngak? ###
                 Sebab,memang aku degil pun:Sebak,memang aku keghah keng pung ###
                 Tak elok kau buat begini:Dok molek mung wak gining ###
                 Kenapa kau sibuk nak ambil tahu?:Bakpe mung sibuk nok ambik tahu? ###
                 Sebab,kau kan adik aku:Sebak,mung kang adik aku ###
                 Bila masa pula aku jadi adik kau?:Bila masa pulok aku jadi adik mung? ###
                 Baru kejap tadi:Baru sakning ###
                 Kau ni otak tak betul ke?:Mung ning otok mereng ke? ###
                 Biarlah kau nak kata apa pun:Biarlah mung nok kata mende pung ###
                 Pergi baliklah kau:Gi baliklah mung ###
                 Aku tak mahu biarkan kau kat sini:Aku takboh lok mung sining ###
                 kenapa pula?:Bakpe pulok? ###
                 Tak ada apa-apa:Takdok mende-mende ###
                {text}:""".format(text=text),
      temperature=0.3,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=[" ###"]
    )
    return response


def hello_world(
    initial_prompt="What is the most dense metal?",
    code_model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.4,
    ):
    print(f"Initial prompt:\n{initial_prompt}\n\n")
    initial_prompt += "```"
    chat_response = openai.ChatCompletion.create(
        model=code_model,
        messages=[
            {'role': 'user', 'content': initial_prompt}
                  ],
        stop="```",
        max_tokens=max_tokens,
        temperature=temperature,
        stream=True
    )
    out_str = ""
    for element in chat_response:
        try: 
            element_str = element["choices"][0]["delta"]["content"]
        except KeyError:
            element_str = ""
        out_str += element_str
    return out_str


# print(call_openapi('kenapa tak makan?'))
print(hello_world())
