from Foundation import NSUserNotification, NSUserNotificationCenter

def notify(title, message):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setInformativeText_(message)
    notification.setSoundName_("NSUserNotificationDefaultSoundName")
    NSUserNotificationCenter.defaultUserNotificationCenter().deliverNotification_(notification)
