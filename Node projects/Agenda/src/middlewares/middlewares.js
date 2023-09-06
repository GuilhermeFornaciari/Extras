exports.checkCsrfError = (err, req, res, next) => {
  if (err && "EBADCSRFTOKEN" === err.code) {
    return res.send("BAD CSRF");
  }
};

exports.csrfMiddleware = (req, res, next) => {
  res.locals.csrfToken = req.csrfToken();
  next();
};
exports.globalMiddleware = (req, res, next) => {
  res.locals.msgs = req.flash("msgs");
  res.locals.element = req.flash("element");
  res.locals.cssClass = req.flash("cssClass");
  next();
};
