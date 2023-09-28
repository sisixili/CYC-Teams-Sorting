import { student_info, Sequelize } from "../models";
const studentinfo = student_info;
const Op = Sequelize.Op;

// Create and Save a new student
export function create(req, res) {
    // Validate request
    if (!req.body.title) {
        res.status(400).send({
          message: "Content can not be empty!"
        });
        return;
    }
    const studentinfo = {
        title: req.body.title,
        description: req.body.description,
        published: req.body.published ? req.body.published : false
      };
       // Save Tutorial in the database
       student_info.create(studentinfo)
        .then(data => {
        res.send(data);
    })
    .catch(err => {
        res.status(500).send({
        message:
        err.message || "Some error occurred while creating the Tutorial."
        });
    });
}

// Retrieve all students from the database.
export function findAll(req, res) {
    const title = req.query.title;
    var condition = title ? { title: { [Op.like]: `%${title}%` } } : null;
  
    studentinfo.findAll({ where: condition })
      .then(data => {
        res.send(data);
      })
      .catch(err => {
        res.status(500).send({
          message:
            err.message || "Some error occurred while retrieving students."
        });
      });
}

// Find a single student with an id
export function findOne(req, res) {
    const id = req.params.id;

    studentinfo.findByPk(id)
      .then(data => {
        if (data) {
          res.send(data);
        } else {
          res.status(404).send({
            message: `Cannot find student with id=${id}.`
          });
        }
      })
      .catch(err => {
        res.status(500).send({
          message: "Error retrieving student with id=" + id
        });
      });
}

// Update a student by the id in the request
export function update(req, res) {
  
}

// Delete a student with the specified id in the request
export function deleteStudent(req,res) {

}