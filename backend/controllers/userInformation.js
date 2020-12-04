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

        let userId = await userInformation.getUserID(username, password)

        if (!userId) return res.send('Username of Password is incorrect')

        req.session.userId = userId

        res.send('Successfully Login')
    })
    .post('/create', async (req, res) => {
        let { username, password } = req.body

        await userInformation.addNewUser(username, password)

        res.send(`${username} Added`)
    })
    .post('/information', async (req, res) => {
        let userId = req.session.userId

        if (!userId) return res.status(403).send('Unanthorized')

        let information = await userInformation.getInformation(
            req.session.userId
        )

        res.send(information)
    })
    .post('/logout', async (req, res) => {
        req.session.userId = undefined

        res.send('Logout')
    })

module.exports = router
