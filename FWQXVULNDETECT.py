import socket

def port_taraması(ip_adresi):
    # Port taramasını daha verimli hale getirmek için, `SYN` taraması kullanılmaktadır.
    for port in range(1, 65535):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect_ex((ip_adresi, port))
            if sock.getpeername()[1] == port:
                sock.close()
                print('IP adresi:', ip_adresi, 'Port:', port)
        except:
            pass

# Örnek kullanım:
ip_adresi = input('IP adresi girin: ')
port_taraması(ip_adresi)

# Yapımcı bilgisi
print('Yapımcı: FWQX | ST40L ve FWQX CYBER TEAM')

