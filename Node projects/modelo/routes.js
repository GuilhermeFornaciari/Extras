const express = require("express");
const routes = express.Router();

//requires
homecontroller = require("./controllers/home");

//controllers
routes.get("/", homecontroller.paginainicial);

module.exports = routes;
