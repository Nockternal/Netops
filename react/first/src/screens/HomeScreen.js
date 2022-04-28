import React, { useState, useEffect } from 'react'
import { Row, Col } from 'react-bootstrap'
//import products from '../products'
import Product from '../components/Product'
import axios from 'axios'

function HomeScreen() {
  const [products, setProducts] = useState([])
  useEffect(() => {
    async function fetchProducts() {
      const { data } = await axios.get('/api/products')
      setProducts(data)
      //console.log(data)
    }
    fetchProducts()
    
  }, [])
  return (
      <div>
          <h1>Home Screen</h1>
          <Row>
              {products.map(product => (
                  <Col sm={12} md={6} lg={4} xl={3} key={product._id}>
                      <Product product={product}></Product>
                </Col>
              ))}
          </Row>
    </div>
  )
}

export default HomeScreen