@load base/utils/files

module Conn;

event connection_established(c: connection)
    {
        local orig_f = open("tets_file");
        set_contents_file(c$id, CONTENTS_BOTH, orig_f);

    }
