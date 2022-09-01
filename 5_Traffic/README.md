1)  One Convolutional Layer leraning 32 filters and 3x3 Kernel \
    One Pooling Layer (2x2) \
    One hidden Layer with size 128 \
    Dropout 0.0 \

    -> Good accuracy but danger of overfitting as dropout = 0.0
```
    Epoch 1/10 
    500/500 [==============================] - 8s 15ms/step - loss: 5.0387 - accuracy: 0.5691
    Epoch 2/10
    500/500 [==============================] - 8s 15ms/step - loss: 0.5175 - accuracy: 0.8698
    Epoch 3/10
    500/500 [==============================] - 7s 14ms/step - loss: 0.2969 - accuracy: 0.9243
    Epoch 4/10
    500/500 [==============================] - 7s 15ms/step - loss: 0.2091 - accuracy: 0.9453
    Epoch 5/10
    500/500 [==============================] - 7s 14ms/step - loss: 0.2045 - accuracy: 0.9511
    Epoch 6/10
    500/500 [==============================] - 7s 15ms/step - loss: 0.1590 - accuracy: 0.9623
    Epoch 7/10
    500/500 [==============================] - 8s 16ms/step - loss: 0.1624 - accuracy: 0.9626
    Epoch 8/10
    500/500 [==============================] - 7s 15ms/step - loss: 0.1794 - accuracy: 0.9600
    Epoch 9/10
    500/500 [==============================] - 7s 14ms/step - loss: 0.1381 - accuracy: 0.9690
    Epoch 10/10
    500/500 [==============================] - 7s 15ms/step - loss: 0.1119 - accuracy: 0.9743
    333/333 - 2s - loss: 0.4420 - accuracy: 0.9430 - 2s/epoch - 5ms/step
```
2) Change dropout to 0.3
    -> loss and accuracy got worse but better to prevent overfitting
```
    Epoch 1/10
    500/500 [==============================] - 9s 16ms/step - loss: 5.2094 - accuracy: 0.0563
    Epoch 2/10
    500/500 [==============================] - 8s 16ms/step - loss: 3.5890 - accuracy: 0.0591
    Epoch 3/10
    500/500 [==============================] - 9s 17ms/step - loss: 3.5393 - accuracy: 0.0587
    Epoch 4/10
    500/500 [==============================] - 8s 16ms/step - loss: 3.5368 - accuracy: 0.0592
    Epoch 5/10
    500/500 [==============================] - 9s 18ms/step - loss: 3.5053 - accuracy: 0.0591
    Epoch 6/10
    500/500 [==============================] - 10s 21ms/step - loss: 3.5007 - accuracy: 0.0591
    Epoch 7/10
    500/500 [==============================] - 11s 21ms/step - loss: 3.4977 - accuracy: 0.0591
    Epoch 8/10
    500/500 [==============================] - 10s 19ms/step - loss: 3.4965 - accuracy: 0.0591
    Epoch 9/10
    500/500 [==============================] - 8s 17ms/step - loss: 3.4958 - accuracy: 0.0591
    Epoch 10/10
    500/500 [==============================] - 8s 16ms/step - loss: 3.4954 - accuracy: 0.0591
    333/333 - 2s - loss: 3.5023 - accuracy: 0.0521 - 2s/epoch - 5ms/step
```

3) Increase number of filters in Convolutional Layer to 64
    -> less loss and more accuracy as more filters will be leraned by the model
```
    Epoch 1/10
    500/500 [==============================] - 24s 47ms/step - loss: 5.9643 - accuracy: 0.0840
    Epoch 2/10
    500/500 [==============================] - 260s 521ms/step - loss: 3.1536 - accuracy: 0.1317
    Epoch 3/10
    500/500 [==============================] - 21s 42ms/step - loss: 3.0521 - accuracy: 0.1483
    Epoch 4/10
    500/500 [==============================] - 14s 28ms/step - loss: 2.8810 - accuracy: 0.1956
    Epoch 5/10
    500/500 [==============================] - 14s 27ms/step - loss: 2.6951 - accuracy: 0.2255
    Epoch 6/10
    500/500 [==============================] - 13s 27ms/step - loss: 2.4096 - accuracy: 0.3225
    Epoch 7/10
    500/500 [==============================] - 13s 26ms/step - loss: 2.1932 - accuracy: 0.3720
    Epoch 8/10
    500/500 [==============================] - 15s 29ms/step - loss: 2.0449 - accuracy: 0.3972
    Epoch 9/10
    500/500 [==============================] - 23s 46ms/step - loss: 1.9119 - accuracy: 0.4433
    Epoch 10/10
    500/500 [==============================] - 23s 45ms/step - loss: 1.7867 - accuracy: 0.4698
    333/333 - 7s - loss: 1.3050 - accuracy: 0.6144 - 7s/epoch - 21ms/step
```

4) pool size to 3x3
    -> increasing the size of pooling causes a decrease in accuracy and increase of loss
    -> better 2x2 pooling
```
    Epoch 1/10
    500/500 [==============================] - 12s 21ms/step - loss: 5.3412 - accuracy: 0.0629
    Epoch 2/10
    500/500 [==============================] - 10s 20ms/step - loss: 3.4577 - accuracy: 0.0800
    Epoch 3/10
    500/500 [==============================] - 10s 20ms/step - loss: 3.0872 - accuracy: 0.1522
    Epoch 4/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.8044 - accuracy: 0.2035
    Epoch 5/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.5238 - accuracy: 0.2470
    Epoch 6/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.3278 - accuracy: 0.2846
    Epoch 7/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.2237 - accuracy: 0.2991
    Epoch 8/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.1805 - accuracy: 0.3255
    Epoch 9/10
    500/500 [==============================] - 10s 21ms/step - loss: 2.1247 - accuracy: 0.3454
    Epoch 10/10
    500/500 [==============================] - 17s 35ms/step - loss: 2.0424 - accuracy: 0.3766
    333/333 - 4s - loss: 1.4052 - accuracy: 0.5594 - 4s/epoch - 12ms/step
```
5) pooling size : 2x2, add second convolutional and pooling layer (first layer 32 filters, second 64 filters)
    -> first layer: learn 32 filters and pooling reduces dimension
    -> second layer: learn 64 filters and reduce dimension again
    -> multiple convolutional layers -> extract more high-level features of input images
    -> accuracy clearly increased and loss decreased 

```
    Epoch 1/10
    500/500 [==============================] - 13s 22ms/step - loss: 3.2451 - accuracy: 0.2539
    Epoch 2/10
    500/500 [==============================] - 11s 22ms/step - loss: 1.5888 - accuracy: 0.5233
    Epoch 3/10
    500/500 [==============================] - 12s 23ms/step - loss: 0.9992 - accuracy: 0.6842
    Epoch 4/10
    500/500 [==============================] - 12s 25ms/step - loss: 0.7178 - accuracy: 0.7745
    Epoch 5/10
    500/500 [==============================] - 19s 39ms/step - loss: 0.5293 - accuracy: 0.8331
    Epoch 6/10
    500/500 [==============================] - 20s 39ms/step - loss: 0.4334 - accuracy: 0.8657
    Epoch 7/10
    500/500 [==============================] - 20s 41ms/step - loss: 0.3433 - accuracy: 0.8962
    Epoch 8/10
    500/500 [==============================] - 20s 40ms/step - loss: 0.3082 - accuracy: 0.9102
    Epoch 9/10
    500/500 [==============================] - 20s 41ms/step - loss: 0.2553 - accuracy: 0.9230
    Epoch 10/10
    500/500 [==============================] - 20s 40ms/step - loss: 0.2174 - accuracy: 0.9356
    333/333 - 5s - loss: 0.1010 - accuracy: 0.9745 - 5s/epoch - 14ms/step
```
6) reduce size of hidden layer to 64
    -> clearly decrease of accuracy and increase of loss
    -> almost no improvement during the epoches
```
    Epoch 1/10
    500/500 [==============================] - 12s 21ms/step - loss: 3.8961 - accuracy: 0.0570
    Epoch 2/10
    500/500 [==============================] - 11s 21ms/step - loss: 3.5846 - accuracy: 0.0572
    Epoch 3/10
    500/500 [==============================] - 10s 20ms/step - loss: 3.5351 - accuracy: 0.0565
    Epoch 4/10
    500/500 [==============================] - 12s 24ms/step - loss: 3.5123 - accuracy: 0.0557
    Epoch 5/10
    500/500 [==============================] - 10s 20ms/step - loss: 3.5017 - accuracy: 0.0568
    Epoch 6/10
    500/500 [==============================] - 10s 21ms/step - loss: 3.4976 - accuracy: 0.0581
    Epoch 7/10
    500/500 [==============================] - 10s 20ms/step - loss: 3.4942 - accuracy: 0.0581
    Epoch 8/10
    500/500 [==============================] - 11s 22ms/step - loss: 3.4931 - accuracy: 0.0570
    Epoch 9/10
    500/500 [==============================] - 16s 32ms/step - loss: 3.4925 - accuracy: 0.0569
    Epoch 10/10
    500/500 [==============================] - 18s 37ms/step - loss: 3.4921 - accuracy: 0.0581
    333/333 - 5s - loss: 3.5073 - accuracy: 0.0536 - 5s/epoch - 14ms/step
```

7) add second hidden layer with size 128 -> two hidden layers first: 64, second 128
    -> accuracy and loss are better than without the second layer
```
    Epoch 1/10
    500/500 [==============================] - 611s 1s/step - loss: 3.8266 - accuracy: 0.0735
    Epoch 2/10
    500/500 [==============================] - 11s 23ms/step - loss: 3.3678 - accuracy: 0.0965
    Epoch 3/10
    500/500 [==============================] - 12s 25ms/step - loss: 3.1190 - accuracy: 0.1573
    Epoch 4/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.7603 - accuracy: 0.2382
    Epoch 5/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.4144 - accuracy: 0.3013
    Epoch 6/10
    500/500 [==============================] - 10s 20ms/step - loss: 2.0641 - accuracy: 0.3722
    Epoch 7/10
    500/500 [==============================] - 11s 23ms/step - loss: 1.7482 - accuracy: 0.4546
    Epoch 8/10
    500/500 [==============================] - 12s 24ms/step - loss: 1.4272 - accuracy: 0.5462
    Epoch 9/10
    500/500 [==============================] - 10s 20ms/step - loss: 1.2042 - accuracy: 0.6204
    Epoch 10/10
    500/500 [==============================] - 11s 23ms/step - loss: 1.0824 - accuracy: 0.6659
    333/333 - 3s - loss: 0.7265 - accuracy: 0.7930 - 3s/epoch - 8ms/step
```

8) set size of first hidden layer also to 128
    -> better accuracy and loss but almost like with one hidden layer with size 128
    -> remove second hidden layer
```
    Epoch 1/10
    500/500 [==============================] - 13s 24ms/step - loss: 3.1525 - accuracy: 0.2626
    Epoch 2/10
    500/500 [==============================] - 12s 24ms/step - loss: 1.4423 - accuracy: 0.5678
    Epoch 3/10
    500/500 [==============================] - 13s 27ms/step - loss: 0.9188 - accuracy: 0.7179
    Epoch 4/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.6479 - accuracy: 0.8046
    Epoch 5/10
    500/500 [==============================] - 12s 24ms/step - loss: 0.5021 - accuracy: 0.8539
    Epoch 6/10
    500/500 [==============================] - 12s 24ms/step - loss: 0.4608 - accuracy: 0.8652
    Epoch 7/10
    500/500 [==============================] - 12s 23ms/step - loss: 0.3452 - accuracy: 0.8980
    Epoch 8/10
    500/500 [==============================] - 12s 24ms/step - loss: 0.3484 - accuracy: 0.9012
    Epoch 9/10
    500/500 [==============================] - 12s 24ms/step - loss: 0.2876 - accuracy: 0.9178
    Epoch 10/10
    500/500 [==============================] - 12s 24ms/step - loss: 0.2801 - accuracy: 0.9228
    333/333 - 3s - loss: 0.1418 - accuracy: 0.9635 - 3s/epoch - 8ms/step
```

9) increase size of hiden layer to 256
    -> no improvement to one hidden layer with size 128
```
    Epoch 1/10
    500/500 [==============================] - 15s 28ms/step - loss: 2.4806 - accuracy: 0.5428
    Epoch 2/10
    500/500 [==============================] - 13s 27ms/step - loss: 0.6056 - accuracy: 0.8268
    Epoch 3/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.3907 - accuracy: 0.8901
    Epoch 4/10
    500/500 [==============================] - 15s 29ms/step - loss: 0.2837 - accuracy: 0.9212
    Epoch 5/10
    500/500 [==============================] - 13s 27ms/step - loss: 0.2166 - accuracy: 0.9391
    Epoch 6/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.2163 - accuracy: 0.9429
    Epoch 7/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.1892 - accuracy: 0.9499
    Epoch 8/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.1852 - accuracy: 0.9501
    Epoch 9/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.1634 - accuracy: 0.9581
    Epoch 10/10
    500/500 [==============================] - 13s 26ms/step - loss: 0.1901 - accuracy: 0.9516
    333/333 - 3s - loss: 0.1755 - accuracy: 0.9636 - 3s/epoch - 8ms/step
```




