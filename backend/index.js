const express = require('express'),
    app = express()

// ? Plugins
const bodyParser = require('body-parser'),
    cors = require('cors'),
    cookieSession = require('cookie-session')

// ? Controllers
const userInformation = require('./controllers/userInformation')
const activityInformation = require('./controllers/activityInformation')
const forumInformation = require('./controllers/forumInformation')

// ? Initialize Plugins
app.use(bodyParser.json())
    .use(cors())
    .use(
        cookieSession({
            name: 'session',
            keys: [
                'THIS_SHOULD_BE_A_VERY_LONG_SECRET_THAT_SHOULD_BE_HARD_TO_GUESSED'
            ],
            httpOnly: true
        })
    )

app.get('/', async (req, res) => {
    res.send('Server is working')
})

app.use('/user', userInformation)
app.use('/activity', activityInformation)
app.use('/forum', forumInformation)

app.listen(3000, () => {
    console.log('> Listening at http://localhost:3000')
})
