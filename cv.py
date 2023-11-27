import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import pytube
from kivy.core.audio import SoundLoader






class MainApp(App):
    def download_file(url):
                local_filename = url.split('/')[-1]
                r = requests.get(url, stream=True)
                with open("/home/smaron/Desktop/python files"+local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk: 
                            f.write(chunk)
    def down(self,link):
        
        link=self.solution.text
        l=link.find("https://www.youtube")
        if l is True:
            
                            

            earl = link
            download_file(earl)
            self.solution.text=''
            return 0
        if link=="":
            return 0
        elif l is not True:
            link=link.replace(' ','+')
            r=requests.get(f"https://www.youtube.com/results?search_query={link}").text
            k=r.find('watch?v=')
            lnk=f"https://www.youtube.com/{r[k:k+19]}"
            pytube.YouTube(lnk).streams.first().download()
            self.solution.text=""

    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False, readonly=False, halign="center", font_size=55)
        main_layout.add_widget(self.solution)
        equals_button = Button(text="Download",font_size=50, pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.down)
        sound=SoundLoader.load('/home/smaron/Desktop/songs/A202o632687774856250000.mp3')
        

        
       
        
        main_layout.add_widget(equals_button)
        
        return main_layout
if __name__ == '__main__':
    app = MainApp()
    app.run()
