from urlextract import URLExtract
from wordcloud import WordCloud
extractor = URLExtract()

def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user']== selected_user]

    num_messages = df.shape[0]

    words=[]
    for message in df['message']:
        words.extend(message.split())

    num_media_omitted = df[df['message']=='<Media omitted>'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages,len(words),num_media_omitted,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index' : 'name','user':'Percent'})
    return x,df

def create_wordcloud(selected_user,df):
    if selected_user !='Overall':
        df = df[df['user']== selected_user]
    wc = WordCloud(width = 500,height = 500,min_font_size=10,background_color= 'white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc