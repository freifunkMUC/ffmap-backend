

Alfred has to run in the background, e.g.

  `alfred -i br-ffm`

Set up a crontab to generate the nodes.json used by the ffmap frontend, e.g.

  `* * * * * /opt/ffmap-backend/mkmap.sh .`

To generate the more detailed nodes_load.json, also add a crontab for it, e.g.

  `0-59/5 * * * * alfred-json -r 159 -f json -z > /var/www/ffmap/nodes_load.json`
  
