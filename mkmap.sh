#!/bin/bash

cd $(dirname $0)

export PATH=/usr/sbin:/usr/local/sbin:$PATH

PEERS=/etc/fastd/ffm-mesh-vpn/peers/
ALIASES=/opt/ffmap-backend/aliases_fastd.json
DEST=/var/www/ffmap-d3/

set -e

"$(dirname "$0")"/mkaliases.py -p $PEERS -d $ALIASES
"$(dirname "$0")"/bat2nodes.py -A -a $ALIASES -a /var/www/ffmap-d3/ffmap-backend/aliases.json -o -d $DEST
#./bat2nodes.py -A -m bat0 -d $DEST
#"$(dirname "$0")"/bat2nodes.py -A -d $DEST


