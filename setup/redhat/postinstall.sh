#!/bin/sh

set -e

TUNIERP_CONFIGURATION_DIR=/etc/tunierp
TUNIERP_CONFIGURATION_FILE=$TUNIERP_CONFIGURATION_DIR/openerp-server.conf
TUNIERP_DATA_DIR=/var/lib/tunierp
TUNIERP_GROUP="tunierp"
TUNIERP_LOG_DIR=/var/log/tunierp
TUNIERP_USER="tunierp"

if ! getent passwd | grep -q "^tunierp:"; then
    groupadd $TUNIERP_GROUP
    adduser --system --no-create-home $TUNIERP_USER -g $TUNIERP_GROUP
fi
# Register "$TUNIERP_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $TUNIERP_USER" 2> /dev/null || true
# Configuration file
mkdir -p $TUNIERP_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $TUNIERP_USER
db_password = False
addons_path = /usr/lib/python2.7/site-packages/openerp/addons
" > $TUNIERP_CONFIGURATION_FILE
chown $TUNIERP_USER:$TUNIERP_GROUP $TUNIERP_CONFIGURATION_FILE
chmod 0640 $TUNIERP_CONFIGURATION_FILE
# Log
mkdir -p $TUNIERP_LOG_DIR
chown $TUNIERP_USER:$TUNIERP_GROUP $TUNIERP_LOG_DIR
chmod 0750 $TUNIERP_LOG_DIR
# Data dir
mkdir -p $TUNIERP_DATA_DIR
chown $TUNIERP_USER:$TUNIERP_GROUP $TUNIERP_DATA_DIR

INIT_FILE=/lib/systemd/system/tunierp.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << 'EOF' > $INIT_FILE
[Unit]
Description=TuniERP Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=tunierp
Group=tunierp
ExecStart=/usr/bin/tunierp.py --config=/etc/tunierp/openerp-server.conf

[Install]
WantedBy=multi-user.target
EOF
easy_install pyPdf vatnumber pydot psycogreen
