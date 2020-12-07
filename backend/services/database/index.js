const connection = require('./connection')
const { userInformation, activityInformation } = require('./table')

module.exports = {
    connection,
    userInformation,
    activityInformation
}