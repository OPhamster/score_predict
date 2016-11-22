#!/usr/bin/python3.4m
from pandas import DataFrame,read_csv,read_json,Categorical
from os import walk
from os.walk import join


def load_data(path):
    train_frame = []
    train_frame = DataFrame(train_frame)
    subreddit_frame = read_json(join(path,"manifest.json"))
    path = join(path,"data")
    for root,dirs,files in walk(path):
        for f in files:
            filepath = join(root,f)
            current_frame = pd.read_csv(join(path,filepath))
            (current_frame,current_author_frame,current_domain_frame) = feature_extract(current_frame,f)
            train_frame.append(current_frame)
            current_author_frame.append(author_frame)
            current_domain_frame.append(author_frame)
            author_frame = current_author_frame.groupby("author").agg("np.sum")
            domain_frame = current_domain_frame.groupby("domain").agg("np.sum")
    author_frame = DataFrame(author_frame["score"]["sum"]/author_frame["score"]["size"])
    author_frame.rename(index=str,columns={0:"author_popularity"})
    return (train_frame,author_frame,domain_frame,subreddit_frame)

def feature_extract(current_frame,filename):
    current_frame = current_frame.drop(["permalink","selftext","thumbnail","edited","link_flair_css_class","author_flair_css_class","is_self","url"],1)
    boundary_utc = calendar.timegm(time.strptime('Jan 1, 2016 @ 00:00:00 UTC','%b %d, %Y @ %H:%M:%S UTC'))

    author_frame.columns,domain_frame.columns = ["id","frequency","total_score"],["name","no_of_hits"]
    current_frame["subreddit"] = str(filename[:-3])

    current_frame["created_utc"] = boundary_utc - current_frame["created_utc"]
    current_frame.rename(index = str,columns={"created_utc":"age","ups":"up_rate","downs":"down_rate","no_of_comments":"comment_rate","distinguished":"level","over_18":"nsfw"})
    current_frame["up_rate"] = current_frame["ups"]/current_frame["age"]
    current_frame["down_rate"] = current_frame["ups"]/current_frame["age"]
    current_frame["comment_rate"] = current_frame["no_of_comments"]/current_frame["age"]
    current_frame["level"] = Categorical(current_frame.distinguished).codes
    author_frame = author_features(current_frame)
    domain_frame = domain_features(current_frame)
    return (current_frame,author_frame,domain_frame)

def author_features(current_frame):
    author_frame = DataFrame()
    author_frame = current_frame.groupby("author").agg({"score":[np.sum,np.size]})
    del author_frame.index.name
    return author_frame

def domain_feature(domain_frame,current_frame):
    domain_frame = DataFrame()
    domain_frame = current_frame.groupby("domain").agg({"score":[np.size]})
    del domain_frame.index.name
    return domain_frame
