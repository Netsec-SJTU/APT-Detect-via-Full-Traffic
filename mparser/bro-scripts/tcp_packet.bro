event tcp_packet(c: connection, is_orig: bool, flags: string, seq: count, ack: count, len: count, payload: string){
    print fmt("^^^^^^^^^^^^^^^");
    # print fmt("Connection: %s", c);
    print fmt("is_orig: %s", is_orig);
    print fmt("flags: %s", flags);
    print fmt("sequence count: %d", seq);
    print fmt("ack: %d", ack);
    print fmt("len: %d", len);
    print fmt("^^^^^^^^^^^^^^^");
    print fmt("payload: %s", payload);
    print fmt("^^^^^^^^^^^^^^^");
}
