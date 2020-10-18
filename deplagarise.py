
map1 = {
    
    'a' : '𝖺',
    'b' : '𝖻',
    'c' : '𝖼',
    'd' : '𝖽',
    'e' : '𝖾',
    'f' : '𝖿',
    'g' : '𝗀',
    'h' : '𝗁',
    'i' : '𝗂',
    'j' : '𝗃',
    'k' : '𝗄',
    'l' : '𝗅',
    'm' : '𝗆',
    'n' : '𝗇',
    'o' : '𝗈',
    'p' : '𝗉',
    'q' : '𝗊',
    'r' : '𝗋',
    's' : '𝗌',
    't' : '𝗍',
    'u' : '𝗎',
    'v' : '𝗏',
    'w' : '𝗐',
    'x' : '𝗑',
    'y' : '𝗒',
    'z' : '𝗓',

}


# for key,val in map1.items():
#     print(' Key : {}  :Val : {} , key # {}  , val # {}'.format(key,val,ord(key),ord(val)))


text_to_replace = '''
We propose a novel coupled mappings method for
low resolution face recognition using deep convolutional neural
networks (DCNNs). The proposed architecture consists of two
branches of DCNNs to map the high and low resolution face
images into a common space with nonlinear transformations.
The branch corresponding to transformation of high resolution
images consists of 14 layers and the other branch which maps
the low resolution face images to the common space includes a 5-
layer super-resolution network connected to a 14-layer network.
The distance between the features of corresponding high and low
resolution images are backpropagated to train the networks. Our
proposed method is evaluated on FERET data set and compared
with state-of-the-art competing methods. Our extensive experimental evaluations show that the proposed method significantly
improves the recognition performance especially for very low
resolution probe face images (11.4% improvement in recognition
accuracy). Furthermore, it can reconstruct a high resolution
image from its corresponding low resolution probe image which
is comparable with the state-of-the-art super-resolution methods
in terms of visual quality.'''

print( 'Initial Text  :{}'.format(text_to_replace))

text_to_replace = list(text_to_replace)

for i,ch in enumerate(text_to_replace):
    if ch in map1:
        text_to_replace[i] = map1[ch]


text_to_replace = ''.join(text_to_replace)


print( 'Converted Text  :{}'.format(text_to_replace))



