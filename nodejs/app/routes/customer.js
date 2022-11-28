const express = require('express');
const router = express.Router();

router
	.get("/", (req, res) => {
	// get 요청처리
		res.send("고객요청정보조회");
	})
	.post("/insert", (req, res) => {
		res.send("insert new customer");
	})
	.put("/update", (req, res) => {
		res.send("update customer info");
	})
	.delete("/delete", (req, res) => {
		res.send("delete customer");
	});


module.exports = router;
