// ? This files contains all encapsulated logic usable queries of userInformation and expose as business logic
const table = require('../../connection')

const getActivitiesRecommendation = async activityIds => {
    const activities = await table('Activity')
        .select(['Activity_Name', 'Activity_Description'])
        .whereIn('Activity_ID', activityIds)

    return activities
}

module.exports = {
    getActivitiesRecommendation
}
