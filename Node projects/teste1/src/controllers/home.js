exports.paginainicial = (req, res) => {
  res.render("index");
};
exports.paginainicialpost = (req, res) => {
  res.send(req.body);
};
