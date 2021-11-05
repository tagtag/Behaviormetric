# TPUモデルへの変換
import tensorflow as tf
import os
tpu_model = tf.contrib.tpu.keras_to_tpu_model(
    model,
    strategy=tf.contrib.tpu.TPUDistributionStrategy(
        tf.contrib.cluster_resolver.TPUClusterResolver(tpu='grpc://' + os.environ['COLAB_TPU_ADDR'])
    )
)
tpu_model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['acc'])
history = tpu_model.fit(train_images, train_labels, batch_size=128,
    epochs=20, validation_split=0.1)