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
        const forumId = req.body.forumId

        let activityId = await forumInformation.getActivityId(forumId)

        let information = await activityInformation.getActivitiesInformation(activityId)

        res.send(information)
    })

    .post('/commentInformation', async (req, res) => {
        const forumId = req.body.forumId

        let comment = await forumInformation.getCommemt(forumId)

        res.send(comment)
    })

    .post('/addComment', async (req, res) => {
        let {forumId, comment} = req.body

        await  forumInformation.addCommemt(forumId, comment)

        res.send(`comment Added`)
    })

module.exports = router

