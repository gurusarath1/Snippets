import pathlib
import torchvision.transforms as transforms
from PIL import Image
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import matplotlib.pyplot as plt

class ImageDataset(Dataset):


    def __init__(self, file_list, labels, transform=None):

        self.file_list = file_list
        self.labels = labels
        self.transform = transform

    def __getitem__(self, index):

        img = Image.open(self.file_list[index])

        if self.transform is not None:
            img = self.transform(img)

        label = self.labels[index]

        return img, label

    def __len__(self):

        return len(self.labels)


if __name__ == '__main__':
    imgdir_path = pathlib.Path('small_image_dataset1')
    file_list = sorted( [ str(path) for path in imgdir_path.glob('*.jpg') ] )
    
    img_height, img_width = 80,120

    transform = transforms.Compose( [
        transforms.ToTensor(),
        transforms.Resize((img_height, img_width))
        ] )


    fig = plt.figure(figsize = (10,6))

    dummy_labels = [1,2,3,4,5]
    image_dataset = ImageDataset(file_list, dummy_labels, transform)

    for i,example in enumerate(image_dataset):

        image = example[0]
        print('Image type and shape -- ', type(image), image.shape)

        ax = fig.add_subplot(2,3,i+1)
        ax.set_xticks([]); ax.set_yticks([])
        ax.imshow(image.numpy().transpose((1,2,0)))

    plt.tight_layout()
    plt.show()

    #------------------------------------------------------------------------

    batch_size = 2
    train_dl = DataLoader(image_dataset, batch_size, shuffle=True)

    for imgs,labels  in train_dl:

        print(imgs.shape)




