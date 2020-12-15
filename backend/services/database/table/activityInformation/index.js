// ? This files contains all encapsulated logic usable queries of userInformation and expose as business logic
const table = require('../../connection')

const getActivitiesRecommendation = async activityIds => {
    const activities = await table('Activity')
        .select(['Activity_Name', 'Activity_Description'])
        .whereIn('Activity_ID', activityIds)

    return activities
}

const getActivitiesInformation = async activityId => {
    const {Activity_ID} = activityId
    const activity = await table('Activity')
        .select(['Activity_Name', 'Activity_Description'])
        .where({Activity_ID: Activity_ID })

    return activity
}


const addHistory = async (userId, activityId) => {
    await table('User_Activity_Status_History').insert({
        User_ID: userId,
        Activity_ID: activityId,
        Status_ID: 3
    })
}


module.exports = {
    getActivitiesRecommendation,
    getActivitiesInformation,
    addHistory
}
