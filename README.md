# GradientDescent
參考[Andrew Ng.](http://blogger.gtwang.org/2013/07/standford-machine-learning-1.html) 的課程學習，實現簡易的`y=3x`回歸近似。


想法是給定一組訓練資料(training data),最小化cost function
<img src="http://chart.googleapis.com/chart?cht=tx&chl= \LARGE J(\theta) = \frac{1}{2}\sum_i(h_\theta(x^{(i)}) - y^{(i)})^2" style="border:none;">

程式碼實做:

- Gradient Descent [my_pred.py](https://github.com/ihongChen/GradientDescent/blob/master/my_pred.py)
- Stochastic Gradient Descent  [my_pred_SGD](https://github.com/ihongChen/GradientDescent/blob/master/my_pred_SGD.py)
