class Notification:
    def send_alert(self, message, user = None):
        if user != None:
            print(f"Alert for {user}: {message}")
        else:
            print(f"General Alert {message}")

my_notif = Notification()
my_notif.send_alert("System maintenance at midnight.")
my_notif.send_alert("Your password expires in 3 days.", "Rahim")