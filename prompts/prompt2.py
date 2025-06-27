def build_prompt2(context: str, query: str) -> str:
    prompt = f"""you have been given the knowledge graph  {context} and the asked query {query}, now your task is to generate a answer for the asked query through the knowledge graph provided. answer should be in text format the graph is for your context only """
    return prompt
