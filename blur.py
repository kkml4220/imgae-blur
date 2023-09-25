import cv2
import os
import sys



def _get_output_file_path(path):
    file_name = os.path.basename(path)
    output_dir_path = os.path.dirname(path)
    output_file_name = f"blured_{file_name}"
    return os.path.join(output_dir_path, output_file_name)


def blur(blur=4):
    path = sys.argv[1]
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    blur_size = (blur, blur)
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    image = cv2.blur(image, blur_size)
    output_file_path = _get_output_file_path(path)
    cv2.imwrite(output_file_path, image)


if __name__ == '__main__':
    blur(5)