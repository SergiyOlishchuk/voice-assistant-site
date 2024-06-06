
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from .data_set import DATA_SET, TO_FUNC
from .assistant import lang_model_answer

vectorize = CountVectorizer()
vectors = vectorize.fit_transform(list(DATA_SET.keys()))

clf = LogisticRegression()
clf.fit(vectors, list(DATA_SET.values()))

def execute_command(command, save_audio_path, api_key):
    user_command_vector = vectorize.transform([command])
    
    predicted = clf.predict_proba(user_command_vector)
    max_probability = max(predicted[0])
    
    if max_probability > 0.5:
        func = TO_FUNC[clf.classes_[predicted[0].argmax()]]
        return func(command, save_audio_path)
    else:
        return lang_model_answer(command, save_audio_path, api_key)

