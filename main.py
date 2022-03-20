from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file("mainapp.kv")


class FirstScreen(Screen):

    def get_image(self):
        # get query from user
        query = self.manager.current_screen.ids.user_query.text
        # get images from wikipedia
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        headers = {'User-agent': 'Mozilla/5.0'}
        req = requests.get(self.get_image(), headers=headers)
        file = open("files/image.jpg", "wb")
        image_path = "files/image.jpg"
        file.write(req.content)
        return image_path

    def search_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
