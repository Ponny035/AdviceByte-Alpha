const knex = require('knex')({
    client: 'mysql',
    connection: {
        host: 'localhost:3306',
        user: 'root',
        password: process.env.PASSWORD,
        database: 'AdviceByte'
    }
})

module.exports = knex
