global g_clikd_btn
global g_sock

g_clikd_btn = None
g_sock = None


def get_clikd_btn():
    global g_clikd_btn
    return g_clikd_btn


def get_sock():
    global g_sock
    return g_sock


def set_clikd_btn(btn):
    global g_clikd_btn
    g_clikd_btn = btn


def set_sock(sock):
    global g_sock
    g_sock = sock
