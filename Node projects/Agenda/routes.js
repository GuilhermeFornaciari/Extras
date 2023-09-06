const express = require("express");
const { Contacts } = require("./src/controllers/contacts");
const routes = express.Router();

//requires
contactsController = require("./src/controllers/contacts");
loginController = require("./src/controllers/Login");

//controllers
routes.get("/Contacts", contactsController.Contacts);
routes.get("/Register", contactsController.registerPage);
routes.get("/Login", loginController.Login);

routes.post("/RegisterContact", contactsController.submitForm);
routes.post("/Login/login", loginController.loginSubmit);
routes.post("/Login/register", loginController.registerSubmit);

module.exports = routes;
