module.exports = (sequelize, Sequelize) => {
    const studentinfo = sequelize.define("student_info", {
      title: {
        type: Sequelize.STRING
      },
      description: {
        type: Sequelize.STRING
      },
      published: {
        type: Sequelize.BOOLEAN
      }
    });
  
    return studentinfo;
  };