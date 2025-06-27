def build_prompt(context: str) -> str:
    prompt = f"""You are a helpful assistant. Use only the information provided in the CONTEXT 
    and use it to construct an efficient knowledge graph.
    Include key biographical data such as birth/death dates and places for completeness.
    Present information in a chronological and logically grouped structure.
    Use specific and technically accurate terminology rather than broad or vague phrases.
    Add quantifiable achievements (e.g., number of patents, awards) to demonstrate impact.
    Avoid redundant phrasing and ensure smooth transitions between ideas.
    Highlight historically significant contributions, not just honorifics or side facts.
    Maintain a formal but engaging tone to balance clarity with readability.
    Ensure each sentence adds unique value to avoid repetitive content.
    CONTEXT:
    {context}
    """
    return prompt
