# notes
'''
This file is used for handling anything image related.
I suggest handling the local file encoding/decoding here as well as fetching any external images.
'''

# package imports
import base64
import os

# image CDNs
image_cdn = 'https://images.dog.ceo/breeds'

# logo information
cwd = os.getcwd()
logo_path = os.path.join(cwd, 'assets', 'logos', 'bodybuilding_diet_app_logo.png')
logo_path1 = os.path.join(cwd, 'assets', 'logos', 'summary.png')
logo_path2 = os.path.join(cwd, 'assets', 'logos', 'daily_diet.png')
logo_path3 = os.path.join(cwd, 'assets', 'logos', 'add_food.png')
logo_path4 = os.path.join(cwd, 'assets', 'logos', 'insights.png')
logo_path5 = os.path.join(cwd, 'assets', 'logos', 'ground3.png')


logo_tunel = base64.b64encode(open(logo_path, 'rb').read())
logo_tunel_1 = base64.b64encode(open(logo_path1, 'rb').read())
logo_tunel_2 = base64.b64encode(open(logo_path2, 'rb').read())
logo_tunel_3 = base64.b64encode(open(logo_path3, 'rb').read())
logo_tunel_4 = base64.b64encode(open(logo_path4, 'rb').read())
logo_tunel_5 = base64.b64encode(open(logo_path5, 'rb').read())

logo_encoded = 'data:image/png;base64,{}'.format(logo_tunel.decode())
logo_encoded1 = 'data:image/png;base64,{}'.format(logo_tunel_1.decode())
logo_encoded2 = 'data:image/png;base64,{}'.format(logo_tunel_2.decode())
logo_encoded3 = 'data:image/png;base64,{}'.format(logo_tunel_3.decode())
logo_encoded4 = 'data:image/png;base64,{}'.format(logo_tunel_4.decode())
logo_encoded5 = 'data:image/png;base64,{}'.format(logo_tunel_5.decode())


def get_dog_image(breed, name):
    '''
    This method assumes that you are fetching specific images hosted on a CDN.
    For instance, random dog pics given a breed.
    '''
    if breed and name:
        return f'{image_cdn}/{breed}/{name}.jpg'
    return None
