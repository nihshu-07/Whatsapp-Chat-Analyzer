# 💬 WhatsApp Chat Analyzer

Transform your WhatsApp conversations into powerful insights with beautiful visualizations

---

## 🎯 Overview

WhatsApp Chat Analyzer is an interactive web application that extracts meaningful insights from your WhatsApp conversations. Visualize message patterns, discover trends, understand communication behavior, and much more  all with a beautiful, intuitive interface.
🔒 Privacy First: Your data is processed locally and never stored on external servers. Complete privacy guaranteed!

---

## 👀 Dashboard

<img width="1919" height="915" alt="image" src="https://github.com/user-attachments/assets/6344368f-8c94-4f0b-a584-05725ca92cd3" />

<img width="1919" height="853" alt="image" src="https://github.com/user-attachments/assets/9d0c47e7-9f7a-472f-a72b-5fe9aebdd24c" />

---

## ✨ Key Features

### 📊 Message Statistics

- Total messages, words, media shared, and links exchanged
- Quick overview of your conversation metrics
- Per user breakdown for group chats

### 📈 Timeline Analysis

- Monthly Timeline: See how your messaging activity changes month by month
- Daily Timeline: Understand your day to day communication patterns
- Smooth interactive charts with trend visualization

### 🔥 Activity Heatmap

- Discover your most active days of the week
- Find your peak messaging hours
- Beautiful heatmap visualization showing activity intensity

### ☁️ Word Cloud

- Visualize your most frequently used words
- See your vocabulary patterns at a glance
- Interactive and colorful representation

### 🔤 Common Words Analysis

- Top 20 most used words with frequency count
- Filter by user for personalized insights
- Bar chart visualization for easy comparison

### ✉️ Emoji Analysis

- Identify your favorite emojis
- See emoji usage frequency
- Understand your emotional expression patterns

### 👥 User Comparison (Group Chats)

- Compare activity levels across group members
- Pie charts showing user contribution percentages
- Bar charts for visual comparison

---

## 📖 How to Use
- Step 1: Export Your WhatsApp Chat
Android:

Open WhatsApp → Select a chat → Menu (⋮) → More → Export Chat
Choose "Without media" for faster processing
Save the .txt file

iOS:

Open WhatsApp → Select a chat → Swipe left → More → Export Chat
Choose "Without media"
Save the .txt file

- Step 2: Upload the File

Click on "📁 Upload Your Chat" in the sidebar
Select the exported .txt file
File size limit: 200MB

- Step 3: Select User

Choose between "Overall" (entire group) or individual users
For group chats, you can filter by specific participants

- Step 4: Click Analyze

Click the "🔍 Analyze" button
View all your insights across different tabs

- Step 5: Explore Tabs

Timeline: Monthly and daily message trends
Activity: Day-wise and month wise activity patterns with heatmaps
Top Users: Most active members (group chats only)
Word Cloud: Visual representation of your vocabulary
Common Words: Top 20 frequently used words
Emojis: Your emoji usage statistics

---

## 🚀 Quick Start

Prerequisites

Python 3.8 or higher
pip (Python package manager)

### Installation

Clone the repository

```bash
git clone https://github.com/nihshu-07/Whatsapp-chat-Analyzer.git
cd Whatsapp-chat-Analyzer
```

Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```
Running the Application

```bash
streamlit run main.py
```
The app will open in your browser at http://localhost:8501
