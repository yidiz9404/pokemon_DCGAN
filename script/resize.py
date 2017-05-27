from PIL import Image
import os


def resize_image(image, size):
    """Resizes an image to the given size."""
    return image.resize(size, Image.ANTIALIAS)

def resize_images(image_dir, output_dir, size):
    """Resizes the images in the image_dir and save into the output_dir."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = os.listdir(image_dir)
    num_images = len(images)
    for i, image in enumerate(images):
        with open(os.path.join(image_dir, image), 'r+b') as f:
            with Image.open(f) as img:
                img = resize_image(img, size)
                img.save(
                    os.path.join(output_dir, image), img.format)
        if i % 100 == 0:
            print ('[%d/%d] Resized the images and saved into %s.'
                   %(i, num_images, output_dir))

def main():
    image_dir = '/Users/twff/Downloads/deep_learning/hw/hw3/data/'
    output_dir = '/Users/twff/Downloads/deep_learning/hw/hw3/data/resize/'
    resize_images(image_dir, output_dir, (40, 40))


if __name__ == '__main__':
    main()
