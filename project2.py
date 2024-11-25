class Device:
    def __init__(self, device_id, device_name):
        self.device_id = device_id
        self.device_name = device_name
    def device_info(self):
        print(f"Device ID: {self.device_id}, Device Name: {self.device_name}")
class WirelessDevice:
    def __init__(self, connectivity_type, frequency):
        self.connectivity_type = connectivity_type
        self.frequency = frequency
    def wireless_info(self):
        print(f"Connectivity Type: {self.connectivity_type}, Frequency: {self.frequency} GHz")
class smartdevice(Device,WirelessDevice):
    def __init__(self, device_id, device_name, connectivity_type, frequency, os_type):
        Device.__init__(self,device_id, device_name)
        WirelessDevice.__init__(self, connectivity_type, frequency)
        self.os_type = os_type
    def smart_info(self):
        print(f"OS Type: {self.os_type}")
         
phn=smartdevice(100,"iphone","WiFi",30,"IOS")
phn.device_info()
phn.wireless_info()
phn.smart_info()