#!/bin/bash

cd $(dirname $0)

export PATH=/usr/sbin:/usr/local/sbin:$PATH

PEERS=/etc/fastd/ffmuc-mesh-vpn/peers
ALIASES=/opt/ffmap-backend/aliases_peers.json
DEST=/usr/share/nginx/html/ffmap/

set -e

"$(dirname "$0")"/mkaliases.py -p $PEERS -d $ALIASES
"$(dirname "$0")"/bat2nodes.py -A -a $ALIASES -a /opt/ffmap-backend/aliases.json -o -d $DEST

