// ? This files contains all encapsulated logic usable queries of userInformation and expose as business logic
const table = require('../../connection')

const getInformation = async activityId => {
    console.log(activityId)
    const activity = await table('Activity')
        .select([
            'Activity_Name',
            'Activity_Description'
        ])
        .where({
            Activity_ID: activityId
        })
        .first()

    return activity
}

module.exports = {
    getInformation
}
