# Enterprise Knowledge Base Q&A System (AWS Bedrock RAG)

## Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system using **Amazon Bedrock Knowledge Bases** and **AWS Foundation Models**.
The application allows users to ask natural language questions about enterprise documents and receive accurate, context-aware responses.

## Architecture

```
User → Streamlit UI → AWS Bedrock Knowledge Base → AWS Model → Response
```

## Features

* Enterprise document Q&A
* Retrieval-Augmented Generation (RAG)
* Amazon Bedrock Knowledge Base integration
* AWS Foundation Models
* Streamlit UI
* Production-ready structure

## Project Structure

```
enterprise-bedrock-rag/
│
├── app/
│   ├── streamlit_app.py
│   ├── rag.py
│   └── config.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

Before running this project, ensure you have:

* Python 3.9+
* AWS Account
* Amazon Bedrock access enabled
* Knowledge Base created in AWS Bedrock

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## AWS Configuration

Configure AWS credentials:

```bash
aws configure
```

Enter:

* AWS Access Key ID
* AWS Secret Access Key
* Default region (e.g. eu-north-1)
* Default output format (json)

## Environment Variables

Create `.env` file:

```
AWS_REGION=region
KNOWLEDGE_BASE_ID=your_knowledge_base_id
MODEL_ARN=your_model_arn
```

## Run Locally

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

## Example Queries

* What is the leave policy?
* How many sections are in the document?
* What is section 42?
* What is probation period?

## Technologies Used

* Python
* AWS Bedrock
* Amazon Bedrock Knowledge Bases
* Streamlit
* Boto3


## Author

O Akshaykumar

