from transformers import pipeline, AutoTokenizer
from langchain_huggingface import HuggingFacePipeline

def load_llm():

    model_name = "HuggingFaceTB/SmolLM2-360M-Instruct"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    pipe = pipeline(
        "text-generation",
        model=model_name,
        tokenizer=tokenizer,
        max_new_tokens=200,
        do_sample=False,
        device=-1  # CPU
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    return llm
