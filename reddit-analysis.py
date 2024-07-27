import os

import praw  # type: ignore[import-untyped]
from openai import OpenAI


def get_openai_sentiment(titles):

    prompt = (
        "You take the role of a system analyzing sentiment of sentences."
        "Your answers are short and concise"
        "When unsure, you do not provide an answer and ask for more information"
    )

    answer_format = (
        "Each title is separated by a comma."
        "Categorize the sentiment with one word."
        "The words can be 'neutral' 'negative', 'positive' based on the sentiment."
        "Provide a percentage breakdown of each sentiment."
        "Run the sentiment analysis 5 times on all titles"
        "Return each run of the analysis"
        "There should be some variations in the percentages"
    )
    titles_str = ",".join(map(str, titles))
    # The Openai credentials are stored in the environment variable OPENAI_API_KEY
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": answer_format},
            {"role": "user", "content": titles_str},
        ],
    )
    print(response.choices[0].message.content)  # noqa: T201


def get_reddit_posts():
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="space-potato:coldnorthadmin:42.42.42 (by u/laurentfdumont)",
    )

    list_titles = []
    for submission in reddit.subreddit("aws").search("amplify", limit=1000):
        list_titles.append(submission.title)

    get_openai_sentiment(list_titles)


def analyse_reddit():
    get_reddit_posts()


if __name__ == "__main__":
    analyse_reddit()
