class Node():
  def __init__(self):
    self.name = ""
    self.id = ""
    self.macs = set()
    self.addresses = set()
    self.interfaces = dict()
    self.flags = dict({
      "online": False,
      "gateway": False,
      "client": False
    })
    self.gps = None
    self.firmware = None
    self.model = None
    self.uptime = None
    self.clientcount = 0
    self.autoupdater = dict({
      "enabled": None,
      "branch": None
    })

  def add_address(self, address):
    address = address.lower()
    self.addresses.add(address)

  def add_mac(self, mac):
    mac = mac.lower()
    if len(self.macs) == 0:
      self.id = mac

    self.macs.add(mac)

    self.interfaces[mac] = Interface()

  def __repr__(self):
    return self.macs.__repr__()

class Interface():
  def __init__(self):
    self.vpn = False

