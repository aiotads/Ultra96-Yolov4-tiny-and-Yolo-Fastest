import tensorflow as tf

def parser(example_proto):
    image_feature_description = {
        'image' : tf.io.FixedLenFeature([], tf.string),
        'height': tf.io.FixedLenFeature([], tf.int64),
        'width' : tf.io.FixedLenFeature([], tf.int64),
        'chans' : tf.io.FixedLenFeature([], tf.int64),
        'label' : tf.io.RaggedFeature(dtype=tf.int64)
    }
    serialized_example = tf.io.parse_single_example(example_proto, image_feature_description)
    label = tf.cast(serialized_example['label'], tf.int32)
    image = tf.io.decode_image(serialized_example['image'], channels=3)
    h = tf.cast(serialized_example['height'], tf.int32)
    w = tf.cast(serialized_example['width'], tf.int32)
    c = tf.cast(serialized_example['chans'], tf.int32)
    return image, label