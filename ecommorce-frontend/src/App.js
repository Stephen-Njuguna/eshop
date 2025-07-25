import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate, useLocation } from "react-router-dom";
import ProductList from "./components/ProductList";
import LoginForm from "./components/LoginForm";
import VendorDashboard from "./components/VendorDashboard";
import VendorProducts from "./components/VendorProducts";

// Route guard component



const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem('vendorToken');
  const location = useLocation();

  if (!token) {
    return <Navigate to="/vendor-login" state={{ from: location }} replace />;
  }

  return children;
};


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/vendor-login" element={<LoginForm />} />
        <Route path="/stores/:slug/products/" element={< VendorProducts />}/>
        <Route
          path="/vendor-dashboard"
          element={
              <VendorDashboard />      
          }
        />
      </Routes>
    </Router>
  );
}

export default App;