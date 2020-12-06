const knex = require('knex')({
    client: 'mysql',
    connection: {
        host: '35.247.156.20',
        user: 'sqlquery',
        password: '5tbu8uuQTWeHgV0Q',
        database: 'AdviceByte'
    }
})

module.exports = knex
