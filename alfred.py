#!/usr/bin/env python3
from subprocess import Popen, PIPE
import json
import os

class alfred:
  def __init__(self,request_data_type = 158):
   	self.request_data_type = request_data_type

  def add_sudo_if_nonroot(self, command_array ):
    """ Adds "sudo" to the command array if the calling user is not root (uid != 0)
    """
    if os.getuid() != 0:
        command_array.insert(0, "sudo")
	
    return command_array

  def aliases(self):

    command = self.add_sudo_if_nonroot(["alfred-json","-r",str(self.request_data_type),"-f","json","-z"])

    alias = {}

    try:
      proc = Popen(command, stdout=PIPE)
      output = proc.communicate()[0]
    except:
      # Killing alfred proc in case of errors, otherwise it will stay FOREVER
      proc.terminate()
      proc.kill()
      return alias

    try:
      alfred_data = json.loads(output.decode("utf-8"))
    except:
      return alias

    for mac,node in alfred_data.items():
      node_alias = {}
      if 'location' in node:
        try:
          node_alias['gps'] = str(node['location']['latitude']) + ' ' + str(node['location']['longitude'])
        except:
          pass

      try:
        node_alias['addresses'] = node['network']['addresses']
      except KeyError:
        pass  
    
      try:
        node_alias['firmware'] = node['software']['firmware']['release']
      except KeyError:
        pass

      try:
        node_alias['model'] = node['hardware']['model']
      except KeyError:
        pass

      try:
        node_alias['uptime'] = node['statistics']['uptime']
      except KeyError:
        pass

      try:
        node_alias['contact'] = node['owner']['contact']
      except KeyError:
        pass

      try:
        node_alias['autoupdater_enabled'] = node['software']['autoupdater']['enabled']
      except KeyError:
        pass
     
      try:
        node_alias['autoupdater_branch'] = node['software']['autoupdater']['branch']
      except KeyError:
        pass
     
      try:
        node_alias['id'] = node['network']['mac']
      except KeyError:
        pass

      if 'hostname' in node:
        node_alias['name'] = node['hostname']
      elif 'name' in node:
        node_alias['name'] = node['name']
      if len(node_alias):
        alias[mac] = node_alias
    return alias

if __name__ == "__main__":
  ad = alfred()
  al = ad.aliases()
  print(al)
