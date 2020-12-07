const { activityInformation } = require('../services/database')

const express = require('express'),
    router = express.Router()

router
    .post('/information', async (req, res) => {
        let {activityId} = req.body
        console.log(activityId)

        let information = await activityInformation.getInformation(activityId)

        res.send(information)
    })
module.exports = router
