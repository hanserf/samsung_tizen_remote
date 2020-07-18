from samsungtv import SamsungTV
class RemoteCtrl():
    def __init__(self,ip='192.168.86.27'):
        self.tv = SamsungTV(ip)

    def key_power(self):
        self.tv.power()
    def key_home(self):
        # Home
        self.tv.home()
    def key_menu(self):
        self.tv.menu()
    def key_source(self):
        self.tv.source()
    def key_guide(self):
        self.tv.guide()

    def key_tools(self):
        self.tv.tools()
    def key_info(self):
        self.tv.info()

    def key_arrow_up(self):
        self.tv.up(count=1)

    def key_arrow_down(self):
        self.tv.down(count=1)

    def key_arrow_left(self):
        self.tv.left(count=1)

    def key_arrow_right(self):
        self.tv.right(count=1)

    def key_execute(self):
        self.tv.enter(count=1)

    def key_return(self):
        self.tv.back(count=1)

    def key_ch_list(self):
        # channel
        self.tv.channel_list()

    def key_ch(self,ch):
        self.tv.channel(ch)

    def key_num(self,digit):
        self.tv.digit(d=digit)

    def key_ch_up(self):
        self.tv.channel_up(count=1)

    def key_ch_down(self):
        self.tv.channel_down(count=1)

    # volume
    def key_vol_up(self):
        self.tv.volume_up(count=1)

    def key_vol_down(self):
        self.tv.volume_down(count=1)

    def key_mute(self):
        self.tv.mute()

    # extra
    def key_color_ctrl_red(self):
        self.tv.red()
    def key_color_ctrl_green(self):
        self.tv.green()
    def key_color_ctrl_blue(self):
        self.tv.blue()
