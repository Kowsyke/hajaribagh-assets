#!/bin/bash
exec /opt/jdk-25/bin/java -Xms4096M -Xmx8192M -XX:+UseZGC -jar fabric-server-launch.jar nogui
