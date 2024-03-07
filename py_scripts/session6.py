from sklearn.decomposition import PCA
import matplotlib as plt


def make_plot(words, model):

    # an empty list for vectors
    X = []
    # get vectors for subset of words
    for word in words:
        X.append(model[word])


    # Use PCA for dimensionality reduction to 2D
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    # create a scatter plot of the projection
    plot = plt.scatter(result[:, 0], result[:, 1])

    # for each word in the list of words
    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))

    plt.title("PCA plot")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")

    return plot
