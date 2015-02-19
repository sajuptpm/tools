
AUTH_HOST=192.168.56.101
AUTH_URL=http://$AUTH_HOST:5000/v2.0
ADMIN_PASSWORD=nova




function replace_ContrailPlugin_ini_conf()
{
	file="/etc/contrail/ContrailPlugin.ini"
	check_replace_value $file KEYSTONE auth_host $AUTH_HOST
        check_replace_value $file KEYSTONE auth_url $AUTH_URL
	check_replace_value $file KEYSTONE admin_password $ADMIN_PASSWORD
}





#############Helper Functions###################

function ini_has_option() {
    local file=$1
    local section=$2
    local option=$3
    local line
    line=$(sed -ne "/^\[$section\]/,/^\[.*\]/ { /^$option[ \t]*=/ p; }" "$file")
    [ -n "$line" ]
}

function iniset() {
    local file=$1
    local section=$2
    local option=$3
    local value=$4

    [[ -z $section || -z $option ]] && return

    if ! grep -q "^\[$section\]" "$file" 2>/dev/null; then
        # Add section at the end
        echo -e "\n[$section]" >>"$file"
    fi
    if ! ini_has_option "$file" "$section" "$option"; then
        # Add it
        sed -i -e "/^\[$section\]/ a\\
$option = $value
" "$file"
    else
        local sep=$(echo -ne "\x01")
        # Replace it
        sed -i -e '/^\['${section}'\]/,/^\[.*\]/ s'${sep}'^\('${option}'[ \t]*=[ \t]*\).*$'${sep}'\1'"${value}"${sep} "$file"
    fi
}


function check_replace_value()
{
    file=$1
    section=$2
    key=$3
    value=$4
    if [[ -n "$value" ]]; then
        if [[ -n "$section" ]]; then
            iniset $file $section $key $value
        else
            iniset $file "DEFAULTS" $key $value
        fi
    fi
}



########################

replace_ContrailPlugin_ini_conf




