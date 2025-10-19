import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

with st.sidebar:
    st.markdown("### 📁 Upload Your Chat")
    st.markdown("---")
    
    uploaded_file = st.file_uploader("Choose a file", type=['txt'])
if uploaded_file is not None:

    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    user_list =df['user'].unique().tolist()
    user_list.remove('notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user= st.sidebar.selectbox("Show Analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        st.markdown("### 📊 Quick Statistics")

        num_messages,words,num_media_omitted,links=helper.fetch_stats(selected_user,df)

        col1, col2, col3, col4 = st.columns(4)

        with col1 : 
            st.metric(label="💬 Total Messages", value=num_messages)
        with col2:
            st.metric(label="📝 Total Words", value=words)
        with col3:
            st.metric(label="🖼️ Media Shared", value=num_media_omitted)
        with col4:
            st.metric(label="🔗 Links Shared", value=links)


        st.markdown("---")

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📈 Timeline", 
        "📅 Activity", 
        "👤 Top Users",
        "☁️ Word Cloud",
        "🔤 Common Words",
        "✉️ Emojis"
    ])
        
        with tab1:

            st.markdown("### 📈 Monthly Timeline")           
            timeline = helper.monthly_timeline(selected_user,df)
            fig,ax = plt.subplots(figsize=(14, 5))
            ax.plot(timeline['time'],timeline['message'],linewidth=2.5, color='#667eea', marker='o', markersize=6)
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)

            st.markdown("### 📈 daily Timeline")
            daily_timeline = helper.daily_timeline(selected_user,df)
            fig,ax = plt.subplots(figsize=(14, 5))
            ax.plot(daily_timeline['day'],daily_timeline['message'],linewidth=2, color='#764ba2', marker='o', markersize=4)
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)
        with tab2:
            st.markdown("### 🔥 Activity by Day and Month")
            col1,col2 = st.columns(2)

            with col1:
                st.markdown("#### Most Active Day")
                busy_day = helper.week_activity_map(selected_user,df)
                fig,ax = plt.subplots(figsize=(14, 5))
                ax.bar(busy_day.index,busy_day.values,color='#667eea', alpha=0.7, edgecolor='#764ba2', linewidth=1.5)
                st.pyplot(fig)

            with col2:
                st.markdown("#### Most Active Month")
                busy_month = helper.month_activity_map(selected_user,df)
                fig,ax = plt.subplots(figsize=(14, 5))
                ax.bar(busy_month.index,busy_month.values, color='#764ba2', alpha=0.7, edgecolor='#667eea', linewidth=1.5)
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)

            st.markdown("#### Heatmap")
            user_heatmap = helper.activity_heatmap(selected_user,df)
            fig,ax = plt.subplots(figsize=(14, 8))
            sns.heatmap(user_heatmap, ax=ax, cmap='YlOrRd', cbar_kws={'label': 'Messages'})
            plt.tight_layout()
            st.pyplot(fig)

        with tab3:

            if selected_user == 'Overall':
                st.markdown("### 👥 Most Active Users")
                x, new_df = helper.most_busy_users(df)
                fig,ax = plt.subplots(figsize=(12, 6))
                
                ax.bar(x.index,x.values,color ='#667eea')
                st.pyplot(fig)

                st.dataframe(new_df)
        with tab4:

            st.markdown("### ☁️ Word Cloud")
            df_wc = helper.create_wordcloud(selected_user,df)
            fig,ax = plt.subplots(figsize=(12, 6))
            ax.imshow(df_wc,interpolation='bilinear')
            plt.tight_layout()
            st.pyplot(fig)

        with tab5:
            most_common_df = helper.most_common_words(selected_user,df)
            st.markdown("### 🔤 Most Common Words")
            fig,ax = plt.subplots(figsize=(12, 6))
            ax.bar(most_common_df[0],most_common_df[1], color='#764ba2', alpha=0.8, edgecolor='#667eea', linewidth=1.5)
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)
        with tab6:
            emoji_df = helper.emoji_helper(selected_user,df)
            st.markdown("### ✉️ Emoji Analysis")
            if len(emoji_df) > 0:
                st.dataframe(emoji_df, use_container_width=True)
            else:
                st.info("No emojis found in the selected chat.")

        