import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_script(user_prompt):
    base_prompt = f"""You are a master anime fight writer. Turn the following prompt into a detailed 1-minute anime fight scene:
    
    Prompt: {user_prompt}
    
    Format: Dialogue + Action. Make it MAPPA-style, cinematic, intense and fluid. Include camera directions and special attacks."""
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": base_prompt}]
    )

    return response.choices[0].message.content
