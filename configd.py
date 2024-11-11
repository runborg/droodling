from rpc_server import create_server
from uuid import uuid4
from datetime import datetime
import pprint
server = create_server("/tmp/configcli.sock")


class cli:
    def __init__(self):
        self.sessions = {}
        self.config   = {}
        print("session system created")

    def session_new(self, session_name):
        print("new session called")
        if not session_name:
            session_name = str(uuid4())

        self.sessions[session_name] = {
                "date": datetime.now(),
                "config": self.config}
        
        return session_name


    def sessions_list(self):
        print("Listing sessions")
        return list(self.sessions.keys())

    def session_remove(self, session_name=None):
        print("Removing session")
        if not session_name in self.sessions:
            return False
        
        del(self.sessions[session_name])
        return True

    def config_show(self, session, edit_level):
        print("Config show")
        config = self.sessions[session_name]["config"]
        return pprint.pformat(config)

    def config_set(self, session, edit_level, option):
        print("Config set")

    def config_delete(self, session, edit_level, option):
        print("Config delete")

    def config_commit(self, session):
        print("Commit config")

    def compline(self, arg):
        ret = ""
        print("compline")
        ret +=f"Sent to completer '{arg[-1]}'\n"
        print(ret)
        return ret

with server:
    server.register_instance(cli())
    server.serve_forever()
