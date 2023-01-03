import datetime

text_rest = """
127.0.0.1       localhost
127.0.1.1       makroscode-pc

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"""
text_focus = """
127.0.0.1       localhost
127.0.0.1      www.animefenix.com
127.0.0.1      www.youtube.com
127.0.1.1       makroscode-pc

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"""
date = datetime.datetime.now()


def file_create():
    
    if date.hour == 6 or date.hour == 21 or date.hour == 7 or date.hour == 8 or date.minute ==30:
        with open("/etc/hosts", "w", encoding="utf_8") as f:
            f.write(text_focus)
    elif date.hour == 18 or date.hour == 19 or date.hour ==20:
        with open("/etc/hosts", "w", encoding="utf_8") as f:
            f.write(text_rest)


def run():
    file_create()


if __name__ == '__main__':
    run()
