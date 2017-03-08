#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import _socket

s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)

# bind ports
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999....')

while True:
    # receive data
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)