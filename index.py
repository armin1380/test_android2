# Import modules and libraries
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera # Import Camera module

# Define your custom widget class
class MyWidget(Widget):
    # Define your widget behavior and properties
    pass

# Define your app class
class MyApp(App):
    # Override the build method
    def build(self):
        # Create a camera instance with index 0 (front camera)
        self.camera = Camera(resolution=(640, 480), index=0)
        # Set the camera to play automatically
        self.camera.play = True
        # Save the image inside a directory in internal memory inside of download folder
        self.camera.export_to_png('/storage/emulated/0/Download/selfie.png')
        # Return the camera widget
        return self.camera

# Run the app
if __name__ == '__main__':
    MyApp().run()