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
  原圖形大小為(22, 50), 這邊為了方便閱讀將圖片大小放大為原圖的4倍。
  ![image](./image/00000.jpg) ![image](./image/resize.jpg)
  將圖片轉成(22, 50)的矩陣
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\left[&space;\begin{matrix}&space;x(0,0)&space;&&space;x(0,1)&space;&&space;\cdots&space;&&space;x(0,55)&space;\\\\&space;x(1,0)&space;&&space;x(1,1)&space;&&space;\cdots&space;&&space;x(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;x(22,0)&space;&&space;(22,1)&space;&&space;\cdots&space;&&space;x(22,55)&space;\\\\&space;\end{matrix}&space;\right]" target="_blank"><img src="https://latex.codecogs.com/png.latex?\left[&space;\begin{matrix}&space;x(0,0)&space;&&space;x(0,1)&space;&&space;\cdots&space;&&space;x(0,55)&space;\\\\&space;x(1,0)&space;&&space;x(1,1)&space;&&space;\cdots&space;&&space;x(1,55)&space;\\\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\\\&space;x(22,0)&space;&&space;(22,1)&space;&&space;\cdots&space;&&space;x(22,55)&space;\\\\&space;\end{matrix}&space;\right]" title="\left[ \begin{matrix} x(0,0) & x(0,1) & \cdots & x(0,55) \\\\ x(1,0) & x(1,1) & \cdots & x(1,55) \\\\ \vdots & \vdots & \ddots & \vdots \\\\ x(22,0) & (22,1) & \cdots & x(22,55) \\\\ \end{matrix} \right]" /></a>
 




