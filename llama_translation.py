import transformers
import streamlit as st

@st.cache_resource
def load_model():
    model_id = "meta-llama/Meta-Llama-3.1-70B"  # Replace with the correct model identifier if necessary
    return transformers.pipeline(
        "text-generation",
        model=model_id,
        tokenizer=model_id
    )

class ModelTranslator:
    def __init__(self):
        self.pipeline = load_model()

    def translate_text(self, text: str) -> str:
        result = self.pipeline(text, max_length=100, num_return_sequences=1)
        return result[0]['generated_text']





# import transformers

# class ModelTranslator:
#     def __init__(self):
#         model_id = "meta-llama/Meta-Llama-3.1-70B"  # Replace with the correct model identifier if necessary
#         self.pipeline = transformers.pipeline(
#             "text-generation",
#             model=model_id,
#             tokenizer=model_id
#         )

#     def translate_text(self, text: str) -> str:
#         result = self.pipeline(text, max_length=100, num_return_sequences=1)
#         return result[0]['generated_text']








