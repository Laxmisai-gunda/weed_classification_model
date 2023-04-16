import os

def main():
    target_dir = 'raw_dataset/CROWFOOT_GRASS'
    bird_name = 'CROWFOOT_GRASS'

    files = os.listdir(target_dir)
    # print(files)

    for idx, name in enumerate(files):
        os.rename('{}/{}'.format(target_dir, name), 'raw_dataset/CROWFOOT_GRASS/{0}_{1:03}.jpg'.format(bird_name,(idx+1)))

if __name__ == '__main__' : 
    main()