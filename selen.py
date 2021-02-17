from selenium import webdriver


class D:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://play.aidungeon.io/main/play?publicId=56a97c53-a172-4bab-8c62-c9335d4f333c')

if __name__ == '__main__':
    x = D()