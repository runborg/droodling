# droodling

This is some sort of test code to implement a junos like configuration framework on linux.

components: 
rpc_server.py : Library for creating a unixsocket server
rpc_client.py : Library for talking to a rpc_server.py unix socket

configd.py    : crude test-implementation of a server using the rpc_server.py framework.
cli.py        : a Client talking to cli.py

z.zsh         : a library for zsh that creates some commands that are passed to configd.py via the unix socket



z.zsh:
This file should be sourced inside a zsh session using `. ./z.zsh`

sourcing this file creates multiple commands that talks to configd.py via cli.py and the unix socket.
commands created:
  configure : opens a configuration session to configd. This creates a env variables with the configd session id generated.
  show      : does not work, but should show the current configuration
  set       : does not work, but should set a config element
  delete    : does not work, but should delete a config element
  commit    : does not work, but should enable a configuration

the script should also intercept the tab key for command completion and the questionmark(?) for generating a help screen and forward it to configd.py
