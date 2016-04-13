from Augmentor import ImageOperations
from Augmentor import ImageSource
from Augmentor import AsciiTable


class Pipeline(object):
    def __init__(self, image_path='.'):
        self.function_list = []
        self.image_path = image_path
        self.image_source = ImageSource.ImageSource(image_path)
        self.image_operations = ImageOperations.ImageOperations()

    def addFlipX(self, chance=1):
        print("addFlipX")
        self.function_list.append(
            [lambda: ImageOperations.ImageOperations.flip_x(self.image_operations, self.image_source, chance), "FlipX"])

    def addFlipY(self, chance=1):
        print("addFlipY")
        self.function_list.append(
            [lambda: ImageOperations.ImageOperations.flip_y(self.image_operations, self.image_source, chance), "FlipY"])

    def addTranspose(self, chance=1):
        print("addTranspose")

    def addRotate90(self, chance=1):
        print("addRotate90")
        self.function_list.append(
            [lambda: ImageOperations.ImageOperations.rotate_90(self.image_operations, self.image_source, chance),
             "Rotate90"])

    def addRotate180(self, chance=1):
        print("addRotate180")
        self.function_list.append(
            [lambda: ImageOperations.ImageOperations.rotate_180(self.image_operations, self.image_source, chance),
             "Rotate180"])

    def addRotate270(self, chance=1):
        print("addRotate270")
        self.function_list.append(
            [lambda: ImageOperations.ImageOperations.rotate_270(self.image_operations, self.image_source, chance),
             "Rotate270"])

    def addResize(self, height, width, chance=1):
        print("addResize")
        self.function_list.append([lambda: ImageOperations.ImageOperations.resize(self.image_operations,
                                                                                  self.image_source, height, width,
                                                                                  chance), "Resize"])

    def addScale(self, height, width, chance=1):
        print("addScale")
        self.function_list.append([lambda: ImageOperations.ImageOperations.scale(self.image_operations,
                                                                                 self.image_source, height, width,
                                                                                 chance), "Scale"])

    def addRotate(self, degree, chance=1):
        print("addRotate")
        self.function_list.append(
            [lambda: ImageOperations.ImageOperations.rotate(self.image_operations, self.image_source, degree, chance),
             "Rotate"])

    def addCrop(self, height, width, chance=1):
        print("addCrop")
        self.function_list.append([lambda: ImageOperations.ImageOperations.crop(self.image_operations, self.image_source,
                                                         height, width, chance), "Crop"])

    def addConvertGrayscale(self, chance=1):
        print("addConvertGrayscale")
        self.function_list.append([lambda: ImageOperations.ImageOperations.convert_grayscale(self, self.image_source,
                                                                                             chance),
                                   "ConvertGrayscale"])

    def execute(self):
        print("Saving " + str(len(self.image_source.list_of_images) * len(
            self.function_list)) + " images to " + self.image_source.root_path)

        for f, _ in self.function_list:
            f()

    def summary(self):
        list_of_operations = []
        for _, function_name in self.function_list:
            list_of_operations.append(function_name)

        table_data = [
            ['Pipline Summary:'],
            [str(len(self.function_list)) + ' operation(s)'],
            ['New size: ' + str(len(self.image_source.list_of_images) + len(self.image_source.list_of_images))],
            ['TODO: Print additional information'],
        ]
        table = AsciiTable(table_data)
        print(table.table)
