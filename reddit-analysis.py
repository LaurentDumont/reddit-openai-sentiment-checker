import os

import click
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
        "Run the sentiment analysis 20 times on all titles"
        "Return each run of the analysis"
        "There should be some variations in the percentages"
        "Return the total % of negative, positive and neutral for all runs aggregated"
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


@click.command()
@click.option('--subreddit', default='Bacon', help='The subreddit to analyze')
@click.option('--keyword', default='Potatoes', help='The keyword to search for')
@click.option('-s', '--limit-search-results', default=50, help='How many search results are returned from the PRAW')
def get_reddit_posts(subreddit, keyword, limit_search_results):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="space-potato:coldnorthadmin:42.42.42 (by u/laurentfdumont)",
    )

    list_titles = []
    for submission in reddit.subreddit(subreddit).search(keyword, limit=limit_search_results):
        list_titles.append(submission.title)

    get_openai_sentiment(list_titles)


def analyse_reddit():
    get_reddit_posts()


if __name__ == "__main__":
    analyse_reddit()
