import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. 데이터 수집 및 전처리
data = {
    'question': [
        "Hello",
        "How are you?",
        "What is your name?",
        "Bye"
    ],
    'answer': [
        "Hi there!",
        "I'm good, thank you!",
        "I am a chatbot.",
        "Goodbye!"
    ]
}

df = pd.DataFrame(data)

# 2. 모델 설계 및 학습
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['question'])
def get_response(user_input):
    user_input_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_input_vector, X)
    closest = np.argmax(similarities, axis=1)
    response = df['answer'].iloc[closest[0]]
    return response

# 3. 챗봇 인터페이스 구성
def chatbot():
    print("Chatbot: Hello! How can I help you? (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
