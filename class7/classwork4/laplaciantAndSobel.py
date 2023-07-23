import numpy as np
import cv2 as cv

def FourierTransform(img):
    img32 = img.astype(np.float32)  # เปลี่ยนภาพให้เป็น float32
    imgFourier = np.fft.fft2(img32)  # คืนเป็นภาพ Spectrum
    imgFourier = np.fft.fftshift(imgFourier) #เลื่อนศูนย์ของภาพมาอยู่ตรงกลาง
    # for magnitude spectrum
    imgReal = np.real(imgFourier)  # แยกส่วนจริงของ Fourier-transformed image
    imgImag = np.imag(imgFourier)  # แยกส่วนจินตภาพของ Fourier-transformed image
    imgMag = np.sqrt(imgReal**2 + imgImag**2)  #  คำนวณสเปกตรัมของภาพโดยใช้สมการ Magnitude = sqrt(Re^2 + Im^2)
    imgMag = np.log(1 + imgMag)  # เพิ่มความชัดเจนในการแสดงผลภาพ
    imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)  # ปรับค่าสเกลของภาพให้สามารถแสดงผลภาพได้

    return imgFourier, imgMag


if __name__ == '__main__': # 1. นำเข้าไลบรารี OpenCV และ NumPy
    
    img = cv.imread('class7/img/catonnote.jpg', 0) #แปลงให้เป็นภาพขาวด้วยพารามิเตอร์เป็น 0
    h, w = img.shape 
    
    # Sobel kernel แบบ Vertical
    sobel_vertical = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])
    
    kernel_length = len(sobel_vertical) #3
    
    #sobel filter in frequency domain
    
    #1.เติมพื้นที่ของ kernel เพื่อให้ขนาดของ kernel เท่ากับขนาดของภาพที่ผ่านการคำนวณ Fourier ทำให้ convolution ในโดเมนความถี่ได้
    kernel_pad = np.pad(sobel_vertical, ((h // 2 , h // 2 - kernel_length), (w // 2 , w // 2 - kernel_length)), mode='constant')
    kernel = np.fft.fftshift(kernel_pad)

    # 2. คำนวณ Fourier transform ทั้ง kernel และ image โดยใช้ฟังก์ชัน FourierTransform
    filterF, filterMag = FourierTransform(kernel)
    imgF, imgMag = FourierTransform(img)
    cv.imwrite('class7/out/imgMag.png', imgMag)
    cv.imwrite('class7/out/filterMag.png', filterMag)

    # 3. คำนวณผลคูณ (dot product) ของภาพที่ผ่านการคำนวณ Fourier-transform และ kernel 
    dotProduct = imgF * filterF  


    # 4. ทำการส่วนกลับของ Fourier transform ให้กับผลคูณเพื่อของรูปที่ได้ผ่านการกรอง
    imgF_filtered = np.fft.ifftshift(dotProduct)
    imgF_filtered = np.fft.ifft2(imgF_filtered)
    filtered = np.real(imgF_filtered)
    imgF_filtered = cv.normalize(filtered, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)  # Normalize the filtered image
    cv.imwrite('class7/out/Sobel-Frequency.png', imgF_filtered)



# Sobel Filter ใน Spatial domain

    sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    sobelX = cv.normalize(sobelX, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    cv.imwrite('class7/out/Sobel-Spatial.png', sobelX)

    # เปรียบเทียบ 2 โดเมน
    compareImage = np.concatenate((imgF_filtered, sobelX), axis=1)


    cv.imshow('Frequency and Spatial domain', compareImage)
    cv.waitKey(0)
    cv.destroyAllWindows()
