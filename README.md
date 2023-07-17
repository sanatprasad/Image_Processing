# Image_Processing

In this work, I investigated several contrast enhancement methodologies, including Histogram Equalization (HE), Adaptive Histogram Equalization (AHE), Contrast Limited 
Adaptive Histogram Equalization (CLAHE), and Local Region Stretch (LRS). 

Histogram Equalization (HE) is a simple and effective method that redistributes the pixel intensities in an image, enhancing the overall contrast. 
It performs well in improving the visibility of details, but it may result in over-amplification of noise and artifacts in some cases. 

Adaptive Histogram Equalization (AHE) addresses the limitations of HE by applying local contrast enhancement. It divides the image into smaller regions and performs histogram 
equalization independently in each region. This approach helps to enhance local details and preserves the global contrast. 

Contrast Limited Adaptive Histogram Equalization (CLAHE) overcomes the drawbacks of AHE by introducing a contrast limitation. It prevents excessive contrast amplification by 
clipping the histogram at a specified threshold. CLAHE effectively enhances local contrast while avoiding over enhancement artifacts. 
It performs well in various image types and is particularly useful in medical imaging and surveillance applications. 

Local Region Stretch (LRS) is a method that enhances contrast based on brightness levels.It splits the image into three brightness levels and applies histogram equalization separately to each level. LRS utilizes 
the weighted sum of the three enhanced images to obtain the final result. This method can effectively enhance images with varying brightness levels and is suitable for applications where 
different regions require different contrast enhancements. 

Overall, each contrast enhancement methodology has its strengths and limitations. The choice of method depends on the specific image characteristics, the desired enhancement goals, and the 
application requirements. Experimentation and careful evaluation are essential to determine the most suitable technique for a given image or scenario. By exploring these 
methodologies, we have gained insights into different approaches for contrast enhancement, which can be applied in various domains, such as image processing, computer vision, 
medical imaging, and more.
