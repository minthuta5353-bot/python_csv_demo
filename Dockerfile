# Python Official Image ကို အသုံးပြုခြင်း
FROM python:3.10-slim

# Working Directory သတ်မှတ်ခြင်း
WORKDIR /app

# လိုအပ်သော requirements ဖိုင်များကို ကူးထည့်ခြင်း
COPY requirements.txt .

# Dependencies များကို Install လုပ်ခြင်း
RUN pip install --no-cache-dir -r requirements.txt

# Project ဖိုင်အားလုံးကို Container ထဲသို့ ကူးထည့်ခြင်း
COPY . .

# Container စတင် run လျှင် app.py ကို လုပ်ဆောင်ရန်
CMD ["python", "app.py"]
