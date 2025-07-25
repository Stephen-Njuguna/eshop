import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const VendorProducts = () => {
  const { slug } = useParams();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/stores/${slug}/products/`)
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(err => console.error('Error fetching products:', err));
  }, [slug]);

  return (
    <div>
      <h1>All products from store: {slug}</h1>
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

export default VendorProducts;