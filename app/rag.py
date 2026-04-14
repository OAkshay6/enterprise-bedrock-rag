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

Use ONLY the information from the retrieved document.
Do NOT use outside knowledge.
Do NOT add extra sections.
Do NOT assume or generate missing information.

If the answer is not found in the document, say:
"Answer not found in document."

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
                        "numberOfResults": 15
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