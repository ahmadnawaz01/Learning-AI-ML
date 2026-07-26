from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
import time

# Set your custom cache directory
os.environ['HF_HOME'] = 'D:/huggingface_cache'

print("Loading model into memory... (This might take 10-30 seconds)")

# Load the model
llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

print("\nModel loaded! Starting inference...")

# Start the timer
start_time = time.time()

# Generate the response
result = model.invoke("What is the capital of Lahore")

# Stop the timer
end_time = time.time()
inference_time = end_time - start_time

# Print the results
print("\n--- RESPONSE ---")
print(result.content)
print("----------------")
print(f"Inference took: {inference_time:.2f} seconds")



print("\nModel loaded! Starting inference...")

# Start the timer
start_time = time.time()

# Generate the response
result = model.invoke("what is the basic of C++")

# Stop the timer
end_time = time.time()
inference_time = end_time - start_time

# Print the results
print("\n--- RESPONSE ---")
print(result.content)
print("----------------")
print(f"Inference took: {inference_time:.2f} seconds")