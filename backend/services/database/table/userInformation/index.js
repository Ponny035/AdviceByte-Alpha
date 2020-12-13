// ? This files contains all encapsulated logic usable queries of userInformation and expose as business logic
const table = require('../../connection')

// ? Read
const isUserExisted = async username => {
    const data = await table('User_Information')
        .select('User_Name')
        .where({
            User_Name: username
        })
        .first()
        .catch(error => {
            throw error
        })

    return data
}

const isEmailExisted = async email => {
    const data = await table('User_Information')
        .select('E_Mail')
        .where({
            E_Mail: email
        })
        .first()
        .catch(error => {
            throw error
        })

    return data
}

// ? Read
const getUserID = async (username, password) => {
    const data = await table('User_Information')
        .select('User_ID')
        .where({
            User_Name: username,
            Password: password
        })
        .first()
        .catch(error => {
            throw error
        })

    return data
}

// ? Read
const addNewUser = async (username, password, firstname, lastname, email, mbtiid, learningstyleid) => {
    await table('User_Information').insert({
        User_Name: username,
        Password: password,
        First_Name: firstname,
        Last_Name: lastname,
        E_Mail: email,
        MBTI_ID: mbtiid,
        Learning_Style_ID: learningstyleid
    })
}

const getInformation = async userId => {
    const score = await table('User_Information')
        .select([
            'Algorithm_Score',
            'Data_Structure_Score',
            'Programming_Score',
            'Mathematic_Score',
            'Language_Score',
            'Communication_Score',
            'Self_Motivation_Score',
            'Problem_Solving_Score'
        ])
        .where({
            User_ID: userId
        })
        .first()

    return score
}

const getFinishActivity = async userId => {
    const query = "SELECT COUNT(`User_ID`) AS count FROM `User_Activity_Status_History` WHERE (CURRENT_DATE - DATE(`Update_At`)) < 30 AND `Status_ID` = 3 AND `User_ID` = " + userId + " GROUP BY `User_ID`"
    const result = await table.schema.raw(query)
    const count = result[0][0]['count']
    return count
}

const getAVGInformation = async userId => {
    const score = await table('User_Information')
        .select([
            'Algorithm_Score',
            'Data_Structure_Score',
            'Programming_Score',
            'Mathematic_Score',
            'Language_Score',
            'Communication_Score',
            'Self_Motivation_Score',
            'Problem_Solving_Score'
        ])
        .where({
            User_ID: 0
        })
        .first()

    return score
}

const getFirstName = async userId => {
    const name = await table('User_Information')
        .select([
            'First_Name'
        ])
        .where({
            User_ID: userId
        })
        .first()

    return name
}

module.exports = {
    isUserExisted,
    getUserID,
    addNewUser,
    getInformation,
    getFinishActivity,
    getAVGInformation,
    getFirstName,
    isEmailExisted
}

