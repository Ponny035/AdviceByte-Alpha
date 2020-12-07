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
const addNewUser = async (username, password) => {
    await table('User_Information').insert({
        User_Name: username,
        Password: password
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

module.exports = {
    isUserExisted,
    getUserID,
    addNewUser,
    getInformation,
    getAVGInformation
}
