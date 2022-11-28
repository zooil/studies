const express = require("express");
const router = express.Router();

router
	.get("/", (req, res) => {
	// get 요청처리
		res.send("상품요청정보조회");
	})
	.post("/insert", (req, res) => {
		res.send("insert new product");
	})
	.put("/update", (req, res) => {
		res.send("update product info");
	})
	.delete("/delete", (req, res) => {
		res.send("delete product");
	});


module.exports = router;
