var app = new Vue({
    el: '#app',
    data: {
        threats: [
            ["xxx", "2018-04-02T16:51:57+08:00", "8.8.8.8", "11", "127.0.0.1", "77", "miao", "miao"]
        ],
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