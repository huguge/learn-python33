#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import _socket

s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # send data
    s.send(data, ('127.0.0.1', 9999))
    # reveive data
    print(s.recv(1024).decode('utf-8'))

s.close()