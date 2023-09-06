const { User } = require("../models/userModel");

exports.Login = (req, res) => {
  console.log(res.locals);
  res.render("Login");
};

exports.loginSubmit = (req, res) => {
  console.log("Login");
  res.send(req.body);
};
exports.registerSubmit = async (req, res) => {
  newuser = new User(req.body);
  await newuser.register();

  if (newuser.error.length > 0) {
    req.flash("msgs", newuser.error);
    req.flash("cssClass", "error");
    req.flash("element", "FormRegister");

    req.session.save(() => res.redirect("/Login"));
    return;
  }

  res.send(req.body);
};
