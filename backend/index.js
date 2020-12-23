const express = require('express')
const app = express()

// ? Plugins
const cors = require('cors')
const cookieSession = require('cookie-session')

// ? Controllers
const userInformation = require('./controllers/userInformation')
const activityInformation = require('./controllers/activityInformation')
const forumInformation = require('./controllers/forumInformation')

// ? Initialize Plugins
app.use(express.json())
    .use(cors())
    .use(
        cookieSession({
            name: 'session',
            keys: [process.env.SECRET],
            httpOnly: true
        })
    )
app.get('/', async (req, res) => {
    res.send('Server is working')
})

app.use('/user', userInformation)
app.use('/activity', activityInformation)
app.use('/forum', forumInformation)

app.listen(process.env.PORT, () => {
    console.log(`> Listening on port ${process.env.PORT}`)
})
