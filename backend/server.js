const express = require("express");
const fs = require("fs");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.get("/", (req, res) => {
    res.send("🚀 Welcome to Webhook API! Use /webhook to send signals.");
});

app.post("/webhook", (req, res) => {
    const order = req.body;

    if (!order || Object.keys(order).length === 0) {
        return res.status(400).json({ message: "Invalid request. JSON body is required." });
    }

    console.log("📩 Received Order:", order);

    const csvHeaders = "timestamp,variety,tradingsymbol,symboltoken,transactiontype,exchange,ordertype,producttype,duration,price,squareoff,stoploss,quantity\n";
    if (!fs.existsSync("signals.csv")) {
        fs.writeFileSync("signals.csv", csvHeaders);
    }

    const timestamp = new Date().toISOString();
    const csvData = `${timestamp},${order.variety},${order.tradingsymbol},${order.symboltoken},${order.transactiontype},${order.exchange},${order.ordertype},${order.producttype},${order.duration},${order.price},${order.squareoff},${order.stoploss},${order.quantity}\n`;

    fs.appendFile("signals.csv", csvData, (err) => {
        if (err) {
            console.error("Error writing to CSV:", err);
            return res.status(500).json({ message: "Error saving order." });
        }
        console.log("Order saved to CSV.");
        return res.status(200).json({ message: "Order received and logged." });
    });
});

app.get("/signals", (req, res) => {
    fs.readFile("signals.csv", "utf8", (err, data) => {
        if (err) {
            console.error("Error reading CSV:", err);
            return res.status(500).json({ message: "Error fetching orders." });
        }

        const rows = data.trim().split("\n").slice(1);
        const orders = rows.map(row => {
            const [timestamp, variety, tradingsymbol, symboltoken, transactiontype, exchange, ordertype, producttype, duration, price, squareoff, stoploss, quantity] = row.split(",");
            return { timestamp, variety, tradingsymbol, symboltoken, transactiontype, exchange, ordertype, producttype, duration, price, squareoff, stoploss, quantity };
        });

        res.json(orders);
    });
});


const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`TradingView Webhook API running on http://localhost:${PORT}`);
});
