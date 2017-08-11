
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(scores):
    """

    :param scores: scores = np.dot(features, weights)
    :return:
    """

    ##########################################################################
    # TODO:
    # hint:
    #
    ##########################################################################


    ##########################################################################
    #                               END OF YOUR CODE
    ##########################################################################


def softmax(scores):
    """

    :param scores:
    :return:
    """
    ##########################################################################
    # TODO:
    # hint:
    # np.exp
    #
    ##########################################################################


    ##########################################################################
    #                               END OF YOUR CODE
    ##########################################################################

def cost_function(features, target, weights):
    """
    :param features:
    :param target:
    :param weights:
    :return:
    """
    scores = np.dot(features, weights)

    ##########################################################################
    # TODO:
    # hint:
    # np.exp, np.log, np.sum
    #
    ##########################################################################


    ##########################################################################
    #                               END OF YOUR CODE
    ##########################################################################

def gradient_descent(features, output_error_signal):
    """
    :param features:
    :param output_error_signal:
    :return:
    """
    ##########################################################################
    # TODO:
    # hint: partial derivatives of cost function is error * features
    ##########################################################################


    ##########################################################################
    #                               END OF YOUR CODE
    ##########################################################################




def logistic_regression(features, target, num_steps, learning_rate, add_intercept = False):
    """
    :param features:
    :param target:
    :param num_steps:
    :param learning_rate:
    :param add_intercept:
    :return:
    """
    if add_intercept:
        intercept = np.ones((features.shape[0], 1))
        features = np.hstack((intercept, features))

    weights = np.zeros(features.shape[1])

    for step in xrange(num_steps):

        scores = np.dot(features, weights)
        predictions = sigmoid(scores)
        output_error_signal = target - predictions
        gradient_descent(features, output_error_signal)
    return weights


def create_features():
    """
    draw random samples from gaussian in higher dimensions (if only 1d is called normal, multi-d called multinormal/multivaraite normal)
    mean, covariance, size
    :return:
    """
    np.random.seed(12)
    num_observations = 10

    x1 = np.random.multivariate_normal([0, 0], [[1, .75],[.75, 1]], num_observations)
    x2 = np.random.multivariate_normal([1, 4], [[1, .75],[.75, 1]], num_observations)

    simulated_separableish_features = np.vstack((x1, x2)).astype(np.float32)
    simulated_labels = np.hstack((np.zeros(num_observations),
                                  np.ones(num_observations)))

    # print simulated_separableish_features[:, 0]

    return (simulated_separableish_features, simulated_labels)


def matplotlib_print_data(simulated_separableish_features, simulated_labels):
    plt.figure(figsize=(12,8))

    plt.scatter(simulated_separableish_features[:, 0], simulated_separableish_features[:, 1],
                c = simulated_labels, alpha = 0.4) # alpha seems to be color darkness
    plt.draw()
    plt.show()


def main():
    (simulated_separableish_features, simulated_labels) = create_features()
    # matplotlib_print_data()

    updated_weights = logistic_regression(simulated_separableish_features, simulated_labels,
                              num_steps = 100, learning_rate = 0.001, add_intercept=True)



if __name__ == '__main__':
    main()