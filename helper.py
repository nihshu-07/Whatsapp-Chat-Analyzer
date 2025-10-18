def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user']== selected_user]

    num_messages = df.shape[0]

    words=[]
    for message in df['message']:
        words.extend(message.split())

    num_media_omitted = df[df['message']=='<Media omitted>'].shape[0]

    return num_messages,len(words),num_media_omitted
    