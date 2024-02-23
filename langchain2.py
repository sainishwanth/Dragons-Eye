# %% [markdown]
# # Dragon's Eye

# %% [markdown]
# ## A sample demonstration using LangChain framework

# %%
from langchain import HuggingFacePipeline, PromptTemplate, LLMChain
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
import torch

# %%
#model = "tiiuae/falcon-7b-instruct"
# Will go out of RAM on Colab
#tokenizer = AutoTokenizer.from_pretrained(model)

model = "tiiuae/falcon-7b-instruct"  # Replace with the model name you were using
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = pipeline(
    "text-generation", #task
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    offload_folder="offload",
    offload_state_dict = True
)

# %%
llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})

# %%
def run(question):
    template = """
    Your name is Dragon's Eye, an AI chatbot playing the role of a dungeon master in the table top game, Dungeons & Dragons. Remember the previous user inputs, keep track of players' scores, and generate scenarios and outcomes based on this. Help the players with the game and respond in first person.
    Question: {question}
    Answer:"""
    prompt = PromptTemplate(template=template, input_variables=["question"])
    
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))

# %%
question = "Explain what is Dungeons & Dragons"
run(question)

# %%
while True:
    question = input()
    run(question)


