import cv2
import os

def main():
    dataset_dir = 'raw_dataset/CROWFOOT_GRASS'
    allowed_extensions = ['.png', '.jpg', '.jpeg']

    files = os.listdir(dataset_dir)
    print('files in given dir. : ')
    print(files)

    for file in files:
        extension = os.path.splitext(file)[1].lower()
        filename = os.path.splitext(file)[0].lower()

        filepath = '{}/{}'.format(dataset_dir, file)

        if extension in allowed_extensions:
            img = cv2.resize(cv2.imread(filepath), (224, 224))

            cv2.imwrite(filepath, img)

        rename_file = '{}/{}.jpeg'.format(dataset_dir, filename)
        os.rename(filepath, rename_file)

if __name__ == '__main__' : 
    main()