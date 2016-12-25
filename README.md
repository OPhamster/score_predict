# score_predict
Gist :: Using simple ml techniques to predict scores of reddit users
This is supposed to determine whether features of a reddit post have a polynomial or a linear relationshio with the score of 
a comment or not. If there lies a relationship - use it to predict the safest score of a certain comment with the current set
of features held by that comment. The data used to train this model is taken from the repo:<br>
data : https://github.com/umbrae/reddit-top-2.5-million/tree/master/data <br>
subreddit data : https://github.com/umbrae/reddit-top-2.5-million/blob/master/manifest.json

The features of a comment being used to train the model are:
  1. age = (border_utc - created_utc)
  2. up_rate = (ups/age)
  3. down_rate = (downs/age)
  4. comment_rate = (no_of_comments/age)
  5. nsfw (over_18 in this case) as a categorical value
  6. subreddit_popularity = (subreddit_subscribers/total_no_of_subscribers)
  7. domain_hits
  8. author_popularity = (total_score_of_author/author_frequency)
