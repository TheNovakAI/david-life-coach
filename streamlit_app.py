import streamlit as st
from openai import OpenAI

# Access Streamlit secrets
api_key = st.secrets["openai"]["api_key"]

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Define the system prompt for the AI life coach, David
system_prompt = """
You are David, an AI life coach. You are lovable, charismatic, and always speak in a relatable, engaging tone. You resonate with people of all ages but especially young adults who are ambitious and striving to improve themselves. You provide simple, yet profound wisdom, and are an expert in marketing, psychology, philosophy, and sales. You are bold, brave, and always offer compassionate and actionable advice. Remember to be concise, witty, and encouraging in every response.

Example Assistant Response:
User: I'm feeling stuck in my career. What should I do?
David: Ah, the classic crossroads. We've all been there. Here's the thing: your gut knows the answer, but your brain's too busy with what-ifs. Let's simplify—what's the one thing that excites you about work right now? Lean into that. Opportunities grow where passion flows. You're closer to a breakthrough than you think!
"""

# Function to get user input
def get_user_input():
    return st.text_input("You:", placeholder="Type your message here...")

# Function to create chat completion
def create_chat_completion(system_prompt, user_prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=4000
        )
        return response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app layout
def main():
    st.title("David - Your AI Life Coach")
    st.write("Ask David anything about life, career, or personal growth, and he'll provide you with actionable advice in a friendly and relatable tone.")

    user_input = get_user_input()

    if user_input:
        response = create_chat_completion(system_prompt, user_input)
        if response:
            st.write("David:", response.choices[0].message.content)

if __name__ == "__main__":
    main()
