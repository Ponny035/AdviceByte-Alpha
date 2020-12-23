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
app.get('/api/', async (req, res) => {
    res.send('Server is working')
})

app.use('/api/user', userInformation)
app.use('/api/activity', activityInformation)
app.use('/api/forum', forumInformation)

app.listen(process.env.PORT, () => {
    console.log(`> Listening on port ${process.env.PORT}`)
})
