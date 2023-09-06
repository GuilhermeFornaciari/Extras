const mongoose = require("mongoose");
const validator = require("validator");

const UserSchema = new mongoose.Schema({
  email: { type: String, required: true },
  psswd: { type: String, required: true },
});

const UserModel = mongoose.model("User", UserSchema);

module.exports.User = class User {
  constructor(body) {
    this.body = body;
    this.error = [];
    this.user = null;
    this.psswd = null;
    this.email = null;
  }

  async register() {
    this.valida();
    if (this.error.length > 0) {
      console.log(this.error);
      return;
    }

    try {
      this.user = await UserModel.create({
        email: this.email,
        psswd: this.psswd,
      });
    } catch {
      (e) => console.log(e);
    }
  }

  valida() {
    this.cleanUp();

    if (!validator.isEmail(this.email)) this.error.push("Email Inválido");
    if (this.psswd.length < 3 || this.psswd.length >= 50)
      this.error.push("A senha precisa ter 3 a 50 caracteres");
  }

  cleanUp() {
    for (let param in this.body) {
      if (typeof this.body[param] !== "string") this.body[key] = "";
    }
    this.email = this.body.email;
    this.psswd = this.body.psswd;
  }
};

module.exports.UserModel = UserModel;
