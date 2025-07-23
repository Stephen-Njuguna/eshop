// src/components/ProductList.js
import React, { useEffect, useState } from 'react';

const ProductList = () => {
  const [products, setProducts] = useState([]);

useEffect(() => {
  fetch('http://127.0.0.1:8000/api/products/')
    .then(response => response.json())
    .then(data => setProducts(data))
    .catch(err => console.error('Error fetching products:', err));
}, []);

  return (
    <div>
      <h1>All Products</h1>
      <div style={{ display: 'grid', gap: '20px' }}>
        {products.map(product => (
          <div key={product.id} style={{ border: '1px solid #ccc', padding: '12px' }}>
            <img
              src={`http://127.0.0.1:8000${product.image}`}
              alt={product.title}
              style={{ width: '100%', maxHeight: '200px', objectFit: 'cover' }}
            />
            <h3>{product.title}</h3>
            <p>{product.description}</p>
            <strong>£{product.price}</strong>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProductList;