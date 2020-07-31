import os, glob
import argparse
import cv2


def switch_coordinates(tab_lines, img_size):
    coord = []
    for tab_line in tab_lines:
        id_ = tab_line[0]
        x_center = float(tab_line[1])
        y_center = float(tab_line[2])
        width = float(tab_line[3])
        height = float(tab_line[4][:-1])

        x1 = str(round((x_center - width/2)*img_size[0]))
        y1 = str(round((y_center - height/2)*img_size[1]))
        x2 = str(round((x_center + width/2)*img_size[0]))
        y2 = str(round((y_center + height/2)*img_size[1]))
        coord.append(x1 + "," + y1 + "," + x2 + "," + y2 + "," + id_)

    return coord

def load_txt(file):
    tab_line = []
    with open(file, 'r') as f:
        for line in f:
            tab_line.append(line[:-1].split(" "))
    return tab_line


def main(args):
    train_path = os.path.join(args.data_dir, 'train')
    val_path = os.path.join(args.data_dir, 'val')
    path = {'train': train_path, 'val': val_path}
    for key, path in path.items():
        print('Processing {} txt'.format(key))
        data_list = glob.glob(path + "/*.png")
        coords = []
        for i, data in enumerate(data_list):
            img_path = data
            height, width, _ = cv2.imread(img_path).shape
            tab_line = load_txt(img_path[:-3] + 'txt')
            coord = switch_coordinates(tab_line, (width, height))
            coords.append([img_path, coord])
            print('\r{:.2f}%'.format((i+1) * 100/len(data_list)), end = '', flush=False)
        print('\nDone!')

            
        with open(os.path.join(args.save_dir, key + ".txt"), "w") as final_file:
            for coord in coords:
                line = ''
                line += coord[0] + " "
                for box in coord[1]:
                    line += box + " "
                line = line[:-1] + "\n"
                final_file.write(line)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", help="target file", type=str, default="../data")
    parser.add_argument("--save_dir", help="target file", type=str, default="../data")
    args = parser.parse_args()
    
    main(args)