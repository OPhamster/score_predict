from numpy import array, mean
import statsmodels.api as sm
from pandas import merge


def train(train_frame, author_frame, domain_frame, subreddit_frame):
    train_frame = train_frame.merge(author_frame, how="inner", on="author")
    train_frame = train_frame.merge(domain_frame, how="inner", on="domain")
    train_frame = sm.add_constant(train_frame)
    train_frame, cross_validation_frame = train_test_splits(
        train_data, test_size=0.4)
    cross_validation_frame, test_frame = train_test_splits(
        cross_validation_frame, test_size=0.25)
    train_score = train_frame["score"]
    train_frame.drop(axis=1, ["score"], inplace=True)
    model = sm.OLS(train_score, train_frame)
    result_model = model.fit_regularized(method="coord_descent", maxiter=500, alpha=0.03, /
        start_params=None, cnvrg_tol=1e-08)
    result_model.summary()
    return (result_model, cross_validation_frame, test_frame)


def test(test_frame):
    # test_score = test_frame["score"]
    # this test frame has no score field coz surprise it doesn't have one
    test_frame.drop(axis=1, ["score"], inplace=True)
    test_result = self.trained_model.predict(test_frame)
    print("predicted score = " + repr(test_result))
    # obs_err = abs(self.trained_model.predict(test_frame) - test_score)
    # mean accuracy coz we need to generalize this model - this could have
    # ramifications - look into it later
    # avg_error = mean(array(obs_err) / array(test_score)))
    # print("average error =" + repr(avg_error))


def cross_validation(cross_validation_frame):
    cross_validation_score = cross_validation_frame["score"]
    cross_validation_frame.drop(axis=1, ["score"], inplace=True)
    obs_err = abs(trained_model.predict(
        cross_validation_frame) - cross_validation_score)
    # mean accuracy coz we need to generalize this model - this could have
    # ramifications - look into it later
    avg_error = mean(array(obs_err) / array(cross_validation_score)))
    print("average error =" + repr(avg_error))
