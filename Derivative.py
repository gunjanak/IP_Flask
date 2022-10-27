import numpy as np
from PIL import Image

def Prewitt_Operator_horizontal(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[-1,-1,-1],
                            [0,0,0],
                            [1,1,1]])
    
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return output
    
def Prewitt_Operator_vertical(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[-1,0,1],
                            [-1,0,1],
                            [-1,0,1]])
    
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return output




def Sobel_Operator_horizontal(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[-1,-2,-1],
                         [0,0,0],
                         [1,2,1]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")

    output = []
    output.append(img)
    output.append(final_image)


    return output

def Sobel_Operator_vertical(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[-1,0,1],
                         [-2,0,2],
                         [-1,0,1]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return output


def Sobel_Operator_45(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[0,-1,-2],
                         [1,0,-1],
                         [2,1,0]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return output

def Sobel_Operator_225(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
    filter_array = np.array([[0,1,2],
                         [-1,0,1],
                         [-2,-1,0]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")
    output = []
    output.append(img)
    output.append(final_image)

    return output


def Laplacian_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
   #defining filter
    filter_array = np.array([[0,1,0],
                         [1,-4,1],
                         [0,1,0]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")

    output = []
    output.append(img)
    output.append(final_image)

    return output

def Elliptical_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
   #defining filter
    filter_array = np.array([[0,1,0],
                         [2,-6,2],
                         [0,1,0]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")

    output = []
    output.append(img)
    output.append(final_image)

    return output


def Parabolic_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
   #defining filter
    filter_array = np.array([[0,1,0],
                         [3,-8,3],
                         [0,1,0]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")

    output = []
    output.append(img)
    output.append(final_image)

    return output




def Hyperbolic_filter(input_image):
    img = input_image.resize((400,400), Image.ANTIALIAS)
    # convert to numpy array 
    numpy_image = np.array(img)
    # array for padding
    array_b = np.zeros((402,402))

    # to pad initial array with zeros in all side
    array_b[1:401,1:401] = numpy_image

    #defining filter
   #defining filter
    filter_array = np.array([[0,1,0],
                         [4,-10,4],
                         [0,1,0]])
    #creating empty list
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

    # resizing lst to shape of original array
    final_array = np.resize(lst,(400,400))

    final_image = Image.fromarray(final_array)
    final_image= final_image.convert("L")

    output = []
    output.append(img)
    output.append(final_image)

    return output
