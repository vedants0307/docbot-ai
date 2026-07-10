from langchain_core.prompts import PromptTemplate


QA_PROMPT = PromptTemplate.from_template(
"""
You are an AI assistant.

Answer ONLY using the provided context.

If the answer does not exist, say:

I could not find that information in the indexed sources.

Context:
{context}

Question:
{question}
"""
)