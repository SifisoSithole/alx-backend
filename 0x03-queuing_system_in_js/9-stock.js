import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 0,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(itemId) {
    return listProducts.filter((items) => items.itemId === itemId);
}

const app = express();
app.listen(1245, () => {
    listProducts.forEach((product) => reserveStockById(product.itemId,
      product.initialAvailableQuantity));
});

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
  
    const item = getItemById(itemId);
    const initialAvailableQuantity = await getCurrentReservedStockById(itemId);
  
    if (item.length > 0) {
      item.currentQuantity = initialAvailableQuantity;
      res.json(item);
      return;
    }
  
    res.status(404).json({ status: 'Product not found' });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
  
    const item = getItemById(itemId);
  
    if (item.length < 1) {
      res.status(404).json({ status: 'Product not found' });
      return;
    }
  
    const initialAvailableQuantity = await getCurrentReservedStockById(itemId);
  
    if (initialAvailableQuantity < 1) {
      res.status(403).json({ status: 'Not enough initialAvailableQuantity available', itemId });
      return;
    }

    reserveStockById(itemId, initialAvailableQuantity);
    res.json({ status: 'Reservation confirmed', itemId });
});

const client = redis.createClient();
const get = promisify(client.get).bind(client);

function reserveStockById(itemId, initialAvailableQuantity) {
    client.set(itemId, initialAvailableQuantity);
}
  
async function getCurrentReservedStockById(itemId) {
    const initialAvailableQuantity = await get(itemId);
    return initialAvailableQuantity;
}