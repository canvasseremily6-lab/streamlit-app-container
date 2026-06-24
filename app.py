import streamlit as st
import matplotlib.pyplot as plt
import joblib 
from PIL import Image 

img = Image.open('Movie-reel.svg.png')
st.image(img, width =200)

@st.cache_data
def load_model():
    """Loads pre-trained naives-bayes claissification model"""
    model = joblib.load('sentiment_model.pkl')
    return model

model = load_model()

st.title('Movie Review Sentiment Analyzer')
st.markdown('Write a movie review and see what sentiment is predicted based on data from IMBD reviews')

user_text = st.text_area(label ='Enter a movie review to analyze', placeholder = 'Write a movie review here')

if st.button(label = 'Analyze'):
    if user_text == '':
        st.write('***Please type a movie review to be analyzed***')
    else: 
        st.session_state['prediction'] = model.predict([user_text])
        st.session_state['probability'] = model.predict_proba([user_text])

if 'prediction' in st.session_state:
    pred = st.session_state['prediction']
    probs = st.session_state['probability']

    if pred == 'positive':
        st.success('Prediction Sentiment: Positive', icon = '👍')
    else: 
        st.error('Predicted Sentiment: Negative', icon = '👎')

    if hasattr(probs, 'flatten'):
        probs = probs.flatten()
    elif isinstance(probs[0], list):
        probs = probs[0]

    labels = ['Negative', 'Positive']

    fig,ax =plt.subplots(figsize = (2,2), dpi = 300)
    ax.pie(probs, labels=labels, autopct='%1.1f%%', textprops={'fontsize':4}, colors = ['#dc143c', '#228b22'])
    ax.set_title('Prediction Probability', fontsize = 4, fontweight= 'bold')
    st.pyplot(fig)
