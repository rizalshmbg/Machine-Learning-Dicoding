# =============================================================================
# PROBLEM C2
#
# Create a classifier for the MNIST Handwritten digit dataset.
# The test will expect it to classify 10 classes.
#
# Don't use lambda layers in your model.
#
# Desired accuracy AND validation_accuracy > 91%
# =============================================================================

import tensorflow as tf


def solution_C2():
    mnist = tf.keras.datasets.mnist

    # YOUR CODE HERE

    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    if __name__ == '__main__':
        model = solution_C2()
        model.save("model_C2.h5")