const connection = require('./connection')
const { userInformation, activityInformation,forumInformation } = require('./table')

module.exports = {
    connection,
    userInformation,
    forumInformation,
    activityInformation
}