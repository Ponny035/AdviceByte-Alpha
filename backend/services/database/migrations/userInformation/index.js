exports.up = function(knex) {
    return knex.schema.createTable('User_Information', table => {
        table.integer('User_ID')
        table.string('User_Name')
        table.string('Password')
        table.string('First_Name')
        table.string('Last_Name')
        table.string('E_Mail')
        table.integer('MBTI_ID')
        table.integer('Learning_Style_ID')
        table.integer('Study_Cluster_ID')
        table.float('Algorithm_Score')
        table.float('Data_Structure_Score')
        table.float('Programming_Score')
        table.float('Mathematic_Score')
        table.float('Language_Score')
        table.float('Communication_Score')
        table.float('Problem_Solving_Score')
        table.float('Self_Motivation_Score')
        table.timestamp('Create_At')
        table.timestamp('Update_At')
    })
}

exports.down = function(knex) {
    return knex.schema.dropTableIfExists('User_Information')
}
