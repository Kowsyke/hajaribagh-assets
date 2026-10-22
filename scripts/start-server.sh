#!/bin/bash
cd "$(dirname "$0")"
exec /usr/bin/java -Xms1536M -Xmx2560M -XX:+UseZGC -jar fabric-server-launch.jar nogui
