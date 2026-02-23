from dotenv import dotenv_values
from langchan.chat_models import init_chat_model


userdata = dotenv_values()


print(userdata("model"))
llm=init_chat_model(
    model=userdata("model")
    , base_url=userdata("base_url")
    ,api_key=userdata("cerebras")
    , temperature=userdata("temperature")
)
risposta =llm.invoke("in che anno è scoppiata la seconda guerra mondiale? rispondi brevemente")
print(risposta.content)

while True:
    domanda = input("COSA VUOI VHIEDERE?")
    if domanda == "esci";
        break
    risposta = llm.invoke(domanda)

    print(risposta.content)