var app = new Vue({
    el: '#app',
    data: {
        threats: [],
        pages: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    methods: {
        async loadThreats() {
            this.threats = await api('api/traffic')
        },
    }
});

app.loadThreats();
