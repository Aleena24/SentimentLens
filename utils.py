import pandas as pd

def extract_reviews(file):
    if file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
    elif file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        raise ValueError("Unsupported file format. Only .csv and .xlsx are allowed.")

    if 'review' not in df.columns:
        raise ValueError("The file must contain a 'review' column.")
    
    reviews = df['review'].tolist()
    return reviews

def process_reviews(reviews):

    sentiment_scores = {
        "positive": 0,
        "negative": 0,
        "neutral": 0
    }

    for review in reviews:
        if "good" in review.lower():
            sentiment_scores["positive"] += 1
        elif "bad" in review.lower():
            sentiment_scores["negative"] += 1
        else:
            sentiment_scores["neutral"] += 1
    
    return sentiment_scores
