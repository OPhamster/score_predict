from numpy import array,mean
import statsmodels.api as sm
from pandas import merge

def train(train_frame,author_frame,domain_frame,subreddit_frame):
    train_frame = train_frame.merge(author_frame,how="inner",on="author")
    train_frame = train_frame.merge(domain_frame,how="inner",on="domain")
    train_frame = sm.add_constant(train_frame)
    train_frame,cross_validation_frame = train_test_splits(train_data,test_size=0.4)
    cross_validation_frame,test_frame = train_test_splits(cross_validation_frame,test_size=0.25)
    train_score = train_frame["score"]
    train_frame.drop(axis=1,["score"],inplace=True)
    model = sm.OLS(train_score,train_frame)
    result_model = model.fit_regularized(method="coord_descent",maxiter=500,alpha=0.03,start_params=None,cnvrg_tol=1e-08)
    result_model.summary()
    return (result_model,cross_validation_frame,test_frame)

def test(trained_model,test_frame):
    test_score = test_frame["score"]
    test_frame.drop(axis=1,["score"],inplace=True)
    obs_err = abs(trained_model.predict(test_frame)-test_score)
    #mean accuracy coz we need to generalize this model - this could have ramifications - look into it later
    avg_acc = mean(array(obs_err)/array(test_score)))
    print("avg accuracy ="+repr(avg_acc))

# def cross_validation(cross_validation_frame,score):
