def crop(image, new_shape):
  
    '''
    image.shape = (batch size, channels, height, width)
    new_shape.shape = (batch size, channels, new_height, new_width)
    '''
    
    center_h_pix = image.shape[2] // 2
    center_w_pix = image.shape[3] // 2
    
    h_crop_start = center_h_pix - (new_shape[2] // 2)
    h_crop_end = h_crop_start + new_shape[2]

    w_crop_start = center_w_pix - (new_shape[3] // 2)
    w_crop_end = w_crop_start + new_shape[3]
 
    cropped_image = image[:, :, h_crop_start:h_crop_end, w_crop_start:w_crop_end]

    return cropped_image
