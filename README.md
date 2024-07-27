### Setup the env variables
```
export OPENAI_API_KEY=POTATO
export REDDIT_CLIENT_ID=POTATO
export REDDIT_CLIENT_SECRET=POTATO
```

### Run the script
```
python -m venv venv
# Note that the requirements.txt file contains more utilities than what the code needs to run
pip install -r requirements.txt
python reddit-analysis.py
```

### Output
```
**Run 1:**
- Positive: 5%
- Neutral: 25%
- Negative: 70%

**Run 2:**
- Positive: 10%
- Neutral: 20%
- Negative: 70%

**Run 3:**
- Positive: 8%
- Neutral: 22%
- Negative: 70%

**Run 4:**
- Positive: 7%
- Neutral: 18%
- Negative: 75%

**Run 5:**
- Positive: 6%
- Neutral: 24%
- Negative: 70%
```