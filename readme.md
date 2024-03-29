# Indroduction of Captch

## What is Captcha?
  * Captcha (English: Completely Automated Public Turing test to tell Computers and Humans Apart
    主要用途: 全自動區分電腦和人類的測試
  * How Captcha work ?
    Server create the picture which combine the distorted letter or image and send it to client side  
---
## Ours Goals
  **We want to predict the answer of Captcha and get over 95% correct percentage**

---

## Image Process

  * How we get sample: Download the Captcha image from website (https://course.fcu.edu.tw/validateCode.aspx

  * Captcha description: 
    The Captcha is maked up with 4 number which is random choosed from number 0-9.
    Image size: (22, 50)
    
  * Count of Captcha: 10000

---
  原圖形大小為(22, 50), 這邊為了方便閱讀將圖片大小放大為原圖的20倍。
  ![image](./image/00000.jpg) ![resize_image](./image/resize.jpg)
  * 單張圖片分析
    在放大圖片後，細看每個位置的數字發現到每個數字的顏色都有一個主要的顏色搭配其他的隨機  色彩去做干擾，並且在數字以外的地方也有灰色區塊出現在隨機的地方再搭配一些隨機的顏色。
---
## 2.1-Split Region Of Image
  將圖片4個數字個別切割出來  
  |Captcha|Digit_1|Digit_2|Digit_3|Digit_4|
  |-------|:-----:|:-----:|:-----:|:-----:|
  |![image](./image/00000.jpg)|![digit_1](./image/digit_1.jpg)|![digit_2](./image/digit_2.jpg)|![digit_3](./image/digit_3.jpg)|![digit_4](./image/digit_4.jpg)|
  |![image](./image/00001.jpg)|![digit_1](./image/00001_digit1.jpg)|![digit2](./image/00001_digit2.jpg)|![image](./image/00001_digit3.jpg)|![image](./image/00001_digit4.jpg)|  
  |![image](./image/00002.jpg)|![digit_1](./image/00002_digit1.jpg)|![digit2](./image/00002_digit2.jpg)|![image](./image/00002_digit3.jpg)|![image](./image/00002_digit4.jpg)|
  |![image](./image/00003.jpg)|![digit_1](./image/00003_digit1.jpg)|![digit2](./image/00003_digit2.jpg)|![image](./image/00003_digit3.jpg)|![image](./image/00003_digit4.jpg)| 
  |![image](./image/00004.jpg)|![digit_1](./image/00004_digit1.jpg)|![digit2](./image/00004_digit2.jpg)|![image](./image/00004_digit3.jpg)|![image](./image/00004_digit4.jpg)| 

## 2.2-Simplify color 
  簡單來說就是將圖片灰度化，這邊是將4個數字切割完後個別灰度化。  
  |Captcha|Gray_Digit1|Gray_Digit2|Gray_Digit3|Gray_Digit4|
  |-------|:---------:|:---------:|:---------:|:---------:|
  |![image](./image/00000.jpg)|![image](./image/00000_digit1_gray.jpg)|![image](./image/00000_digit2_gray.jpg)|![image](./image/00000_digit3_gray.jpg)|![image](./image/00000_digit4_gray.jpg)|
  |![image](./image/00001.jpg)|![image](./image/00001_digit1_gray.jpg)|![image](./image/00001_digit2_gray.jpg)|![image](./image/00001_digit3_gray.jpg)|![image](./image/00001_digit4_gray.jpg)|
  |![image](./image/00002.jpg)|![image](./image/00002_digit1_gray.jpg)|![image](./image/00002_digit2_gray.jpg)|![image](./image/00002_digit3_gray.jpg)|![image](./image/00002_digit4_gray.jpg)|
  |![image](./image/00003.jpg)|![image](./image/00003_digit1_gray.jpg)|![image](./image/00003_digit2_gray.jpg)|![image](./image/00003_digit3_gray.jpg)|![image](./image/00003_digit4_gray.jpg)|
  |![image](./image/00004.jpg)|![image](./image/00004_digit1_gray.jpg)|![image](./image/00004_digit2_gray.jpg)|![image](./image/00004_digit3_gray.jpg)|![image](./image/00004_digit4_gray.jpg)|
## 2.3 Standardization per pixel
  * 將矩陣中每個向素標準化，用下列規則  

  <a href="https://www.codecogs.com/eqnedit.php?latex=\bar&space;x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar&space;x" title="\bar x" /></a> 代表每個向素的平均數, 
 <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a>代表矩陣裡每個元素  
 <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\begin{cases}&space;1&space;&\text{if&space;}&space;x&space;\le&space;\bar&space;x&space;\\\\&space;0&space;&\text{if&space;}&space;x&space;>&space;\bar&space;x&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\begin{cases}&space;1&space;&\text{if&space;}&space;x&space;\le&space;\bar&space;x&space;\\\\&space;0&space;&\text{if&space;}&space;x&space;>&space;\bar&space;x&space;\end{cases}" title="f(x) = \begin{cases} 1 &\text{if } x \le \bar x \\\\ 0 &\text{if } x > \bar x \end{cases}" /></a>
## 2.2-Find Similar Image
  |Representive of 4|Be tested img|Hamming Distance|Measurement error|Result|
  |:---------------:|:-----------:|:--------------:|:---------------:|:----:|
  |![image](./image/00000_digit1_gray.jpg)|![image](./image_for_poster/00088_gray.jpg)|5|13|T|
  |![image](./image/00000_digit1_gray.jpg)|![image](./image_for_poster/00099_gray.jpg)|45|13|F|
  |![image](./image/00000_digit1_gray.jpg)|![image](./image_for_poster/00101_gray.jpg)|35|13|F|
  |![image](./image/00000_digit1_gray.jpg)|![image](./image_for_poster/00111_gray.jpg)|50|13|F|
  |![image](./image/00000_digit1_gray.jpg)|![image](./image_for_poster/00120_gray.jpg)|39|13|F|
  |![image](./image/00000_digit1_gray.jpg)|![image](./image_for_poster/00125_gray.jpg)|3|13|T|
  |![image](./image/00000_digit1_gray.jpg)|![image](./image_for_poster/00215_gray.jpg)|41|13|F|



  * Hamming distance  
  將下列的矩陣的每個同樣索引的元素值做比對如果不相同的話測量誤差 + 1  
  如果測量誤差 < 13 我們就認定兩張圖片是相似的圖片。  
  用上述方法手動標記一張圖片後，即可找出目錄中相似的圖片

  * <a href="https://www.codecogs.com/eqnedit.php?latex=\left[&space;\begin{matrix}&space;x(0,0)&space;&&space;x(0,1)&space;&&space;\cdots&space;&&space;x(0,55)&space;\\\\&space;x(1,0)&space;&&space;x(1,1)&space;&&space;\cdots&space;&&space;x(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;x(22,0)&space;&&space;(22,1)&space;&&space;\cdots&space;&&space;x(22,55)&space;\\\\&space;\end{matrix}&space;\right]" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left[&space;\begin{matrix}&space;x(0,0)&space;&&space;x(0,1)&space;&&space;\cdots&space;&&space;x(0,55)&space;\\\\&space;x(1,0)&space;&&space;x(1,1)&space;&&space;\cdots&space;&&space;x(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;x(22,0)&space;&&space;(22,1)&space;&&space;\cdots&space;&&space;x(22,55)&space;\\\\&space;\end{matrix}&space;\right]" title="\left[ \begin{matrix} x(0,0) & x(0,1) & \cdots & x(0,55) \\\\ x(1,0) & x(1,1) & \cdots & x(1,55) \\\\ \vdots & \vdots & \ddots & \vdots \\\\ x(22,0) & (22,1) & \cdots & x(22,55) \\\\ \end{matrix} \right]" /></a>                   <a href="https://www.codecogs.com/eqnedit.php?latex=\left[&space;\begin{matrix}&space;f(0,0)&space;&&space;f(0,1)&space;&&space;\cdots&space;&&space;f(0,55)&space;\\\\&space;f(1,0)&space;&&space;f(1,1)&space;&&space;\cdots&space;&&space;f(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;f(22,0)&space;&&space;f(22,1)&space;&&space;\cdots&space;&&space;f(22,55)&space;\\\\&space;\end{matrix}&space;\right]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left[&space;\begin{matrix}&space;f(0,0)&space;&&space;f(0,1)&space;&&space;\cdots&space;&&space;f(0,55)&space;\\\\&space;f(1,0)&space;&&space;f(1,1)&space;&&space;\cdots&space;&&space;f(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;f(22,0)&space;&&space;f(22,1)&space;&&space;\cdots&space;&&space;f(22,55)&space;\\\\&space;\end{matrix}&space;\right]" title="\left[ \begin{matrix} f(0,0) & f(0,1) & \cdots & f(0,55) \\\\ f(1,0) & f(1,1) & \cdots & f(1,55) \\\\ \vdots & \vdots & \ddots & \vdots \\\\ f(22,0) & f(22,1) & \cdots & f(22,55) \\\\ \end{matrix} \right]" /></a>  





