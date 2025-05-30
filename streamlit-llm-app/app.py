from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain 
from langchain.chat_models import ChatOpenAI

# Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示
st.markdown("""
### アプリの概要
このアプリは、さまざまな分野の専門家になりきったAIからアドバイスを受け取ることができます。

### 操作方法
1. 下の入力欄に質問や相談内容を入力してください。
2. 専門家の種類を選択してください
3. 「送信」ボタンを押すと、選択した専門家になりきったAIが回答を返します。
""")

def get_expert_response(input_text, expert_type):
    if expert_type == "引っ越しの専門家":
        system_message = "あなたは引っ越しの専門家です。簡潔で的確なアドバイスを提供してください。"
    elif expert_type == "健康とフィットネスの専門家":
        system_message = "あなたは健康とフィットネスの専門家です。簡潔で的確なアドバイスを提供してください。"
    else:
        system_message = "あなたは一般的なアドバイザーです。簡潔で的確なアドバイスを提供してください。"

    # 変数名をinputに統一
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("user", "{input}")
    ])

    llm = ChatOpenAI(model_name="gpt-4.1-nano", temperature=0.5)
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)

    # inputというキーワード引数で渡す
    response = llm_chain.run(input=input_text)
    return response

# ユーザーからの入力欄と専門家タイプの選択
input_text = st.text_input("質問や相談内容を入力してください")
expert_type = st.radio("専門家の種類を選択してください", ["引っ越しの専門家", "健康とフィットネスの専門家"])

if st.button("送信"):
    if input_text:
        response = get_expert_response(input_text, expert_type)
        st.markdown("#### 回答")
        st.write(response)
    else:
        st.warning("質問や相談内容を入力してください。")


