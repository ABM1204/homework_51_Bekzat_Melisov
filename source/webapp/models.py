class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.satiety_level = 40
        self.happy_point = 40
        self.is_sleeping = False

    def feed_cat(self):
        if not self.is_sleeping:
            self.satiety_level = min(100, self.satiety_level + 15)
            self.happy_point = min(100, self.happy_point + 5)
            if self.satiety_level > 100:
                self.happy_point = max(0, self.happy_point - 30)

    def play_cat(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happy_point = max(0, self.happy_point - 5)
        else:
            from random import randint
            if randint(1, 3) == 1:
                self.happy_point = 0
            else:
                self.happy_point = min(100, self.happy_point + 15)
            self.satiety_level = max(0, self.satiety_level - 10)

    def put_cat_to_bed(self):
        self.is_sleeping = True


    def change_image(self):
        if self.happy_point >= 70:
            return 'images/smiling-cat-for-web.jpg'
        elif self.happy_point > 40:
            return 'images/normal-cat.jpeg'
        elif self.happy_point <= 40:
            return 'images/sad-cat.jpg'
