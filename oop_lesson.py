class Door:
    # Class attributes
    material = 'Wood'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def open(self):
        print('Door opened')

    def close(self):
        print('Door closed')


def main():
    door_1 = Door(80, 180)

    door_2 = Door(60, 180)

    print(door_1.material)
    print(door_2.material)


    #
    # print(door_1)
    # print(door_2)
    # door_1.width = 80
    # door_1.height = 180
    # print(door_1.width)
    # print(door_1.height)
    # print(door_1.height * door_1.width)



if __name__ == "__main__":
    main()