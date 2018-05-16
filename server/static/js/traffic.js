var app = new Vue({
    el: '#app',
    data: {
        threats: [{
            "id": "dd36b79e",
            "threat": "SQLi",
            "time": "2018-04-02 16:51:57",
            "srcip": "8.8.8.8",
            "srcport": "11",
            "dstip": "127.0.0.1",
            "dstport": "77",
            "proto": "HTTP",
            "severity": "medium",
            "reference": "SQLmap Payload",
            "tags": "",
        }, {
            "id": "ecb1771b",
            "threat": "XSS",
            "time": "2018-04-02 16:51:57",
            "srcip": "8.8.8.8",
            "srcport": "11",
            "dstip": "127.0.0.1",
            "dstport": "77",
            "proto": "HTTP",
            "severity": "medium",
            "reference": "Nginx Waf",
            "tags": "",
        }, {
            "id": "c0a36f62",
            "threat": "RCE",
            "time": "2018-04-02 16:51:57",
            "srcip": "8.8.8.8",
            "srcport": "11",
            "dstip": "127.0.0.1",
            "dstport": "77",
            "proto": "HTTP",
            "severity": "high",
            "reference": "CVE-2018-7600",
            "tags": "",
        }, {
            "id": "c0a36f62",
            "threat": "scan",
            "time": "2018-04-02 16:51:57",
            "srcip": "8.8.8.8",
            "srcport": "11",
            "dstip": "127.0.0.1",
            "dstport": "77",
            "proto": "HTTP",
            "severity": "low",
            "reference": "Nmap Scan",
            "tags": "",
        }]
    },
    methods: {
        init: function() {
            $.ajax({
                type: 'post',
                url: 'create',
                data: {
                    name: name,
                },
                cache: false,
                dataType: 'json',
                success: (data) => {
                    if (data.status == "suc") {
                        this.islogin = true;
                        this.monsters = data.data;
                    } else {
                        alert(data.msg);
                    }
                },
                error: (err) => {
                    console.log('err', err);
                }
            });
        },
    }
});
