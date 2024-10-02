import streamlit as st

# Define questions and answers
quiz_data = [
    {
        "question": "What was our first Meet?",
        "options": ["Sir ka office ", "Movie", "Park", "Cafe"],
        "answer": "Sir ka office "
    },
    {
        "question": "What is my favorite memory of us?",
        "options": ["barish me sath rhna ", "The concert", "Cooking together", "Stargazing"],
        "answer": "barish me sath rhna "
    },
    {
        "question": "Where would I love to travel with you?",
        "options": ["jo rasta kabhi khatm na honn", "Tokyo", "New York", "London"],
        "answer": "jo rasta kabhi khatm na honn"
    },
    {
        "question": "What is my favorite thing about you?",
        "options": ["Your DANCE", "Your kindness", "Your sense of humor", "Your intelligence"],
        "answer": "Your DANCE"
    },
    {
        "question": "What song reminds me of you?",
        "options": ["maine khud ko de dia tujhko", "Thinking Out Loud", "All of Me", "Can't Help Falling in Love"],
        "answer": "maine khud ko de dia tujhko"
    },
]

# Set up the Streamlit app
st.title("💖 Love Quiz 💖")
st.balloons()
st.write("Let's see how well you know me!")

# Initialize session state for score and answered questions
if 'score' not in st.session_state:
    st.session_state.score = 0

if 'answered' not in st.session_state:
    st.session_state.answered = [False] * len(quiz_data)

# Quiz loop
for i, question in enumerate(quiz_data):
    st.subheader(question["question"])
    
    # Only show options if the question hasn't been answered yet
    if not st.session_state.answered[i]:
        answer = st.radio("Choose an option:", question["options"], key=f"answer_{i}")
        
        if st.button("Submit", key=f"submit_{i}"):
            st.session_state.answered[i] = True  # Mark question as answered
            if answer == question["answer"]:
                st.success("Correct! 🎉")
                st.session_state.score += 1
            else:
                st.error("Oops! That's not right. 😢")
    else:
        # Indicate the question has already been answered
        st.write("You already answered this question.")

# Display the final score after all questions are answered
if all(st.session_state.answered):
    st.write(f"You got {st.session_state.score} out of {len(quiz_data)} correct!")
    
# Button to show score
if st.button("Show Score"):
    if all(st.session_state.answered):  # Check if all questions have been answered
        st.write(f"You got {st.session_state.score} out of {len(quiz_data)} correct!")
    else:
        st.warning("Please answer all questions before checking your score!")

st.write("Thanks for taking the quiz! 💖")
