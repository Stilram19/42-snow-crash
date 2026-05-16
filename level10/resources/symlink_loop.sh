#!/bin/bash

while true; do
    rm -f /tmp/sl
    touch /tmp/sl
    rm -f /tmp/sl
    ln -s ~/token /tmp/sl
done
