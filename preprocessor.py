import re
import pandas as pd
def preprocess(data):
    pattern = r'(\d{1,2}\/\d{1,2}\/\d{2,4},\s\d{1,2}:\d{2}\s?(?:am|pm)\s-\s)'

    messages = re.split(pattern, data)[1:]
    messages = [msg.strip().replace('\u202f',' ').replace('\u200e','') for msg in messages]
    message = messages[1::2]
    dates = messages[::2]
    df = pd.DataFrame({'user_message': message, 'message_date' : dates})
    df['message_date'] =  df['message_date'].str.replace('-',' ')
    df['message_date'] = (df['message_date']
                  .str.replace('\u202f', ' ', regex=False)   
                  .str.replace('\u200e', '', regex=False)    
                  .str.strip())
    df['message_date'] =pd.to_datetime(df['message_date'], format="%d/%m/%y, %I:%M %p",
                                 dayfirst=True, errors='coerce')
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'(.+?):\s+', message, maxsplit=1)
        if len(entry) > 1:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns =['user_message'],inplace = True )
    df['user']=df['user'].str.replace(':',' ')
    df['year']=df['message_date'].dt.year
    df['month']=df['message_date'].dt.month_name()
    df['month_num']=df['message_date'].dt.month
    df['day']=df['message_date'].dt.day
    df['day_name'] = df['message_date'].dt.day_name()
    df['hour'] = df['message_date'].dt.hour
    df['minute'] = df['message_date'].dt.minute
    return df