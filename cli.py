from rpc_client import connect_client
import shlex
import sys
import os


def exit_help(msg):
    print(msg)
    print(".....")
    sys.exit(1)


class cli():
    def __init__(self, client):
        self.client=client

    def cmd_session_new(self, args):
        n = self.client.session_new(False)
        print(n)

    def cmd_sessions_list(self, args):
        print("list sessions")
        print(self.client.sessions_list())

    def cmd_session_remove(self, args):
        print("remove session")
        if len(args) != 1:
            exit_help("Wrong number of args")

    def cmd_config_show(self, args):
        session = os.getenv("CONFIG_SESSION")
        level = shlex.split(os.getenv("CONFIG_EDIT_LEVEL", ''))
        print("!Config")
        print(self.client.config_show(session, level))

    def cmd_config_set(self, args):
        session = os.getenv("CONFIG_SESSION")
        level = shlex.split(os.getenv("CONFIG_EDIT_LEVEL", ''))
        print("Set config")
        self.client.config_set(session, level, args)

    def cmd_config_del(self, args):
        session = os.getenv("CONFIG_SESSION")
        level = shlex.split(os.getenv("CONFIG_EDIT_LEVEL", ''))
        print("Delete config")
        self.client.config_delete(session, level, args)

    def cmd_config_commit(self, args):
        session = os.getenv("CONFIG_SESSION")
        self.client.config_commit()

    def cmd_comp_set(self, args):
        print(shlex.split(" ".join(args)), file=sys.stderr)

    def cmd_compline(self, args):
        if len(args) < 1:
            exit_help("not enough arguments")

        print(self.client.compline(args[0]))

if __name__ == "__main__":
    client = connect_client("/tmp/configcli.sock")
    if len(sys.argv) < 2:
        print(sys.argv)
        exit_help("No arguments passed to cli")

    cli_commands = cli(client)
    args = list(sys.argv[1:])
    command = args.pop(0).lower()
    cmd = getattr(cli_commands, f'cmd_{command}')
    cmd(args)
