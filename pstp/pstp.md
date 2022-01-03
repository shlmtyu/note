# ML predict TSEC weighted index from Macroeconomics view with Long short-term memory (LSTM) units of a recurrent neural network (RNN).
# 以總體經濟角度來預測台灣股票加權指數之LSTM RNN 機器學習。  

## 資料取自1997/07/02~2018/07/31約21年的台灣加權指數，和其他各國的股票加權指數，與各國匯率值，並台灣貨幣總計數和利率...等值， 台灣數據資料若為空值以刪除處理，他國資料若為空值用前一日值帶入，讓數據處於無變動性，但仍可維持樣本數； 匯率轉為以台幣計價(一台幣可兌換多少外幣)，數字越高代表台幣越強勢，可能有較多現金流進入； 其他數值(台灣貨幣總計數和利率)只取得月平均，以同月同值帶入。  

## 因資料具時間序列特性，故選擇以LSTM RNN來建模。 

## Closed economy model 封閉經濟模型  

Model assumption:$ Y= W_x +B $  

Predicted model:hat_y=hat_wX+hat_b
Good model : Min [(hat_y-Y)/N]-->0
Input features X:tw_Open,tw_High,tw_Low,tw_Close,tw_Adj_Close
Output label Y:next_day_High
Long Short-Term Memory cell (LSTM) = 2 layers
Neurons = 10 unit

## Small open economy model 小型開放經濟  

## Open economy model 開放經濟
## Market Exchange Rates 匯率市場
## Monetary Economy 貨幣市場
