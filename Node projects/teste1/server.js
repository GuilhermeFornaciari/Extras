require("dotenv").config();
const express = require("express");
const app = express();
const path = require("path");
const routes = require("./routes");
const mongoose = require("mongoose");
const helmet = require("helmet");
const csrf = require("csurf");
const {
  checkCsrfError,
  csrfMiddleware,
} = require("./src/middlewares/middlewares");
const session = require("express-session");
const MongoStore = require("connect-mongo");
const flash = require("connect-flash");

//#####################
mongoose
  .connect(process.env.CONNECTIONSTRING)
  .then(() => app.emit("ready"))
  .catch((e) => console.log(e));

///
const sessionOptions = session({
  secret: "iuhnqgbecfrvigvhf",
  Store: MongoStore.create({ mongoUrl: process.env.CONNECTIONSTRING }),
  resave: false,
  saveUninitialized: false,
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 * 7,
    httpOnly: true,
  },
});

//####################################################
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(helmet());
app.use(sessionOptions);
app.use(flash());

app.use(express.static(path.resolve(__dirname, "public")));
app.set("views", path.resolve(__dirname, "src", "views"));
app.set("view engine", "ejs");


app.use(csrf());
app.use(checkCsrfError);
app.use(csrfMiddleware);

app.use(routes);



app.on("ready", () => {
  app.listen(3000, () => console.log("Acesse: http://localhost:3000"));
});
