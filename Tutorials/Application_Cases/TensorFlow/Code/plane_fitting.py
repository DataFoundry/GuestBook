# Step 1����������Ҫ�Ŀ�
import tensorflow as tf
import numpy as np


# Step 2��ʹ�� NumPy ���ɼ����ݣ�phony data��, �ܹ� 100 ����
x_data = np.float32(np.random.rand(2, 100)) # �������
y_data = np.dot([0.100, 0.200], x_data) + 0.300


# Step 3������һ������ģ��
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b


# Step 4����С������
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)


# Step 5����ʼ������
init = tf.initialize_all_variables()


# Step 6������ͼ��graph��
sess = tf.Session()
sess.run(init)

# Step 7�����ƽ��
for step in xrange(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print step, sess.run(W), sess.run(b)

# �õ������Ͻ�� W: [[0.100  0.200]], b: [0.300]