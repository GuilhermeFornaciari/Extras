const express = require("express");
const routes = express.Router();

//requires
homecontroller = require("./src/controllers/home");

//controllers
routes.get("/", homecontroller.paginainicial);
routes.post("/", homecontroller.paginainicialpost);

module.exports = routes;
