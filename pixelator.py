import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def main(file_name1, file_name2):
  from PIL import Image
  import numpy as np
  import itertools
  import matplotlib.pyplot as plt
  from sklearn.metrics import confusion_matrix

  im_s = Image.open(file_name1)
  im_b = Image.open(file_name2)
  file_tobe_saved = "pixelator_view.png"

  img_s_list = []
  img_s_score = 0
  for pixel in iter(im_s.getdata()):
      int_val = getIfromRGB(pixel)
      img_s_list.append(int_val)
      img_s_score += (int_val % 255) # Just get the modulo of 255

  img_b_list = []
  img_b_score = 0
  for pixel in iter(im_b.getdata()):
      int_val = getIfromRGB(pixel)
      img_b_list.append(int_val)
      img_b_score += (int_val % 255) # Just get the modulo of 255

  new_img_b_list2 = []
  count = 0
  for pixel in img_s_list:
      diff = (img_b_list[count] - pixel) % 255 # Just get the modulo of 255
      new_img_b_list2.append(diff)
      count += 1
  added = sum(new_img_b_list2[0:len(new_img_b_list2)])
  pixelator_val = added/(im_s.width + im_s.height)
  print('Pixelator value: ', pixelator_val)

  if (img_s_score != 0.0):
    percent_diff = ((img_s_score/(im_s.width + im_s.height)) - pixelator_val)/(img_s_score/(im_s.width + im_s.height))
    print('Total Image Score: ', (img_s_score/(im_s.width + im_s.height)))
    print('Image Difference: ', (100.0 - percent_diff*100))
  else:
    print('Total Image Score: ', (img_s_score))
    print('Image Difference: ', (img_s_score*100))

  data_array = np.array(new_img_b_list2)
  shape = (im_s.height, im_s.width)
  diff_matrix = data_array.reshape(shape)

  #print(diff_matrix)

  print('[i] CREATING PIXELATOR VIEW')
  # Plot non-normalized confusion matrix
  plt.figure()
  plot_matrix(diff_matrix, classes='', normalize=False,title='Pixelator View')
  plt.savefig(file_tobe_saved)
  plt.show()

def plot_matrix(cm, classes,
                          normalize=False,
                          title='Pixelator View',
                          cmap=plt.cm.Blues):
    """
    Normalization can be applied by setting `normalize=True`.
    """
    import numpy as np
    import itertools
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("[Normalized representation]")
    else:
        print("[Representation without normalization]")

    #print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    '''
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    '''

    plt.tight_layout()
    #plt.ylabel()
    #plt.xlabel()

def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return red, green, blue

def getIfromRGB(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    #print(red, green, blue)
    RGBint = (red<<16) + (green<<8) + blue
    return RGBint

if __name__ == '__main__':
    import sys
    import os.path
    args1 = False
    args2 = False
    try:
        args1 = sys.argv[1]
        args2 = sys.argv[2]
        print("Smaller image file: " + args1)
        print("\nLarger image file: " + args2)
        print("\nFinding the Pixelator value between " + args1 + " and " + args2 + "::\n\n")
    except IndexError:
        args1 = False
        args2 = False
    if(args1 != False or args1 != False):
        file_name1 = str(args1)
        file_name2 = str(args2)
        is_file1 = os.path.isfile(file_name1)
        is_file2 = os.path.isfile(file_name2)
        if (is_file1 == False or is_file2 == False):
            print('\nError::\n\nWrong file selected! Please, check the path and file name again.\n')
            sys.exit(1)
        main(file_name1, file_name2)
    else:
        print('\nError::\n\nNo file selected!\nPlease, select the files first.\n')
