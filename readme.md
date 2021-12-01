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

  [digit_1](./image/digit_1.jpg)[dig_2](./image/digit_2.jpg)[digit_3](./image/digit_3.jpg)[digit_4](./image/digit_4.jpg)
## 2.2-Simplify color 

## 2.3 Standardization per pixel
  * 將每個向素標準化，用下列規則  

  <a href="https://www.codecogs.com/eqnedit.php?latex=\bar&space;x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar&space;x" title="\bar x" /></a> 代表每個向素的平均數, 
 <a href="https://www.codecogs.com/eqnedit.php?latex=x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a>代表矩陣裡每個元素  
 <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)&space;=&space;\begin{cases}&space;1&space;&\text{if&space;}&space;x&space;\le&space;\bar&space;x&space;\\\\&space;0&space;&\text{if&space;}&space;x&space;>&space;\bar&space;x&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;\begin{cases}&space;1&space;&\text{if&space;}&space;x&space;\le&space;\bar&space;x&space;\\\\&space;0&space;&\text{if&space;}&space;x&space;>&space;\bar&space;x&space;\end{cases}" title="f(x) = \begin{cases} 1 &\text{if } x \le \bar x \\\\ 0 &\text{if } x > \bar x \end{cases}" /></a>
## 2.2-Find Similar Imgae

  * Hamming distance 


  
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\left[&space;\begin{matrix}&space;x(0,0)&space;&&space;x(0,1)&space;&&space;\cdots&space;&&space;x(0,55)&space;\\\\&space;x(1,0)&space;&&space;x(1,1)&space;&&space;\cdots&space;&&space;x(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;x(22,0)&space;&&space;(22,1)&space;&&space;\cdots&space;&&space;x(22,55)&space;\\\\&space;\end{matrix}&space;\right]" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left[&space;\begin{matrix}&space;x(0,0)&space;&&space;x(0,1)&space;&&space;\cdots&space;&&space;x(0,55)&space;\\\\&space;x(1,0)&space;&&space;x(1,1)&space;&&space;\cdots&space;&&space;x(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;x(22,0)&space;&&space;(22,1)&space;&&space;\cdots&space;&&space;x(22,55)&space;\\\\&space;\end{matrix}&space;\right]" title="\left[ \begin{matrix} x(0,0) & x(0,1) & \cdots & x(0,55) \\\\ x(1,0) & x(1,1) & \cdots & x(1,55) \\\\ \vdots & \vdots & \ddots & \vdots \\\\ x(22,0) & (22,1) & \cdots & x(22,55) \\\\ \end{matrix} \right]" /></a>
 




