#assignment 6

'''
write a program to modify images
the image format we are going to use is PPM

PPM image format:
    the PPM image format is encoded in human readable plain text. the image has 2 main parts:
        1. header
        2. body

    PPM header:
        the header is always the top three uncommented lines in the file

        ex:
        p3
        4 4
        255

        the first line specifies the image ending that is contained within the file. we will always use the P3 specification

        the second line specifies the number of pixel columns and rows present in the image. so in this example, we have a 4 by 4 pixel image

        the third row indicates the maximum value for each red, gree, blue. max value is 255

    PPM body:
        below the header is the body of the PPM file. eachpixel has a red, green, and blue value

        ex:
        255 0 0     0 255 0     0 0 255     255 255 255

        with these values, the pixel in the first column and first row has RGB value of (255,0,0), which equates to red
'''

'''
write a program to prompt the user for the name of an input PPM image. produce an output ppm image file for each of the collowing modifications to the input PPM image
    1. flip vertically
    2. flip horizontally
    3. remove a primary color
    4. negate colors
    5. apply high contrast
    6. add random noise
    7. apply grayscale
    8. apply horizontal blur
'''
import random
def welcome():
    print("Welcome to the PPM Image Manipulation Program")

def read_in_file(filename):
    '''
    opens file and reads contents
    returns: file
    '''
    input_file = open(filename, "r")
    return input_file

def create_out_file(filename):
    '''
    creates file
    returns: file
    '''
    output_file = open(filename, "w")
    return output_file

def write_to_file(data, filename):
    '''
    takes in a file and writes to the file
    '''
    print(data, file=filename)

def close_file(filename):
    '''
    closes the file
    '''
    filename.close()

def get_ppm_file():
    '''
    asks the user for the original ppm file
    returns: file
    '''
    ppm_file = input("Please enter the name of the input PPM image file: ")
    return ppm_file

#file functions
def process_header(infile, outfile):
    '''
    accepts input and output file objects
    writes the first three lines of the input image to the output image
    '''
    encoding = get_image_encoding(infile)
    dimensions = get_dimensions(infile)
    max_value = get_max_value(infile)
    write_to_file(encoding, outfile)
    write_to_file(dimensions, outfile)
    write_to_file(max_value, outfile)

def process_body(infile, outfile, modification):
    '''
    accepts an input file object, output file object, and a string specified modification according to modification
    '''

def load_image_data(infile):
    '''
    accepts an input file object
    reads the data from the input PPM image into a 2d list of tuples
    returns: 2d list
    '''
    tuple_list = []
    for i in infile.readlines():
        line = i.replace(" ", ", ")
        line = line.replace("\n", "")
        line = [int(i) for i in line]
        print(line)
        break

def get_image_encoding(infile):
    encoding = infile.readline()
    return encoding

def get_dimensions(infile):
    line = infile.readline()
    line = line.strip()
    columns = line[0]
    rows = line[1]
    return columns, rows

def get_max_value(infile):
    value = infile.readline()
    return value

#image modifications
def apply_vertical_flip(image_2dlist, outfile):
    '''
    accepts a 2d list of tuples and an outfile object
    flips the image data vertically
    '''

def apply_horizontal_flip(image_2dlist, outfile):
    '''
    accepts a 2d list of tuples and an outfile object
    flips the image data horizontally
    '''

def apply_horizontal_blur(image_2dlist, outfile):
    '''
    accepts a 2d list of tuples and an outfile object
    horizontally blurs image
    '''

#RGB value modifications
def negative(num):
    '''
    accepts a single integer RGB value
    subtracts 255 and takes the absolute value of the result
    returns the modified values
    '''
    negated_num = abs(num - 255)
    return negated_num

def high_contrast(num):
    '''
    accepts a single integer RGB value
    if the value is greater than 127, sets it to 255
    otherwise sets it to zero
    returns the modified value
    '''
    if num > 127:
        num = 255
    else:
        num = 0
    return num

def random_noise(num):
    '''
    accepts a single integer RGB value
    generates a random number in the range[-50,50] and adds it to the value
    returns the modified value
    '''
    rand = random.randint(-50,50)
    num += rand
    return num

def gray_scale(rgb):
    '''
    accepts a rgb tuple
    computes the average of the RGB values in the tuple
    returns a new tuple where each value is the average
    '''
    total = 0
    for value in rgb:
        total += value
    avg = total / len(rgb)
    new_rgb = (avg, avg, avg)
    return new_rgb

def remove_color(rgb, color_to_remove):
    '''
    accepts a rgb tuple and a string representing the color to remove
        ex: 'r', 'b', 'g'
    returns a new tuple with the appropriate red, green, or blue set to 0
    '''
    if color_to_remove == 'r':
        rgb[0] = 0
    elif color_to_remove == 'g':
        rgb[1] = 0
    elif color_to_remove == 'b':
        rgb[2] = 0
    else:
        print("Invalid input")
    return rgb

def main():
    welcome()
    ppm_file = get_ppm_file()
    in_file = read_in_file(ppm_file)

    sample = create_out_file("sample.ppm")
    process_header(in_file, sample)
    load_image_data(in_file)




main()
