import kivy
from kivy.app import App
from kivy.uix.label import Label
import iperf3

class MyIperf3App(App):
    def build(self):
        client = iperf3.Client()
        # client.server_hostname = 'iperf3-server-hostname'
        # client.port = 5201
        # result = client.run()
        
        # if result.error:
        #     text = f'Error: {result.error}'
        # else:
        #     text = f'Upload: {result.sent_Mbps} Mbps, Download: {result.received_Mbps} Mbps'

        return Label(text="Hello")

if __name__ == '__main__':
    MyIperf3App().run()
