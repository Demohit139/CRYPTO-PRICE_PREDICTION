# %%
import mwclient 
import time


# %%
site =mwclient.Site("en.wikipedia.org")
page=site.pages["Bitcoin"]

# %%
revs=list(page.revisions())

# %%
revs[0]

# %%
revs = sorted(revs, key=lambda rev: rev["timestamp"])

# %%
revs[0]

# %%
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def find_sentiment(text):
    sent=sentiment_pipeline([text[:250]])[0]
    score = sent["score"]
    if sent["label"] == "NEGATIVE":
        score *=-1
    return score

# %%
edits = {}

for rev in revs:
    date= time.strftime("%Y-%m-%d", rev["timestamp"])

    if date not in edits:
        edits[date]= dict(sentiments=list(), edit_count=0)

    edits[date]["edit_count"] +=1

    comment= rev["comment"]
    edits[date]["sentiments"].append(find_sentiment(comment))


