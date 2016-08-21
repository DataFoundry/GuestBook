# Step 1����������Ҫ�Ŀ�
import tensorflow as tf
import numpy as np

# Step 2��ʹ�� Numpy ���ɼ����ݣ�phony data�����ܹ�100 ���㣬y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32) 
y_data = x_data * 0.1 + 0.3

# Step 3������һ������ģ��
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Step 4����С������
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Step 5����ʼ������
init = tf.initialize_all_variables()

# Step 6������ͼ
sess = tf.Session()
sess.run(init)

# Step 7�����ֱ��
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

# �õ������Ͻ�� W: [0.1], b: [0.3]