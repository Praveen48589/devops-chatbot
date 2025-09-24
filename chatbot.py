import os
from transformers import pipeline

# Load Hugging Face model
chatbot_model = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

# DevOps commands
def check_docker():
    return os.popen("docker ps").read()

def check_disk():
    return os.popen("df -h").read()

def deploy_app():
    return os.popen("kubectl rollout restart deployment my-app").read()

# Main chatbot logic
def devops_chatbot(query):
    query = query.lower()

    if "docker" in query:
        return check_docker()
    elif "disk" in query:
        return check_disk()
    elif "deploy" in query:
        return deploy_app()
    else:
        response = chatbot_model(query, max_length=100, num_return_sequences=1)
        return response[0]["generated_text"]
