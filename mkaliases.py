#!/usr/bin/env python3
# Make aliases script ported to python
# author: baldo,sargon 

import os
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p','--peers-source', action='store',
                    help='directory where peer descriptions are stored',required=True)

parser.add_argument('-d','--destination-file', action='store',
                    help='destination file for generated alias list',required=True,
                    metavar='FILE')

args = parser.parse_args();

options = vars(args)

# TODO Sanity checks

peerlist = {}

for fn in os.listdir(options['peers_source']):
  absFn = options['peers_source'] + '/' + fn
  if os.path.isfile(absFn):
    peerfile = open(absFn,'r')
    try:
      peerlines = peerfile.readlines()
      peer = {}
      mac  = None
      for pl in peerlines:
        pls = pl.split() 

        if len(pls) > 1:
          if pls[1] == "Knotenname:":
            peer['name'] = pls[2]
          elif pls[1] == "Koordinaten:":
            peer['gps'] = ' '.join(pls[2:])
          elif pls[1] == "MAC:":
            # TODO Validity checks
            mac = pls[2]
#          elif pls[0] == "remote":
          elif pls[1] == "remote":  #geänderde syntax!
            peer['vpn'] = True
      if mac:
        peerlist[mac] = peer 
    except UnicodeDecodeError as e:
      print("Decoding error in %s, ignoring peer: %s" % (absFn,e));
    finally:
      peerfile.close()

alias_json = open(options['destination_file'],'w')
try:
  alias_json.write(json.dumps(peerlist))
finally:
  alias_json.close()
