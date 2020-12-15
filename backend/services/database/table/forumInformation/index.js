// ? This files contains all encapsulated logic usable queries of userInformation and expose as business logic
const table = require('../../connection')

// ? Read

const getforum = async forumId => {
    const query = "SELECT Activity_Name FROM Activity WHERE `Activity_ID` IN (SELECT `Activity_ID` FROM `Forum`)"
    const result = await table.schema.raw(query)
    const activity_name = result[0]
    return activity_name
}

const getActivityId = async forumId => {
    const activityId = await table('Forum')
        .select([
            'Activity_ID'
        ])
        .where({
            Forum_ID: forumId
        })
        .first()

    return activityId
}

const getCommemt = async forumId => {
    const activityId = await table('Comment')
        .select([
            'Comment'
        ])
        .where({
            Forum_ID: forumId
        })

    return activityId
}

const addCommemt = async (forumId, comment) => {
    await table('Comment').insert({
        Forum_ID: forumId,
        Comment: comment
    })
}

module.exports = {
    getActivityId,
    getCommemt,
    getforum,
    addCommemt
}

