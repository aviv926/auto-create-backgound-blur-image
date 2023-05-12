# auto-create-backgound-blur-image
The code was created with the aim of taking from a photo folder all the images that are not 1920 x 1080 in size and turning them into such without harming the original quality of the image

The code is generated using GPT4 The text I wrote to him was:

I'm editing a video clip and there are many photos whose size is not full size, that is 1920 x 1080, 
the problem is that when I put these photos into the editing software they are too small for my sequence
and a situation arises that out of 1920 x 1080 there is a black background and this makes the clip ugly 
I want you to write code in Python that will do the following on an entire folder of images and export all the images to a new folder called "1920 X 1080"

1. Any image that is 1080 x 1440 automatically do the following:
The image that is 1080 x 1440 will be adjusted to 1920 x 1080 but with 70 percent blur, while the original image that is 1080 x 1440 will be unblurred and in its original size without cropping

2. Any image that is 1080 x 1920 the code will keep the image at 1080 x 1920, but create a background with 70 percent blur from the original 1920 x 1080 image while the original 1080 x 1920 image will be unblurred and in its original size without cropping

3. Otherwise, any image that is not 1920 x 1080 automatically do the following:
The non-1920x1080 image will be stretched to 1920x1080 but with 70 percent blur, while the original non-1920x1080 image will be unblurred and at its original size without cropping

# How to run?
The operating instructions are super simple to operate

The Pillow library is needed
```
pip install Pillow
```

run the following command:
```
python.exe 1.py
```

What this will do is simply take any image that is not 1920 x 1080 and make it 1920 x 1080 without harm changing the original image

Done :) 

# for example
### before:
![1](https://github.com/aviv926/auto-create-backgound-blur-image/assets/51673860/482e9346-7184-4472-9037-49e4b4adb2fd)

### after:
![1](https://github.com/aviv926/auto-create-backgound-blur-image/assets/51673860/6a7a2def-9770-4c82-ab6f-34abf2abca11)

# Problems to fix in the code:

Any image size 1080 x 1440 do the following:
The image will be adjusted to 1920 x 1080 but with 30 percent blur in the background, while the original image which is 1080 x 1440 will be without blur and in its original size without cropping or re-adjustment just as it is in the original

The code does add a blur to the background, but it turns the image right side up...I couldn't figure out why

# Privacy Policy:

It works 100% locally on the computer
NO DATA SENT TO ANYWHERE

# license etc.
You are welcome to suggest and make any changes you want to this code. If you made a change that benefited you, I would be happy if you shared it.
