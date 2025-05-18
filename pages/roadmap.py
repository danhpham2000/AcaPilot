import streamlit as st
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from vector import storage_context, vector_store
from schema import *
import pandas as pd
import os



embed_model = OpenAIEmbedding(model="text-embedding-3-large", api_key=os.getenv("OPENAI_API_KEY"))
model = OpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))




st.title("Roadmap for student")





st.subheader("Smart tips for classes")
if "roadmap" not in st.session_state or not st.session_state.roadmap:
    st.warning("Go to Dashboard to add your class to get smart tips")
else:
    for r in st.session_state.roadmap:
        for single_r in r.resources:
            r_df = pd.DataFrame(
                {
                    "Title": [single_r.title],
                    "Description": [single_r.description]
                }
            )


            st.data_editor(r_df, hide_index=True)




st.subheader("Resources for classes")

if "resources" not in st.session_state or not st.session_state.resources:
    st.warning("There is no roadmap available. Please go to Dashboard and add classes")

else:
    for resource in st.session_state.resources:
        st.write(resource)
        