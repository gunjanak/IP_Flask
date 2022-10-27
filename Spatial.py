import numpy as np
from PIL import Image

def smooth_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    array_b = np.zeros((402,402))

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[1/9,1/9,1/9],
                         [1/9,1/9,1/9],
                         [1/9,1/9,1/9]])

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(3+i),j:(3+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.sum(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return(output)


def sharp_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    array_b = np.zeros((402,402))

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[-1/9,-1/9,-1/9],
                         [-1/9,8/9,-1/9],
                         [-1/9,-1/9,-1/9]])

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(3+i),j:(3+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.sum(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)


    return(output)



def min_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    array_b = np.zeros((402,402))

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

    #filter_array = np.array([[1,1,1],
     #                     [1,1,1],
      #                     [1,1,1]])

    #defining filter
    filter_array = np.array([[3,3,3],
                           [3,3,3],
                           [3,3,3]])

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(3+i),j:(3+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.min(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return(output)


def max_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    array_b = np.zeros((402,402))

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

    #filter_array = np.array([[1,1,1],
     #                     [1,1,1],
      #                     [1,1,1]])

    #defining filter
    filter_array = np.array([[3,3,3],
                           [3,3,3],
                           [3,3,3]])

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(3+i),j:(3+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.max(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")

    output = []
    output.append(img)
    output.append(final_image)

    return(output)




def median_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)

    #array for padding
    array_b = np.zeros((402,402))

    #to pad initial array with zeros
    array_b[1:401,1:401] = numpy_image

   
    #defining filter
    filter_array = np.array([[3,3,3],
                           [3,3,3],
                           [3,3,3]])

    #creating an empty list
    lst = []
    for i in range(400):
        for j in range(400):
            #extracting part of array equal to filter size
            array_c = array_b[i:(3+i),j:(3+j)]
            
            #applying filter
            array_mul = np.multiply(filter_array,array_c)
            array_sum = np.median(array_mul)
            
            # putting calculated value in list
            lst.append(array_sum)

    #resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image = final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return(output)



def high_boost(input_image):
    high_pass = sharp_filter(input_image)
    high_pass = high_pass[1]
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)

    A = 3
    high_boost = (A-1)*numpy_image + high_pass
    final_image = Image.fromarray(high_boost)
    final_image= final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return output