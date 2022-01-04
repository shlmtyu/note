# ML predict TSEC weighted index from Macroeconomics view with Long short-term memory (LSTM) units of a recurrent neural network (RNN).
# 以總體經濟角度來預測台灣股票加權指數之LSTM RNN 機器學習。  

### 資料取自1997/07/02~2018/07/31約21年的台灣加權指數，和其他各國的股票加權指數，與各國匯率值，並台灣貨幣總計數和利率...等值， 台灣數據資料若為空值以刪除處理，他國資料若為空值用前一日值帶入，讓數據處於無變動性，但仍可維持樣本數； 匯率轉為以台幣計價(一台幣可兌換多少外幣)，數字越高代表台幣越強勢，可能有較多現金流進入； 其他數值(台灣貨幣總計數和利率)只取得月平均，以同月同值帶入。  

#### 因資料具時間序列特性，故選擇以LSTM RNN來建模。 

## § Closed economy model 封閉經濟模型  

### Model assumption 模型假設：Y= WX +B  

### Predicted model預測型：y= wX+b  

### Good model 預測衡量：Min [(y-Y)/N]-->0  

### Input features X 輸入參數：tw_Open 開盤價,tw_High 最高價,tw_Low 最低價,tw_Close 收盤價,tw_Adj_Close 調整收盤價  

### Output label Y 輸出值：next_day_High 隔天最高價  

### Long Short-Term Memory cell (LSTM) = 2 layers  

### Neurons = 10 unit  
### > Train model 訓練模型  
#### >　Result結果:Loss maxnum= 0.03219068 ; Loss minmun= 0.0040088445
##### ![Alt text](/pstp/jpg/train_n5_u10_l2_b60_s20_lr0001_i200_p5.png)

### > Test model
#### >　Result結果:Loss maxnum= 0.03219068 ; Loss minmun= 0.0040088445
##### ![Alt text](/pstp/jpg/test_n5_u10_l2_b60_s20_lr0001_i200_p5.png)

### Conclusion結論:
#### 設計構想:利用各國股票加權指數(設計似封閉和開放經濟體系)，各國匯率和貨幣相關參數(貨幣市場)，來建立模型，更了解LSTM RNN的運作情形， 並依其關連與影響度，可再進一步依不同產業分析，建立似供應鏈的流動結構模型。
#### Learning rate小讓loss曲線較平順的下降，但training較緩慢，訓練次數增加loss值可以在下降，training時設dropout=.5降低overfitting問題。 模型驗證偏差程度約趨近於0表示模型越好。

## § Small open economy model 小型開放經濟  
### Model assumption 模型假設：Y= WX +B  

### Predicted model預測型：y= wX+b  

### Good model 預測衡量：Min [(y-Y)/N]-->0  

### Input features X 輸入參數：tw_Open 開盤價,tw_High 最高價,tw_Low 最低價,tw_Close 收盤價,tw_Adj_Close 調整收盤價,  
###                           add Japan's stock index and China's  增加日本和中國的股價指數

### Output label Y 輸出值：next_day_High 隔天最高價  

### Long Short-Term Memory cell (LSTM) = 2 layers  

### Neurons = 16 unit  
### > Train model 訓練模型  
#### >　Result結果:maxnum= 0.19225891 ; Loss minmun= 0.004171721
##### ![Alt text](/pstp/jpg/train_n8_u16_l2_b60_s20_lr0001_i200_p5.png)

### > Test model
#### >　Result結果:The deviation of this predict: 0.011017222390028763
##### ![Alt text](/pstp/jpg/test_n8_u16_l2_b60_s20_lr0001_i200_p5.png)

### Conclusion結論:
#### 加入日本和中國的重要股票加權指數，增加鄰近重要國家對台灣股票投資的影響， Features從5個增為8個，LSTM cell內的神經元從10增為16，模型變複雜可能變異量增加，易有overfitting的問題， 但因bias也變大，可能樣本數較少，致underfitting的問題。

## § Open economy model 開放經濟  
### Model assumption 模型假設：Y= WX +B  

### Predicted model預測型：y= wX+b  

### Good model 預測衡量：Min [(y-Y)/N]-->0  

### Input features X 輸入參數：tw_Open 開盤價,tw_High 最高價,tw_Low 最低價,tw_Close 收盤價,tw_Adj_Close 調整收盤價  
###                           add Countries's stock index 加入亞洲、歐洲和美洲...等國家的重要股票加權指數

### Output label Y 輸出值：next_day_High 隔天最高價  

### Long Short-Term Memory cell (LSTM) = 2 layers  

### Neurons = 40 unit  
### > Train model 訓練模型  
#### >　Result結果:maxnum= 0.23616102 ; Loss minmun= 0.0024677394
##### ![Alt text](/pstp/jpg/train_n20_u40_l2_b60_s20_lr0001_i400_p5.png)

### > Test model
#### >　Result結果:The deviation of this predict: 0.021472024183719053
##### ![Alt text](/pstp/jpg/test_n20_u40_l2_b60_s20_lr0001_i400_p5.png)

### Conclusion結論:
#### 加入亞洲、歐洲和美洲...等國家的重要股票加權指數，對台灣股票投資的影響， Features從8個增為20個，LSTM cell內的神經元從16增為40，增加訓練次數loss值降低，但模型便更複雜產生overfitting現象。

## § Market Exchange Rates 匯率市場  
### Model assumption 模型假設：Y= WX +B  

### Predicted model預測型：y= wX+b  

### Good model 預測衡量：Min [(y-Y)/N]-->0  

### Input features X 輸入參數：tw_Open 開盤價,tw_High 最高價,tw_Low 最低價,tw_Close 收盤價,tw_Adj_Close 調整收盤價  
###                           add Countries's Market Exchange Rates 加入各國的匯率

### Output label Y 輸出值：next_day_High 隔天最高價  

### Long Short-Term Memory cell (LSTM) = 2 layers  

### Neurons = 21 unit  
### > Train model 訓練模型  
#### >　Result結果:maxnum= 1.2233338 ; Loss minmun= 0.00209085
##### ![Alt text](/pstp/jpg/train_n21_u21_l2_b60_s20_lr0001_i400_p5_er.png)

### > Test model
#### >　Result結果:The deviation of this predict: 0.05328915600824949
##### ![Alt text](/pstp/jpg/test_n21_u21_l2_b60_s20_lr0001_i400_p5_er.png)

### Conclusion結論:
#### 加入亞洲、歐洲和美洲...等國家的匯率，對台灣股票投資的影響， Features為21個，LSTM cell內的神經元從為21，loss值差不多小降而已，但預測偏差就大很多。

### > 調整
#### Features為21個，LSTM cell內的神經元減為20，隱藏層增為3，模型複雜度、變異程度增，loss值略增，但預測水準有改善。
### >> Train model 訓練模型  
#### >>　Result結果:maxnum= 0.08592842 ; Loss minmun= 0.0031158105
##### ![Alt text](/pstp/jpg/train_n21_u20_l3_b60_s20_lr0001_i400_p5_er.png)

### > Test model
#### >　Result結果:The deviation of this predict: 0.05328915600824949
##### ![Alt text](/pstp/jpg/test_n21_u20_l3_b60_s20_lr0001_i400_p5_er.png)


## § Monetary Economy 貨幣市場  
### Model assumption 模型假設：Y= WX +B  

### Predicted model預測型：y= wX+b  

### Good model 預測衡量：Min [(y-Y)/N]-->0  

### Input features X 輸入參數：tw_Open 開盤價,tw_High 最高價,tw_Low 最低價,tw_Close 收盤價,tw_Adj_Close 調整收盤價  
###                           add rate and M1A、M1B、M2 增加貨幣總計數

### Output label Y 輸出值：next_day_High 隔天最高價  

### Long Short-Term Memory cell (LSTM) = 2 layers  

### Neurons = 17 unit  
### > Train model 訓練模型  
#### >　Result結果:maxnum= 0.39326754 ; Loss minmun= 0.0075723063
##### ![Alt text](/pstp/jpg/train_n17_u17_l2_b80_s40_lr0001_i400_p5_r.png)

### > Test model
#### >　Result結果:The deviation of this predict: 0.040529010967603876
##### ![Alt text](/pstp/jpg/test_n17_u17_l2_b80_s40_lr0001_i400_p5_r.png)

### Conclusion結論:
#### 加入貨幣總計數M1A、M1B、M2和利率...等，對台灣股票投資的影響， Features為17個，LSTM cell內的神經元從為17，loss值與偏差程度跟預期的一樣不會太好，因為利率和貨幣總計數...等值並沒有收集到完整的數據。
#### 總資料量大約五千多筆而已，再分training data和test data，其實數據量真的太少， 但透過實做學習，可以更深刻的了解LSTM RNN的運作，參數調整對Model預測的影響， 對LSTM當參數或隱藏層神經元數量增加，易有overfitting的問題，近幾年有相關的論文研究，可再進一步了解。

