const { userInformation } = require('../services/database')

const express = require('express'),
    router = express.Router()

router
    .get('/:username', async (req, res) => {
        let { username } = req.params

        let user = await userInformation.isUserExisted(username)

        res.send(`${username} is${!user ? ' not' : ''} existed`)
    })
    .post('/login', async (req, res) => {
        let { username, password } = req.body

        let User_ID = await userInformation.getUserID(username, password)

        if (!User_ID) return res.send('Username of Password is incorrect')

        res.send(User_ID)
    })
    .post('/create', async (req, res) => {
        let { username, password } = req.body

        await userInformation.addNewUser(username, password)

        res.send(`${username} Added`)
    })
    .post('/information', async (req, res) => {
        const userId = req.body.userId

        if (!userId) return res.status(403).send('Unanthorized')

        let information = await userInformation.getInformation(userId)

        res.send(information)
    })
    .post('/avginformation', async (req, res) => {
        let avginformation = await userInformation.getAVGInformation()

        res.send(avginformation)
    })

    .post('/finishActivity', async (req, res) => {
        const userId = req.body.userId
        
        if (!userId) return res.status(403).send('Unanthorized')

        let activityCount = await userInformation.getFinishActivity(userId)

        res.send(activityCount+"")
    })

module.exports = router

