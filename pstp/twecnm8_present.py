# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:21:05 2019

@author: Joyce
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read part of column
all_num=18
#RNN_LSTM OUTPUT NUMBER
output_size=1
#RNN_LSTM INPUT NUMBERS
input_size=all_num-output_size
#RNN_LSTM ONE HIDE LAYER NEURONS NUMBERS
rnn_unit=17
#RNN_LSTM HIDE LAYER NUMBERS
hide_layers=2

batch_size=60
time_step=20
learning_rate=0.0001

train_end=3000
test_begain=train_end+1

#open and read original data
original_data=open('ml_data_all_rate.csv')
#[row:M,column:N]
read_original_data=pd.read_csv(original_data)
#select column:1~all_num
select_data=read_original_data.iloc[:,:all_num].values
#select_data[:1]

#Receive training data
def get_train_data(batch_size,time_step,train_end):
    intercept_data=select_data[0:train_end]
    #normalize
    normalize_train_data=(intercept_data-np.mean(intercept_data,axis=0))/np.std(intercept_data,axis=0)
    batch_index=[]
    train_x,train_y=[],[]
    for i in range(len(normalize_train_data)-time_step):
        if i % batch_size==0:
            batch_index.append(i)
        x=normalize_train_data[i:i+time_step,output_size:all_num]
        #add dimension
        y=normalize_train_data[i:i+time_step,0,np.newaxis]
        train_x.append(x.tolist())
        train_y.append(y.tolist())
    batch_index.append(len(normalize_train_data)-time_step)
    return batch_index,train_x,train_y
#Receive testing data
def get_test_data(time_step,test_begain):
    intercept_data=select_data[test_begain:]
    mean_test_data=np.mean(intercept_data,axis=0)
    std_test_data=np.std(intercept_data,axis=0)
    normalize_test_data=(intercept_data-mean_test_data)/std_test_data
    sample_size=(len(normalize_test_data)-time_step-1)//time_step
    test_x,test_y=[],[]
    for i in range(sample_size):
        x=normalize_test_data[i*time_step:(i+1)*time_step,output_size:all_num]
        y=normalize_test_data[i*time_step:(i+1)*time_step,0]
        test_x.append(x.tolist())
        test_y.extend(y)
    x=normalize_test_data[(i+1)*time_step:,output_size:all_num]
    y=normalize_test_data[(i+1)*time_step:,0]
    test_x.append(x.tolist())
    test_y.extend(y.tolist())
    return mean_test_data,std_test_data,test_x,test_y       
    
#LSTM model
weights={
        'in':tf.Variable(tf.random_normal([input_size,rnn_unit])),
        'out':tf.Variable(tf.random_normal([rnn_unit,output_size]))
        }
biases={
        'in':tf.Variable(tf.constant(0.1,shape=[rnn_unit,])),
        'out':tf.Variable(tf.constant(0.1,shape=[output_size,]))
        }
keep_prob=tf.placeholder(tf.float32,name='keep_prob')

def lstmcell():
    basic_lstm=tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    dropout=tf.nn.rnn_cell.DropoutWrapper(basic_lstm,output_keep_prob=keep_prob)
    return basic_lstm

def rnn_lstm(X):
    #[,time_step,input_size],3-D
    lengh_num=tf.shape(X)[0]
    #[time_step]
    time_step=tf.shape(X)[1]
    #[input_size,rnn_unit],2-D
    weight_in=weights['in']
    #[rnn_unit,]
    bias_in=biases['in']
    #[,input_size],2-D
    input_features=tf.reshape(X,[-1,input_size])
    #input value wx+b
    #[,input_size]*[input_size,rnn_unit]+[rnn_unit,]=[,rnn_unit]
    input_rnn=tf.matmul(input_features,weight_in)+bias_in
    #[,time_step,rnn_unit]
    input_rnn=tf.reshape(input_rnn,[-1,time_step,rnn_unit])
    cell=tf.nn.rnn_cell.MultiRNNCell([lstmcell() for i in range(hide_layers)])
    initialize_state=cell.zero_state(lengh_num,dtype=tf.float32)
    output_rnn,last_states=tf.nn.dynamic_rnn(cell,input_rnn,initial_state=initialize_state,dtype=tf.float32)
    #[,rnn_unit]
    output=tf.reshape(output_rnn,[-1,rnn_unit])
    #[rnn_unit,output_siz],2-D
    weight_out=weights['out']
    #[output_size,]
    bias_out=biases['out']
    #[,rnn_unit]*[rnn_unit,output_siz]+[output_size,]=[,output_size]
    predict_label=tf.matmul(output,weight_out)+bias_out
    return predict_label,last_states

#train lstm model
def train_lstm(batch_size,time_step,train_end,learning_rate):
    features_x=tf.placeholder(tf.float32,shape=[None,time_step,input_size])
    label_y=tf.placeholder(tf.float32,shape=[None,time_step,output_size])
    batch_index,train_x,train_y=get_train_data(batch_size,time_step,train_end)
    with tf.variable_scope("layer_lstm"):
        predict_label, _ =rnn_lstm(features_x)
    loss=tf.reduce_mean(tf.square(tf.reshape(predict_label,[-1])-tf.reshape(label_y,[-1])))    
    train_op=tf.train.AdamOptimizer(learning_rate).minimize(loss)
    #save model number
    saver=tf.train.Saver(tf.global_variables(),max_to_keep=0)
    loss_array=[]
    iteration_array=[]
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        #iteration
        for i in range(400):
            for step in range(len(batch_index)-1):              
                _,loss_=sess.run([train_op,loss],feed_dict={features_x:train_x[batch_index[step]:batch_index[step+1]],
                                                            label_y:train_y[batch_index[step]:batch_index[step+1]],
                                                            keep_prob:0.5})   
            if i % 40 ==0:
                print("Number of iterations:",i,"loss",loss_)
            loss_array.append(loss_)
            iteration_array.append(i)
        plt.plot(iteration_array,loss_array,color='#054E9F')
        plt.title("Plot of Model Loss on Training Datasets")
        plt.xlabel("Iteration")
        plt.ylabel("Loss Value")
        plt.show()
        print("Loss maxnum=",np.max(loss_array),"; Loss minmun=",np.min(loss_array))
        print("Model save:", saver.save(sess,'model\\model.ckpt'))

#test LSTM model       
def test_lstm(time_step,train_begain,learning_rate):
    features=tf.placeholder(tf.float32,shape=[None,time_step,input_size])
    mean_test_data,std_test_data,test_x,test_y=get_test_data(time_step,train_begain)
    with tf.variable_scope("layer_lstm",reuse=tf.AUTO_REUSE):
        predict_label, _ =rnn_lstm(features)
    saver=tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        #restore parameter
        module_file=tf.train.latest_checkpoint('model')
        saver.restore(sess,module_file)
        test_predict=[]
        for step in range(len(test_x)-1):
            prob=sess.run(predict_label,
                          feed_dict={features:[test_x[step]],
                                     keep_prob:1})
            predict=prob.reshape((-1))
            test_predict.extend(predict)
        test_y=np.array(test_y)*std_test_data[0]+mean_test_data[0]
        test_predict=np.array(test_predict)*std_test_data[0]+mean_test_data[0]
        deviation=np.average(np.abs(test_predict-test_y[:len(test_predict)])/test_y[:len(test_predict)])
        print("The deviation of this predict:",deviation)
        plt.figure()        
        plot_predicted, = plt.plot(test_predict, label='Predicted',color='b')
        plot_test, = plt.plot(test_y, label='Real_Label',color='r')
        plt.legend([plot_predicted, plot_test],['Predicted', 'Real_Label'])
        plt.title("Label and Prediction Curver")
        plt.xlabel("Iteration")
        plt.ylabel("Taiwan index")
        plt.show()
    return       

train_lstm(batch_size,time_step,train_end,learning_rate)
test_lstm(time_step,test_begain,learning_rate)
    