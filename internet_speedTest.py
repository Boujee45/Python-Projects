#pip install speedtest-cli
import speedtest as st

def Speed_Test():
    # 1. Initialize the class with ()
    test = st.Speedtest()

    print("Loading server list and finding best server...")
    test.get_best_server() # Optional: finds the fastest server for you

    # 2. Call the methods with () to actually run the test
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download Speed in Mbps: ", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload Speed in Mbps: ", up_speed)

    # 3. Access results after the tests have run
    ping = test.results.ping
    print("Ping: ", ping)

Speed_Test()