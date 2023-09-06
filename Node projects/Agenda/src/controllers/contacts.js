const { NewContact, contactModel } = require("../models/contactModel");

exports.Contacts = (req, res) => {
  res.render("Contacts");
};
exports.registerPage = (req, res) => {
  res.render("register");
};

exports.submitForm = (req, res) => {


  const Contact = new NewContact(
    req.body.name,
    req.body.lastname,
    req.body.email,
    req.body.fone
  );

  res.send(Contact);
};
