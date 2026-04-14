import boto3
from config import AWS_REGION, KNOWLEDGE_BASE_ID, MODEL_ARN

client = boto3.client(
    "bedrock-agent-runtime",
    region_name=AWS_REGION
)

def ask_question(query):
    response = client.retrieve_and_generate(
        input={
            "text": f"""
You are answering from an HR policy document.

Instructions:
- If section number is mentioned, find exact section
- Carefully search retrieved context
- Return exact section content
- Do not guess

Question: {query}
"""
        },
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                "modelArn": MODEL_ARN,
                "retrievalConfiguration": {
                    "vectorSearchConfiguration": {
                        "numberOfResults": 20,
                        "overrideSearchType": "SEMANTIC"
                    }
                },
                "generationConfiguration": {
                    "inferenceConfig": {
                        "textInferenceConfig": {
                            "temperature": 0
                        }
                     }
                }
            }
        }
    )

    return response["output"]["text"]