const knex = require('knex')({
    client: 'mysql',
    connection: {
        host: 'localhost:3306',
        user: 'root',
        password: 'advicebyte',
        database: 'AdviceByte'
    }
})

module.exports = knex
