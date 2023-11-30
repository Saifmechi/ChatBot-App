# chatbot.py
import openai

# Set your OpenAI API key
openai.api_key = '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'

def generate_response(prompt):
    try:
        # Use OpenAI GPT-3 to generate a response based on the prompt
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            temperature=0.2,
            stop=None,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating response from OpenAI: {e}")
        return f"Error generating response: {e}"
