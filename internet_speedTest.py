#pip install speedtest-cli
import speedtest as st

def Speed_Test():
    test = st.SpeedTest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download Speed in Mbps: ", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload Speed in Mbps: ", up_speed)

    ping = test.results.ping
    print("Ping: ",ping)
Speed_Test()