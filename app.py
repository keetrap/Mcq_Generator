import json
import traceback
import pandas as pd
from langchain_community.callbacks import get_openai_callback
from src.mcqgen.utils import read_file, get_table_data
from src.mcqgen.logger import logging
from src.mcqgen.mcqgen import gen_eval_chain
import streamlit as st

with open('response.json','r') as f:
    RESPONSE_JSON=json.load(f)
    
flag=False

st.title("MCQ Generator Using GPT-3 and Langchain 🦜️🔗")

with st.form("user_input"):
    uploaded_file = st.file_uploader("Upload a pdf or txt", type=["txt","pdf"])
    mcq_number=st.number_input("Number of MCQs",min_value=2, max_value=10)
    tone=st.selectbox("Complexity Level of Questions",["Easy","Medium","Hard"])
    submit=st.form_submit_button("Generate MCQs")
     
    if submit and uploaded_file is not None and mcq_number and tone:
        with st.spinner("Generating MCQs..."):
            try:
                text=read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response=gen_eval_chain(
                        {
                            "text": text,
                            "number": mcq_number,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )

            except Exception as e:
                st.error("An error occurred while generating MCQs.")
                st.error(traceback.format_exc())
            
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    st.success("MCQs Generated Successfully")
                    table_data=get_table_data(response.get("quiz"))
                    if table_data is not None:
                        df=pd.DataFrame(table_data)
                        df.index+=1
                        csv = df.to_csv(index=False).encode('utf-8')
                        flag=True
                        st.table(df)
                        st.text_area(label="Review",value=response.get("review"))
                    else:
                        st.error("Error in table data")
                else:
                    st.error("Error in response")
            
if flag:
    st.download_button(label="Download CSV", data=csv, file_name='generated_mcqs.csv', mime='text/csv')
                   