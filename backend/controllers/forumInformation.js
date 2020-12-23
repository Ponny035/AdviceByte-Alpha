const { forumInformation } = require('../services/database')
const { activityInformation } = require('../services/database')

const express = require('express'),
    router = express.Router()

router

    .post('/forumList', async (req, res) => {

        let list = await forumInformation.getforum()

        res.send(list)
    })

    .post('/herderInformation', async (req, res) => {
        const forumId = req.body.activityId

        let activityId = await forumInformation.getActivityId(forumId)
        const {Activity_ID} = activityId
        let information = await activityInformation.getActivitiesInformation(Activity_ID)

        res.send(information)
    })


    .post('/commentInformation', async (req, res) => {
        const forumId = req.body.forumId

        let comment = await forumInformation.getCommemt(forumId)

        res.send(comment)
    })

    .post('/addComment', async (req, res) => {
        let {forumId, comment, userId} = req.body

        await  forumInformation.addCommemt(forumId, comment)

        let activityId = await forumInformation.getActivityId(forumId)
        const {Activity_ID} = activityId

        activityInformation.addHistory(userId, Activity_ID)

        res.send(`comment Added`)
    })

module.exports = router

