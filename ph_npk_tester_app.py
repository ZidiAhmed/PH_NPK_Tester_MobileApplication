from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import objc

class PhNpkTesterApp(BoxLayout):
    def __init__(self, **kwargs):
        super(PhNpkTesterApp, self).__init__(**kwargs)

        self.orientation = 'vertical'

        intro_label = Label(text="Welcome to the Ph and NPK Tester App!\nConnect your NPK and Water pH sensors.")
        self.add_widget(intro_label)

        self.water_ph_label = Label(text="Water pH:")
        self.add_widget(self.water_ph_label)

        self.npk_label = Label(text="NPK Values:")
        self.add_widget(self.npk_label)

        update_button = Button(text="Start Test")
        update_button.bind(on_press=self.show_popup)
        self.add_widget(update_button)

        self.bluetooth_device = None

    def update_values(self, nitrogen_val, phosphorus_val, potassium_val):
        water_ph = f"Water pH: {self.get_water_ph()}"
        npk = f"N: {nitrogen_val}, P: {phosphorus_val}, K: {potassium_val}"

        self.water_ph_label.text = water_ph
        self.npk_label.text = npk

    def show_popup(self, instance):
        if self.bluetooth_device is not None:
            # Simulate receiving data from Arduino via Bluetooth
            nitrogen_val = 25  # Replace with actual values
            phosphorus_val = 40
            potassium_val = 60

            self.update_values(nitrogen_val, phosphorus_val, potassium_val)
        else:
            self.show_sensor_not_connected_popup()

    def discover_bluetooth_devices(self):
        devices = objc.lookUpClass('IOBluetoothDevice').pairedDevices()
        if devices:
            self.bluetooth_device = devices[0]  # Assuming the first paired device is the one you want
            print(f"Found Bluetooth device: {self.bluetooth_device.name().UTF8String()}")
        else:
            print("No paired Bluetooth devices found.")

    def get_water_ph(self):
        # Implement the method to get water pH
        return 7.0  # Replace with actual water pH value

    def show_sensor_not_connected_popup(self):
        popup = Popup(title='Sensor Not Connected',
                      content=Label(text='Please connect the NPK and Water pH sensors.'),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class PhNpkTesterAppApp(App):
    def build(self):
        app = PhNpkTesterApp()
        app.discover_bluetooth_devices()  # Automatically discover paired Bluetooth devices on app startup
        return app

if __name__ == '__main__':
    PhNpkTesterAppApp().run()
