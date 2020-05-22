#%%
# pip(3) install twitterscraper
import twitterscraper as ts
from twitterscraper import query_tweets
import datetime as dt 
import pandas as pd 

#%%
begin_date = dt.date(2020,1,1)
end_date = dt.date(2020,1,2)

limit = 1000
lang = 'english'

#%%
# for specific key word
# tweets = query_tweets("LGBT", begindate = begin_date, enddate = end_date, limit = limit, lang = lang)

#%%
# for specific user
tweets = ts.query.query_tweets_from_user("tim_cook")

#%%
df = pd.DataFrame(t.__dict__ for t in tweets)

# %%
df.to_csv('tim_cook.csv')
